#22.A company decided to give a bonus of 5% to an employee if his/her year of
#service is more than 5 years. Ask users for their salary and year of service and
#print the net bonus amount.
salary=int(input("enter salary"))
year=int(input("enter year"))
if year>5:
    bonus=salary*5/100
    print("net bonus amount is",bonus)
else:
    print("service not more 5 years")
