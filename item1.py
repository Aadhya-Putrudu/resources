print("List of Items:")
print("1. Lava Blaze 5g----------- 10999")
print("2. Samsung S23 FE---------- 30999")
print("3. Godrej Locker----------- 14099")
print("4. Voltas Air Conditioner-- 24999")
print("5. Evidson Earphones------- 9999")
print("6. Onida Android Tv-------- 24999")

cost1=10999
cost2=30999
cost3=14099
cost4=24999
cost5=9999
cost6=24999

print("Please enter number of items purchased or zero if not purchased:")
item1=int(input("Enter number of Lava phones purchased:"))
item2=int(input("Enter number of Samsung phones purchased:"))
item3=int(input("Enter number of Godrej Lockers purchased:"))
item4=int(input("Enter number of Voltas ACs purchased:"))
item5=int(input("Enter number of Evidson earphones purchased:"))
item6=int(input("Enter number of Onida TVs purchased:"))

count=0
flag=0
Total_cost=0
Coupon=10000


if item1>0:
	count=count+item1
	Total_cost=Total_cost+(item1*cost1)
if item2>0:
	count=count+item2
	Total_cost=Total_cost+(item2*cost2)
if item3>0:
	count=count+item3
	Total_cost=Total_cost+(item3*cost3)
if item4>0:
	count=count+item4
	Total_cost=Total_cost+(item4*cost4)
if item5>0:
	count=count+item5
	Total_cost=Total_cost+(item5*cost5)
if item6>0:
	count=count+item6
	Total_cost=Total_cost+(item6*cost6)

Payable_amount=Total_cost

if count>=4 or Total_cost>=100000:
	Payable_amount=Total_cost-Coupon
	flag=1

print("------------------------Bill------------------------")
if item1>0:
	print("Lava Blaze 5g -----------",item1,"=",item1*cost1)
if item2>0:
	print("Samsung S23 FE ----------",item2,"=",item2*cost2)
if item3>0:
	print("Godrej Locker -----------",item3,"=",item3*cost3)
if item4>0:
	print("Voltas Air Conditioner --",item4,"=",item4*cost4)
if item5>0:
	print("Evidson Earphones -------",item5,"=",item5*cost5)
if item6>0:
	print("Onida Android Tv --------",item1,"=",item6*cost6)

print("                           __________")
print("Total Cost                =",Total_cost)
if flag==1:
	print("Coupon                    =",Coupon)

print("Payable Amount            =",Payable_amount)



