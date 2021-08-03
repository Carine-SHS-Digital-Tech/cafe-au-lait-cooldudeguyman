#code = 01000101010001010100010010101
tw = 0
special = 1
totals = {
    "total orders": 0,
    "total days income": 0,
    "total GST": 0,
}
while special == 1:
    order = {

    }
    operation = input("What operation? ")
    operation = operation.lower()
    if operation == "order":
        account = input("enter name: ")
        order[account] = ""
        time = input("time to pick up: ")
        order["time of order"] = time
        error1 = 0
        while error1 == 0:
            TorE = input("enter number (1)take away or (2)eat in: ")
            if TorE == 1:
                tw = tw = 1.05
                order["order type"] = TorE
                error1 = error1 + 1
            elif TorE == 2:
                order["order type"] = TorE
                error1 = error1 + 1
            else:
                print("miss input re enter")
        print("""(1) Cappuccino $3.00
        (2)	Espresso $2.25
        (3)	Latte $2.50
        (4)	Iced Coffee $2.50""")
        morecoffee = 0
        while morecoffee == 0:
            coffee = input("what coffee do you want (enter number): ")
            if coffee == 1:
                order["Cappuccino"]
            quantity = input(int("how many do you want: "))
                   

