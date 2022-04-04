n = int(input("Enter a raw: "))
k = 2*n
for i in range(0,n):
    for j in range(0,i+1):
        print("*",end="")
    k = k-2
    for j in range(0,i+1):
        print("*",end="")
    print("")