## BA10B

B = ' '.join(input().split()).split()
B_trans, B_seq, Ax, Ay, Az, Bx, By, Bz = B[0], B[6], float(B[15]), float(B[16]), float(B[17]), float(B[19]), float(B[20]), float(B[21])
P = 1

for i in range(len(B_seq)):
  tr = 1
  if B_seq[i] == 'A':
    if B_trans[i] == 'x': tr = Ax
    elif B_trans[i] == 'y': tr = Ay
    else: tr = Az
  else:
    if B_trans[i] == 'x': tr = Bx
    elif B_trans[i] == 'y': tr = By
    else: tr = Bz
  P = P * tr

print(P)
