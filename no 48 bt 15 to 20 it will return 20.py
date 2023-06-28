#48.Write a Python program to sum of two given integers. However, if the sum is
#between 15 to 20 it will return 20.
a=int(input("enter number"))
b=int(input("enter number"))
sum=a+b
if (sum>15 and sum<20):
    print("it will return 20",sum)
else:
    print("it will not return 20",sum)
