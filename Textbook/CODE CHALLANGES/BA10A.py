## BA10A

A = ' '.join(input().split()).split()
seq, AA, AB, BA, BB = A[0], float(A[8]), float(A[9]), float(A[11]), float(A[12])
P = 1/2

for i in range(len(seq)):
  tr = 1
  if i == 0 : continue
  if seq[i-1] == 'A':
    if seq[i] == 'A': tr = AA
    else: tr = AB
  else:
    if seq[i] == 'A': tr = BA
    else: tr = BB
  P = P * tr

print(P)
