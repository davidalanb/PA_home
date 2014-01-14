#!/usr/bin/perl -w
#
# David Benedetto
# codon usage script
#
use strict;
use warnings;

sub usage()
{
   print STDERR q(   Usage: ./gbg-codon-usage [-s] [-c] [-d] [-b] geneFile.fna
   		The program takes a fasta file as input and outputs a chart with the genes on the y-axis 
		and the codons (sorted by amino acid) on the x-axis (default to "output-geneFile.txt")
		-s:	output tsv (tab separated values) for spreadsheets
			to "output-geneFile.csv"
		-c: output hard codon counts instead of frequency
		-d: output some more codon info (be careful about running this on large datasets)
			to "debug-geneFile.txt"
		-b: output four codon family, third position nucleotide bias information 
			to "bias-geneFile.csv"
   ), "\n";
   exit;
}

if ( @ARGV < 1 ) # if less than 1 arg
{
   &usage();
}


###########################################
#  Setup flags and i/o
###########################################


my $fnaFile = $ARGV[@ARGV-1];
my ($name) = $fnaFile =~ /(.*?)\.fna/;
my $outFile = "output-$name.txt";
my $totoutFile = "totout-$name.csv";
my $biasFile;
my $totbiasFile;
my $debugFile;

my $sprdsht = 0;
my $hardcnt = 0;
my $debug = 0;
my $bias = 0;

if ( @ARGV > 1 )
{
	for ( my $i=0; $i<(@ARGV-1); $i++ )
	{
		if ( $ARGV[$i] eq "-s" )
		{
			$sprdsht = 1;
			$outFile = "output-$name.csv";
		}
		elsif ( $ARGV[$i] eq "-c" )
		{
			$hardcnt = 1;
		}
		elsif ( $ARGV[$i] eq "-d" )
		{
			$debug = 1;
			$debugFile = "debug-$name.txt";
			open ( DEBUGOUT, ">$debugFile" ) or die "> Unable to open $debugFile";
		}
		elsif ( $ARGV[$i] eq "-b" )
		{
			$bias = 1;
			$biasFile = "bias-$name.csv";
			$totbiasFile = "totbias-$name.csv";
			open ( BIASOUT, ">$biasFile" ) or die "> Unable to open $biasFile";
			open ( TOTBIASOUT, ">$totbiasFile" ) or die "> Unable to open $totbiasFile";
		}
	}
}

open ( FNAIN, $fnaFile )  or die "> Unable to open $fnaFile";
open ( OUT, ">$outFile" ) or die "> Unable to open $outFile";
open ( TOTOUT, ">$totoutFile" ) or die "> Unable to open $totoutFile";


###########################################
#  Variable Initialization
###########################################


my %output_arr;

my @aminolist = qw(Start Phe Leu Leu1 Ile Met Val Ser Pro Thr Ala Tyr His 
	Gln Asn Lys Asp Glu Cys iTGA Trp Arg Ser1 Arg1 Gly Stop Stop1);
	
# note that Leu1, Ser, and Arg are 4 codon groups of 6 codon families	
my @fourcodonfams = qw(Val Pro Thr Ala Gly Leu1 Ser Arg);

# note that Leu, Ser1, and Arg1 are 2 codon groups of 6 codon families
my @twocodonfamsGA = qw(Leu Gln Lys Glu Arg1);
my @twocodonfamsTC = qw(Phe Tyr His Asn Asp Cys Ser1); 

