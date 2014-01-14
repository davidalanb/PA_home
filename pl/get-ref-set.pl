#!/usr/bin/perl
#
# David Benedetto
# 5/2007
#
# get-ref-set.pl <genes.fna>
#
# Pulls highly expressed ribosomal proteins out of a gene nucleic acid file
#

use strict;
use warnings;

if ( @ARGV != 1 ) {
    print "Usage: getRefSet.pl <genes.fna>\n\n";
    exit;
}

# set up command line arguments
my $infile = $ARGV[0];

$infile =~ /(.*?)\.fna/;

my $name = $1;
print "infile=$name\n";

# set up source and dest files
open ( IN, "$infile" ) or die "Cannot load $infile";

open ( OUT, ">$name-refset.fna" ) or die "Cannot load $name-refset.fna";

$/ = ">";

while ( <IN> ) {

    chomp;
    
    my ( $header, $sequence ) = split( /\n/, $_, 2 ); # split into two list variables
    next unless ( $header && $sequence );             # next unless there is a sequence and a header

	if ( $header =~ /( L(\d+) )|( S(\d+) )/ ) {
		print OUT ">$header\n$sequence";		
	}

}

