def odd_even(n):
    if(n%2==0) :
        return(n,"is a Even Number")
    else :
        return n,"is a Odd Number"

number = int(input("Enter a Number : "))
x=odd_even(number)
print(x)        