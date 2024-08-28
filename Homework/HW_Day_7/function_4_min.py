def minimum(n1,n2,n3,n4) :
    if (n1<n2) and (n2<n3) and (n1<n4) :
        print(n1,"is the Smallest Number")
    elif (n2<n1) and (n2<n3) and (n2<n4) :
        print(n2,"is the Smallest Number")
    elif (n3<n1) and (n3<n2) and (n3<n4) :
        print(n3,"is the Smallest Number")
    else :
        print(n4,"is the Smallest Number") 

# n1,n2,n3,n4 are the 4 numbers passed to the function




l1=int(input("Enter Number 1 :"))
l2=int(input("Enter Number 2 :"))
l3=int(input("Enter Number 3 :"))
l4=int(input("Enter Number 4 :"))

minimum(l1,l2,l3,l4)

# l1,l2,l3,l4 are the 4 numbers to be enetered by the user