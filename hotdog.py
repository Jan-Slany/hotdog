while True:
	mena = input("Vyber měnu z které chtete převáďet [Kč/Párek v rohlíku] ").lower()
	hodnota_parku = 20

	try:
		if mena.startswith("k"):
			pocet_kc = float(input("Zadejte počet Kč: "))
			print("")

			pocet_parku = pocet_kc/hodnota_parku

			match pocet_parku:
				case 1:
					print("{} Párek v rohlíku".format(pocet_parku))
					print("")
				case 2, 3, 4:
					print("{} Párky v rohlíku".format(pocet_parku))
					print("")
				case default:
					print("{} Párků v rohlíku".format(pocet_parku))
					print("")

	except ValueError as e:
		print("Zadej čislo")

	except Exception as e:
		print(e)

	try:
		if mena.startswith("p"):
			pocet_parku = float(input("Zadejte počet Párků v rohlíku: "))
			print("")

			pocet_kc = pocet_parku*hodnota_parku

			print("{} Kč".format(pocet_kc))
			print("")

	except ValueError as e:
		print("Zadej čislo")

	except Exception as e:
		print(e)

	again = input("Chcete převádět dál? ").lower()

	if again != "ano":
		break
	else:
		print("------------")
