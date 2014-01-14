#!/usr/bin/perl
#
# David Benedetto
# 4/2007
#
# separatechromosomes.pl <genes.fna>
#
# Breaks a gene file up into chromosomes
#

use strict;
use warnings;

if ( @ARGV != 1 ) {
    print "Usage: separate-chromosomes.pl <genes.fna>\n\n";
    exit;
}

# set up command line arguments
my $infile = $ARGV[0];

$infile =~ /(.*?)\.fna/;
my $name = $1;

# set up source and dest files
open ( IN, "$infile" ) or die "Cannot load $infile";

open ( OUT, ">$name-1.fna" ) or die "Cannot load $name-1.fna";

$/ = ">";

my $position = 0;
my $cnt = 1;

while ( <IN> ) {

    chomp;
    
    my ( $header, $sequence ) = split( /\n/, $_, 2 ); # split into two list variables
    next unless ( $header && $sequence );             # next unless there is a sequence and a header

	if ( $header =~ / (\d+)\.\./ ) {
		
		if ( (int $1) < $position ) {
			$cnt++;
			open ( OUT, ">$name-$cnt.fna") or die "Cannot load $name-$cnt.fna";
		}
		
		print OUT ">$header\n$sequence";
		
		$position = (int $1);
	}

}

