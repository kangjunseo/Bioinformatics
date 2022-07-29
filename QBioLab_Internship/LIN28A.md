# LIN28A

# Summary

### About LIN28

- LIN28의 3가지 중요 역할 : developmental transition, glucose metabolism, tumorigenesis
- matuation of let-7 microRNAs 억제
- translation of certain mRNAs 향상

### In This Study

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled.png)

- obtain genome-wide view of molecular function of LIN28A
- RNA crosslinking-immunoprecipitation-sequencing(CLIP-seq), ribosome footprinting 활용
- large number of spliced mRNAs에 결합
    - AAGNNG, AAGNG, UGUG(less freuently) 인식
    - terminal loop of a small hairpin에 있음
- periendoplasmic reticulum (ER) area 근처에 존재
    - ER로 갈 예정인 mRNA들의 번역 억제
    - transmembrane proteins, ER/Golgi lumen proteins, secretory proteins의 합성 감소
    

따라서, 본 논문은 ER-associated translation을 위한 selective regulatory mechanism을 제안하고, LIN28A의 secretory pathway에 있는 gene의 global suppressor로서의 예상치 못한 역할들을 밝혀냄.

# Introduction

### LIN28

원래는 *Caenorhabditis elegans*(회충)의 developmental timing regulator 역할의 conserved RNA binding protein, animal development 중에 발현이 엄격히 억제됨

- *Lin28a*와 *Lin28b* 두가지의 homolog
- *Lin28a*는 embryonic stem cells (ESCs)에서 잘 발현, fibroblast를 induced pluripotent stem cells로 변경하는 4 factors중 하나기도 함
- Perturbation of *Lin28* → development defect와 tumorigenesis 초래
    - ex) mouse에서 *Lin28a* deficiency → undergrowth, lethality in early stages of development, ectopic expression으로는 overgrowth와 delayed timing of puberty
- *Lin28a/b*는 malignant transformation 촉진, 발현이 많은 종류의 tumor의 advanced stage와 연관
    - hepatocarcinoma, nephroblastoma, ovarian carcinoma, germ cell tumor

### LIN28 as a suppressor of *let-7* microRNA biogenesis

- 핵에서는 LIN28이 *let-7*의 primary transcript, 즉 pri-*let-7*에 결합함 → RNase III에 의한 processing 방해
- 세포질에서는 *let-7*의 precursor form인 pre-*let-7*과 상호작용 → pre-*let-7* processing 방해
- TUTase 4를 recruit → pre-*let-7*의 oligo-uridylation 유도 → DICER processing을 효과적으로 막음, 또한 RNA degradation을 도움
- LIN28B는 주로 nucleolus에 localize 되어있음 → nuclear processing을 방해
- 반면 LIN28A는 cytoplasmic compartmet에 주로 발견됨 → TUTase 4와 같이 활동

### RNA binding domains of LIN28 homologs

- cold shock domain(CSD)
- cluster of two CCHC-type zinc finger motifs
- pre-*let-7*의 “GGAG” sequence → zinc finger domain의 binding site → zinc finger는 *let-7* regulation에 중요

### Additional functions of LIN28

- retinoic-acid-induced neurogliogenesis → *Lin28a* 과발현은 early embryonic cell의 fate decision과 관련된 특정 trascription factor들의 발현을 바꿈 (*let-7* level 증가 전)
- muscle-specific *Lin28a* knockout mice (*let-7* level 변화 x) → glucose tolerance와 insulin resistance 망가짐
- LIN28A는 mRNA, cosediments with polysome과 상호작용 (sucrose gradient centrifuge 시)
- *Igf2, Oct4*와 같은 특정 mRNA의 translation을 향상시킴

### Technique used for identifying LIN28A-interacting RNAs

- CLIP-seq (a.k.a HITS-CLIP) combines UV crosslinking, immunoprecipitation, and high-throughput sequencing
- 살아있는 세포의 UV 조사 → bases와 amino acids 사이의 covalent bond → RNA-protein interaction의 생리적 상태 확인 가능
- crosslinking → 더 가혹한 조건으로 IP 진행 → cell lysates에서 흔히 일어나는 인공적인 RNA-protein interaction 제거
- coimmunopurified RNA fragment sequencing → interacting transcriptome의 global view 제공, target RNA의 exact binding site의 mapping을 가능하게 함

