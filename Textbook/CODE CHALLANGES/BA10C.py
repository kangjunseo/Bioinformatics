## BA10C

C = ' '.join(input().split()).split('--------')
C_seq = C[0].rstrip()
L = len(C_seq)
init = 0.5
C_trans, C_Emis = C[3].split(), C[4].split()
AA, AB, BA, BB = map(float, [C_trans[3], C_trans[4], C_trans[6], C_trans[7]])
Ax, Ay, Az, Bx, By, Bz = map(float, [C_Emis[4], C_Emis[5], C_Emis[6], C_Emis[8], C_Emis[9], C_Emis[10]])

dp = [[0 for _ in range(2)] for _ in range(L)]
prev = [['' for _ in range(2)] for _ in range(L)]
for i in range(L): 

    ## initialization
    if i == 0:
        dp[i][0], dp[i][1] = init, init
        if C_seq[i] == 'x':
            dp[i][0] *= Ax
            dp[i][1] *= Bx
        elif C_seq[i] == 'y':
            dp[i][0] *= Ay
            dp[i][1] *= By
        else:
            dp[i][0] *= Az
            dp[i][1] *= Bz

    ## induction
    else:
        if dp[i-1][0] * AA > dp[i-1][1] * BA:
            dp[i][0] = dp[i-1][0] * AA
            prev[i][0] = 'A'
        else:
            dp[i][0] = dp[i-1][1] * BA
            prev[i][0] = 'B'

        if dp[i-1][0] * AB > dp[i-1][1] * BB:
            dp[i][1] = dp[i-1][0] * AB
            prev[i][1] = 'A'
        else:
            dp[i][1] = dp[i-1][1] * BB
            prev[i][1] = 'B'


        if C_seq[i] == 'x':
            dp[i][0] *= Ax
            dp[i][1] *= Bx
        elif C_seq[i] == 'y':
            dp[i][0] *= Ay
            dp[i][1] *= By
        else:
            dp[i][0] *= Az
            dp[i][1] *= Bz

ans = ''
if dp[L-1][0] > dp[L-1][1]:
    ans = 'A'
    prev_l = 'A'
else:
    ans = 'B'
    prev_l = 'B'
    
for i in range(L-1):
    if prev_l == 'A':
        ans += prev[L-i-1][0]
        prev_l = 'A'
    else:
        ans += prev[L-i-1][1]
        prev_l = 'B'

print(ans[::-1])
