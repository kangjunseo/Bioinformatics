# Mission2. Samfile, Ribosome density. CLIP enrichment, and GO terms

상태: 완료
시작 날짜: June 24, 2022 → June 29, 2022
실습자: 준서 강

# 목적

- Samfile과 bamfile의 구조를 이해하고, pandas를 활용하여 직접 Samfile의 read count를 계산해보기
- 계산한 read count들로 각 CLIP enrichment와 각 조건에서의 ribosome density와 clip enrichment를 구하고, Figure4D 와 Figure5B 를 그리기

# 과정

### Figure 4D

x축 : CLIP/untreat, y축 : (RPF-siLin28a/PolyA-siLin28a)/(RPF-siLuc/PolyA-siLuc)

- [x]  SAM file 읽어서 필요한 정보만 추출하는 함수 만들기
- [x]  read 개수 table 만들기
- [x]  matplotlib으로 시각화

<aside>
❓ 궁금한 점: 전체적으로 y_axis가 논문보다 2만큼 아래로 평행 이동된 이유?

</aside>

→ 절대값은 크게 의미가 없는 값이라 전체적으로 shift 되는 것은 문제 x, correlation coefficient가 더 중요한 값!

### Figure 5B/S6A

- [x]  gene ontology data download
- [x]  기존 Figure 4D에 사용한 code를 변형하기 (ENSMUST 정보로 바꾸기)
- [x]  Ensembl transcript와 기존 table을 매칭 시켜서, gene ontology 정보 추가
- [x]  Extended experimental procedures를 참고하여, gene ontology 구분 기준 정하기
- [x]  gene ontology가 반영된 figure 그리기
- [x]  2개 이상 localized 되는 것들 제외하고 표 다시 구성
- [x]  figure 세부적 요소 마무리

# 결과

### Figure 4D

![Untitled](Mission2%20Samfile,%20Ribosome%20density%20CLIP%20enrichment%209591ccd57f12488a9ad505e0a74f7bbc/Untitled.png)

### Figure 5B/S6A(임시)

![Untitled](Mission2%20Samfile,%20Ribosome%20density%20CLIP%20enrichment%209591ccd57f12488a9ad505e0a74f7bbc/Untitled%201.png)

### Figure 5B/S6A(완성)

![Untitled](Mission2%20Samfile,%20Ribosome%20density%20CLIP%20enrichment%209591ccd57f12488a9ad505e0a74f7bbc/Untitled%202.png)

# 소스 코드

초반 부분은 Figure 4D, 후반 부분은 Figure 5B 관련 내용입니다.

[https://github.com/kangjunseo/Bioinformatics/blob/main/QBioLab_Internship/Mission2.ipynb](https://github.com/kangjunseo/Bioinformatics/blob/main/QBioLab_Internship/Mission2.ipynb)

# 아이디어

1. 임시로 그린 Figure 5B는 논문보다 훨씬 sample 개수가 많아보임
    
    → 일단 교집합들은 그냥 버리는 것이 좋아보임
    
2. 그럼에도 눈으로 볼때, 아직 점들이 논문보다 많아 보임
    
    → 임의로 각각 400개씩 random sampling 후, 이것들을 scatter plot으로 그림
    

위 두 과정을 거치니, 조금 더 논문과 비슷한 Figure를 그릴 수 있었습니다!

# *Question에 대한 Answer*

### 1. What is flag at samfile (or bamfile)?

Sequencing 상태를 나타냅니다. flag가 4인 경우는 잘못 매핑된 경우라 분석에서는 제거하고 진행해야 합니다. 0은 정상, 16은 반대로 mapping 된 경우, 256은 secondary alignment가 진행된 경우입니다.

### 2. Why we use log2 (or log10) scale to draw a plot?

이러한 수많은 데이터들을 다룰 때, 또 통계적 분석을 할 때 log scaling은 정말 유용합니다. 일단 data의 편차를 줄이는 용도로 유용합니다. skewness와 kurtosis를 줄일 수 있기 때문에, data를 normalize 하는 효과를 가져올 수 있습니다. 

또한, 매우 큰 숫자의 크기를 대폭 줄여주므로 연산이 매우 용이 합니다. 다른 데이터는 억 이상의 숫자를 가지는 경우도 있을 텐데, log10 스케일 상에서는 1자리 숫자로 표현가능한 정도로 줄일 수 있습니다.

### 3. Why we use cutoff to filter the read-count?

cutoff를 정해서 filtering 하지 않으면 수많은 이상치들이 figure에 포함되게 됩니다. 이런 outlier들은 정말 소수의 케이스이므로, 실험 분석에 큰 도움이 되지도 않고, 오히려 정상적인 결과와 다른 결과를 유도할 수도 있습니다. 특히 cutoff를 적용하지 않으면, read count가 10000이상인 경우와 30이하인 경우가 같은 가중치로 점이 찍히는 것과 마찬가지이니, filtering은 더욱 정확한 분석에 큰 기여를 할 수 있습니다.
