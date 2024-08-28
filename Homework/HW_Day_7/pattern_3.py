number=int(input("Enter a Number : "))
x=-1

for i in range(1,number+1):
    x=x+1
    for j in range(1,2*number):
        
        if (j>=number-x) and (j<=number+x) and (k==1):
            print("*",end=" ")
            k=0
        else :
            print("  ",end="")
            k=1
    print()

          
            
            

                