### In this study

- pre-*let-7* 뿐만 아니라 수많은 LIN28A target mRNA들을 찾음
- binding site analyses → LIN28A binding motif의 일반적인 특징들 밝혀냄
- ribosome footprinting → ER pathway의 translation suppressor로서의 LIN28A 역할 밝힘

# Results

### LIN28A CLIP-seq from Mouse Embryonic Stem Cells

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%201.png)

**Figure 1A** : mESCs를 UV 처리 → RNase A로 lysis 후 antibody로 immunoprecipitate → linker ligate → RT-PCR로 증폭 → Illumina Genome Analyzer IIx로 시퀀싱

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%202.png)

**Figure S1A** : Left - LIN28A-RNA conjugate에 3’ linker만 연결된 것 autoradiography, Right - 5’ linker도 붙인 RT-PCR product

3’ linker의 길이가 짧아서 결과가 확실하게 나오지는 않았음

- LIN28A-interacting RNAs의 specific isolation을 확실시 하기 위해, 3가지 다른 library와 3가지 antibody로 진행 (1 rabbit - Abcam, 2 mouse - 35L33G, 2J3)

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%203.png)

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%204.png)

**Figure 1B, S1B** : siGFP는 control, siLin28a는 LIN28A가 depleted된 실험군, Left - LIN28A immunoprecipitation 결과의 western blot, Right - autoradiography of 5’-32P-labeled RNA-LIN28A complex

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%205.png)

**Figure S1C** : 3개의 library의 transcript level enrichment correlation 조사 → 0.93으로 충분한 reproducibility 확보

### Confirmation of the *Let-7* Family as a Target of LIN28A

- *let-7* family miRNA는 LIN28A의 target으로 가장 많이 연구 되었으므로, positive control로 아주 중요한 역할을 하게 됨

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%206.png)

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%207.png)

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%208.png)

**Figure 1C, S2A, S2B** : pre-let-7g의 terminal loop에 있는 GGAG motif 확인, 하단에 site mutation rateRK shannon’s entropy로 나타나 있음, 7 read 미만의 tag는 모두 삭제함

S2A, S2B는 minus strand로 진행됨

**Figure 1D** : predicted secondary structure of pre-let-7g, GGAG motif는 red로 표시됨

- *let-7* family가 mESC에서 유일한 LIN28A의 miRNA target인지 불확실 → CLIP-seq library로 다른 LIN28A-interacting miRNA 분석
- miRNA의 precursor 양을 정확하게 분석하는 방법 x → mature miRNA signal 활용

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%209.png)

**Figure 1E** : LIN28A CLIP-seq enrichment level(x축) - miRNA level change after *Lin28a* knockdown(y축)의 scatter plot

- mir-677, mir-708 같은 comparable enrichment도 있지만 knockdown에서의 변화가 거의 x
    
    → *let-7* family가 LIN28A의 유일한 functional miRNA target
    

### LIN28A Binds to *Let-7* Precursors through the GGAG Motif

이전 연구 결과 : pre-let-7 terminal loop의 GGAG motif → CCHC zinc finger domain의 binding center, LIN28A의 특이적 인식에 필요

- 거의 모든 let-7g CLIP tag는 GGAG sequence 포함 → CLIP library가 LIN28A와 pre-let-7g 사이의 생리학적인 상호 작용 충분히 반영
- Figure 1C, 1D를 보면, sequence alteration들이 자주 일어나는 것을 확인 가능
    - 특히, motif의 첫번째 G가 자주 치환됨
    - Figure S2A, S2B에도 유사한 치환 패턴이 관찰됨
- 이러한 alteration은 LIN28A로의 UV crosslinking에 따른 결과임
    - proteinase 처리 후에도 일부 peptide가 남아있어서 reverse transcription을 방해

### Crosslinking-Induced Errors Allow Identification of LIN28A Binding Sites at Single-Nucleotide Resolution

