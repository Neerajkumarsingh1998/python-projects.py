def display_menu(menu):
    print("Welcome to Patel Restaurant")
    for item, price in menu.items():
        print(f"{item}: {price}")


def take_order(menu):
    order_total = 0
    while True:
        item = input("Enter the name of item you want to order: ").strip().lower()
        if item in menu:
            order_total += menu[item]
            print(f"Your item '{item}' has been added to your order.")
        else:
            print(f"Ordered item '{item}' is not available!")

        another_order = input("Do you want to order another item? (yes/no): ").strip().lower()
        if another_order != "yes":
            break

    return order_total


def main():
    menu = {
        'pizza': 40,
        'salad': 20,
        'panirchila': 80,
        'pasta': 60,
        'cold coffee': 100
    }

    display_menu(menu)
    order_total = take_order(menu)
    print(f"The total amount to pay is: {order_total}")
if __name__=="__main__":
    main()