#comment from git
#comment from vs
menu = {'mango':10,'strawberry':20,'grapes':30,'apple':40,'pineapple':50,'allmix':60}
print("MENU : ",menu)
bill = {}
order = {}
while True :
    juice = list(map(str,input("ENTER WHICH JUICE YOU WANT :").split()))
    quantity = list(map(int,input("ENTER QUANTITY :").split()))
    for i in range(len(juice)):
        if juice[i] not in bill :
            bill.update({juice[i]:0})
            order.update({juice[i]:quantity[i]})
            temp = menu[juice[i]]*quantity[i]
            bill[juice[i]] = bill[juice[i]] + temp 
        else :
            temp = menu[juice[i]] * quantity[i]
            bill[juice[i]] = temp + bill[juice[i]]
            order[juice[i]] = order[juice[i]] + quantity[i]

    q = int(input("DO YOU WNAT ANYTHING PRESS 1 ELSE 0 :"))
    if q == 1:
        continue
    elif q == 0 :
        break
    else:
        print("INVALID INPUT")
        break

sum=0
line='__'
space=' '
print(f"{line*40}")
print(f" JUICE {space:5} QUANTITY {space:5} COST_OF_EACH_JUICE {space:5} TOTAL_COST_OF_EACH _JUICE")
print(f"{line*40}")
for i in bill:
    sum=sum+bill[i]
    print(f"| {i:15} {order[i]} {' '*15} {menu[i]} {' '*20} {bill[i]} ")

print(f"{line*40}")
print(f"{' '*45}TOTAL AMOUNT : {sum}")
print(f"{line*40}")