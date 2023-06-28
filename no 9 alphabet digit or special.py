#.Write a python program to input any character and check whether it is alphabet,
#.digit or special character.

character=input("enter character:-")
if character>="A" and character<="Z" or character>="a" or character<="z":
    print("alphabet")
elif character>="0" and character<="9":
    print("digit number")
else:
    print("spicial character")
