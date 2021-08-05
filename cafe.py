#code = 01000101010001010100010010101
import csv
special = 1
cool = 1
totals = {
    "THIS IS A DAILY SUMMARY": "",
    "total orders": 0,
    "total days income": 0,
    "total GST": 0,
    "take away orders": 0,
    "eat in orders": 0,
    }
while special == 1:
    numnum1 = 0
    numnum2 = 0
    numnum3 = 0
    numnum4 = 0
    order = {}
    tw = 1
    price = 0
    print("operations: order and daily summary")
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
                order["order type"] = "take away"
                error1 = error1 + 1
            elif TorE == "2":
                order["order type"] = "eat in"
                error1 = error1 + 1
            else:
                print("miss input re enter")
        print("""            (1)Cappuccino $3.00
        (2)	Espresso $2.25
        (3)	Latte $2.50
        (4)	Iced Coffee $2.50""")
        morecoffee = 0
        while morecoffee == 0:
            coffee = input("what coffee do you want (enter number): ")
            if coffee == "1":
                quantity1 = input("how many do you want: ")
                numnum1 = numnum1 + int(quantity1)
                order['number of Cappuccino ($3.00 each)'] = numnum1
                order["single Cappuccino GST"] = round(3 * 0.1, 2)
                price = price + int(quantity1) * 3
            elif coffee == "2":
                quantity1 = input("how many do you want: ")
                numnum2 = numnum2 + int(quantity1)
                order["number of Espresso ($2.25 each)"] = numnum2
                order["single Espresso GST"] = round(2.25 * 0.1, 2)
                price = price + int(quantity1) * 2.25
            elif coffee == "3":
                quantity1 = input("how many do you want: ")
                numnum3 = numnum3 + int(quantity1)
                order["number of Latte ($2.50)"] = numnum3
                order["single Latte GST"] = round(2.5 * 0.1, 2)
                price = price + int(quantity1) * 2.5
            elif coffee == "4":
                quantity1 = input("how many do you want: ")
                numnum4 = numnum4 + int(quantity1)
                order["number of Iced Coffee ($2.50)"] = numnum4
                order["single Iced Coffee GST"] = round(2.5 * 0.1, 2)
                price = price + int(quantity1) * 2.5
            else:
                print("thats not an opption")
            error2 = 0
            while error2 == 0:
                cont = input("do you want to order another coffee? y/n: ")
                if cont == "y":
                    print("""                       (1)Cappuccino $3.00
                    (2)	Espresso $2.25
                    (3)	Latte $2.50
                    (4)	Iced Coffee $2.50""")
                    error2 = error2 + 1 
                elif cont == "n":
                    morecoffee = morecoffee + 1
                    error2 = error2 + 1 
                else:
                    print("answer using y or n")
            totals["total orders"] = totals["total orders"] + 1
        
        if tw == 1.05:
            price = price * tw
            price = round(price, 2)
            totals["take away orders"] + 1
            GST = price * 0.1
            GST = round(GST, 2)
            priceGST = price + GST
            priceGST = round(priceGST, 2)
            totals["total GST"] = totals["total GST"] + GST
            totals["total days income"] = totals["total days income"] + priceGST
            totals["take away orders"] = totals["take away orders"] + 1
            order["total(without GST)"] = price
            order["total(with Gst)"] = priceGST
            print("heres your receipt", order, ":)")
            ordertocsv = str(order) + "\n"
            storedata = open("daily_order.csv", "a")
            storedata.write(ordertocsv)
        elif tw == 1:
            totals["eat in orders"] + 1
            GST = price * 0.1
            GST = round(GST, 2)
            priceGST = price + GST
            priceGST = round(priceGST, 2)
            totals["total GST"] = totals["total GST"] + GST
            totals["total days income"] = totals["total days income"] + priceGST
            totals["eat in orders"] = totals["eat in orders"] + 1
            order["total(without GST)"] = price
            order["total(with Gst)"] = priceGST
            print("heres your receipt", order, ":)")
            ordertocsv = str(order) + "\n"
            storedata = open("daily_order.csv", "a")
            storedata.write(ordertocsv)
            storedata.close()
    elif operation == "daily summary":
        print(totals)
        totalstocsv = str(totals) + "\n"
        storedata = open("daily_order.csv", "a")
        storedata.write(totalstocsv)
        storedata.close()
        totals = {
            "THIS IS A DAILY SUMMARY": "",
            "total orders": 0,
            "total days income": 0,
            "total GST": 0,
            "take away orders": 0,
            "eat in orders": 0,
        }    
    else:
        print("this is not an operation")
