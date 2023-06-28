#43.Accept the age, sex (‘M’, ‘F’), number of days and display the wages accordingly
#If age does not fall in any range then display the following message: “Enter
#appropriate age”
#Age Sex Wage/day
#>=18 and <30 M 700
#F 750
#>=30 and <=40 M 800
#F 850
sex=input("enter name")
age=int(input("enter age"))
day=int(input("enter wage"))
if sex=="m" and age>=18 and age<30:
    wage=day*700
    print("wage is",wage)
elif sex=="f" and age>=18 and age<30:
    wage=day*750
    print("wage is",wage)
elif sex=="m" and age>=30 and age<=40:
    wage=day*800
    print("wage is",wage)
elif sex=="f" and age>=30 and age<=40:
    wage=day*850
    print("wage is",wage)
else:
    print("no wage")
