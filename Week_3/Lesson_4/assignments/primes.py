#prime 1-99
  # Python program to display all the prime numbers within an interval

lower = 1
upper = 100

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 0:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)

def prime_num():
    print(1,100)