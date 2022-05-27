def pattern(size):
    alpha=64
    for i in range(size-1,-1,-1):
        for j in range(i):
            print("__",end="")
        for k in range(size-1,i,-1):
            print(chr(alpha+k),end="_")
        print()
    
pattern(3)
