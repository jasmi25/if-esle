#Write a python program to find a minimum number among
#the three user inputs?
a=int(input("enter number"))
b=int(input("enter number"))
c=int(input("enter number"))
if a<b and c>a:
    print("a is minimum")
elif b<a and c>b:
    print("b is minimum")
elif c<b and a>c:
    print("c is minimum")
else:
    print("no minimum")
