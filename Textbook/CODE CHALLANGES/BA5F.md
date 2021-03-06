# Find a Highest-Scoring Local Alignment of Two Strings
## Problem
Local Alignment Problem
Find the highest-scoring local alignment between two strings.

Given: Two amino acid strings.

Return: The maximum score of a local alignment of the strings, followed by a local alignment of these strings achieving the maximum score. Use the PAM250 scoring matrix and indel penalty σ = 5. (If multiple local alignments achieving the maximum score exist, you may return any one.)


```python
import sys
limit_number = 15000
sys.setrecursionlimit(limit_number)

PAM250 = {'A': {'A': 2, 'C': -2, 'E': 0, 'D': 0, 'G': 1, 'F': -3, 'I': -1, 'H': -1, 'K': -1, 'M': -1, 'L': -2, 'N': 0, 'Q': 0, 'P': 1, 'S': 1, 'R': -2, 'T': 1, 'W': -6, 'V': 0, 'Y': -3}, 
'C': {'A': -2, 'C': 12, 'E': -5, 'D': -5, 'G': -3, 'F': -4, 'I': -2, 'H': -3, 'K': -5, 'M': -5, 'L': -6, 'N': -4, 'Q': -5, 'P': -3, 'S': 0, 'R': -4, 'T': -2, 'W': -8, 'V': -2, 'Y': 0}, 
'E': {'A': 0, 'C': -5, 'E': 4, 'D': 3, 'G': 0, 'F': -5, 'I': -2, 'H': 1, 'K': 0, 'M': -2, 'L': -3, 'N': 1, 'Q': 2, 'P': -1, 'S': 0, 'R': -1, 'T': 0, 'W': -7, 'V': -2, 'Y': -4}, 
'D': {'A': 0, 'C': -5, 'E': 3, 'D': 4, 'G': 1, 'F': -6, 'I': -2, 'H': 1, 'K': 0, 'M': -3, 'L': -4, 'N': 2, 'Q': 2, 'P': -1, 'S': 0, 'R': -1, 'T': 0, 'W': -7, 'V': -2, 'Y': -4}, 
'G': {'A': 1, 'C': -3, 'E': 0, 'D': 1, 'G': 5, 'F': -5, 'I': -3, 'H': -2, 'K': -2, 'M': -3, 'L': -4, 'N': 0, 'Q': -1, 'P': 0, 'S': 1, 'R': -3, 'T': 0, 'W': -7, 'V': -1, 'Y': -5}, 
'F': {'A': -3, 'C': -4, 'E': -5, 'D': -6, 'G': -5, 'F': 9, 'I': 1, 'H': -2, 'K': -5, 'M': 0, 'L': 2, 'N': -3, 'Q': -5, 'P': -5, 'S': -3, 'R': -4, 'T': -3, 'W': 0, 'V': -1, 'Y': 7}, 
'I': {'A': -1, 'C': -2, 'E': -2, 'D': -2, 'G': -3, 'F': 1, 'I': 5, 'H': -2, 'K': -2, 'M': 2, 'L': 2, 'N': -2, 'Q': -2, 'P': -2, 'S': -1, 'R': -2, 'T': 0, 'W': -5, 'V': 4, 'Y': -1}, 
'H': {'A': -1, 'C': -3, 'E': 1, 'D': 1, 'G': -2, 'F': -2, 'I': -2, 'H': 6, 'K': 0, 'M': -2, 'L': -2, 'N': 2, 'Q': 3, 'P': 0, 'S': -1, 'R': 2, 'T': -1, 'W': -3, 'V': -2, 'Y': 0}, 
'K': {'A': -1, 'C': -5, 'E': 0, 'D': 0, 'G': -2, 'F': -5, 'I': -2, 'H': 0, 'K': 5, 'M': 0, 'L': -3, 'N': 1, 'Q': 1, 'P': -1, 'S': 0, 'R': 3, 'T': 0, 'W': -3, 'V': -2, 'Y': -4}, 
'M': {'A': -1, 'C': -5, 'E': -2, 'D': -3, 'G': -3, 'F': 0, 'I': 2, 'H': -2, 'K': 0, 'M': 6, 'L': 4, 'N': -2, 'Q': -1, 'P': -2, 'S': -2, 'R': 0, 'T': -1, 'W': -4, 'V': 2, 'Y': -2}, 
'L': {'A': -2, 'C': -6, 'E': -3, 'D': -4, 'G': -4, 'F': 2, 'I': 2, 'H': -2, 'K': -3, 'M': 4, 'L': 6, 'N': -3, 'Q': -2, 'P': -3, 'S': -3, 'R': -3, 'T': -2, 'W': -2, 'V': 2, 'Y': -1}, 
'N': {'A': 0, 'C': -4, 'E': 1, 'D': 2, 'G': 0, 'F': -3, 'I': -2, 'H': 2, 'K': 1, 'M': -2, 'L': -3, 'N': 2, 'Q': 1, 'P': 0, 'S': 1, 'R': 0, 'T': 0, 'W': -4, 'V': -2, 'Y': -2}, 
'Q': {'A': 0, 'C': -5, 'E': 2, 'D': 2, 'G': -1, 'F': -5, 'I': -2, 'H': 3, 'K': 1, 'M': -1, 'L': -2, 'N': 1, 'Q': 4, 'P': 0, 'S': -1, 'R': 1, 'T': -1, 'W': -5, 'V': -2, 'Y': -4}, 
'P': {'A': 1, 'C': -3, 'E': -1, 'D': -1, 'G': 0, 'F': -5, 'I': -2, 'H': 0, 'K': -1, 'M': -2, 'L': -3, 'N': 0, 'Q': 0, 'P': 6, 'S': 1, 'R': 0, 'T': 0, 'W': -6, 'V': -1, 'Y': -5}, 
'S': {'A': 1, 'C': 0, 'E': 0, 'D': 0, 'G': 1, 'F': -3, 'I': -1, 'H': -1, 'K': 0, 'M': -2, 'L': -3, 'N': 1, 'Q': -1, 'P': 1, 'S': 2, 'R': 0, 'T': 1, 'W': -2, 'V': -1, 'Y': -3}, 
'R': {'A': -2, 'C': -4, 'E': -1, 'D': -1, 'G': -3, 'F': -4, 'I': -2, 'H': 2, 'K': 3, 'M': 0, 'L': -3, 'N': 0, 'Q': 1, 'P': 0, 'S': 0, 'R': 6, 'T': -1, 'W': 2, 'V': -2, 'Y': -4}, 
'T': {'A': 1, 'C': -2, 'E': 0, 'D': 0, 'G': 0, 'F': -3, 'I': 0, 'H': -1, 'K': 0, 'M': -1, 'L': -2, 'N': 0, 'Q': -1, 'P': 0, 'S': 1, 'R': -1, 'T': 3, 'W': -5, 'V': 0, 'Y': -3}, 
'W': {'A': -6, 'C': -8, 'E': -7, 'D': -7, 'G': -7, 'F': 0, 'I': -5, 'H': -3, 'K': -3, 'M': -4, 'L': -2, 'N': -4, 'Q': -5, 'P': -6, 'S': -2, 'R': 2, 'T': -5, 'W': 17, 'V': -6, 'Y': 0}, 
'V': {'A': 0, 'C': -2, 'E': -2, 'D': -2, 'G': -1, 'F': -1, 'I': 4, 'H': -2, 'K': -2, 'M': 2, 'L': 2, 'N': -2, 'Q': -2, 'P': -1, 'S': -1, 'R': -2, 'T': 0, 'W': -6, 'V': 4, 'Y': -2}, 
'Y': {'A': -3, 'C': 0, 'E': -4, 'D': -4, 'G': -5, 'F': 7, 'I': -1, 'H': 0, 'K': -4, 'M': -2, 'L': -1, 'N': -2, 'Q': -4, 'P': -5, 'S': -3, 'R': -4, 'T': -3, 'W': 0, 'V': -2, 'Y': 10}}

def LABackTrack(v, w):
    graph = [[0 for _ in range(len(w)+1)] for _ in range(len(v)+1)]
    BackTrack = [['' for _ in range(len(w)+1)] for _ in range(len(v)+1)]
    maxnode = (0,0)
    
    for i in range(0,len(v)+1): BackTrack[i][0]+='s'
    for j in range(1,len(w)+1): BackTrack[0][j]+='s'
    
    for i in range(1,len(v)+1):
        for j in range(1,len(w)+1):
            graph[i][j] = max(0, graph[i-1][j]-5,graph[i][j-1]-5,graph[i-1][j-1]+PAM250[v[i-1]][w[j-1]])
            if(graph[i][j] > graph[maxnode[0]][maxnode[1]]): maxnode = (i,j)
            
            if graph[i][j]==0: BackTrack[i][j]+='s'
            elif graph[i][j]==graph[i-1][j]-5: BackTrack[i][j]+='d'
            elif graph[i][j]==graph[i][j-1]-5: BackTrack[i][j]+='r'
            elif graph[i][j]==graph[i-1][j-1]+PAM250[v[i-1]][w[j-1]]: BackTrack[i][j]+='m'
    
    print(graph[maxnode[0]][maxnode[1]])
    return BackTrack, maxnode

def OutputLA(backtrack, v, i, j):
    if backtrack[i][j]=='s': return ''
    elif backtrack[i][j]=='d': return OutputLA(backtrack, v, i-1, j) + v[i-1]
    elif backtrack[i][j]=='r': return OutputLA(backtrack, v, i, j-1) + '-'
    else: return OutputLA(backtrack, v, i-1, j-1) + v[i-1]

def OutputLA2(backtrack, v, i, j):
    if backtrack[i][j]=='s': return ''
    elif backtrack[i][j]=='d': return OutputLA2(backtrack, v, i-1, j) + '-'
    elif backtrack[i][j]=='r': return OutputLA2(backtrack, v, i, j-1) + v[j-1]
    else: return OutputLA2(backtrack, v, i-1, j-1) + v[j-1]

v, w = input().split()
BT, maxnode = LABackTrack(v, w)

print(OutputLA(BT,v,maxnode[0],maxnode[1]))
print(OutputLA2(BT,w,maxnode[0],maxnode[1]))
```

    LWRPMVLNGAYQKTMNCNYTMYMESSSKGLSPWANAHDCYMCQIPKWTCSHFDAKVEWSYHNKICPMGIAFKRSPNAAHEPCTFISGASRYKIPCYRGHKYPQWMIPAFWMPAERDPMGCGYHNNRYVFWRDCSPEKEPLSNFMPYQCDSQLPNRKDNSHETVVRPPHMSHSYDPQMGGLQFRYLTCCMNRTGIEVVNPHSVNWKCHHAVDWCFYWNLYMLHYFATLTGQDNTAWCTTFKTEASYNNQCQAGYTLKHCVCNPHPGKDKRRLCVKWYTETHQEWGEWRQAMDTRQSMSQARKEKFRAAQFTDRLFSAMRHVMPDDGLWASQYVNNVFSPFHEAYTDDEWSPYKKGQDQPLLTVTPFWTAEWTSLWSCTCEKIDPNEWSLNTWCMLWSQRHCVISNPQRTQWANKNHGVHHQVSQPRWQCWGCRHWKSHDSQIQQNQCFFKDSQTMRLIFRGHWMYKNMCIQESATEDSELDNYIDMKIYRSEVVMMAMSTFRRTTREPWCKWKPTCVPWGLLSCPHYHEGTRMWEKTTHYLGKCRCWLFWPAMKQSVKQKKPTRRQRWQKAIHDYQFCCTDEFTRWWFAMGVCQQWLKVACETFLRSKSSTPMHCKFADQWIFFIEPTVYWYMDEYLFKCIRKHEEEILRWVMSWSGNWPERSMMHWESVSTGSNKMADFAVVMDFGTVSPRWDKCYCWFMSPLDFTPVYCQIIRDDWHAFFRENSLGWEPDGWFKSPVLDDSQLEYDTAWGIFKMCHMMPVYDWFHLCLVSHWDLDKDAIYYLQERHDHYPVNLDIWCNLFTASGYATLGQDTRWEYVTKMMFFTRLSTLVNWYRFRSIRQYHSKAAIIHIYDQNPAPVKCFEEDETTNFNSVGMWIETICSSLDIWYWAMKYQPTEMTIQYICVNPWRRLTKYGIMTGQRAMDMFYPEQHYDEKTMHCMSAYNYMWPFCHIYEHAGWHYNWTAKRLVVTLYLLQVTCHMSIAVMMKPTAMNSKNPRILYNWPMMTPDFCGVGWYMRFDNCRICHKLIFVHAIRAWGANFVQVFHQTKIMIQKGQYSNFNPQVLCADNLYQWPAAWKIFFFCLAQHRGCCWHKGAQVKPLHFYCKWNFRKFQLIPPEKVDVSLVQYCEQANTSTGENIFMLWWYFQLLNQQISGMGWVVTTMCDWAYPMYTKAVHHTSMGMWWQVMEQMWFTGPYQKFAFPCPGNTACIVTDPETKMRQGRMKYHNPIKHQFDCCMYCAVWDMNVMWFCAKWQPCWADGHGQHNDWCVEHAHTEVEGGLICYPEKKLKILGPRDNTIVWSDAVWITRGYFFGIEVWCPAREQIDQACKMSPLSSMFCEEREYGDVFHDVYQIMLQMPGKVYPQMFSFCLEWSVKQAFTMIVGCQITDPEISVWWSHAVHTALEMKSISAKFQKHVWNYYTGEMTWWCNGSGPVVKLEDDQQLCMNPEIMDSYRAITNSHIMNYWGFDWKVAIIWKHTQKEMEMFFSLFPINQDQWHIGWRSCQYTCRDMVSGPHSEIYSKTFPAKFDLCGIHRATAKFFHEPQHCCMQAIFSQAWTGHPICMQSTTKNMVRRPSTNLLQNQTKIIVINARSDAFSRHWFPKTYMRMGKRTHPYLASTMSCNQTTYFCVNEYWGKQTLQYNLPKYGYNDTWQAHFIYYCWSMACDEDFNVEKCPCFIWTEFWFMSFTIMYMDCHVYHVMNYGSLIVRRYKFSTALFKHLKSTECYAHYLGAWDRKKSHTGSQQEDQYIMEHGEWMCGISNTAGWSYFKMWSRQDMQFKWYNNQVFCWPLDKQLIDPTISDSPPLKWIKTSNIAYNQYHCGVLHEATTDCWWNRPIKDNYMWLPGRMILRWHKMWQQCGISYFSPPYQEEGLFKPEVIMTPSCIVEQFDGLQCHGFNREDSPLFQINVPKPTQNNNMSGDDYLPVDYILNFRNMMRHVMCFVEMNDFEHWYSKGYQSWDSDMCDLKWSWRMWDFVTQMNCNNKCCNKHRQTQWIFPWTDRYIHIVNANCLQHIMSWNMQRVNMIVHHIIFQPQDQYILRFECTQGYHRFAFTMTECKTQNLARFNFMFENWMQGDFMAAPAPGGKPEVTRYMQASRFYLQFHIKDPYTCSPFPETKVAMNCLVRRNNCNVEDYYMRKVFWYDRRMCLWTPTHVIMLQMHWFKWPDEPRDAMPDKSTQESLVSQGWCHQIQENRILILADEHKTTDNLRRHQRAEHNQPPRGDKSTEFFGNLGGPMLCAHANYWFDLKSGVYLHSRDPAHHQMLSFHDPIWILPADWMLIHPVMNVVQGNNVYQYKMYSEQEEQLSPATQGGLLLPFLYDQVAPSRVAFKQQQNSYQEDGMWFNHGAGGCMEQYGWDTPYWRWWTCEQNHSKNSQTEPHLVFSNAAKQWWTWPMYGAWVICVFPRWEYQHMRMPSLTISACDGHMGMVRMKFNPLQQSYSNLKVFSFIHYVAMIACYCKLSCGSEQDTKHCLWQHHEILCIELVPQFWESCTHNVAKFKSMSCTLMYECGETTIWWCMLALKDETDQENYAILQTYWQYFTKYVDDECWPCMGIAQYVALVHDHQACSMFALSVQMDRAHKQAEGKSPRCLENCRPGIFRFENHASDYDTKPVTPYDHCEVMTSEKCEYEAQLLSDGYRTDYWNPNFVKMTYVIHKIQYQCAETRQNSHTKMHTHAAVQIRDMWMWWMTWWSACGSIRAWMRA MEFGIKSLVMKRLELSDREQAPDDLPFGTLGWRNWDSAREETPSHIHERVSLYYLHREGDNMCIRPFCRQDLFSRNVPDMMRFRLTWGLLQNLVVRVRDHNSLKCVRIFPCFSCQFHCFITPYPLMHPLFYPGGISHDWKHWAVYVRGEKMINDPADTISKEWSNIPYMHQYVCNPCHFYYYTQMDHDNLYMCVHWNIEVVDNYCHNNDTYPWAACFHCEMRASHSPGYYQGGYWEPTCPARHAHSQDPMTWFNLEVFIPLTPETWGPRLDWHFLPKCVNTAKMQKCSYAQDQSMKVPAKKDEFWFHQICQDRYIPTHPDMPEKTLWAMLHDVYQRMQTCKSYMGKFQHHDGYHMDIYFQAFAQCMRNWLSHYQDSNIDWNQPLPEAFKCVKKYWSCRVWVSDMTGSNWNKKCHLPPYMNNWECAFHGLHWETMAYHLNMAKVAEHVKEMTEHCGMANCLWDSMSFQDIVHHLDQEHVNGDRVYWWTDWMWINQKPTKPIVQFSFTGHTHNDVSCAQRPKEYLNEATLVVDINHAYGMFTPCTWINTACSASEAEYCARTVQHIIMNFYCTKPNKIRHGMEQTNSPNNKINHFWGNQNRTQEGSHVHIMCVSFYGAKLEWMNGLPPKMYTNTMNKDVDMIPIPMGKLHAITWCLTILKYVTYGRKTWIGSFSMQNMCQPAVIFIIQNHWEGLHENEWYTMMNWEAIPIRLCICQQHYFWVAHMSSGYWFFTCYQFKIHGYSIMVRSHRKFVYFTSNWMFRQALALGYHNPVVISVAHEFDEKILMEYHIPESHSKEKDGKDCFCWADWIVYLPKRFIAYVEYLVNYRNKKILVPYKYDVSCNTNDTQCYGHTNRSARQTMIRQRAMDSIIPGDYDPFVKLVPGTHCMSAYQFNHIYLHAGTHKNWTAKRLTLYLLQVTCHSPKVIWMSQASFEIGVMKMMKPTRIHFESRFTQNSKNVKRGCHPRILYNWEVFYPGVCGPRFETTYHMSLICKKLIFVHAIYVWGIAFVACKESVFHQTKIMIQQGQYSFSNVEEHQVYQWPAAWKIRFSPCQCFFHHRFFRMYYLAQHRHMVKPWKFGKEFYCNNREKVDVSLQENTSTGENILWSLWWYFQLLNSQISGMGWVVWTEDTMCDWAYPMYTKAVNNGMWWQVMEGMWFTGMECYQKFAFPCPYYWTWVTNNYFCRQPRYKDCCNNIMVWTCAGRCKNGFFVAKWQPCWADGHGQHNDWCEDAHTEVEGGLICYPEKLGPRDNTIVWSDAVWITRGYFFGIEVWCPAREQIDKCCEREGHHFNGDVFHDVVVYPQMFSFCLEWSVKQAFTMIVGCQITDPEISVWWSHAVTALEMKSIKMSKWLKIYYTGEMTWSPQEIPPGSGPVVKLEDDDSSIWKLCMNPEIMDSYRAITNSHIMNWKHTQKEMEMFFSLFPINQDQWQIGWRSCQDTCRDMVSFPHSEIYSKTAGIIPWDVKLCSYNCDLCGAKFFCEPHMQAWPGIKICMQWTTKNMVRRPSTLLQNQTKAFSRWFGKTYMRMGKRTHPKLASTMSCNYFCPKYGYNSGTHKTHKRDLQAHCDCFNQCGDFNQEKCPCFIWTEFWFMSFTSMYMDCHVYHVKNEDADDTTAWGSWIVERYFSSTALFKHLGSTARMCYAHYLGTDRKKSIHVKTRAGQTQEDQYIEAGEWMPNHAGNSYGFQDMGFKWYNNQFCWPLDKQLIDPTKSPPLKWIKTSNIAYNQYHCGVLHVGMPFQATTSCWWNRLYMWLPGRMIRWHKIWQQCGISHFSTTPQEEGSFKEVIMTPSCGLQCHGFNCEDVKPLYMWIWDDQINRPKPVFWELGQNESNMSGDDYGHDLDSPDDAFQTDYYLNFRTEMNDTEGYQSWDSTMLKMWDFVTQMNCNNTCSCGPPIHMDSIDPQCYFDLLVNIIPVWTQVFFAGSLTAQRGHSMHRHVVCVCECSLVYIPWLHSLTHDNVSSVYGEFRDKEQEKHHSMWGVDMQYICEFPVGQRHEAHCYQISPFDQKGLNKKIAKGDAADHPEACMADWPYQTGRWPPRWNVIWPGHETCGENVPEHDINIKHWVLIAKECYRMIVMSFQMVSHHVDGSLLKIGSYYVPQGEENEWPSLPMMSKYVALVSVYTQNQITGWEHSGERDTGRVWNWHPTNYVMRTVANPFYHQEPNYQRCVGNHASNAGPKLRSHRERPERDTKGVSVIIWHHCKCQPYNPIDRVDYKNVFSGDQQMPVCDWNSIQVSHETMKIRCNSNAQPTGEMPGYSKLCHQGRGRVNKYMKHMNPDQYTLTSKPMDKKFFASHWYRTGWFPYCFASWKQTDPHFHDVRHTTGLDCTHLCMSQQDDSGNLLIRLCDTLMRYASQWYWSHFPHPKVEPWNGDDGIRMQDKSAWEQAAFHSMGEILSLANHKKGIFNWRRTEDNTEWYRWLGRRYYHESQFSQTMNIRVKIVTACNSASAKKIRLGKNLFPEEVLYVSFHCETFMCGHHRPQQGMMCNNPPMAQHVREKMSPSFHAWNFCHMIFEHWLLEPVKVYACTCHYFFQYVNHSGYWYCHKSCFLITYKQLWHAPYTQLCIPKALCLDTQDPMQSVHHQIEVSYQLEIVPWWAYSNHKKPEETMWTQSDPGFFAFWQHMDEANNKGNILLWHHMWCYMKVYIVHESWMVTACMRVEFSHK
    3648
    KWTCSHFDAKVEWSYHNKICPMGIAFKRSPNAA-HEP-CTFISGASRYKIPCYRGHKYP-QW-MIPAFWMPA-ERDPMGCG--YHNNRYVFWRDCSPEKEPLSNFMPYQCD-SQ-LPNRKDNSH-ETVVR-PPH-MSHSYDPQMGGLQFRYLTCCMNRTGIEVVNPHSVNWKCHHAVDWCFYWNLYMLHYFATLTGQDNTAWCTTFKTE--ASYNNQC-QAGYTLKHCVCNPHPGKDKRRLCVKWYT-ETHQEWG-E-WRQAMDTRQSMSQ-ARKEKFRAAQFTDRLFSAMRHVMPDDGLWASQYVNNVFSPFHEAYTDDE-WSPYKKGQDQPLLTVTPFWTAEWTSLWSCTCEKIDPN-EWSLNTWCML-WSQRHCVISNPQRTQWANKNHGVHHQVSQPRWQCWGCRHWKSHDSQIQQNQCFFKDSQTMRLIFRGHWMYKNMCIQESATEDSELDNYIDMKIYRSEVVMMAMSTFRRTTREPWCKWKPTCVPWGLLSCPHYHEGTRMWEKTTHYLGKCR-CWLFWPA-MKQSVKQKKPTRRQRWQKAIHDYQFCCTDEFTRWWFAMGVCQQWLKVACETFLRSKSSTPMHCKFADQWIFFIEPTV-YWYMDEYLFKCIRKHEEEILRWVMSWSGNWPERSMMH-WESVSTGSNKMADFAVV-MDFGTVSPRWDKCYCWFMSPLDFTPVYCQIIRDDWHAFFRENSLG-WEPDGWFKSPVLDDSQLEYD-TAW-GIF--K-MCHMMPVY--D--WFHLCLVSHW-DL-DKDAI-YYLQERHDHYP-V-NL--DIW---CNLFTASGYATLGQDTR-WEYVTKM-MFFTRLSTLVNWYRFR---SI-RQYHSKAAIIHIYDQNPAPVKCFEEDETTN-FNSVGMWIETICSSLDIWY--WAMKYQPTEMTI--QY-I-C-VN-P--WRRLTKYG--IMTGQRAMDMFYPEQHYDE--KTM---HCMSAYNYMWPFCHIYEHAGWHYNWTAKRLVVTLYLLQVTCH------MS-----IAVM-M-KPT-----AM---NSKN------PRILYNWPMMTPDFCGVGWY-MRFDNCRICHKLIFVHAIRAWGANFV---Q-VFHQTKIMIQKGQYSNFNPQVLCADNLYQWPAAWKIFFF-C--LAQHRGCCWHKGAQVKPLHFYCK-WNF-RKFQLIPPEKVDVSLVQYCEQANTSTGENIF-MLWWYFQLLNQQISGMGWVV-T--TMCDWAYPMYTKAVHHTSMGMWWQVMEQMWFTG-P-YQKFAFPCPGNTACIVTDPETKMRQGRMKYHNPIKHQFDCCMYCAVWD-MNV-M--WFCAKWQPCWADGHGQHNDWCVEHAHTEVEGGLICYPEKKLKILGPRDNTIVWSDAVWITRGYFFGIEVWCPAREQIDQACKMSPLSSMFCEEREYGDVFH-DVYQIMLQMPGKVYPQMFSFCLEWSVKQAFTMIVGCQITDPEISVWWSHAVHTALEMKSISAKFQKHVW-N-YYTGEMTWWCN----GSGPVVKLEDDQ----QLCMNPEIMDSYRAITNSHIMNYWGFDWKVAIIWKHTQKEMEMFFSLFPINQDQWHIGWRSCQYTCRDMVSGPHSEIYSKT--F-PAKFDLCGIH-RA-TAKFFHEPQHCCMQAIFSQAWTGHPICMQSTTKNMVRRPSTNLLQNQTKIIVINARSDAFSRHWFPKTYMRMGKRTHPYLASTMSCNQTTYFCVNEYWGKQTLQYNLPKYGYNDTWQAHFIYYCWSMACDEDFNVEKCPCFIWTEFWFMSFTIMYMDCHVYHVMN--------YGSLIVRRYKFS-TALFKHLKSTE--CYAHYLGAWDRKKS-H--T-GSQ-QEDQYIMEHGEWMCGISNTAGWSY-FKMWSRQDMQFKWYNNQVFCWPLDKQLIDPTISDSPPLKWIKTSNIAYNQYHCGVLH-----EATTDCWWNRPIKDNYMWLPGRMILRWHKMWQQCGISYFSP-PYQEEGLFKPEVIMTPSCIVEQFDGLQCHGFNRED-SPLFQ-I-N--V--PKPT-----QNN-NMSGDDYLPVDYILNFRNMMRHVMCFVEMN-DFEHWYSKGYQSWDSDMCDLKWSWRMWDFVTQMNCNNKC-CNKHRQTQWIFPWTDRYIHIVNANCLQHIMSWNMQRVNMIVHHIIFQPQDQYILRFECTQGYHRFAFTMTECKTQNLARFNFMFENWMQGDFMAAPAPGGKPEVTRYMQASRFYLQFHIKDPYTCSPFP-ETKVAMNCL-VRR-NNCNVEDYYMRKVFWYDRR-MCL--WTPTHVIMLQMHW-FKWPDEPRDAMPDKSTQESL-VSQGWCHQIQE-NRILILADEHKTTDNLR-RHQRAEHNQPPRGDKSTEFFGNLGGPMLCAHANYWFDLKSGVYLHSRDPA-HHQMLSFHDPIWIL-PADWMLIHPVMNVV-QGNNVYQ-YK-MYSEQEE-QL-S----PATQG-GL-LLPFLY-D-QV-AP-SRVAFKQQQNSYQEDGM--W--FN--HGAGG--CM-E-Q-YGWDTP-YWRWWTCEQNHSK-NS---QTEP-HLVF-SNA-AKQWWT--WPMY-GAWV-ICVFPRW-EYQ-HMRMPSLTIS-ACDGHMGMVRMK-FNPLQQSYSN-LKVF-S--F-IHYV-AMIACYCKLSCGSEQDTKHCLWQHHEILCI-ELVPQFWESCTHNVAKFKSMSCTLMYECGETTIW--WCMLALKDETDQENYA-ILQTYW-QYFTKYVDDECWPC-MGIAQYVA-LVH-DHQACSMFALSVQMDRAHKQAEGKSPRCL-ENCRPGIFR-FENHASDYDTKPVTPYDHCEVMTSEKCEYE-A-QLLSDGY--RTDYW--NPN-FVKMTYV-IHKIQY-Q-C-AETR-QNSHTKMHT-HAAVQIR-DMWMWWMTWWS
    NWDSAR-EETPS-HIHERV-SL-YYLHREGDNMCIRPFCR-QDLFSR-NVP-DM-MRFRLTWGLLQNLVVRVRDHNSLKCVRIFPCFSCQF-H-CFITPYPLMHPLFYPGGISHDWKHWAVYVRGEKMINDPADTISKEW-SNIPYMH-QYV-C--NPCHF-YYYTQ-MD---HDNLYMCVHWNIEVVDNYCH-N-NDTYPWAACFHCEMRASHSPGYYQGGY-WEP-TCPARHAHSQDPM-T-WFNLEVFIPLTPETWGPRLD-WHFLPKCVNTAKMQKCSYAQDQ-S-MKVPAKKDEFWFHQICQDRYIPTHPDMPEKTLWAMLHDVY-QRMQTCKSY-MGKFQHH-D-GYH-MDIYFQ-AFAQ-CMRNW-LSHY--QDSN-IDW-N--QPLPEAFKCVK-KYWSCRVWVS-D--MTGSN-WNKKCH-LP-PYMNNW---E-C----AFHG--L-HWETMA-YHLNMAKVA-EHVKEMT-EH-CG-MANCL-WDSMS---FQDIVHHLDQE-HVNGD-RVYW--WTDWMWINQKPTKPIVQFSFTGHTHN-DVSCAQRPKEYLNEATLVVD-INHAYGMFTPC-TWINTACSASEA-EY-CARTVQHIIMN-F-Y-CT-KPNK-I-RHGME-QTNSPNNKINHFWGNQNR-TQEGSHVHIMCVSF--YGAKLE----W-MNGLP-PKMYTNTMNKD-VDMIPI-PMGKLHAITWCLT-ILK-Y-VTYGRKTWIGSFSMQNMCQPAVIFIIQNHWEGL-HENEWYTMMNWEAIPIRLCICQQHYFWVAHMSSGYWFFTCYQFKIHGYSIMVRSHRKFVYFTSNWMFRQALA-L-G-YHNPVVISVAHEFDEKI-LME-Y-HIPES-HS-KEKDGKDCFCWAD-WIVYLPKRF-IAYVEYLVNYRNKKILVPYKYDVSCNTNDTQCYGHTNRSARQTMIRQRAMDSIIPGD-YDPFVKLVPGTHCMSAYQF--N--HIYLHAGTHKNWTAKRL--TLYLLQVTCHSPKVIWMSQASFEIGVMKMMKPTRIHFESRFTQNSKNVKRGCHPRILYNWEVFYPGVCG-PRFETTYHMSLICKKLIFVHAIYVWGIAFVACKESVFHQTKIMIQQGQYS-FS-NVE-EHQVYQWPAAWKIRFSPCQCFFHHR-F-FRMYYLAQHRHMV-KPWKFGKEFYCNNREKVDVSL-Q--E--NTSTGENILWSLWWYFQLLNSQISGMGWVVWTEDTMCDWAYPMYTKAVNN---GMWWQVMEGMWFTGMECYQKFAFPCPYYWT-WVTNNYFC-RQPR--Y----K---DCCNNIMVWTCAGRCKNGFFVAKWQPCWADGHGQHNDWC-EDAHTEVEGGLICYPEK-L---GPRDNTIVWSDAVWITRGYFFGIEVWCPAREQIDK-C---------CE-RE-GHHFNGDVFH---DVV--VYPQMFSFCLEWSVKQAFTMIVGCQITDPEISVWWSHAV-TALEMKSI--KMSK--WLKIYYTGEMTWSPQEIPPGSGPVVKLEDDDSSIWKLCMNPEIMDSYRAITNSHIMN-W----K------HTQKEMEMFFSLFPINQDQWQIGWRSCQDTCRDMVSFPHSEIYSKTAGIIPWDVKLCSYNCDLCGAKFFCEP-H--MQA-----WPGIKICMQWTTKNMVRRPST-LLQNQTK-----A----FSR-WFGKTYMRMGKRTHPKLASTMSCN---YFCPK-Y-GYNS-G-T-HK-THKRDLQAH--CDCFN-QCG-DFNQEKCPCFIWTEFWFMSFTSMYMDCHVYHVKNEDADDTTAWGSWIVERY-FSSTALFKHLGSTARMCYAHYLGT-DRKKSIHVKTRAGQTQEDQYI-EAGEWM-P-NH-AGNSYGF-----QDMGFKWYNNQ-FCWPLDKQLIDPT-K-SPPLKWIKTSNIAYNQYHCGVLHVGMPFQATTSCWWNR-L---YMWLPGRMI-RWHKIWQQCGISHFSTTP-QEEGSFK-EVIMTPSC------GLQCHGFNCEDVKPLYMWIWDDQINRPKPVFWELGQNESNMSGDDY-GHD--LDSPDDAFQTDYYLNFRTEMND--TEGYQSWDSTM--LK----MWDFVTQMNCNNTCSCGPPIHMDSIDP--QCYFDLL-VNIIP-V--WT-Q-V-FFAGSLT--AQ-----R-G--HSMHRHVVCVCEC-S--LV-Y--I--PWLHS-LTHDNVSSVYGEF-RDKEQEKHHSMWGVDMQYICE-FPVGQRHEAHCYQISPFDQKGLNKKIAKGDA-ADHPEACMADW-PYQTGRWPPRWNVIWPG--HETCGENVPEHDINIKH-WVLIAKECYRMIVMS-FQMVSHHVDGSLLKIGSYYVPQGEEN-EW-PSL--PMM-S--KY-VALVS-VYTQNQITGWEHSGERDTGRVWNWHPTNYVM-RTVANPFYHQEPNYQRCVGNHASNAGPKLRSHRERPERDTKGVSVIIWHHCKCQPYNPIDRVDYKNVFSGDQQMPVCDWNSIQVSHETMKIRCNSNAQPTG-EMPGYSKL--CHQGRGRVNKYMKHMNPDQYTLTSKPMDKKFFASHW--YRTGWFPYC-FASWKQTDPHFHDVRHTTGLDCT-HLCMSQQDDSGNLLIRLCDTLMRYASQWYWSHFPHPKVEPW-NGDDGIRMQDK-SAWEQAAFHSMGEILS-L-AN--HKKGIFNWRR-T---E-DNTE-WYRW--LG-RRYYHESQFSQTMNI-RVKIVTACNSASAKKIRLGKNLFPEEVLYVSFH-CETF-MCGH-HRPQQGMMCNNPP-MAQHVREKMSPSF--HAWNF-CHMI--FEH-WLLEPVKV-YACTCHYFFQ-YVNHSGYWYCHKSCFL-ITYKQLWHAPYTQLCIPKALCLDTQDPMQSVHHQIEVSYQLEI--VPWWA



```python

```
