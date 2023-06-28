#35.Write a program to accept the cost price of a bike and display the road tax to be
#paid according to the following criteria :
#a. Cost price (in Rs) Tax
#b. > 100000 15 %
#c. > 50000 and <= 100000 10%
#d. <= 50000 5%
cp=int(input("enter cost:-"))
if cp>100000:
    tax=cp*15/100
    print("road tax to be paid=",tax)
elif cp>50000 and cp<=100000:
    tax=cp*10/100
    print("road tax to be paid=",tax)
elif cp<=50000:
    tax=cp*5/100
    print("road tax to be paid=",tax)
else:
    print("no tax")
