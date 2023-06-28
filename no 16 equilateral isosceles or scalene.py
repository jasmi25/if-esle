#16.Write a python program to check whether the triangle is equilateral, isosceles or
#scalene triangle.
a=int(input("enter angles"))
b=int(input("enter angles"))
c=int(input("enter angles"))
if a==b==c:
    print("equilateral")
elif a==b or b==c or c==a:
    print("isoscel")
else:
    print("scalene")
