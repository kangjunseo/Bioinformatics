# Mission4. CLIPseq analysis

상태: 완료
시작 날짜: July 8, 2022 → July 29, 2022
실습자: 준서 강

# 목적

- CLIP-seq을 통해 RNA -protein binding site를 밝혀내는 과정을 이해하기
- IGV라는 tool을 숙지하고, 이를 활용하여 논문의 여러가지 Figure들을 그려보기

# 과정

### 1. Figure S2A

- [x]  IGV 설치 및 환경 설정

→ 연구실 pc 권한 문제(비밀번호)로 인해 일단 desktop app 방식은 당장은 사용불가

→ 현재 web app version도 있어서 일단 그것으로 시도 중입니다!

- [x]  IGV 사용법 숙지하기

```bash
# reference gene은 web app 상에 올라와있는 mm39 ref gene 활용

# CLIP_35L33G를 인덱싱해서 올리려는데 samtools index에서 오류 발생
samtools index Aligned.out.bam # Error Message : Chromosome blocks not continuous

# 문제 해결을 위해 sort를 진행하고 다시 시도
samtools sort Aligned.out.bam -o sorted_Aligned.out.bam
samtools index sorted_Aligned.out.bam

# 이렇게 생성된 sorted bam file과 bai file을 IGV에 올리고, mirlet7d gene 부분을 보니 매핑이
# 많이 되어있는 것을 확인!
```

- [x]  filtering 하기 위해 bam file을 다시 sam file로 convert
- [x]  dataframe으로 필요한 정보들만 불러와서 shannon entropy 계산

→ 현재 entropy 값들이 mutation 부위 다른 곳에서 너무 크게 나와서 이유를 찾고 있습니다.

- [x]  raw data 살펴보기

→ 이 과정을 통해, chr8의 read들도 섞여있다는 것을 파악하여 제거하였고, 뒤쪽의 entropy noise들은 deletion을 적절히 반영하지 못하여서 그렇다는 것을 파악했습니다.

- [x]  deletion 반영해주기 (gap을 다른 임의의 문자 ‘D’로 추가해주기)

→ deletion을 반영해주니 논문과 같이 가장 높은 peak 옆의 peak도 높게 나타났습니다.

- [x]  Figure S2A 마무리

### 2. Figure S2C, Figure S2D

