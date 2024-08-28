number = int(input("Enter a Number : "))

for i in range(1,number+1):
    for j in range(1,i+1):
        if(j==1):
            print("[",end=" ")
        print(j,end=" ")
        if(j==i):
            print("]")
            print("\n")
