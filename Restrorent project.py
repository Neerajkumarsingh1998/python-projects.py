
menu={
        'pizza':40,
        'pasta':60,
        ' cold coffee':100,
}
print("welcome to patel restaurant")
print("pizza:40",
      "pasta:60",
      "coldcoffee:100")
order_total=0
item_1=input("Enter the name of item you want to order= ")
if item_1 in menu:
    order_total +=menu [item_1]
    print(f"your item {item_1}has been added to your order")
else:
    print(f"order item {item_1}is not avaialable yet!")
another_order=input("Do you want to another item?(yes/No)")
if another_order!="yes":

    item_2=input("Enter the name of second item=")
    if item_2 in menu:
        order_total +=menu[item_2]
        print(f"Item{item_2}has been added to order")
    else:
        print(f"ordered item {item_2}is not avaialable!")
another_order = input("Do you want to another item?(yes/No)")
if another_order == "yes":
    item_3 = input("Enter the name of second item=")
    if item_3 in menu:
        order_total += menu[item_3]
        print(f"Item{item_3}has been added to order")
    else:
        print(f"ordered item {item_3}is not avaialable!")
print(f"The total amount of items to pay is{order_total}")