- [x]  1안. cigar string을 extend 해주기 위해 ‘jvarkit’ 활용 ([http://lindenb.github.io/jvarkit/SamFixCigar.html](http://lindenb.github.io/jvarkit/SamFixCigar.html))

```bash
git clone "https://github.com/lindenb/jvarkit.git"
cd jvarkit
./gradlew samfixcigar # 여기서 jdk complier 관련 error 발생
# Caused by: : Error running javac compiler
# Caused by: java.io.IOException: Cannot run program "javac"
```

<aside>
❓ 궁금한 점:  현재 sam file에 있는 cigar string만으로는 substitution을 구별할 수 없을 것 같아서, mission 설명에 적혀있는 “exteneded cigar string”을 활용하여 진행하려 하는데, 이 방향이 맞을까요..?

그리고, extended cigar string으로 변환하는 tools들은 대부분 java 기반인 것 같은데, sudo가 막혀있어서 jdk 확장 설치가 조금 어렵습니다…ㅠ

</aside>

- [x]  reference sequence와 read sequence를 활용해 substitution과 deletion을 효과적으로 구분해 낼 수 있는 알고리즘 고안해보기
- [x]  20개 bin으로 나누는 함수 (20분율로 pos를 나타내고 int로 버림)
- [x]  각각의 bin에 del, ins, sub(A,T,G,C) 넣기

### 3. Figure S3C, Figure 2A

- [x]  weblogo tutorial 찾아보기
- [x]  python dict로 LIN28A binding site 부위들 골라내기 (entropy 0.8 이상)
- [x]  -10 ~ +10의 서열 parsing
- [x]  weblogo로 결과 확인하기

### 4. Figure 2B, 2D

- [x]  기존 sequence 들을 hexamer motif에 맞게 parsing
- [x]  pandas groupby로 frequency 계산
- [ ]  같은 과정을 flanking sequence에도 적용하기

# 결과

### 1. Figure S2A

- IGV로 본 결과(compact view)

![Untitled](Mission4%20CLIPseq%20analysis%20dcdb8cf6d9e247029d022cd657f2c50d/Untitled.png)

- detail view

![Untitled](Mission4%20CLIPseq%20analysis%20dcdb8cf6d9e247029d022cd657f2c50d/Untitled%201.png)

48,689,528 bp와 48,689,529 bp에 많은 mutation을 확인할 수 있습니다.

- entropy figure

![Untitled](Mission4%20CLIPseq%20analysis%20dcdb8cf6d9e247029d022cd657f2c50d/Untitled%202.png)

초반에는 정말 엉망인 entropy figure가 그려졌는데, chr8의 read들을 제거하니 앞쪽의 noise들이 전부 사라졌고, 이상하게 뒤쪽에만 noise가 남아있어서, 이것은 명백하게 deletion이 seq에 반영되지 않아서 그럴 것이라고 생각하여 그 부분을 반영해 줬더니 위와 같이 entropy가 깔끔하게 나왔습니다.

위의 그림과 bp position도 정확하게 일치합니다. (x축에 +48,689,000을 하면 일치)

### 2. Figure S2C, Figure S2D

- substitution figure

![Untitled](Mission4%20CLIPseq%20analysis%20dcdb8cf6d9e247029d022cd657f2c50d/Untitled%203.png)

<aside>
❓ 궁금한 점: 대충 경향은 비슷하나, 본 논문의 figure와는 사뭇 다른 느낌인데, 따로 추가적인 작업들이 필요할까요…? softclip이 있는 read는 제거하였고, isoform의 경우는 고려하든 안하든 비슷하게 figure가 그려지는 것 같습니다. @Hyeshik Chang 

일단 가운데 부위에서 substitution 자주 일어난다는 것은 확실하게 확인할 수 있을 것 같습니다!

</aside>

- deletion과 insertion까지 포함된 version (Figure S2C)

- 수정 전

가운데의 움푹 들어간 부분이 뭔가 figure를 이상하게 만들고 있습니다.

![Untitled](Mission4%20CLIPseq%20analysis%20dcdb8cf6d9e247029d022cd657f2c50d/Untitled%204.png)

- 수정 후 (softclip data도 포함)

전체적인 양상은 figure와 조금 달라지기는 했으나, 가운데 부분이 다소 개선되었습니다.

![Untitled](Mission4%20CLIPseq%20analysis%20dcdb8cf6d9e247029d022cd657f2c50d/Untitled%205.png)

- substitution base 별로

- 수정 전

위의 substitution 부분을 base pair별로 나눈 것에 불과하기 때문에 비슷한 애로사항을 가지고 있습니다.

![Untitled](Mission4%20CLIPseq%20analysis%20dcdb8cf6d9e247029d022cd657f2c50d/Untitled%206.png)

- 수정 후 (softclip data도 포함)

softclip data만 포함시키고 알맞게 조정하였을 때는 C의 substitution이 너무 높게 나와 flag 16과 272를 추가로 제거하여 figure와 유사하게 만들 수 있었습니다. U의 경우만 후반부에 조금 높게 나옵니다.

![Untitled](Mission4%20CLIPseq%20analysis%20dcdb8cf6d9e247029d022cd657f2c50d/Untitled%207.png)

- deletion base별 (수정 반영)

![Untitled](Mission4%20CLIPseq%20analysis%20dcdb8cf6d9e247029d022cd657f2c50d/Untitled%208.png)

- insertion base별 (수정 반영)

![Untitled](Mission4%20CLIPseq%20analysis%20dcdb8cf6d9e247029d022cd657f2c50d/Untitled%209.png)

### 3. Figure S3C, Figure 2A

- Figure S3C

![Untitled](Mission4%20CLIPseq%20analysis%20dcdb8cf6d9e247029d022cd657f2c50d/Untitled%2010.png)

<aside>
❓ 궁금한 점: -1 pos의 A가 논문에 비하면 entropy가 다소 낮은 것 같은데, 이 정도만으로도 유의미한 수치인지 궁금합니다! @Hyeshik Chang

</aside>

- Figure 2A

![Untitled](Mission4%20CLIPseq%20analysis%20dcdb8cf6d9e247029d022cd657f2c50d/Untitled%2011.png)

![Untitled](Mission4%20CLIPseq%20analysis%20dcdb8cf6d9e247029d022cd657f2c50d/Untitled%2012.png)

### 4. Figure 2B, 2D

- Figure 2B

논문과 마찬가지로 “AAGGAG” motif가 가장 많이 발견되었고, “AAGNNG” type의 motif가 자주 발견되었습니다.

![Untitled](Mission4%20CLIPseq%20analysis%20dcdb8cf6d9e247029d022cd657f2c50d/Untitled%2013.png)

- Figure 2D

7번째의 GA……UG를 제외하고 모든 경우에서 WC pair를 만족하는 것을 볼 수 있습니다.

![Untitled](Mission4%20CLIPseq%20analysis%20dcdb8cf6d9e247029d022cd657f2c50d/Untitled%2014.png)

# 소스 코드

[https://github.com/kangjunseo/Bioinformatics/blob/main/QBioLab_Internship/Mission4.ipynb](https://github.com/kangjunseo/Bioinformatics/blob/main/QBioLab_Internship/Mission4.ipynb)