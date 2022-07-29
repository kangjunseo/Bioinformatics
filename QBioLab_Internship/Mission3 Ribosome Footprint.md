# Mission3. Ribosome Footprint

상태: 완료
시작 날짜: June 29, 2022 → July 7, 2022
실습자: 준서 강

# 목적

Ribosome footprint density에 대해 이해하고, 왜 triplicate pattern이 나오는지 이해해보기

Figure S5A를 다양하게 그려보기

# 과정

- [x]  GTF file parsing

<aside>
❓ GTF parsing 과정에서 직접 parsing을 하려는데, 시간이 너무 오래 걸려서, pd.read_csv에 옵션을 여러가지 주는 방향으로 해결함.

</aside>

- [x]  여러 가지 filter를 적용해서 유효한 transcript들만 남기기
- [x]  GTF 파일을 활용하여, 5’-UTR 정보 얻어내기 → Sam file의 pos 정보 조정
- [x]  stop codon 그림 : 5-UTR도 빼고, CDS 만큼도 추가로 빼기
- [x]  longest isoform만 남기기
- [x]  figure 마무리
- [x]  siLuc 파일 받아오기
- [x]  gene, transcript 부분은 chunk 단위로 읽어오는 과정에서 미리 parsing 하기

<aside>
❓ siLuc 원본 파일이 12GB 정도여서 그런지, sam은 물론이고, bam을 불러오는 모듈을 사용해도 계속해서 kernel이 죽는 현상이 발생합니다. 따라서 현재는 pandas의 chunksize를 활용해서 해결해보려고 노력중입니다.

</aside>

### 교수님 피드백 후 추가 진행할 것들

- [x]  sam file parsing 방식을 좀 더 효율적으로 바꿔보기

→ 성공적으로 진행되었음 (siLuc도 문제 없이 parsing 완료)

- [x]  stop codon 이후에 나타나는 read들을 분석해보기

→ read count로 정렬 후, 0 이후에 가장 많이 나타난 몇몇 gene들을 살펴보았으나, 크게 특이사항은 없고 gene type도 “protein_coding”이라고 되어있음. 아마도 다른 쪽 (filtering은 아닌 듯함)의 문제가 있는 것으로 예상됨

→ soft clipping 고려 후 아주 조금 개선되기는 했음

- [x]  non coding gene이 있는지 살펴보기

<aside>
❓ gencode 상 gene type을 “protein_coding”인 것만 모두 넣었는데, 이 경우에도 추가로 filtering 해야 할 gene들이 따로 있을까요?

</aside>

- [x]  soft clipping을 고려하지 않은 alignment로 다시 진행해보기

```bash
STAR --runThreadN 10 --genomeDir $ref_gene_path --readFilesIn $fastq_path'/SRR458756C.fastq' --outFileNamePrefix $align_path'/RPF_siLuc2/' --outFilterMismatchNoverLmax 0.1 --alignEndsType EndToEnd
STAR --runThreadN 10 --genomeDir $ref_gene_path --readFilesIn $fastq_path'/SRR458757C.fastq' --outFileNamePrefix $align_path'/RPF_siLin28a2/' --outFilterMismatchNoverLmax 0.1 --alignEndsType EndToEnd
```

soft clipping을 고려하지 않게도 해보았지만, 그전 figure와 크게 달라지지는 않은 것 같습니다.

# 결과

작업 진행 중인 코드입니다.

[https://github.com/kangjunseo/Bioinformatics/blob/main/QBioLab_Internship/Mission3.ipynb](https://github.com/kangjunseo/Bioinformatics/blob/main/QBioLab_Internship/Mission3.ipynb)

### 1. Figure S5A (gene 1개, transcriptome 기준, start codon 근처)

![Untitled](Mission3%20Ribosome%20Footprint%2094acd32e8c4d4537ac96e23af3429fd4/Untitled.png)

### 2. Figure S5A (gene 1개, stop codon 근처)

![Untitled](Mission3%20Ribosome%20Footprint%2094acd32e8c4d4537ac96e23af3429fd4/Untitled%201.png)

<aside>
❓ gene 1개만 고른 경우에는, triplicate pattern도 잘 보이지 않는 듯하고, 전체적인 그래프 양상도 많이 다른 것 같습니다. mapping 된 gene들 중 read count가 높은 것들 중에 그나마 가장 괜찮은 그림이 그려진 gene을 골랐습니다.

</aside>

### 3. Figure S5A (gene 여러 개, transcriptome 기준, genome + strand에서 코딩하는 gene만)

![Untitled](Mission3%20Ribosome%20Footprint%2094acd32e8c4d4537ac96e23af3429fd4/Untitled%202.png)

![Untitled](Mission3%20Ribosome%20Footprint%2094acd32e8c4d4537ac96e23af3429fd4/Untitled%203.png)

gene을 여러 개 사용하니 triplicate pattern도 잘 보이고, 논문과 그래프 양상도 적당히 비슷합니다!

### 4. Figure S5A (gene 여러 개, longest isoform 적용, soft clipping 적용 전)

- siLin28a

![Untitled](Mission3%20Ribosome%20Footprint%2094acd32e8c4d4537ac96e23af3429fd4/Untitled%204.png)

![Untitled](Mission3%20Ribosome%20Footprint%2094acd32e8c4d4537ac96e23af3429fd4/Untitled%205.png)

longest isoform을 제거하니 종결 코돈 이후의 outlier와 -15보다 upstream의 outlier가 많이 줄어 들었습니다.

- siLuc

![Untitled](Mission3%20Ribosome%20Footprint%2094acd32e8c4d4537ac96e23af3429fd4/Untitled%206.png)

![Untitled](Mission3%20Ribosome%20Footprint%2094acd32e8c4d4537ac96e23af3429fd4/Untitled%207.png)

- Figure처럼 통합

![Untitled](Mission3%20Ribosome%20Footprint%2094acd32e8c4d4537ac96e23af3429fd4/Untitled%208.png)

→ 아직 추가 분석을 적용하지 않아, triplicate pattern과 stop codon 이후의 peak들이 잡히지 않았습니다. 아마 soft clipping이 고려된 버전으로 다시 해보면 좀 더 명확한 그림이 나올 것으로 예상됩니다!

### 5. Figure S5A (soft clipping 고려하지 않은 버전)

![Untitled](Mission3%20Ribosome%20Footprint%2094acd32e8c4d4537ac96e23af3429fd4/Untitled%209.png)

종결 코돈 이후의 peak들이 조금 개선되었고, 전체적으로는 이전 그림과 비슷한 것 같습니다..! @Hyeshik Chang 

# 소스 코드

[https://github.com/kangjunseo/Bioinformatics/blob/main/QBioLab_Internship/Mission3.ipynb](https://github.com/kangjunseo/Bioinformatics/blob/main/QBioLab_Internship/Mission3.ipynb)

# 아이디어