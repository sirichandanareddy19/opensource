A,B,C,X=list(map(int,input().split()))
if (A+B>=X or A+C>=X or B+C>=X):
    print("YES")
else:
    print("NO")