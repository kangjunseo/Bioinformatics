# Linux Command Line for Bioinformatics

상태: 완료
시작 날짜: June 23, 2022
실습자: 준서 강

# 목적

리눅스 커맨드 라인 경험은 어느정도 있지만, Bioinformatics에서 주로 사용하는 것들을 좀 더 익혀서 이후 프로젝트에 차질이 없도록 하기 위해

# Terminal Basics

활용자료 : [https://sandbox.bio/tutorials?id=terminal-basics](https://sandbox.bio/tutorials?id=terminal-basics)

기본적인 `ls` , `head` , `tail` , `grep` 등의 사용법을 익히는 과정

### 기초 커맨드

```bash
echo "Hello World" # 출력
pwd # 현재 경로
ls # 현재 경로 상의 하위 폴더 / 디렉토리 나열
ls -l # l 옵션을 추가하여 접근권한 등의 세부정보 추가
```

### `head` , `tail` 로 문서 개요보기

```bash
head 파일명 # 주로 csv, tsv와 같은 파일들에 앞부분 row들을 보여줌, 해당 파일이 어떤 구성으로
					  # 되어있는지, 어떤 columns들에 어떤 정보들이 있는지 등을 간략하게 파악 가능
head -n 숫자 파일명 # -n 옵션 뒤에 숫자를 부여해서 어느정도의 정보를 보여줄것인지 조절 가능
tail 파일명 # head와 똑같지만, 앞에서부터가 아니라 끝에서 부터 보여줌
```

### `grep` 으로 문서에서 원하는 단어 찾기

```bash
grep "찾고 싶은 단어" 파일명 # 파일에서 원하는 단어가 있는 부분 찾기
grep -i "찾고 싶은 단어" 파일명 # i 옵션을 통해서 대소문자 구문 없이 찾을 수 있음
grep -v "빼고 싶은 단어" 파일명 # v 옵션을 통해서 빼고 싶은 단어를 빼고 모두 찾기 가능
```

### piping으로 여러 가지 커맨드 결합하기

```bash
grep -v "빼고 싶은 단어" 파일명 | tail -n 3 # grep을 할 때 | operator로 두 커맨드를 piping
grep "찾고 싶은 단어" 파일명 | wc -1 # 결과가 몇 개 나왔는지 counting
grep "찾고 싶은 단어" 파일명 > output 파일명 # > operator를 통해 출력되는 결과를 파일로 만들어 
                                           # 저장
#FASTA format에서 >를 찾고 싶을 때는 quote를 꼭 붙이기!
grep ">" 파일명 # O
grep > 파일명 # X, 이러면 해당 파일이 다 날아가버림
cp 백업파일 파일명 # 백업 파일이 없다면 돌이킬 수 없으므로 주의하자...

#이런 위험성을 조금이나마 줄이는 방법..!
cat 파일명 | grep ">" #이렇게 하면 원본 파일이 날아갈 확률이 크게 줄어듦!
```

### 환경변수 이용하기

```bash
#환경변수 abc, def를 할당
abc=123
def=hello
echo $abc #환경변수 abc에 저장된 123 출력
unset abc #환경변수 abc 할당 해제
env #환경변수 전체 보기
```

# Data exploration with awk

활용 자료 : [https://sandbox.bio/tutorials?id=awk-intro&step=0](https://sandbox.bio/tutorials?id=awk-intro&step=0)

### Filtering data

```bash
#Extract columns
awk '{ print $n }' orders.tsv | head # n번째 column만 출력하기
awk '{ print $0 }' orders.tsv | head # 0을 넣게 되면 전체 출력 (1 based indexing 인듯..)
awk '{ print $NF } ' orders.tsv | head # NF를 넣으면 마지막 column 출력
awk '{ print $2, $3 } ' orders.tsv | head # 이렇게 하면 2번째, 3번째 column 같이 출력 
awk -F "\t" '{ print $2, $3 } ' ordrs.tsv | head # delimeter를 tab 단위로 변경

#Extract rows
awk -F "\t" '$3 == "Chicken Bowl"' orders.tsv | head # 3번째 column이 "Chicken Bowl"인
                                                     # row들 출력
awk -F "\t" '{ if($3 == "Chicken Bowl") print $2, $3 }' orders.tsv | head
# if 문을 통해서 3번쨰 column이 "Chicken Bowl"인 row들만 2번째, 3번째 column을 출력
```

```bash
#Exercise1
touch large_orders.tsv # 빈 파일 생성, 굳이 필요는 없음
awk -F "\t" ' { if($2>=5) print $0 }' orders.tsv > large_orders.tsv

# column 2가 quantity이므로 이것이 5이상인 것들만 전체를 프린트하고, 그것을 large_orders.tsv
# 에 저장하는 방식
```

### Variables

```bash
awk -F "\t" ' \
BEGIN { sum = 0 } \ # Begin block에서 변수 초기화
{ if($3 == "Chicken Bowl") sum += $2 } \ # Body block에서 메인으로 작동시킬 코드 진행
END { print(sum) }' orders.tsv # 마지막으로 실행된 결과 출력

awk -F "\t" ' \
{ if($3 == "Chicken Bowl") sum += $2 } \ # Body block에서 메인으로 작동시킬 코드 진행
END { print(sum) }' orders.tsv
# 명시적으로는 sum을 초기화해 주어야하지만, awk가 알아서 자동으로 sum을 초기화 해줌

awk 'BEGIN{ print(5/7) }' # body가 없으면 굳이 파일명 필요 x, 간단한 float 계산 등에 유용
```

```bash
#Exercise2
awk -F "\t" '\
BEGIN { max = 0 }
{ if($3 == "Bottled Water" && $2 > max) max = $2}\
END { print(max) }' orders.tsv > largest_order.tsv

# max라는 변수를 초기화하여서, Bottled Water를 구매한 row들에 한해서 max값이 얼마인지 조사
# 그 후 그 결과값을 largest_order.tsv에 저장
```

### Arrays

```bash
awk -F "\t" '{ if($3 ~ /Burrito/) print }' orders.tsv | head 
# 틸데(~)를 통해서 Burrito가 있는 모든 line을 출력(정규 표현식 방식)

awk -F "\t" '\
	{ if($3 ~ /Burrito/) counts[$3] += $2 } \
	END { print counts["Chicken Burrito"] }'
order.tsv
# array counts를 암묵적으로 만듦, array는 key - value 형식인듯

awk -F "\t" '\
	{ if($3 ~ /Burrito/) counts[$3] += $2 }\
	END { for(k in counts) print(k, counts[k])
}' orders.tsv
# key - value 형식으로 접근하여 출력
```

```bash
awk -F "\t" '{\
	sub(/\$/, "", $NF); \ # 마지막 column의 $ 표시 제거 -> integer로 만들어 줌
	if($3 ~ /Burrito/) counts[$3] += $NF * $2 # 이 줄에서 사칙연산을 쓰므로 윗 줄이 필요
} \
	END { for(k in counts) print(k, counts[k])
}' orders.tsv
# sub는 임시적으로 특정부분(여기선 $NF)를 변환시키고, 바뀐 개수를 return함
# $는 특수문자이므로 escape를 통해서 바꿈
```

```bash
#Exercise3
#이중 if문과 semicolon 활용, 괄호 문제 때문에 조금 시간이 걸렸습니다..!
awk -F "\t" '{ \
  if($3 ~ /Burrito/){ \
    counts[$3] += $2;  # 이 부분에서 semicolon을 적지 않아서 계속 syntax error 발생했었음
    if($4 ~ /Guacomole/){
      G_counts[$3] += $2; # Guacomole이 $4에 포함된 경우의 수를 G_counts에서 셈
    }\
  }\
}\
	END { for(k in counts) print(k, G_counts[k]/counts[k])
}' orders.tsv > burritos_guac.tsv
```

# 후기

간단한 코딩 연습과 함께, Shell을 다뤄보는 좋은 경험이었다. `awk`의 작동 메커니즘은 `pandas` 와 크게 다르지 않아서, 좀 더 편하게 익힐 수 있었다.

추가로, 마지막 Exercise를 풀 때, nested if문을 써야 하는데, 간단한 구글링을 통해서 [https://www.linuxcommands.site/linux-text-processing-commands/linux-awk-command/shell-awk-if-else-if-else/](https://www.linuxcommands.site/linux-text-processing-commands/linux-awk-command/shell-awk-if-else-if-else/) 이 문서의 도움을 받아서 해결하였다.