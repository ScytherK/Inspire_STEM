
"""
Program that deduces the next term in a geometric progression.
Date: 20/02/2024
Created by Scyther
n^th = a + (n-1)d
The n^th term is the number of whalefas...
a is the fist term
n is the kerea...
d is the common difference
"""

import math

a = float(input ("Enter first term"))
n = float(input ("Enter number of terms"))
d = float(input ("Enter the common difference"))

Nth = a+(n-1)*d

print(str(n) + "th term is equal to" + str(Nth))