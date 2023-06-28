#19.Write a python program to input basic salary of an employee and calculate its
#Gross salary according to following:
#Basic Salary <= 10000 : HRA = 20%, DA = 80%
#Basic Salary <= 20000 : HRA = 25%, DA = 90%
#Basic Salary > 20000 : HRA = 30%, DA = 95%
bs=int(input("enter number:-"))
if bs<=10000:
    hrd=(bs*20/100)
    da=(bs*80/100)
    gs=(bs+hrd+da)
    print(gs)
elif bs<=20000:
    hrd=(bs*25/100)
    da=(bs*90/100)
    gs=(bs+hrd+da)
    print(gs)
elif bs>20000:
    hrd=(bs*30/100)
    da=(bs*95/100)
    gs=(hed+da+bs)
    print(gs)
else:
    print("no gross salary")
