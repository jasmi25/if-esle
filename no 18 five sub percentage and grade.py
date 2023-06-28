#18.Write a python program to input marks of five subjects Physics, Chemistry,
#Biology, Mathematics and Computer. Calculate percentage and grade according
#to following:
#Percentage >= 90% : Grade A
#Percentage >= 80% : Grade B
#Percentage >= 70% : Grade C
#Percentage >= 60% : Grade D
#Percentage >= 40% : Grade E
#Percentage < 40% : Grade F
Physics=int(input("enter marks:-"))
Chemistry=int(input("enter marks:-"))
Biology=int(input("enter marks:-"))
Mathematics=int(input("enter marks:-"))
Computer=int(input("enter marks:-"))
total=Physics+Chemistry+Biology+Mathematics+Computer
Percentage=total/500*100
if Percentage>=90 and Percentage<=100:
    print("Grade A")
elif Percentage>=80 and Percentage<90:
    print("Grade B")
elif Percentage>=70 and Percentage<80:
    print("Grade C")
elif Percentage>=60 and Percentage<70:
    print("Grade D")
elif Percentage>=40 and Percentage<60:
    print("Grade E")
elif Percentage<40:
    print("Grade F")
else:
    print("fail")
    
    
    

    
    
