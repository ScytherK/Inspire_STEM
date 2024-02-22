# Strings in python.
# Date : 22/02/2024
# Created by : Scyther.

city = "nairobi"

# Convert to upper case
print(city)
print("\n\n") # Prints a new line
print(city.upper())
#  The box brackets allow you to get specific characters in a string
print (city[0])
print (city[1])
print (city[2])
print (city[3])
print (city[4])
print (city[5])
print (city[6])

# The reverse of words in a string is given forward and backward
print (city[-1])
print (city[-2])

name = "SCYTHER KIBENJEEE"
print(name)
print("\n\n")
print(name.lower())

town = "        Naivasha    "
print(town)
print("\t") #opens a new tab
print(town.strip())

# Add two strings

f_name = "Scyther"
s_name = "Kibenjee"
full_name = f_name + s_name

print(full_name)

# Replacing a character
# In the occurence of multiple characters, all of them will be replaced.
fruit = "orange"

print(fruit.replace("o","y"))

# Split string : 
subject = "Physical,sciences"
print(subject.split(":"))

age = 30
height = 1.7
print("I am {} years old".format(age))

print("I am {0} years old and {1} metres tall".format(age,height))