- library에 non-miRNA transcript도 많음 → pre-let-7 말고도 다른 RNA와도 상호작용
- 정확한 mapping을 위해, mutation을 일부 활용하였음

 

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2010.png)

- **Figure S2C** : mutation error가 RNA-seq에 비해 CLIP-seq library에서 더 많이 일어남
- **Figure S2D** : pre-let-7과 마찬가지로, G에서 가장 많은 mutation이 있었음
- CLIP-seq의 경우 가운데 부분이 error가 비교적 높은 이유 : UV crosslinking으로 인해 남아있는 부위가 있기 때문
- RNA-seq의 양 끝 말단 error 이유 : 초반 부분 - imaging 상태가 안 좋음, 끝 부분은 splicing 등으로 인한 alignment 어려움

- LIN28A-binding site를 Shannon’s entropy를 활용하여 찾음
    - nucleotide composition의 randomness를 정량화함
    - single-nucleotide polymorphism/paralogous genes로 부터 기인한 false positive를 줄여줌
        
        ![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2011.png)
        
- **Figure S3A** : Shannon’s entropy를 적용한 Site mutation rate와 LIN28A enrichemnt level 사이의 유의미한 correlation 발견됨 → mutated site들이 LIN28A binding site에서 유래되었을 것임
- **Figure S3B** : 516,259개의 putative binding site가 0.1%의 false discovery rate로 나타남 → LIN28A 결합 부위는 21.7 G 마다 발생
- mRNA마다 평균적으로 38.5개 정도 발생 → LIN28A binding은 일부 RNA가 아니라 훨씬 더 많은 RNA들과 결합한다고 생각하게 함

### LIN28A Favors Single-Stranded Purine-Rich Motifs

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2012.png)

- **Figure S3C** : LIN28A binding site의 패턴 조사

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2013.png)

- **Figure 2A** : consensus sequence를 찾기 위해 imformation content(top)와 frequency(bottom)   조사 → “AAGNGG”
- **Figure 2B** : 10 most frequently observed sequene로, “AAGGAG”가 가장 자주 등장하였음

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2014.png)

- **Figure 2C** : LIN28A-interacing hexamer들을 clustering하여 smiliarity network를 만듦. AAGNNG, AAGNG(N), (N)UGUG(N)로 대부분을 설명할 수 있음
- “AAGNNG”가 LIN28A binding site의 주축을 이루고 있는데, 이는 LIN28A의 two zinc finger motif가 “AGNNG”를 인식한다는 다른 최근 논문과 일맥상통함
- 가장 적게 나온 “UGUG” motif는 이 논문에서 처음 발견 되었고, 아마도 LIN28A binding의 다른 mode에 영향을 주는 것으로 추측 됨

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2015.png)

- **Figure S4** : 각 group의 EMSA 결과, recombinant LIN28A protein과 synthesized RNA segment 활용 → UGUG가 가장 약한 결합력
- CLIP-seq에서 자주 치환된 G에 돌연변이가 나면, LIN28A affinity를 크게 떨어뜨림 → motif들이 실제 LIN28A binding site를 나타낼 확률이 높음

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2016.png)

- **Figure 2D** : binding motif 주변 서열들은 서로 상보적인 경우가 많음 (pre-let-7의 stem 부분을 담당)

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2017.png)

- **Figure 2E** : Random sequence에 비해 WC-pair를 구성하는 경향이 확실히 뚜렷함(left), AAGNG pentamer의 경우(right)도 유사함

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2018.png)

- **Figure S3D** : folding energy analysis, 더 강한 구조(낮은 free energy)는 CLIP libraries에서 나타남
- hairpin 구조가 LIN28A-recognition를 더 쉽게 일어나도록 도움
- 5-7 bp 정도의 stem을 가진 terminal loop hairpin에 위치한 “AAG(N)NG” motif에 결합하는 것이 가장 합리적인 듯함!

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2019.png)

- **Figure S3E** : AAGGAG를 비롯한 유사한 sequence들이 거의 반이 CLIP-seq에 의해 free energy가 -6kcal/mol 이었음 → 분석을 통해 밝혀낸 sequence들이 LIN28A binding site와 충분히 연관됨

### Messenger RNAs Are the Major LIN28A Targets

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2020.png)

