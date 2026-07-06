running = True

while running:

print("="*40)
print("Chemistry Calculator")
print("="*40)

print("1. Calculate Molar Mass")
print("2. Gram to Mole Converter")
print("3. Mole to Gram Converter")
print("4. Percent Composition")
print("5. Exit")

choice = input("Choose an option (1-5): ")
print("You selected:", choice)



if choice == "1":
    print("\nMolar Mass Calculator\n")
elif choice == "2":
    print("\nGram to Mole Converter\n")
elif choice == "3":
    print("\nMole to Gram Converter\n")
elif choice == "4":
    print("\nPercent Composition\n")
elif choice == "5":
    print("\nThank you for using Chemistry Calculator!")
    running = False
else:
    print("\nInvalid option!\n")
