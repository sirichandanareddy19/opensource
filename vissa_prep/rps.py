A,B=input().split()
wins={
    'R':'P','P':'S','S':'R'
    
}
if A==B:
    print("NULL")
elif wins[A]==B:
    print("Charan")
else:
    print("Vignesh")