- **Figure 3A** : LIN28A와 interact 하는 RNA의 종류에 대해 조사 → 42%가 mRNA로 매핑되었음, 반면에  miRNA는 고작 0.07%(그 중 0.05%가 *let-7* loci)
- **Figure 3B** : intronic region에서는 강하게 depleted 됨 → LIN28A는 mature mRNA들과 반응

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2021.png)

- **Figure 3C** : start과 stop codon 근처 분석 → CDS, 3’-UTR에 비해, 5’-UTR이 현저히 적음

### LIN28A Reduces Ribosome Occupancy without Affecting mRNA Abundance

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2022.png)

- **Figure 4A** : LIN28A와 mRNA 양의 상관관계 분석 → 큰 관계가 없음
- 이전 연구들에서 LIN28A가 *Igf2*, cyclin A 등 여러 mRNA의 translation positive regulator로 작용한다는 일관성 있는 결과 O
- **Figure 4B** : LIN28A가 mESC에서 polysome과 결합함

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2023.png)

- **Figure 4C** : Lucfierase를 silencing한 siLuc (control)과 siLin28a를 이용한 ribosome footprinting의 과정, 간단히 말하면 각 cell에서 ribosome 결합 부위만 모아서 sequencing

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2024.png)

- **Figure S5A, S5B** : ribosome footprint의 density가 start codon의 근처와 upstream에서 높음 → CDS를 상당히 정확하게 파악, three-nucleotide periodicity도 합리적임

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2025.png)

- **Figure 4D :** LIN28A와 ribosome density 간의 강한 positive correlation이 발견됨 → siLin28a이 siLuc보다 ribosome occupancy가 높음 → LIN28A는 target mRNA의 translation을 억제할 것임
- **Figure 4E** : ribosome density change의 cumulative distribution (D를 그냥 다른 방식으로 표현)

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2026.png)

- **Figure S5C** : Figure 4E와 같은 작업을 다른 여러 antibody로 진행한 것
    
    ![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2027.png)
    
- **Figure S5D** : Western blot을 통해, *Lin28a* knockdown 이후 각각의 gene들의 변화 관찰
    
    → 실제로 mRNA를 target으로 translational repression을 진행
    
- **Figure S5E** : let-7 target들은 mRNA abundance, ribosome occupancy 둘 다 영향 x

### LIN28A Targets mRNAs Destined for Endoplasmic Reticulum

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2028.png)

- **Figure 5A** : LIN28A에 의해 조절되는 translatoin을 GO(gene ontology) analysis
    
    → cellular component와 관련된 GO term들이 가장 biased됨
    
- ER 관련 protein들이 대부분 LIN28A target이고, nucleus, cytoplasm의 경우는 표시 수가 적음
- 이것조차도 사실은 nuclear protein이 overestimated 된 것임 (histone mRNA는 deplete 되므로)

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2029.png)

- **Figure 5B** : integral membrane protein(주로 ER-associated translation 함) → 다른 protein에 비해 4~6 fold 이상으로 LIN28A와 반응
- 추가로, Lin28a knockdown에서 integral membrane protein들의 translation이 active 해짐
- **Figure 5C** : validation으로 RER에서의 35S-methionine incorporation 비교 조사

- tail-anchored transmembrane protein은 다른 ER-associated mRNA들과 달리, cytosol에서 합성되어 ER로 posttranslationally translocated 됨

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2030.png)

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2031.png)

- **Figure 5D, Figure S6B** :  tail-anchored transmembrane protein은 CLIP-seq과 ribosome density 모두 LIN28A-depleted cell에서 증가하지 않음
    
    → 이 패턴은 cytosol에서 온 다른 mRNA와 유사 → LIN28A가 ER-associated translation에 특화되어있다는 주장을 강화시킴
    
- regulation의 selectivity를 이해 → ER-associated mRNA들이 LIN28A-recognition motif를 더 가져오는지 확인해야 함

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2032.png)

- **Figure S3F** :  HMM을 이용하여 모든 mRNA의 LIN28A-recognition site를 예측

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2033.png)

- **Figure S6C** : ER과 non-ER의 차이가 별로 나지 않음 → sequence나 structural feature로는 구분 X

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2034.png)

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2035.png)

