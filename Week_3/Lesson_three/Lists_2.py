Friends = ["Kibenje","Kivinya","Kibesty","Kivutoo"]
for friend in Friends:
    print(friend)

enemies = Friends[:] # Copying one list to another.
print (enemies)

Fruits = ["Apples","Mangoes","Melons","Pineapple","Guava"]
# [:num] slices a list down to the num indicated.
print(Fruits[:3])

del Fruits[0]
print(Fruits)

squares = []

for x in range(0,11):
    squares.append(x**2)

print(squares)