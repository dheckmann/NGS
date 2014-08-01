#!/usr/bin/python

#230714 DH
# usage: diff_fasta.py fasta_to_substract_from fasta_to_substract

from Bio import SeqIO
import sys

seqiter = SeqIO.parse(open(sys.argv[1], "rU"), 'fasta') #create iteration object from fasta

#[ seq.features for seq in seqiter]

# array of 
#seqiter_subseT_IDs = [seq.id for seq in seqiter_subset]

# check structure of the record object
#for record in seqiter :
#	if not record.id in seqiter_subseT_IDs:
#		print "%s" % (record.id)

for record in seqiter :
	print " ID = %s, name = %s, length %i, alphabet %s, with %i features, decription %s" \
	      % ( record.id, record.name, len(record.seq), record.seq.alphabet,  len(record.features), record.description)
