#45. Accept the number of days from the user and calculate the charge for library
#according to following :
#First five days : Rs 2/day.
#Six to ten days : Rs 3/day.
#Ten to 15 days : Rs 4/day
#After 15 days : Rs 5/day
day=int(input("enter day: "))
if day>=1 and day<=5:
    charge=day*2
    print("charge for library= ",charge)
elif day>=6 and day<=10:
    charge=day*3
    print("charge for library= ",charge)
elif day>=10 and day<=15:
    charge=day*4
    print("charge for library= ",charge)
elif day>15:
    charge=day*5
    print("charge for library= ",charge)
else:
    print("no charge")
