list1="""
1. Lava Blaze 5g ---------- 10999
2. Samsung S23 FE --------- 50999
3. Godrej Locker ---------- 14999
4. Evidson Earphones ------ 999
5. Onida Android Tv ------- 19999
6. Voltas Air Conditioner - 24999
7. Usha Fan --------------- 7999
8. Karbonn Jumbo 5g ------- 14999
9. Celkon Karishma 5g ----- 19999
10. Apple iphone 14 ------- 68999
"""

print(list1)

Name_list=["Lava Blaze 5g","Samsung S23 FE","Godrej Locker","Evidson Earphones",
			"Onida Android Tv","Voltas Air Conditioner","Usha Fan",
			"Karbonn Jumbo 5g","Celkon Karishma 5g","Apple iphone 14"]

Price_list=[10999,50999,14999,999,19999,24999,7999,14999,19999,68999]

print("Enter details or zero to stop.")

check=1
count=0
Total_cost=0
list_num=[]
list_quantity=[]
list_cost=[]
Coupon=10000
flag=0

while check>0:
	item_num=int(input("Enter item number:"))
	if item_num == 0:
		break
	item_quantity=int(input("Enter quantity:"))
	if item_num >0:
		count=count+item_quantity
		Total_cost=Total_cost+(item_quantity*Price_list[item_num-1])
		list_num.append(item_num-1)
		list_quantity.append(item_quantity)
		list_cost.append(item_quantity*Price_list[item_num-1])
	check=item_num

j=0

print("---------------------Bill--------------------")
for i in list_num:
	print(f"{Name_list[i]:<29}X{list_quantity[j]:>4} = {list_cost[j]:>9}")
	j=j+1


Payable_amount=Total_cost

if count>=4 or Total_cost>=100000:
	Payable_amount=Total_cost-Coupon
	flag=1


print(" "*34 +"____________")
print(f"Total Cost{' '*25}= {Total_cost:>9}")
if flag==1:
	print(f"Coupon{' '*29}= {Coupon:>9}")

print(f"Payable Amount{' '*21}= {Payable_amount:>9}")