my %aminos = (
    Phe => ["TTT", "TTC"],
    Leu => ["TTA", "TTG"],
	Leu1 => ["CTT", "CTC", "CTA", "CTG"],
    Ile => ["ATT", "ATC", "ATA"],
	Start => ["sATG", "sGTG", "sCTG", "sTTG", "sATT"],
	Met => ["ATG"],
	Val => ["GTT", "GTC", "GTA", "GTG"],
	Ser => ["TCT", "TCC", "TCA", "TCG"], 
	Pro => ["CCT", "CCC", "CCA", "CCG"],
	Thr => ["ACT", "ACC", "ACA", "ACG"],
	Ala => ["GCT", "GCC", "GCA", "GCG"],
	Tyr => ["TAT", "TAC"],
	Stop => ["TAA", "TAG"],
	His => ["CAT", "CAC"],
	Gln => ["CAA", "CAG"],
	Asn => ["AAT", "AAC"],
	Lys => ["AAA", "AAG"],
	Asp => ["GAT", "GAC"],
	Glu => ["GAA", "GAG"],
	Cys => ["TGT", "TGC"],
	Stop1 => ["TGA"],
	iTGA => ["iTGA"],
	Trp => ["TGG"],
	Arg => ["CGT", "CGC", "CGA", "CGG"], 
	Ser1 => ["AGT", "AGC"],
	Arg1 => ["AGA", "AGG"],
	Gly => ["GGT", "GGC", "GGA", "GGG"],
);

# master usage 
my %usage;
my %totusage;

foreach my $amino ( @aminolist )
{	
	foreach my $codon( @{ $aminos{ $amino } } )
	{
		$usage{ $codon } = 0;
		$totusage{ $codon } = 0;
	}	
}

# total number of genes in inputfile
my $genecounts = 0;

# number of codons in a gene
my $genecodoncnt = 0;

# total number of codons
my $totcodoncnt = 0;

# used for aggregate bias information
#
my @totalbias4fam;
my $totalcodons4fam = 0;
#
my @totalbias2fam;
my $totalcodons2famGA = 0;
my $totalcodons2famTC = 0;

# used for per gene bias information
my @genebias;
my $genecodons4fam = 0;

# initialize
for (my $i=0; $i<4; $i++){
	$genebias[$i] = 0;
	$totalbias4fam[$i] = 0;
	$totalbias2fam[$i] = 0;
}


###########################################
#  Now we're ready to start reading the fnaFile
###########################################


local $/ = ">";

my $read = <FNAIN>;
my $linecount = 0;

if ( $read ne ">" )
{
	print STDERR "error, file doesn't start with valid header:$read\n";
	exit;
}

