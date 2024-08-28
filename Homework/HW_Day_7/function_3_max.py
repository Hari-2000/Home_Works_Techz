def maximum(n1,n2,n3) :
    if (n1>n2) and (n2>n3) :
        print(n1,"is the Largest Number")
    elif (n2>n1) and (n2>n3) :
        print(n2,"is the Largest Number")
    else :
        print(n3,"is the Largest Number") 

# n1,n2,n3 are 3 numbers passed to the function




l1=int(input("Enter Number 1 :"))
l2=int(input("Enter Number 2 :"))
l3=int(input("Enter Number 3 :"))

maximum(l1,l2,l3)

# l1,l2,l3 are 3 numbers to be enetered by the user