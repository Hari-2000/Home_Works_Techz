x=[1,1000,(2,55,'India',[1,100,1000,100,'UK']),1,20]

print(x)

x[x.index(20)]='abcd'

print(x)

x[2]=(2,55,'Japan',[1,100,1000,100,'UK'])

print(x)



# Tuples are Immutable
# Tuples present inside a list are Mutable 