$read = <FNAIN>;
while( $read )
{
	
	###########################################
	#  Print amino acids and codons to output file
	###########################################
	
	if ( (($sprdsht == 0) and ($linecount % 25 == 0)) or ($linecount == 0) ){
		
		if ( $sprdsht == 0 )
			{print OUT "\t\t\t";}
		else
			{print OUT "\t\t"}

		foreach my $amino ( @aminolist )
		{	
			print OUT "$amino";

			foreach my $codon( @{ $aminos{ $amino } } )
			{
				print OUT "\t";
			}
		}

		if ( $sprdsht == 0 )
			{print OUT "\n\t\tTOT\t";}
		else
			{print OUT "\n\tTOT\t"}

		foreach my $amino ( @aminolist )
		{	
			foreach my $codon( @{ $aminos{ $amino } } )
			{
				print OUT "$codon\t";
			}	
		}

		print OUT "\n";
		
	}
	
	###########################################
	#  Setup bias output file
	###########################################
	
	if (($bias == 1) && ($linecount == 0))
	{
		print BIASOUT "\tG\tA\tT\tC\n";
	}
	
	###########################################
	#  Process a read (a gene in our case)
	###########################################
	
	chomp( $read );
	
	# split the read up
	my ( $id, $rest, $seq ) = $read =~ /(\S*)(.*?)\n([\s\S]*)/;
	
	if ( $debug == 1 )
	{
		print DEBUGOUT "\n\n---debugging output---\n\n";
	}
	
	# get rid of the whitespace
	$seq =~ s/[\n\r]//g;
	
	if( $seq =~ /^(ATG|GTG|CTG|TTG|ATT)(.{3})*?(TAA|TAG|TGA).*/ )
	{	
		$genecounts++;	
		my $aftertga = "";		
		
		for( my $count=0; $count< length($seq); $count+=3)
		{
			my $codon = substr( $seq, $count, 3 );
			
			if ( $debug == 1 )
			{
				print DEBUGOUT "$codon\n";
			}
			
			$genecodoncnt++;
			
			if ( $codon =~ /TGA/ )
			{
				## check to see if the sequence continues in a valid way after this
				#
				if ( $aftertga eq "" )
				{
					$seq =~ /^(ATG|GTG|CTG|TTG|ATT)(.{3})*?TGA(.*)/;
					$aftertga = $3;
				}
				else
				{
					$aftertga =~ /(.{3})*?TGA(.*)/;
					$aftertga = $2;
				}
				
				if ( $debug == 1 )
				{
					print DEBUGOUT "aftertga: ";
					for ( my $cnt=0; $cnt < length($aftertga); $cnt+=3)
					{
						print DEBUGOUT substr( $aftertga, $cnt, 3 ), " ";
					}
					print DEBUGOUT "\n";
				}
			
				if ($aftertga =~ /^([GATC]{3}?)*(TAA|TAG|TGA).*/ )
				{
					$usage{ "iTGA" }++;
				}
				else
				{	
					$usage{ "TGA" }++;
					$count = length($seq);
				}
			}
			elsif( $codon =~ /TAA|TAG/ )
			{	
				$usage{ $codon }++;
				$count = length($seq);	# break
			}
			else
			{
				## distinguish start codons from internal codons
				#
				if( $count == 0 )
				{
					$usage{ "s$codon" }++
				}
				else
				{
					$usage{ $codon }++;
				}
			}
			
		} # end for (length of seq)
		
	} # end if (seq is valid)
	
	if ( $debug == 1 )
	{
		print DEBUGOUT "\n---end debugging output---\n\n";
	}
	
	
	###########################################
	#  Incrememt third nucleotide usage for four codon families
	###########################################
	
	
	if ( $bias == 1 ) {
		foreach my $amino ( @fourcodonfams )
		{	
			foreach my $codon( @{ $aminos{ $amino } } )
			{
				$genecodons4fam += $usage{ $codon };
				
				if ( substr( $codon, 2, 1) eq "G" )
				{
					$genebias[0] += $usage { $codon }; 
				}
				elsif ( substr( $codon, 2, 1) eq "A" )
				{
					$genebias[1] += $usage{ $codon };
				}
				elsif ( substr( $codon, 2, 1) eq "T" )
				{
					$genebias[2] += $usage{ $codon };
				}
				elsif ( substr( $codon, 2, 1) eq "C" )
				{
					$genebias[3] += $usage{ $codon };
				}
			}
		}
		foreach my $amino ( @twocodonfamsGA )
		{
			foreach my $codon( @{ $aminos{ $amino }}) {
				
				$totalcodons2famGA += $usage{ $codon };
				
				if ( substr( $codon, 2, 1) eq "G" ) {
					$totalbias2fam[0] += $usage{ $codon };
				}
				elsif ( substr( $codon, 2, 1) eq "A" ) {
					$totalbias2fam[1] += $usage{ $codon };
				}
			}
		}
		foreach my $amino ( @twocodonfamsTC )
		{
			foreach my $codon( @{ $aminos{ $amino }}) {
				
				$totalcodons2famTC += $usage{ $codon };
		
				if ( substr( $codon, 2, 1) eq "T" ) {
					$totalbias2fam[2] += $usage{ $codon };
				}
				elsif ( substr( $codon, 2, 1) eq "C" ) {
					$totalbias2fam[3] += $usage{ $codon };
				}
			}
		}
	}
	
	$totalcodons4fam += $genecodons4fam;
	for( my $i=0; $i<4; $i++ )
	{
		$totalbias4fam[$i] += $genebias[$i];
	}
	
	
	###########################################
	#  Output results from this gene and reset usage for the next gene
	###########################################
	
	
	print OUT "$id\t$genecodoncnt\t";
	
	foreach my $amino ( @aminolist )
	{	
		foreach my $codon( @{ $aminos{ $amino } } )
		{
			if( $genecodoncnt >0 )
			{
				if ( $hardcnt == 0)
					{print OUT sprintf("%0.3f\t", $usage{ $codon }/$genecodoncnt);}
				else
					{print OUT "$usage{ $codon }\t";}
			}
			
			$totusage{ $codon } += $usage{ $codon };
			$usage{ $codon } = 0;
		}
	}
	
	print OUT "\n";
	
	
	###########################################
	#  Output bias results to bias file
	###########################################
	
	
	if( $genecodons4fam > 0)
	{
		print BIASOUT "$id\t";
		print BIASOUT sprintf( "%0.3f\t%0.3f\t%0.3f\t%0.3f\n",
			$genebias[0]/$genecodons4fam, $genebias[1]/$genecodons4fam, 
			$genebias[2]/$genecodons4fam, $genebias[3]/$genecodons4fam );
	}
	
	# get next read
	$read = <FNAIN>;	
	$linecount++;
	
	$totcodoncnt += $genecodoncnt;
	
	# reset gene by gene bias variables
	$genecodons4fam = 0;
	$genecodoncnt = 0;
	for( my $i=0; $i<4; $i++){
		$genebias[$i] = 0;
	}
	
} # end readloop


