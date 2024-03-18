# Functions are a block of code running together as a unit.

# Defining a function....
def print_name():
    print("My name is Kibenjeee")

# Calling the function...
print_name()
print_name()
print_name()


def print_details(name, age, id, gender):
    print("I am {0}. I am an{1} 18 yo. My id number is {2}. I am a {3}".format(name, age, id, gender))

print_details("Kibenjeee", "18", "23652793", "Female")
 
def sum_nums(x,y):
    return x + y
z = sum_nums(10,20)
print (z)

def prod_num(x,y):
    return x*y
print (prod_num(10,20))

def print_odds(first_num,last_num):
    for i in range(first_num,last_num,2):
        print(i)
print_odds(1,15)