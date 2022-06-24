# Mission1. Download Data and Align

상태: 완료
시작 날짜: June 21, 2022
실습자: 준서 강

# 목적

RNA sequencing에 필요한 reference file들과 실제로 논문에 쓰인 SRA file들을 다운로드하고, adapter를 제거한 후, alignment를 해보는 과정 경험해보기

# 과정

## 2022.06.21

인턴십 첫 날이라, 논문 읽기에 집중하고 Mission 1은 간단하게 영상을 보고 따라해보는 과정 정도만 진행하였다. 일단 Gencode에서 reference data를 다운로드하는 것까지는 성공하였고, SRA file 1개만

wget으로 download 하고 fastq-dump를 활용해 fastq 형식으로 파일을 바꾸는 것 까지 성공하였다.

그런데, fastx_clipper를 활용해 adapter로 자르는 과정에서 어떤 adapter를 써야하는지 조금 헷갈린다. 이전의 slack에도 비슷한 질문이 올라왔어서, 이것에 대한 답변을 참고하고, 논문을 좀 더 읽어보면서 이해도를 높이면 자연스럽게 해결될 문제 같기는 하다.

### 2022.06.23

gzip을 통해 reference 파일들의 압축을 풀고, 나머지 SRA file들을 다운로드 받고 fastq로 전환하는 과정과 적절한 adapter를 사용하여 clipping 까지 진행하려 한다. 일단은 fastq로 전환하는 과정이 생각보다 오래걸리고 있어서, 그 시간동안 논문을 읽는 중이다.

적절한 adapter를 찾을 때 참고로 활용한 방법은 밑의 코드 블럭과 같아 `grep` command를 활용해서 각각을 매칭시켰다.

- fastx_clipper 사용 시 주의할 점

input file default option이 stdin이라서 되도록이면 -i option을 통해서 인풋 파일을 꼭 설정해 주어야할 듯!

### 2022.06.24

준비한 파일들을 바탕으로 본격적으로 genome index를 만들기 시작함. 아무래도 파일들이 기본 크기가 상당하다 보니, 커맨드가 멈춰있는 것을 자주 보게 되는데, 이 때 `ps ax | grep {실행 시킨 프로그램}` 을 다른 터미널에서 실행하면, 프로세스가 잘 돌아가고 있는지 확인 가능하다. 기본 조건들로만 돌렸더니, ram 관련 이슈가 있어서 해당 부분의 옵션을 error message를 참고하여 추가해주었다.

alignment도 준비를 마쳤다. 다음 미션을 보니 6개의 sam file을 활용하는 다른 미션인 것 같아, alignment를 6번 따로 돌리는 코드로 작성하였다.

# 소스 코드

### 2022.06.21

```bash
#Gencode에서 reference file download
wget https://ftp.ebi.ac.uk/pub/databases/gencode/Gencode_mouse/release_M29/gencode.vM29.primary_assembly.annotation.gtf.gz
#나머지는 Fasta file을 local로 다운로드 하여서 서버로 업로드 하였음

#논문의 Accession Numbers의 링크로 접속하여 SRA file 다운로드
wget https://sra-pub-run-odp.s3.amazonaws.com/sra/SRR458753/SRR458753
fastq-dump SRR458753
fastx_clipper -a {adapter sequence} SRR458753.fastq # 아직 이부분은 못함
```

### 2022.06.23

```bash
#gzip을 통해 gz 파일 압축 풀기
gzip -d gencode.vM29.primary_assembly.annotation.gtf.gz gencode.vM29.transcripts.fa.gz GRCm39.primary_assembly.genome.fa.gz

#나머지 SRA file들 다운로드 및 fastq로 전환
wget https://sra-pub-run-odp.s3.amazonaws.com/sra/SRR458754/SRR458754
wget https://sra-pub-run-odp.s3.amazonaws.com/sra/SRR458755/SRR458755
wget https://sra-pub-run-odp.s3.amazonaws.com/sra/SRR458756/SRR458756
wget https://sra-pub-run-odp.s3.amazonaws.com/sra/SRR458757/SRR458757
wget https://sra-pub-run-odp.s3.amazonaws.com/sra/SRR458758/SRR458758

fastq-dump SRR458754 SRR458755 SRR458756 SRR458757 SRR458758

# adapter sequence로 clip
modban_illumina=CTGTAGGCACCATCAATTCGTATGCCGTCTTCTGCTTG
illumina_SRA15=ATCTCGTATGCCGTCTTCTGCTTG
illumina_TruSeq=TGGAATTCTCGGGTGCCAAGGAACTCCAGTCAC

# adapter sequence 고를 때 참고로 활용한 방법
grep $adapter SRR45875X.fastq # 이것으로 결과가 여러 개 나오면 높은 확률로 맞는 것
# 이 방법과 논문 내용을 고려하여 알맞은 adapter를 선정

fastx_clipper -a $modban_illumina -i SRR458753.fastq -o SRR458753C.fastq
fastx_clipper -a $illumina_SRA15 -i SRR458754.fastq -o SRR458754C.fastq
fastx_clipper -a $illumina_SRA15 -i SRR458755.fastq -o SRR458755C.fastq
fastx_clipper -a $illumina_SRA15 -i SRR458756.fastq -o SRR458756C.fastq
fastx_clipper -a $illumina_SRA15 -i SRR458757.fastq -o SRR458757C.fastq
fastx_clipper -a $modban_illumina -i SRR458758.fastq -o SRR458758C.fastq

```

