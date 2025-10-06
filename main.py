weight = float(input("Enter your weight: "))
unit = input("Kilograms or Pounds? (K or L): ")
CONVERSION_RATE = 2.205 


if unit == "K":
    converted_weight = weight * CONVERSION_RATE
    new_unit = "Lbs."
    print(f"Your weight is: {round(converted_weight, 1)} {new_unit}")

elif unit == "L":
    converted_weight = weight / CONVERSION_RATE
    new_unit = "Kgs."
    print(f"Your weight is: {round(converted_weight, 1)} {new_unit}")

else:
    print("Invalid unit. Please enter 'K' or 'L'.")