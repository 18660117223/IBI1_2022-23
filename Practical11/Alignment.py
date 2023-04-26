#Summary
#Findings:
#HUMAN and MOUSE: Score: 3579 Same amino acids percentage: 82.11180124223603
#MOUSE and CAT: Score: 3592 Same amino acids percentage: 81.73913043478261
#HUMAN and CAT Score: 3717 Same amino acids percentage: 85.21739130434783
#Interpretation: The sequences of human and cat are most closely related. After searching the internet, I have found that the evolutionary tree showed that: 
#The common ancestor of Homo sapiens and Felis catus diverged approximately 87 million years ago.
#The common ancestor of Felis catus and Mus musculus diverged approximately 93 million years ago.
#The common ancestor of Homo sapiens and Mus musculus diverged approximately 105 million years ago.
#So the ancestors of humans, cats and mice separated relatively early, and that humans and cats were more closely related.

seq1='MSSSSWLLLSLVAVTAAQSTIEEQAKTFLDKFNHEAEDLFYQSSLASWNYNTNITEENVQNMNNAGDKWSAFLKEQSTLAQMYPLQEIQNLTVKLQLQALQQNGSSVLSEDKSKRLNTILNTMSTIYSTGKVCNPDNPQECLLLEPGLNEIMANSLDYNERLWAWESWRSEVGKQLRPLYEEYVVLKNEMARANHYEDYGDYWRGDYEVNGVDGYDYSRGQLIEDVEHTFEEIKPLYEHLHAYVRAKLMNAYPSYISPIGCLPAHLLGDMWGRFWTNLYSLTVPFGQKPNIDVTDAMVDQAWDAQRIFKEAEKFFVSVGLPNMTQGFWENSMLTDPGNVQKAVCHPTAWDLGKGDFRILMCTKVTMDDFLTAHHEMGHIQYDMAYAAQPFLLRNGANEGFHEAVGEIMSLSAATPKHLKSIGLLSPDFQEDNETEINFLLKQALTIVGTLPFTYMLEKWRWMVFKGEIPKDQWMKKWWEMKREIVGVVEPVPHDETYCDPASLFHVSNDYSFIRYYTRTLYQFQFQEALCQAAKHEGPLHKCDISNSTEAGQKLFNMLRLGKSEPWTLALENVVGAKNMNVRPLLNYFEPLFTWLKDQNKNSFVGWSTDWSPYADQSIKVRISLKSALGDKAYEWNDNEMYLFRSSVAYAMRQYFLKVKNQMILFGEEDVRVANLKPRISFNFFVTAPKNVSDIIPRTEVEKAIRMSRSRINDAFRLNDNSLEFLGIQPTLGPPNQPPVSIWLIVFGVVMGVIVVGIVILIFTGIRDRKKKNKARSGENPYASIDISKGENNPGFQNTDDVQTSF'

seq2='MSSSSWLLLSLVAVTTAQSLTEENAKTFLNNFNQEAEDLSYQSSLASWNYNTNITEENAQKMSEAAAKWSAFYEEQSKTAQSFSLQEIQTPIIKRQLQALQQSGSSALSADKNKQLNTILNTMSTIYSTGKVCNPKNPQECLLLEPGLDEIMATSTDYNSRLWAWEGWRAEVGKQLRPLYEEYVVLKNEMARANNYNDYGDYWRGDYEAEGADGYNYNRNQLIEDVERTFAEIKPLYEHLHAYVRRKLMDTYPSYISPTGCLPAHLLGDMWGRFWTNLYPLTVPFAQKPNIDVTDAMMNQGWDAERIFQEAEKFFVSVGLPHMTQGFWANSMLTEPADGRKVVCHPTAWDLGHGDFRIKMCTKVTMDNFLTAHHEMGHIQYDMAYARQPFLLRNGANEGFHEAVGEIMSLSAATPKHLKSIGLLPSDFQEDSETEINFLLKQALTIVGTLPFTYMLEKWRWMVFRGEIPKEQWMKKWWEMKREIVGVVEPLPHDETYCDPASLFHVSNDYSFIRYYTRTIYQFQFQEALCQAAKYNGSLHKCDISNSTEAGQKLLKMLSLGNSEPWTKALENVVGARNMDVKPLLNYFQPLFDWLKEQNRNSFVGWNTEWSPYADQSIKVRISLKSALGANAYEWTNNEMFLFRSSVAYAMRKYFSIIKNQTVPFLEEDVRVSDLKPRVSFYFFVTSPQNVSDVIPRSEVEDAIRMSRGRINDVFGLNDNSLEFLGIHPTLEPPYQPPVTIWLIIFGVVMALVVVGIIILIVTGIKGRKKKNETKREENPYDSMDIGKGESNAGFQNSDDAQTSF'

