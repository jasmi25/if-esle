num=int(input("enter number:-"))
if num%3==0 and num%7==0:
    print("ice cream")
elif num%7==0:
    print("ice")
elif num%3==0:
    print("cream")
else:
    print("no ice cream")
