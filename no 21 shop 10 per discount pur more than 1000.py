#21.A shop will give a discount of 10% if the cost of the purchased quantity is more
#than 1000. Ask the user for quantity, Suppose, one unit will cost 100. Judge and
#print total cost for user.
quantity=int(input("enter quantity:-"))
cost=100
dis=10/100
tc=quantity*cost-dis
if tc>1000:
   print("tc is",tc-dis*tc)
else:
    print("did not get discount",cost*quantity)
