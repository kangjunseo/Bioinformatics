# Open Reading Frames
## Problem
Either strand of a DNA double helix can serve as the coding strand for RNA transcription. Hence, a given DNA string implies six total reading frames, or ways in which the same region of DNA can be translated into amino acids: three reading frames result from reading the string itself, whereas three more result from reading its reverse complement.

An open reading frame (ORF) is one which starts from the start codon and ends by stop codon, without any other stop codons in between. Thus, a candidate protein string is derived by translating an open reading frame into amino acids until a stop codon is reached.

Given: A DNA string s of length at most 1 kbp in FASTA format.

Return: Every distinct candidate protein string that can be translated from ORFs of s. Strings can be returned in any order.


```python
I = input().split()
seq=''
complements = str.maketrans('ATGC','TACG')

# get sequence info from FASTA 
for value in I:
    if '>' not in value: seq+=value

# get reverse complement of seq
comp=seq.translate(complements)
rev_comp=''.join(reversed(comp))
```

    >Rosalind_6646 CGCGTACGGGCCGCGCAACTTTCCAGGTCACCAGGCTACGAAAAGGTATCGGTCATGGTG ATAATAGACCTGCGCTTCTCGCACTTAACATACCGGAGTGTGTGCAAAGTTCTGCATTCA TTAAACTCTTGAAATCAATAATTCGCATAATTTAAGACCTAACCTGGATAACGCATTTCC GAACGGACCAAAGATTGGGGGGTATAGTACCGCCAGAACTGTACACTGAGGAACGTTGAT GTCTTGGGGAGGGTTTGGTCAATATGAAGCCCTGTGTATCGGTAACTACTATGCTATATG ATGGACACCAAATTGACATCGAGGTGCGCGTCACCGCGCCGAGTCGTAGGGGATCATCTA GTTTCATCTATGCCGGAACCGCGAAAATTGGTACTAAGGCATCTGATACGCCGGTGGACC CTCCATGGTCGGGCACTTGCCAACTTTTGGAATGAGCCCACGCAGCCTCAGTCGCACCGA GTTATAGCTATAACTCGGTGCGACTGAGGCTGCGTGGGCTCATATCGCTCCTAAAAGTAA TTATTCTTACTATACAGAACGGAATAATCCGGTTAACCCCCCTATTTCCTAGTATCCCGA CTTCGGCATTAACCTGATTTTCGGGTCGAATACTAAAGGTCTACTGTTTAGTTAAAAAGG TGCAGTGCTAGGGCTTGGCCGCGATACCAGGTCATCGAAATGAATGATCCTTACCTCTCC AACCGCGCGCAAGAGGAACCCTCCCGCGATCCCCTATTTCAATGTAACGGTCTAGAAACT CGCACAGTGGGACCTGCGAGGGCCTCGTCGTGTCTCCACTATCCTGAGCAGGCCGGCAAG ATAGAAGGATTACCAGGAAACCTCAAGATCAATATTAGTACAGGTCATACCAAATGATCC CAGCCTTAACGTAGCCAGCTTGTTTGTTTGTTGCTTCTAAGAACAAATGTCAACTCATGC CCATGGTAGTTTAT



```python
frames = set()
ATGs = [[] for _ in range(6)]
codon = """TTT F      CTT L      ATT I      GTT V
TTC F      CTC L      ATC I      GTC V
TTA L      CTA L      ATA I      GTA V
TTG L      CTG L      ATG M      GTG V
TCT S      CCT P      ACT T      GCT A
TCC S      CCC P      ACC T      GCC A
TCA S      CCA P      ACA T      GCA A
TCG S      CCG P      ACG T      GCG A
TAT Y      CAT H      AAT N      GAT D
TAC Y      CAC H      AAC N      GAC D
TAA Stop   CAA Q      AAA K      GAA E
TAG Stop   CAG Q      AAG K      GAG E
TGT C      CGT R      AGT S      GGT G
TGC C      CGC R      AGC S      GGC G
TGA Stop   CGA R      AGA R      GGA G
TGG W      CGG R      AGG R      GGG G """.split()
codon_dict = dict(zip(codon[::2],codon[1::2]))
targets = seq, seq[1:], seq[2:], rev_comp, rev_comp[1:], rev_comp[2:]

#find start points
for idx, frame in enumerate(targets) :
    for i in range(len(frame)-2):
        triplet = ''
        if(i%3==0) :
            triplet = frame[i] + frame[i+1] + frame[i+2]
            if(codon_dict[triplet] == 'M'):
                ATGs[idx].append(i)
                
#encode from start points to stop codons
for idx, frame in enumerate(targets) :
    for start in ATGs[idx] :
        PROT = ''
        for i in range(len(frame[start:])-2) :
            triplet = ''
            if(i%3==0) :
                triplet = frame[start+i] + frame[start+i+1] + frame[start+i+2]
                
                #stop codon
                if(codon_dict[triplet] == 'Stop'):
                    frames.add(PROT)
                    break
                
                PROT+=codon_dict[triplet]

for i in frames:
    print(i)
```

    MGMS
    MNDPYLSNRAQEEPSRDPLFQCNGLETRTVGPARASSCLHYPEQAGKIEGLPGNLKINISTGHTK
    MSIWCPSYSIVVTDTQGFILTKPSPRHQRSSVYSSGGTIPPNLWSVRKCVIQVRS
    MPKSGY
    MTCTNIDLEVSW
    MEGPPAYQMP
    MLSARSAGLLSP
    MPEPRKLVLRHLIRRWTLHGRALANFWNEPTQPQSHRVIAITRCD
    MIPYDSAR
    MS
    MQNFAHTPVC
    MSPRSLSRTEL
    MLYDGHQIDIEVRVTAPSRRGSSSFIYAGTAKIGTKASDTPVDPPWSGTCQLLE
    MRIIDFKSLMNAELCTHSGMLSARSAGLLSP
    MKLDDPLRLGAVTRTSMSIWCPSYSIVVTDTQGFILTKPSPRHQRSSVYSSGGTIPPNLWSVRKCVIQVRS
    MRYPG
    MVGHLPTFGMSPRSLSRTEL
    MIPALT
    MTDTFS
    MP
    MTWYRGQALALHLFN
    MILTSPTARKRNPPAIPYFNVTV
    MMDTKLTSRCASPRRVVGDHLVSSMPEPRKLVLRHLIRRWTLHGRALANFWNEPTQPQSHRVIAITRCD
    MKPCVSVTTMLYDGHQIDIEVRVTAPSRRGSSSFIYAGTAKIGTKASDTPVDPPWSGTCQLLE
    MSWGGFGQYEALCIGNYYAI
    MVIIDLRFSHLTYRSVCKVLHSLNS
    M
    MDTKLTSRCASPRRVVGDHLVSSMPEPRKLVLRHLIRRWTLHGRALANFWNEPTQPQSHRVIAITRCD
    MNAELCTHSGMLSARSAGLLSP



```python

```
