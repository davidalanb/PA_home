#!/usr/bin/perl
#
# Lina Faller
# 4/2007
#
# separate-strands.pl <genes.fna>
#
# This script takes a fasta file with several gene sequences and outputs
# two files, one containing the genes encoded on the plus strand of
# the genome, and one containing the genes on the minus strand.
#

use strict;

if ( @ARGV < 1 ) {
    print "Usage: separate-strands.pl <genes.fna>\n\n";
    exit;
}

# set up command line arguments
my $infile = $ARGV[0];

$infile =~ /(.*?)\.fna/;
my $name = $1;

# set up source and dest files
open ( IN, "$infile" ) or die "Cannot load $infile";
open ( P_OUT, ">$name-plus.fna" ) or die "Cannot load $name-plus.fna";
open ( M_OUT, ">$name-minus.fna" ) or die "Cannot load $name-minus.fna";

$/ = ">";

while ( <IN> ) {

    chomp;
    
    my ( $header, $sequence ) = split( /\n/, $_, 2 ); # split into two list variables
    next unless ( $header && $sequence );             # next unless there is a sequence and a header

    if ( $header =~ /\(\-\)/ ) {
        print M_OUT ">$header\n$sequence";
    }
    
    else {
        print P_OUT ">$header\n$sequence";
    }
}

