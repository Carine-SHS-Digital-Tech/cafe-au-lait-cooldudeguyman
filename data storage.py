dick = {"take away":0,
"dine-in":0,
"total order":0,
"num of Cappuccino":0,
"num of Espresso":0,
"num of Latte":0,
"num of Iced Coffee":0,
}
take = 0
print("""•	Cappuccino $3.00
•	Espresso $2.25
•	Latte $2.50
•	Iced Coffee $2.50
""")
aoro = input("take away or dine in? ")
if aoro.lower is "take away":
    take = take + 1
    dick["take away"] + 1
    
print(dick)