# Find a Middle Edge in an Alignment Graph in Linear Space
## Problem
Middle Edge in Linear Space Problem
Find a middle edge in the alignment graph in linear space.

Given: Two amino acid strings.

Return: A middle edge in the alignment graph of these strings, where the optimal path is defined by the BLOSUM62 scoring matrix and a linear indel penalty equal to 5. Return the middle edge in the form “(i, j) (k, l)”, where (i, j) connects to (k, l).


```python
BLOSUM62 ={'A': {'A': 4, 'C': 0, 'E': -1, 'D': -2, 'G': 0, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 0, 'W': -3, 'V': 0, 'Y': -2}, 
           'C': {'A': 0, 'C': 9, 'E': -4, 'D': -3, 'G': -3, 'F': -2, 'I': -1, 'H': -3, 'K': -3, 'M': -1, 'L': -1, 'N': -3, 'Q': -3, 'P': -3, 'S': -1, 'R': -3, 'T': -1, 'W': -2, 'V': -1, 'Y': -2}, 
           'E': {'A': -1, 'C': -4, 'E': 5, 'D': 2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': -2, 'L': -3, 'N': 0, 'Q': 2, 'P': -1, 'S': 0, 'R': 0, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 
           'D': {'A': -2, 'C': -3, 'E': 2, 'D': 6, 'G': -1, 'F': -3, 'I': -3, 'H': -1, 'K': -1, 'M': -3, 'L': -4, 'N': 1, 'Q': 0, 'P': -1, 'S': 0, 'R': -2, 'T': -1, 'W': -4, 'V': -3, 'Y': -3}, 
           'G': {'A': 0, 'C': -3, 'E': -2, 'D': -1, 'G': 6, 'F': -3, 'I': -4, 'H': -2, 'K': -2, 'M': -3, 'L': -4, 'N': 0, 'Q': -2, 'P': -2, 'S': 0, 'R': -2, 'T': -2, 'W': -2, 'V': -3, 'Y': -3}, 
           'F': {'A': -2, 'C': -2, 'E': -3, 'D': -3, 'G': -3, 'F': 6, 'I': 0, 'H': -1, 'K': -3, 'M': 0, 'L': 0, 'N': -3, 'Q': -3, 'P': -4, 'S': -2, 'R': -3, 'T': -2, 'W': 1, 'V': -1, 'Y': 3}, 
           'I': {'A': -1, 'C': -1, 'E': -3, 'D': -3, 'G': -4, 'F': 0, 'I': 4, 'H': -3, 'K': -3, 'M': 1, 'L': 2, 'N': -3, 'Q': -3, 'P': -3, 'S': -2, 'R': -3, 'T': -1, 'W': -3, 'V': 3, 'Y': -1}, 
           'H': {'A': -2, 'C': -3, 'E': 0, 'D': -1, 'G': -2, 'F': -1, 'I': -3, 'H': 8, 'K': -1, 'M': -2, 'L': -3, 'N': 1, 'Q': 0, 'P': -2, 'S': -1, 'R': 0, 'T': -2, 'W': -2, 'V': -3, 'Y': 2}, 
           'K': {'A': -1, 'C': -3, 'E': 1, 'D': -1, 'G': -2, 'F': -3, 'I': -3, 'H': -1, 'K': 5, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -1, 'S': 0, 'R': 2, 'T': -1, 'W': -3, 'V': -2, 'Y': -2}, 
           'M': {'A': -1, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': 0, 'I': 1, 'H': -2, 'K': -1, 'M': 5, 'L': 2, 'N': -2, 'Q': 0, 'P': -2, 'S': -1, 'R': -1, 'T': -1, 'W': -1, 'V': 1, 'Y': -1}, 
           'L': {'A': -1, 'C': -1, 'E': -3, 'D': -4, 'G': -4, 'F': 0, 'I': 2, 'H': -3, 'K': -2, 'M': 2, 'L': 4, 'N': -3, 'Q': -2, 'P': -3, 'S': -2, 'R': -2, 'T': -1, 'W': -2, 'V': 1, 'Y': -1}, 
           'N': {'A': -2, 'C': -3, 'E': 0, 'D': 1, 'G': 0, 'F': -3, 'I': -3, 'H': 1, 'K': 0, 'M': -2, 'L': -3, 'N': 6, 'Q': 0, 'P': -2, 'S': 1, 'R': 0, 'T': 0, 'W': -4, 'V': -3, 'Y': -2}, 
           'Q': {'A': -1, 'C': -3, 'E': 2, 'D': 0, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 1, 'M': 0, 'L': -2, 'N': 0, 'Q': 5, 'P': -1, 'S': 0, 'R': 1, 'T': -1, 'W': -2, 'V': -2, 'Y': -1}, 
           'P': {'A': -1, 'C': -3, 'E': -1, 'D': -1, 'G': -2, 'F': -4, 'I': -3, 'H': -2, 'K': -1, 'M': -2, 'L': -3, 'N': -2, 'Q': -1, 'P': 7, 'S': -1, 'R': -2, 'T': -1, 'W': -4, 'V': -2, 'Y': -3}, 
           'S': {'A': 1, 'C': -1, 'E': 0, 'D': 0, 'G': 0, 'F': -2, 'I': -2, 'H': -1, 'K': 0, 'M': -1, 'L': -2, 'N': 1, 'Q': 0, 'P': -1, 'S': 4, 'R': -1, 'T': 1, 'W': -3, 'V': -2, 'Y': -2}, 
           'R': {'A': -1, 'C': -3, 'E': 0, 'D': -2, 'G': -2, 'F': -3, 'I': -3, 'H': 0, 'K': 2, 'M': -1, 'L': -2, 'N': 0, 'Q': 1, 'P': -2, 'S': -1, 'R': 5, 'T': -1, 'W': -3, 'V': -3, 'Y': -2}, 
           'T': {'A': 0, 'C': -1, 'E': -1, 'D': -1, 'G': -2, 'F': -2, 'I': -1, 'H': -2, 'K': -1, 'M': -1, 'L': -1, 'N': 0, 'Q': -1, 'P': -1, 'S': 1, 'R': -1, 'T': 5, 'W': -2, 'V': 0, 'Y': -2}, 
           'W': {'A': -3, 'C': -2, 'E': -3, 'D': -4, 'G': -2, 'F': 1, 'I': -3, 'H': -2, 'K': -3, 'M': -1, 'L': -2, 'N': -4, 'Q': -2, 'P': -4, 'S': -3, 'R': -3, 'T': -2, 'W': 11, 'V': -3, 'Y': 2}, 
           'V': {'A': 0, 'C': -1, 'E': -2, 'D': -3, 'G': -3, 'F': -1, 'I': 3, 'H': -3, 'K': -2, 'M': 1, 'L': 1, 'N': -3, 'Q': -2, 'P': -2, 'S': -2, 'R': -3, 'T': 0, 'W': -3, 'V': 4, 'Y': -1}, 
           'Y': {'A': -2, 'C': -2, 'E': -2, 'D': -3, 'G': -3, 'F': 3, 'I': -1, 'H': 2, 'K': -2, 'M': -1, 'L': -1, 'N': -2, 'Q': -1, 'P': -3, 'S': -2, 'R': -2, 'T': -2, 'W': 2, 'V': -1, 'Y': 7}}

def LinearMidEdge(v, w, top, bot, l, r):
    graph = [[0 for _ in range(2)] for _ in range(bot-top+1)]
    back = [[0 for _ in range(2)] for _ in range(bot-top+1)]
    mid = int((l+r)/2)
    
    
    for i in range(bot-top+1): graph[i][1]-=i*5
    
    for i in range(l+1,mid+2):
        for j in range(bot-top+1): graph[j][0]=graph[j][1]
        graph[0][1]=graph[0][0]-5
        for j in range(1,bot-top+1):
            graph[j][1] = max(graph[j-1][1]-5,graph[j][0]-5,graph[j-1][0]+BLOSUM62[v[j-1]][w[i-1]])
    
    
    for i in range(bot-top,-1,-1): back[i][1]=-(bot-top-i)*5
    
    for i in range(r,mid,-1):
        for j in range(bot-top,-1,-1): back[j][0]=back[j][1]
        back[bot-top][1]=back[bot-top][0]-5
        for j in range(bot-top-1,-1,-1):
            back[j][1] = max(back[j+1][1]-5,back[j][0]-5,back[j+1][0]+BLOSUM62[v[j]][w[i-1]])
            
    
    sum_ = [[0 for _ in range(2)] for _ in range(bot-top+1)]
    max_graph, max_back, max_i, max_j = -1e9, -1e9, 0, 0
    for i in range(bot-top+1):
        sum_[i][0] = (graph[i][0]+back[i][1])
        if(max_graph <= sum_[i][0]): 
            max_graph = sum_[i][0]
            max_i = i
            
        sum_[i][1] = (graph[i][1]+back[i][0])
        if(max_back < sum_[i][1]): 
            max_back = sum_[i][1]
            max_j = i
            
    print((max_i,mid),(max_j,mid+1))

    
v, w = input().split()
LinearMidEdge(v,w,0,len(v),0,len(w))
```

    NKCKEFPELCTLTKSWNKCCNTQYQCTHKTVIEVHDNIAIDQECLEHNSDISLRRTQFDCMDHHFHFTIKEGNIYEWFKYNKHHGFNEWWITTLMNESEPNVLHKYEEFWQNLGNMGTFTQCMRITNLPYQCKWYPSEEGDWPICIWNAEHRTIHAGDPDCQVQGTAGISWRGERFNHVRPERLVAKYPESKFEKSNFYNAQCYVQPYEPQWAMSRTCALMPTTPWDNGDESIMSGRMPETINFDKVTKVPAQHSNVWCSKQLQKKEKMYDEIAQCDDCTWFMIDGFPTTMQYNSMVKAAQKQHGDVGFDKAMYSHALNNSSVFLERVQLVMELNEFWAQDVGKIVHHVYYKRYTTYEEAHYPKGQAHFKMVVRNMKGGCMHVHHMAWTILGLEVYQDKVMPHASHVLVHHGLMSPAMYYSIYDEVNDRNSFTFWRHFMWGYPRHWEHVVRKPNDAFWVISNWFFDMGYPDTHGTTRMMKFTLQVAGPMMSIMQSTGDFVRVSFTIGMECCLQRAHHQDCERVAAYFCHDCRYNNCHIVGKCTMFRRENPERTMSQKCNTMAMHFTYIASLTIHPSYGWKSGFQVCKSGNPQDLQRDLENMWFSVQYEFKYSSMWPFHSCGGQGCYTKGYYGNDIVPQPAYFEQNCSKCLISLVRYGWLMAPVYGRVHTIIQQECLWQALLNWNTKFGCITECQCSCWVWFHCPEEADHHARDLPLHYDWSFPKVYYNKCEKFCFWGCWIHYMKILMTDMYYVHPYYQIPESLNNSEYYFEGTWAKGIFWWWVVKAHYFTYRVIPLIKSLSAHHIITTMYCMYNFWGNDQLMEWGGFFNADQQINTSEYPSLWYMNVIMSDNGESKHFCINSMYYFHKVLESIWVGTKSITGFVSFKHVMYFTQNIIYPFQRSWGCMTIWASWFSVFFDMHKWFINFDIAMRKMCAISVIPMEGWIGQPGPMWRPGVIDHDCRTGQREPCTISDFTTGFFWQSQSFYIGVKSFHIAFVWGDQVTKMQIKINNYHHDWWQWALSDFCMDIKEVHVG KWMWHPWDLEKGSVIQTLKQYAAFGVMRSSHLKRFVDYGLMVRKDKNFTTIVKYFFKKQYQPTIVRHNGHHVEIHLMGEMQYLFGIRARYNSHLWISVLMPTQTATPIRFVWYVSKPVIPHRRGDEGNHKNYETIQNMWCEMRDMIMYYFYICLCNPLPTVVLRMEIAFIIRSFFKEMQPCMSHMKNYRYLAGTYWWITQYVADADAMADIICCLIWEKLIKKETLEVAVATNLITVFCWIHFLMIEIHTYGYGPEWHVRMTKIQVCECFGWDKGCDGIRLFKQQHPEEYGTKYLTVRQLKIPAFYGFVNMSIEGDCFSSFKEPKLHLPMIDNGFYQEHMPRDGMRNTTNYHNSSTCTETWSTFVYPKRVERFRKFHMALYRVYLWMKNCHQEHKSSCTCKYRAHLAQWVEWGCIGAQDYSMTQAAYMCICKRLSYHCVVPCFVDEIPHLRKPNDAFWVIPHDTHGTTRMMKFMSIMYMEAQSTVSFTIGHECCLQRAHHQDCEHVAAYFCHDRGRCCRYNNCHIVGKCTMFRTERTDKKCKCRRRMIERTMSQKFNTMFLLGGVYMHFTNEGAIYSLTIHPSYGRKSGFQVMTKNCNACNTCEFHASKVIVDPHQGFSWQETVLFHNEPVVTADAHMKGMLDVQAQAVSEALWRVDCGRDNMNVMSEKRPEMIVSFHECSATPDEVAWWCNIAHMWLVYRAQQGAMQIEGLQDWMDGHFHRWGFDGPAVDKNNAEGPHAADSEEAMRCQRHPKCTINRDPPGSNFLVGCDNDIAKELKIPLGPVMAQCNDADIGIAMDQVSKWYPHCDANEGVITGKIAYTTAISGAITTDYVDNYHLSIDPEPMMRRISTSGGSLFNGWNGHFYIIPTLVILWPAEKCFEDKAVELMLPWKGGIHNYTKAQVDECMHQQIMVLTAHDGCNTPSIEAQCNTYFGCKDDIEWRTQFHVIGPQPESMRTELDSTQGVYHRDGNGIQYLDWDMPHIQRENFKLRNQNSIAGPEDRCFNSDEEEKAHANFFGCGLNQSNPPFYWKNKNKYIMIHYD
    (534, 521) (535, 522)



```python

```
