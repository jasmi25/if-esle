#.Write a python program to check whether a number is divisible by 5 and 11 or
#not.

#num=int(input("enter number"))
#if num%5==0 and num%11==0:
#   print("divisivale by 5 and 11")
#else:
#   print("not divisivale by 5 and 11") 
num=int(input("enter number"))
if num%5==0 and num%11==0:
    print("divisivale by 5 and 11")
    
elif num%11==0:
    print("11")
elif num%5==0: 
    print("5")
else:
   print("not divisivale by 5 and 11")
