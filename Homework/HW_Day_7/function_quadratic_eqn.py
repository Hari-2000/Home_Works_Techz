import math as m


a=int(input("Enter First Number : "))
b=int(input("Enter Second Number : "))
c=int(input("Enter Third Number : "))

k = b**2 - 4*a*c

x1 = (-1*b+m.sqrt(k))/(2*a)
x2 = (-1*b-m.sqrt(k))/(2*a)

print("Solutions are ", x1 , "and", x2)
