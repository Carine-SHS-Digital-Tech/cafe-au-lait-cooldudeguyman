#code = 01000101010001010100010010101
import csv
special = 1 # i used this to make it loop forever
totals = {
    "THIS IS A DAILY SUMMARY": "",
    "total orders": 0,
    "total days income": 0,
    "total GST": 0,
    "take away orders": 0,
    "eat in orders": 0,
    } # all data in daily summery
while special == 1: # while loop that goes on forever(unless stoped)
    numnum1 = 0 
    numnum2 = 0
    numnum3 = 0
    numnum4 = 0 # all used for calculating quantity
    order = {} #dictionary
    tw = 1 #take away fee
    price = 0
    print("operations: order and daily summary")
    operation = input("What operation? ") # to make a new order or daily summary
    operation = operation.lower() # even if its in caps it works
    if operation == "order":
        account = input("enter name: ") #info for order
        order["name"] = account #putting it in the dictionary
        time = input("time to pick up: ") #info for order
        order["time of order"] = time #putting it in the dictionary
        error1 = 0 # used to repeat untill its right
        while error1 == 0:
            TorE = input("enter number (1)take away (has a 5% fee) or (2)eat in: ") #info for order
            if TorE == "1": # check if its option 1
                tw = 1.05 # its adding the take away fee
                order["order type"] = "take away" #putting it in the dictionary
                error1 = error1 + 1 #ends loop
            elif TorE == "2": # checking if its option 2
                order["order type"] = "eat in" #putting it in the dictionary
                error1 = error1 + 1 #ends loop
            else:
                print("miss input re enter") # makes you loop to begining
        print("""            (1)Cappuccino $3.00
        (2)	Espresso $2.25
        (3)	Latte $2.50
        (4)	Iced Coffee $2.50""") #menu
        morecoffee = 0 # used to repeat untill its right
        while morecoffee == 0: #loop
            coffee = input("what coffee do you want (enter number): ") # entered num is what coffee you want
            if coffee == "1": # works if its 1
                quantity1 = input("how many do you want: ") #asks for how many you want
                numnum1 = numnum1 + int(quantity1) #keeps adding quantity
                order['number of Cappuccino ($3.00 each)'] = numnum1 #added to dict
                order["single Cappuccino GST"] = round(3 * 0.1, 2) #added to dict and rounds to 2 digits
                price = price + int(quantity1) * 3 #adds to price
            elif coffee == "2": # works if its 2
                quantity1 = input("how many do you want: ") #asks for how many you want
                numnum2 = numnum2 + int(quantity1) #keeps adding quantity
                order["number of Espresso ($2.25 each)"] = numnum2 #added to dict
                order["single Espresso GST"] = round(2.25 * 0.1, 2) #added to dict and rounds to 2 digits
                price = price + int(quantity1) * 2.25 #adds to price
            elif coffee == "3": # works if its 3
                quantity1 = input("how many do you want: ") #asks for how many you want
                numnum3 = numnum3 + int(quantity1) #keeps adding quantity
                order["number of Latte ($2.50)"] = numnum3 #added to dict
                order["single Latte GST"] = round(2.5 * 0.1, 2) #added to dict and rounds to 2 digits
                price = price + int(quantity1) * 2.5 #adds to price
            elif coffee == "4": # works if its 4
                quantity1 = input("how many do you want: ") #asks for how many you want
                numnum4 = numnum4 + int(quantity1) #keeps adding quantity
                order["number of Iced Coffee ($2.50)"] = numnum4 #added to dict
                order["single Iced Coffee GST"] = round(2.5 * 0.1, 2) #added to dict and rounds to 2 digits
                price = price + int(quantity1) * 2.5 #adds to price
            else:
                print("thats not an opption") #loops back
            error2 = 0
            while error2 == 0: #used to ask if you want another if yes repeats above section if not it ends
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
        
        if tw == 1.05: # checks if its take away then adds stuff to the totals and order dict then adds the orders dict to daily_orders.csv
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
        elif tw == 1: # checks if its eat in then adds stuff to the totals and order dict then adds the orders dict to daily_orders.csv
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
    elif operation == "daily summary": # prints totals and stores them + resets the daily summary then goes back to begining
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
    else: # goes back to beggining
        print("this is not an operation")
