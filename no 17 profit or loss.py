#17.Write a python program to calculate profit or loss.
sp=float(input("enter sale price:-"))
cp=float(input("enter cost price:-"))
if sp>cp:
    print("profit=",sp-cp)
elif sp==cp:
    print("no frofit no loss")
else:
    print("loss=",cp-sp)
