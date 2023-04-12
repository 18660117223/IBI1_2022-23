#open to read the aiming file
#count the lines
#determine the seq
#see the lines in the fhand line by line
#if the line starts with >, it is title; if not, write it in seq
#for title: eliminate the contents except the title(the name of the gene)
#in seq: find the sequences ending with TAG and write them including the title and sequence in the file TAG_genes
#elimate the existing content in seq to turn to the new gene
fhand=open('Saccharomyces_cerevisiae.R64-1-1.cdna.all.fa','r')
count=0
seq=""
for line in fhand:
 if line.startswith('>'):
  title=line.split(" ")[0]
  if count!=0:
   if line.endswith('TGA\n'):
    new=open('TGA_genes.fa','a')
    new.write(f'{title}\n{seq}')
    new.close
   count=count+1
   seq=""
 else:
  seq=seq+line

