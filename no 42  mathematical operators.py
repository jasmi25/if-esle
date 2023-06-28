#42.Write a program to accept two numbers and mathematical operators and perform
#operation accordingly.
#Like:
#Enter First Number: 7
#Enter Second Number : 9
#Enter operator : +
#Your Answer is : 16
num1=int(input("enter any number:-"))
num2=int(input("enter any number:-"))
operator=input("enter operator:-")
if operator=="+":
    print(num1+num2)
elif operator=="-":
    print(num1-num2)
elif operator=="*":
    print(num1*num2)
elif operator=="/":
    print(num1/num2)
elif operator=="%":
    print(num1%num2)
elif operator=="**":
    print(num1**num2)
elif operator=="//":
    print(num1//num2)

         
