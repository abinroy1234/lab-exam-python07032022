import math
p=int(input("enter the principal amount"))
r=int(input("enter the rate of interest"))
n=int(input("enter the number of years"))
a=p*(1+r/100)**n
print("amount after {} year is:".format(n),a)
c=a-p
print("compound interest for {} year is:".format(n),c)



