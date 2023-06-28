#33. Write a program to display the last digit of a number.
num=int(input("enter number"))
if num>9:
    a=num%10
    print(a)
else:
    print("no digit number")
