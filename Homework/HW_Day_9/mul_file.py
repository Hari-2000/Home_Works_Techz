number = int(input("Enter A Number : "))

f_name = f"{number}.txt"


f_object = open(f_name,'w')

for i in range(1,11) :    
    f_object.writelines(f"{number}*{i}={number*i}\n")

f_object.close()