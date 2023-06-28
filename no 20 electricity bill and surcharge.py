#20.Write a python program to input electricity unit charges and calculate total
#electricity bill according to the given condition:
#For first 50 units Rs. 0.50/unit
#For next 100 units Rs. 0.75/unit
#For next 100 units Rs. 1.20/unit
#For unit above 250 Rs. 1.50/unit
#An additional surcharge of 20% is added to the bill
unit=int(input("enter unit"))
if unit<=50:
    amount=unit*0.50
    surcharge=unit*20/100
    print(amount+surcharge)
elif unit>50 and unit<=150:
    amount=unit*0.75
    surcharge=unit*20/100
    print(amonut+surcharge)
elif unit>150 and unit<=250:
    amount=unit*1.20
    surcharge=unit*20/100
    print(amonut+surcharge)
elif unit>250:
    amount=unit*0.150
    surcharge=unit*20/100
    print(amonut+surcharge)
else:
    print("no unit")
    
    
    
