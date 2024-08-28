number = int(input("Enter a Value : "))

for i in range(1,number+1):
    for j in range(i):
        print("*",end=" ")
    print("\n")    