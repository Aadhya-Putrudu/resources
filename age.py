data={}

name1=input("Enter your name:")
age1=int(input("Enter your age:"))
name2=input("Enter your name:")
age2=int(input("Enter your age:"))
name3=input("Enter your name:")
age3=int(input("Enter your age:"))

data={name1:age1,name2:age2,name3:age3}

print(data)
large=name1
#print(data[large])
if data[name2]>data[large]:
	large=name2
if data[name3]>data[large]:
	large=name3

print("The elder one name is",large)