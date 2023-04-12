#open to read the aiming file
#ask the user to input stop codon
#count the lines
#determine the seq
#see the lines in the fhand line by line
#if the line starts with >, it is title; if not, write it in seq, but strip the line feed
#find the number of the coding sequences and name it as number, add it in title
#for title: eliminate the contents except the title(the name of the gene)
#in seq: find the sequences ending with the input stop codon and write them including the title and sequence in a new file
#elimate the existing content in seq to turn to the new gene
fhand=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
stop_codon=input
count=0
seq=""
for line in fhand:
 if line.startswith('>'):
  title1=line.split(" ")[0]
  if count!=0:
   if line.endswith('stop_codon'):
    number="the number of coding sequences:"+str(seq.count(stop_codon))
    title=title1+number
    new=open(stop_codon+'_stop_genes.fa','a')
    new.write(f'{title}\n{seq}\n')
    new.close
   count=count+1
   seq=""
 else:
  seq=seq+line.strip('\n')