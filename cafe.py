#code = 01000101010001010100010010101
tw = 0
special = 1
totals = {
    "total orders": 0,
    "total days income": 0,
    "total GST": 0,
}
while special == 1:
    order = {}
    operation = input("What operation? ")
    operation = operation.lower()
    if operation == "order":
        account = input("enter name: ")
        order[account]
        time = input("time to pick up: ")
        order["time of order"] = time
        TorE = input("take away or eat in: ")
        TorE = TorE.lower
        order[TorE]
        if TorE == "take away":
            tw = tw = 1.05
        print("""•	Cappuccino $3.00
        •	Espresso $2.25
        •	Latte $2.50
        •	Iced Coffee $2.50""")
        