seq3='MSGSFWLLLSFAALTAAQSTTEELAKTFLEKFNHEAEELSYQSSLASWNYNTNITDENVQKMNEAGAKWSAFYEEQSKLAKTYPLAEIHNTTVKRQLQALQQSGSSVLSADKSQRLNTILNAMSTIYSTGKACNPNNPQECLLLEPGLDDIMENSKDYNERLWAWEGWRAEVGKQLRPLYEEYVALKNEMARANNYEDYGDYWRGDYEEEWTDGYNYSRSQLIKDVEHTFTQIKPLYQHLHAYVRAKLMDTYPSRISPTGCLPAHLLGDMWGRFWTNLYPLTVPFGQKPNIDVTDAMVNQSWDARRIFKEAEKFFVSVGLPNMTQGFWENSMLTEPGDSRKVVCHPTAWDLGKGDFRIKMCTKVTMDDFLTAHHEMGHIQYDMAYAVQPFLLRNGANEGFHEAVGEIMSLSAATPNHLKTIGLLSPGFSEDSETEINFLLKQALTIVGTLPFTYMLEKWRWMVFKGEIPKEQWMQKWWEMKREIVGVVEPVPHDETYCDPASLFHVANDYSFIRYYTRTIYQFQFQEALCRIAKHEGPLHKCDISNSSEAGKKLLQMLTLGKSKPWTLALEHVVGEKKMNVTPLLKYFEPLFTWLKEQNRNSFVGWNTDWRPYADQSIKVRISLKSALGDEAYEWNDNEMYLFRSSVAYAMREYFSKVKNQTIPFVEDNVWVSNLKPRISFNFFVTASKNVSDVIPRSEVEEAIRMSRSRINDAFRLDDNSLEFLGIQPTLSPPYQPPVTIWLIVFGVVMGVVVVGIVLLIVSGIRNRRKNNQARSEENPYASVDLSKGENNPGFQHADDVQTSF'

BLOSUM62 = '''A  4  0 -2 -1 -2  0 -2 -1 -1 -1 -1 -2 -1 -1 -1  1  0  0 -3 -2
C  0  9 -3 -4 -2 -3 -3 -1 -3 -1 -1 -3 -3 -3 -3 -1 -1 -1 -2 -2
D -2 -3  6  2 -3 -1 -1 -3 -1 -4 -3  1 -1  0 -2  0 -1 -3 -4 -3
E -1 -4  2  5 -3 -2  0 -3  1 -3 -2  0 -1  2  0  0 -1 -2 -3 -2
F -2 -2 -3 -3  6 -3 -1  0 -3  0  0 -3 -4 -3 -3 -2 -2 -1  1  3
G  0 -3 -1 -2 -3  6 -2 -4 -2 -4 -3  0 -2 -2 -2  0 -2 -3 -2 -3
H -2 -3 -1  0 -1 -2  8 -3 -1 -3 -2  1 -2  0  0 -1 -2 -3 -2  2
I -1 -1 -3 -3  0 -4 -3  4 -3  2  1 -3 -3 -3 -3 -2 -1  3 -3 -1
K -1 -3 -1  1 -3 -2 -1 -3  5 -2 -1  0 -1  1  2  0 -1 -2 -3 -2
L -1 -1 -4 -3  0 -4 -3  2 -2  4  2 -3 -3 -2 -2 -2 -1  1 -2 -1
M -1 -1 -3 -2  0 -3 -2  1 -1  2  5 -2 -2  0 -1 -1 -1  1 -1 -1
N -2 -3  1  0 -3  0  1 -3  0 -3 -2  6 -2  0  0  1  0 -3 -4 -2
P -1 -3 -1 -1 -4 -2 -2 -3 -1 -3 -2 -2  7 -1 -2 -1 -1 -2 -4 -3
Q -1 -3  0  2 -3 -2  0 -3  1 -2  0  0 -1  5  1  0 -1 -2 -2 -1
R -1 -3 -2  0 -3 -2  0 -3  2 -2 -1  0 -2  1  5 -1 -1 -3 -3 -2
S  1 -1  0  0 -2  0 -1 -2  0 -2 -1  1 -1  0 -1  4  1 -2 -3 -2
T  0 -1 -1 -1 -2 -2 -2 -1 -1 -1 -1  0 -1 -1 -1  1  5  0 -2 -2
V  0 -1 -3 -2 -1 -3 -3  3 -2  1  1 -3 -2 -2 -3 -2  0  4 -3 -1
W -3 -2 -4 -3  1 -2 -2 -3 -3 -2 -1 -4 -4 -2 -3 -3 -2 -3 11  2
Y -2 -2 -3 -2  3 -3  2 -1 -2 -1 -1 -2 -3 -1 -2 -2 -2 -1  2  7'''.split('\n')
for i in range(len(BLOSUM62)):
 BLOSUM62[i] = BLOSUM62[i].split()
