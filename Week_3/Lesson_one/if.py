# If function

age = 25
if age > 18:
    print("You may drive")

# If...and...
salary = 45000
if salary >30000 and salary<50000:
    salary = salary*1.1
    print(salary)

# If....else...
grade = 70
if grade>=84 and <=90:
    print("You get a calculator")
elif grade >=50 and <=83:
    print("You get a mathematical set")
else:
    print("You get nothing😂")

# If.... else
current_sal=int(input("Input current salary"))
if current_sal>=30000 and current_sal<=50000:
    new_sal = current_sal * 1.1
else:
    new_sal= current_sal
print (new_sal)
