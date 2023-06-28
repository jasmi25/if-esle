#46.Write a Python program to find those numbers which are divisible by 7 and
#multiple of 5, between 1500 and 2700 (both included).
num=int(input("enter number: "))
if num>=1500 and num<=2700 and num%7==0 and num%5==0:
    print(" divisible")
else:
    print(" not divisible")
    
