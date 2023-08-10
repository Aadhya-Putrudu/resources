def main():
    list1()
    Name_list=["Lava Blaze 5g","Samsung S23 FE","Godrej Locker","Evidson Earphones",
            "Onida Android Tv","Voltas Air Conditioner","Usha Fan",
            "Karbonn Jumbo 5g","Celkon Karishma 5g","Apple iphone 14"]

    Price_list=[10999,50999,14999,999,19999,24999,7999,14999,19999,68999]
    check=1
    count=[0]
    Total_cost=[0]
    list_num=[]
    list_quantity=[]
    Coupon=10000
    flag=0

    while check!=4:
        options()
        option=int(input("Enter your choice : "))
        check=option
        if option==1:
            add_item(check,count,Total_cost,list_num,list_quantity,Price_list)
            print(list_num)
            print(list_quantity)
        elif option ==2:
            remove_item(list_num,count,list_quantity,Price_list,Total_cost)
            print(list_num)
            print(list_quantity)
        elif option ==3:
            bill_preview()

        print(list_num)
        print(list_quantity)

    print_bill(Name_list,list_quantity,Total_cost,count,Coupon,flag,list_num,Price_list)

def list1():
    list2="""
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
    print(list2)

def options():
    print("1. Add items")
    print("2. Remove items")
    print("3. Bill Preview")
    print("4. Print Bill")

def bill_preview():
    print("Feature coming soon :)")

def add_item(check,count,Total_cost,list_num,list_quantity,Price_list):
    while check>0:
        index=-1
        item_num=int(input("Enter item number:"))
        if item_num == 0:
            break
        item_quantity=int(input("Enter quantity:"))
        if item_num >0:
            flag=0
            if item_num in list_num:
                index1=list_num.index(item_num)
                flag=1
            if flag==1:
                list_quantity[index1]+=item_quantity
            else:
                list_num.append(item_num)
                list_quantity.append(item_quantity)

            count[0]=count[0]+item_quantity
            Total_cost[0]=Total_cost[0]+(item_quantity*Price_list[item_num-1])
        check=item_num




def remove_item(list_num,count,list_quantity,Price_list,Total_cost):
    list_num2=list_num.copy()
    list_quantity2=list_quantity.copy()
    print(list_num2)
    print(list_quantity2)
    check=1
    flag=0
    while check>0:
        item_num=int(input("Enter item number:"))
        if item_num == 0:
            break
        item_quantity=int(input("Enter quantity:"))
        if item_num>0:
            if item_num in list_num:
                index1 = list_num.index(item_num)
            res_quantity=list_quantity2[index1]-item_quantity
            if res_quantity<=0:
                list_num2.pop(index1)
                list_quantity2.pop(index1)
            else:
                list_quantity2[index1]=res_quantity
        count[0] = count[0] - item_quantity
        Total_cost[0] = Total_cost[0] - (item_quantity * Price_list[item_num - 1])

    list_num[:]=list_num2.copy()
    list_quantity[:]=list_quantity2.copy()
    print(list_num2)
    print(list_quantity2)



def print_bill(Name_list,list_quantity,Total_cost,count,Coupon,flag,list_num,Price_list):
    print("---------------------Bill--------------------")
    j=0
    for i in list_num:
        print(f"{Name_list[i-1]:<29}X{list_quantity[j]:>4} = {list_quantity[j]*Price_list[i-1]:>9}")
        j=j+1


    Payable_amount=Total_cost[0]

    if count[0]>=4 or Total_cost[0]>=100000:
        Payable_amount=Total_cost[0]-Coupon
        flag=1


    print(" "*34 +"____________")
    print(f"Total Cost{' '*25}= {Total_cost[0]:>9}")
    if flag==1:
        print(f"Coupon{' '*29}= {Coupon:>9}")

    print(f"Payable Amount{' '*21}= {Payable_amount:>9}")

    print(count[0])



main()
