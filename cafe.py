#code = 01000101010001010100010010101
import csv
special = 1
totals = {
    "THIS IS A DAILY SUMMARY": "",
    "total orders": 0,
    "total days income": 0,
    "total GST": 0,
    "take away orders": 0,
    "eat in orders": 0,
}
while special == 1:
    order = {}
    tw = 1
    price = 0
    operation = input("What operation? ")
    operation = operation.lower()
    if operation == "order":
        account = input("enter name: ")
        order["name"] = account
        time = input("time to pick up: ")
        order["time of order"] = time
        error1 = 0
        while error1 == 0:
            TorE = input("enter number (1)take away (has a 5% fee) or (2)eat in: ")
            if TorE == "1":
                tw = tw = 1.05
                order["order type"] = TorE
                error1 = error1 + 1
            elif TorE == "2":
                order["order type"] = TorE
                error1 = error1 + 1
            else:
                print("miss input re enter")
        print("""        (1)    Cappuccino $3.00
        (2)	Espresso $2.25
        (3)	Latte $2.50
        (4)	Iced Coffee $2.50""")
        morecoffee = 0
        while morecoffee == 0:
            coffee = input("what coffee do you want (enter number): ")
            if coffee == "1":
                quantity1 = input("how many do you want: ")
                order["Cappuccino num"] = quantity1
                price = price + int(quantity1) * 3
            elif coffee == "2":
                quantity1 = input("how many do you want: ")
                order["Espresso num"] = quantity1
                price = price + int(quantity1) * 2.25
            elif coffee == "3":
                quantity1 = input("how many do you want: ")
                order["Latte num"] = quantity1
                price = price + int(quantity1) * 2.5
            elif coffee == "4":
                quantity1 = input("how many do you want: ")
                order["Iced Coffee num"] = quantity1
                price = price + int(quantity1) * 2.5
            else:
                print("thats not an opption")
            error2 = 0
            while error2 == 0:
                cont = input("do you want to order another coffee? y/n: ")
                if cont == "y":
                    print("""        (1)    Cappuccino $3.00
                    (2)	Espresso $2.25
                    (3)	Latte $2.50
                    (4)	Iced Coffee $2.50""")
                    error2 = error2 + 1 
                elif cont == "n":
                    morecoffee = morecoffee + 1
                    error2 = error2 + 1 
                else:
                    print("answer using y or n")
        totals["total orders"] + 1
        
        if tw == 1.05:
            price = price * tw
            totals["take away orders"] + 1
        elif tw == 1:
            totals["eat in orders"] + 1
        GST = price * 0.1
        priceGST = price + GST
        totals["total GST"] + GST
        totals["total days income"] + priceGST
        order["total(without GST)"] = price
        order["total(with Gst)"] = priceGST
        print("heres the info about order", order, ":)")
        
        storedata = open("daily_order.csv", "a")
        storedata.write(order)
        storedata.close()
    elif operation == "daily summary":
        print(totals)
        storedata = open("daily_order.csv", "a")
        storedata.write(totals)
        storedata.close()
    else:
        print("this is not an operation")
