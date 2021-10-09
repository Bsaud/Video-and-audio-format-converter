menu={'hommus':{ 'name':'hommus','price':30.0}, 'lantil':{'name':'lantil','price':25.0}}
print('menu')
for key in menu:
    print(menu[key]["name"] +' '+ str(menu[key]["price"]))
bill=0.0 
ordered_items=list()
while True:
    order=input('enter the name of the dish: ')
    nop=float(input('how many: '))
    ordered_items.append(order)
    order_price=menu[order]['price'] * nop
    bill=bill+order_price
    more=input("do you want to add more? yes // no: ")
    if more=='no':
        break
    elif more=='yes':
        continue
print('recipt \n')
for i in ordered_items:
    print(i)
print("the total bill price is "+str(bill)+ " OMR")
        