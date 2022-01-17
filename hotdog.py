x = float(input("Kč to Párek v rohlíku: "))
print("")

y = x*20

if y == 1:
	print("{} Párek v rohlíku".format(y))
elif y == 2 or y == 3 or y == 4:
	print("{} Párky v rohlíku".format(y))
else:
	print("{} Párků v rohlíku".format(y))