##Take a user input of three digit numbers and print their
#reverse output.
#Ex. input 654
#Output 456
num=int(input("enter three digt number:- "))
if num>=100 and num<=999:
    a=num//10
    A=num%10
    b=a//10
    B=a%10
    A=str(A)
    b=str(b)
    B=str(B)
    print(A+B+b)
else:
    print("not a three digit number")

