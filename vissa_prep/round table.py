x=int(input())
def table(x):
    if x==0:
        return 1
    else:
        return x*table(x-1)
print(table(x))
