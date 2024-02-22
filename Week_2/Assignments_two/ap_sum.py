#This is a programme to show sum of numbers in an arithmetic progression.
# Date : 20/02/2024
# Created by : Scyther

"""
-> Sn=n/2[2a+(n-1)d]
-> a is the first term of the AP.
-> n is the number of terms.
-> d is the common difference.
"""

a = int(input("enter first term: "))
n = int(input("enter number of terms in the AP: "))
d = int(input("enter common difference between the terms: "))

# Sn is the sum of the number of terms in the AP.
Sn = (n/2)*(2*a+((n-1)*d))

print("The sum of " + str(n) + "terms in the AP is : " +str(Sn))