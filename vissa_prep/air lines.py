x,n=map(int,input().split())
carry=x*100
left_passengers=max(0,n-carry)
if left_passengers>0:
    min_no_of_planes=(left_passengers+99)//100
else:
    min_no_of_planes=0
print(min_no_of_planes)