- **Figure 5E, Figure S6D** : motif score로 비교하면 ER이 CLIP-seq에서 더 자주 detected 됨
    
    → LIN28A-recognition element 말고 다른 additional factor가 있을 것임.
    

### LIN28A Is Localized in Peri-ER Area

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2036.png)

- **Figure 6A** : LIN28A signal이 ER 주변에서 감지됨 (KDEL은 ER-retention signal), cytosolic protein인 GAPDH와는 분포가 구별됨

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2037.png)

- **Figure 6B** : 가시성을 위한 Figure 6A의 ectopically expressed version

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2038.png)

- **Figure 6C** : subcellular fractionation → LIN28A가 RER의 microsomal fraction에 존재하는 것 확인
- tubulin, ATF6 cytosol fragment와 같은 cytosolic protein들은 RER microsomal fraction에서 검출되지 않았지만, LIN28A는 확실한 양이 검출됨
    
    → LIN28A는 RER의 cytosolic surface에 결합하는 것으로 추측 (ER-associated mRNA들이 translated 되는 곳)
    
- colocalization을 통해, LIN28A는 다른 mRNA 보다 ER-associated mRNA들과 더 자주 interact 할 것임

# Discussion

- CLIP-seq은 LIN28A binding site들을 genomic scale에서 single-nucleotide resolution으로 mapping 할 수 있게 함
- 최근 연구에서 coimmunoprecipitation과 oligo-dT enrichment, deep sequencing을 융합하여 LIN28A target을 찾는 연구를 진행함

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2039.png)

- **Figure S7A** : 위에서 언급한 그 연구의 data set과 너무 다름 (상관계수가 거의 0에 가까움)
    
    → 아마도 이전 연구의 방법이 indirect interaction에 취약하고, washing condition에 따라 상황이 바뀔 수 있기 때문이라고 생각됨
    
    → 본 연구가 더 정확한 LIN28A target들을 제공하였음
    

- CLIP-seq 분석으로 발견된 LIN28A binding motif는 이전에 biochemical & structural studies와 pre-let-7에서 유사하였음
- 본 연구는 추가적인 genome-wide functional evidence를 ribosome footprinting을 통해 제공함
    
     → 연구에서 확인된 mRNA가 실제로 LIN28A의 functional target임을 보여줌
    
- CLIP-seq approach의 주요 장점 : mutated sequence를 확인함으로써 binding site를 mapping 할 수 있음 → terminal loop의 small hairpin - AAGNNG
- first G (가장 많이 mutated 된) → zinc finger motif의 Lys160와 hydrogen bond 형성
- CSD-RNA interaction은 발견은 못함 → CSD가 RNA와 너무 느리게 반응해서 그런듯
- recognition element가 낮고, LIN28A가 풍부함 → mRNA당 38.5 site가 결합할 정도로 많은 mRNA들이 LIN28A에 결합

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2040.png)

- **Figure 7A** : LIN28A의 localization model
- LIN28A는 이미 transcript level에서 intracellular localization에 의해 이동함
- LIN28A-recognition element의 경우, mRNA가 LIN28A와 얼마나 자주 interact 하고, 어떤 position에 load 되는 지를 결정

- LIN28A는 ER-associated translation을 supress 함
- LIN28A는 CDS나 3’UTR에서 interact 함 → elongation 전이나 중간에 관여할 것으로 예상

- Weissman lab의 최근 보고에 의하면, 미분화 ESC에서 EB에 비해 integral membrane protine의 translation efficiency가 상당히 낮았음
    
     → *Lin28a*가 EB에서 downregulated 되기 때문
    

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2041.png)

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2042.png)

- **Figure 7B, S7B, S7C** : 2 data간의 상당한 overlap 발견
- EB differentiation 중에 upregulated 되는 gene → LIN28A-depleted ESC에서 enhance

![Untitled](LIN28A%2084001ba378db44ae8ddd43d143d714ca/Untitled%2043.png)

- **Figure S7D** : common pluripotency marker들은 모두 decreased 되지 않음
    
    → LIN28A depletion이 주요 원인일 것이라고 생각 가능