#################################################################
#  Output totals
#################################################################


print TOTOUT "\t\t";
foreach my $amino ( @aminolist )
{	
	print TOTOUT "$amino";
	foreach my $codon( @{ $aminos{ $amino } } )
	{
		print TOTOUT "\t";
	}
}
print TOTOUT "\n\tTOT\t";
foreach my $amino ( @aminolist )
{	
	foreach my $codon( @{ $aminos{ $amino } } )
	{
		print TOTOUT "$codon\t";
	}	
}
print TOTOUT "\n$name\t$totcodoncnt\t";
foreach my $amino ( @aminolist )
{	
	foreach my $codon( @{ $aminos{ $amino } } )
	{
		if( $totcodoncnt >0 )
		{
			if ( $hardcnt == 0)
				{print TOTOUT sprintf("%0.3f\t", $totusage{ $codon }/$totcodoncnt);}
			else
				{print TOTOUT "$totusage{ $codon }\t";}
		}
	}
}
print TOTOUT "\n";


###########################################
#  Output bias information to biasFile
###########################################


if ( $bias == 1 )
{
	
	print TOTBIASOUT "\tG\tA\tT\tC\n";
	
	if ($totalcodons4fam > 0) {
		print TOTBIASOUT "4codons-$name\t";
		print TOTBIASOUT sprintf( "%0.3f\t%0.3f\t%0.3f\t%0.3f\n",
			$totalbias4fam[0]/$totalcodons4fam, $totalbias4fam[1]/$totalcodons4fam, 
			$totalbias4fam[2]/$totalcodons4fam, $totalbias4fam[3]/$totalcodons4fam );
	}
	if ($totalcodons2famGA > 0) {
		print TOTBIASOUT "2codonsGA-$name\t";
		print TOTBIASOUT sprintf( "%0.3f\t%0.3f\n",
			$totalbias2fam[0]/$totalcodons2famGA, $totalbias2fam[1]/$totalcodons2famGA);
	}
	if ($totalcodons2famTC > 0) {
		print TOTBIASOUT "2codonsTC-$name\t";
		print TOTBIASOUT sprintf( "\t\t%0.3f\t%0.3f\n",
			$totalbias2fam[2]/$totalcodons2famTC, $totalbias2fam[3]/$totalcodons2famTC);
	}
}