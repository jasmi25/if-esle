#15.Write a python program to input all sides of a triangle and check whether the
#triangle is valid or not.

a=int(input("enter angles sides"))
b=int(input("enter angles sides"))
c=int(input("enter angles sides"))
if a+b>c and b+c>a and c+a>b:
    print("valid")
else:
    print("not valid")
    
