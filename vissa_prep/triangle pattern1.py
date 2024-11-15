n=int(input())
a=1
for i in range(1,n+1):
    print(*range(a,a+i))
    a+=i