matrix={}
for i in range(len(BLOSUM62)):
 for j in range(1, len(BLOSUM62[0])):
  matrix[BLOSUM62[i][0] + '\t' + BLOSUM62[j-1][0]] = BLOSUM62[i][j]

t=[[0]]
for n in range(1, len(seq2)+1):
    t[0].append(n*(-5))
for i in range(1, len(seq1)+1):
    t.append([i*(-5)] + [0]*len(seq2))
    for j in range(1, len(seq2)+1):
        if seq1[i-1] == seq2[j-1]:
            t[i][j] = t[i-1][j-1] + int(matrix[seq1[i-1]+'\t'+seq2[j-1]])
        else:
            t[i][j] = max(t[i-1][j]-5, t[i][j-1]-5, t[i-1][j-1]+int(matrix[seq1[i-1]+'\t'+seq2[j-1]]))

b=[[0]]
for n in range(1, len(seq3)+1):
    b[0].append(n*(-5))
for i in range(1, len(seq2)+1):
    b.append([i*(-5)] + [0]*len(seq3))
    for j in range(1, len(seq3)+1):
        if seq2[i-1] == seq3[j-1]:
            b[i][j] = b[i-1][j-1] + int(matrix[seq2[i-1]+'\t'+seq3[j-1]])
        else:
            b[i][j] = max(b[i-1][j]-5, b[i][j-1]-5, b[i-1][j-1]+int(matrix[seq2[i-1]+'\t'+seq3[j-1]]))

l=[[0]]
for n in range(1, len(seq3)+1):
    l[0].append(n*(-5))
for i in range(1, len(seq1)+1):
    l.append([i*(-5)] + [0]*len(seq3))
    for j in range(1, len(seq3)+1):
        if seq1[i-1] == seq3[j-1]:
            l[i][j] = l[i-1][j-1] + int(matrix[seq1[i-1]+'\t'+seq3[j-1]])
        else:
            l[i][j] = max(l[i-1][j]-5, l[i][j-1]-5, l[i-1][j-1]+int(matrix[seq1[i-1]+'\t'+seq3[j-1]]))

def identity(seq1,seq2):
 Seq1=seq1
 Seq2=seq2
 identity=0
 group=list(zip(Seq1,Seq2))
 for p in group:
  if p[0]==p[1]:
   identity=identity+1
 percentage=identity/len(Seq1)*100
 return percentage


print("HUMAN and MOUSE:")
print("Score:",t[len(seq1)][len(seq2)])
print("Same amino acids percentage:",identity(seq1,seq2))
print("MOUSE and CAT:")
print("Score:",b[len(seq2)][len(seq3)])
print("Same amino acids percentage:",identity(seq2,seq3))
print("HUMAN and CAT:")
print("Score:",l[len(seq1)][len(seq3)])
print("Same amino acids percentage:",identity(seq1,seq3))
