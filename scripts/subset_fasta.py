#!/usr/bin/python


from Bio import SeqIO
import sys
wanted = [line.strip() for line in open(sys.argv[2])]
seqiter = SeqIO.parse(open(sys.argv[1], "rU"), 'fasta') #create iteration object from fasta
#SeqIO.write((seq for seq in seqiter if seq.id in wanted), sys.stdout, "fasta")


# check structure of the record object
for record in seqiter :
    print " ID = %s, name = %s, length %i, alphabet %s, with %i features, decription %s" \
          % ( record.id, record.name, len(record.seq), record.seq.alphabet,  len(record.features), record.description)
