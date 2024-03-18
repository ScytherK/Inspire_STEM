"""
These are mutable list.
First set of quotation marks before the colon is the key.
Second set of quotation marks after the colon is the value.
"""
laptop = {"Make":"Hewlett Packard","Colour": "Silver", "Mass": "3 kg", "Year of manufacture": "2021"}
for key,value in laptop.items():
    print("\n")
    print(key)
    print(value)

# To print specific specs;
    print(laptop["Make"])

# Changing a value in the dictionary;
laptop["Colour"] = "red"
print(laptop)

# To add into the dictionary;
laptop["Size"] = "1200mm x 600mm"
print(laptop)

# Deleting an item in the dictionary;
del laptop["Colour"]
print (laptop)