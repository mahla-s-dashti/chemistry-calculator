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
    print("Molar Mass Calculator")
elif choice == "2":
    print("Gram to Mole Converter")
elif choice == "3":
    print("Mole to Gram Converter")
elif choice == "4":
    print("Percent Composition")
elif choice == "5":
    print("Goodbye!")
else:
    print("Invalid option")