### 2022.06.24

```bash
ssh sandbox # 메모리 제한 일시적으로 해제
ref_gene_path=/home/qbio1/kangjunseo/tutorials/ref_gene # 오류 예방을 위해 절대 경로 사용

# reference file들로 genome index 생성
# 오류 해결 : 램 옵션과 작은 genome scaling 옵션 추가
STAR \
--runThreadN 10 \
--runMode genomeGenerate \
--genomeDir $ref_gene_path  \
--genomeFastaFiles $ref_gene_path'/gencode.vM29.transcripts.fa' $ref_gene_path'/GRCm39.primary_assembly.genome.fa' \
--sjdbGTFfile $ref_gene_path'/gencode.vM29.primary_assembly.annotation.gtf' \
--limitGenomeGenerateRAM 106832418400 \
--genomeSAindexNbases 12

# Alignment
mkdir alignment
mkdir alignment/PolyA_untreat alignment/PolyA_siLuc alignment/PolyA_siLin28a alignment/RPF_siLuc alignment/RPF_siLin28a alignment/CLIP_35L33G
fastq_path=/home/qbio1/kangjunseo/tutorials/fastq
align_path=/home/qbio1/kangjunseo/tutorials/alignment

STAR --runThreadN 10 --genomeDir $ref_gene_path --readFilesIn $fastq_path'/SRR458753C.fastq' --outFileNamePrefix $align_path'/PolyA_untreat/'
STAR --runThreadN 10 --genomeDir $ref_gene_path --readFilesIn $fastq_path'/SRR458754C.fastq' --outFileNamePrefix $align_path'/PolyA_siLuc/'
STAR --runThreadN 10 --genomeDir $ref_gene_path --readFilesIn $fastq_path'/SRR458755C.fastq' --outFileNamePrefix $align_path'/PolyA_siLin28a/'
STAR --runThreadN 10 --genomeDir $ref_gene_path --readFilesIn $fastq_path'/SRR458756C.fastq' --outFileNamePrefix $align_path'/RPF_siLuc/'
STAR --runThreadN 10 --genomeDir $ref_gene_path --readFilesIn $fastq_path'/SRR458757C.fastq' --outFileNamePrefix $align_path'/RPF_siLin28a/'
STAR --runThreadN 10 --genomeDir $ref_gene_path --readFilesIn $fastq_path'/SRR458758C.fastq' --outFileNamePrefix $align_path'/CLIP_35L33G/'
```

# Question에 대한 Answer

### 1. What is difference between mapping and align?

일단 alignment가 좀 더 정확하게 서열을 바탕으로 진행하는 것으로, 이 gene의 어느 부위에 근거하는지, 어떤 base들이 일치하는지를 더 중요하게 생각해서 진행하는 것이다. alignment의 경우는 좀 더 정확한 결과를 나타내지만, 시간이 상당히 걸린다.

mapping의 경우는 정확한 염기서열에는 크게 관심이 없고, 적당히 어떤 부위인지를 파악하는 방법이다. mapping의 경우는 alignment와 큰 차이를 보이지 않는 경우도 있어서, 경우에 따라서는 매우 효율적인 방법으로 쓰이기도 한다.

### 2. Why alignment programs need index to align?

Alignment program들의 algorithm이 suffix array, MMP와 같은 것들을 사용하는데, 이러한 알고리즘 상 기반 정보가 되는 index가 있으면 훨씬 더 효율이 좋아지기 때문이다.

index는 말 그대로 책갈피인데, genome index를 구축한다는 것은, human이나 mouse의 gene library를 기반으로 여러 곳에 책갈피를 꽂는 작업을 해둬서, 필요할 때마다 이곳에서 정보를 가져다 사용할 수 있게끔 하는 과정이라고 볼 수 있다.

### 3. Why alignment programs need annotation file to align sequencing file to genome reference?

마찬가지로, annotation file에서 정보를 가져다가 활용할 수 있음 → 훨씬 더 빠른 속도로 alignment/mapping 하는데에 기여

# 결과

특별한 이슈 없이 모든 과정이 잘 마무리 된 것 같다. 이번 미션을 통해 linux command에 한층 더 익숙해질 수 있었고, bioinformatic 분석이 어떤 과정으로 이루어지는지 경험해볼 수 있었다. adapter sequence를 제거하는 코드는 직접 만들어 볼만도 할 것 같기도 한데, 워낙 input 파일의 크기가 커서 이미 만들어진 좋은 알고리즘을 활용하는 것이 시간적으로는 더 좋을 것 같다.

추가) 5번째 alignment까지는 잘되서 6번째도 문제가 없을 것이라 생각했는데, quota를 초과해버려서 더 진행할 수 없었다. 살펴보니 SAM 파일이 용량이 매우 커서 발생한 일인듯 하다. 급한대로 fastq 파일을 모두 지운 후 다시 진행하였다.