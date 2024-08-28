def factorial(number) :
    if(number<=0):
        return "Factorial for the Entered Number ",number," is not Possible"
    elif(number>0) :
        value=1
        for i in range(number,1,-1):
            value=value*i
        return "Factorial for the Entered Number ",number," is", value

n=int(input("Enter a Number : "))
print(factorial(n))

