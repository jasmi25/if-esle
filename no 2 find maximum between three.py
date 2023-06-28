#.Write a python program to find maximum between three numbers.
a=int(input("enter number:-"))
b=int(input("enter number:-"))
c=int(input("enter number:-"))
if a>b and a>c:
    print("a is greater=",a)
elif b>a and b>c:
    print("b is gerater=",b)
else:
    print("c is greater=",c)
