#51. Write a Python program to find the median of three values. Go to the
#editor
#i. Expected Output:
#i. Input first number: 15
#iii. Input second number: 26
#iv. Input third number: 29
#v. The median is 26.0


a=float(input("enter number"))
b=float(input("enter number"))
c=float(input("enter number"))
if a>b and a<c:
    print("median number is a",a)
elif b>a and b<c:
    print("median number is b",b)
elif c>b and c<a:
    print("median number is c",c)
