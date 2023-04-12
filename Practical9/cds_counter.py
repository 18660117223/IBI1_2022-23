#import the re library
#input the sequence
#find all sequences that begin with ATG and end with TAG and put them in a list called number1
#find all sequences that begin with ATG and end with TAA and put them in a list called number2
#count the total number by adding the length of number1 and number2
#print the total number
import re
seq='ATGCAATCGACTACGATCTGAGAGGGCCTAA'
number1=re.findall(r'^ATG.+?TGA',seq)
number2=re.findall(r'^ATG.+?TAA',seq)
total_number=len(number1)+len(number2)
print(total_number)