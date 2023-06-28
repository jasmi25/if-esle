#32.Write a program to calculate the electricity bill (accept number of unit from user)
#according to the following criteria :
#Unit Price
#First 100 units no charge
#Next 100 units Rs 5 per unit
#After 200 units Rs 10 per unit
#(For example if input unit is 350 than total bill amount is Rs2000)
unit=int(input("enter unit"))
if unit<100:
    print("no charge")
elif unit>100 and unit<=200:
    e_bill=unit*5
    print("electricity bill is",e_bill)
elif unit>200:
    a=unit-100
    b=100*5
    bill=a*10-b
    print("electricity bill is",bill)
else:
    print("no bill")
