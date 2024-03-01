import sys
def ibm_calculate():
    """Calculates and prints the Body Mass Index (BMI) category based on weight and height."""

    bmi_index = {
        'Severe Thinness': (0.00, 16.00),
        'Underweight': (16.00, 18.49),
        'Normal Weight': (18.50, 24.99),
        'Overweight': (25.00, 29.99),
        'Obese class 1': (30.00, 34.99),
        'Obese class 2': (35.00, 39.99),
        'Obese class 3': (40.00, float('inf')),  # Updated for python 3.6+
    }

    while True:
        try:
            weight = float(input("What is your current body weight (in kg): "))
            height = float(input("What is your current height (in cm): "))

            # Validate input values
            if weight <= 0:
                raise ValueError("Weight must be greater than 0 kg.")
            if height < 120:
                raise ValueError("Height must be greater than or equal to 120 cm.")

            height_converted = height / 100
            bmi = weight / (height_converted * height_converted)

            # Find matching category and print result
            for category, (min_value, max_value) in bmi_index.items():
                if min_value <= bmi < max_value:
                    print(f"IBM category: {category}\n (BMI: {bmi}")
                    break  # Exit loop after finding a match

        except (ValueError, TypeError) as e:
            print("Invalid input:", e)

        # Ask if user wants to continue
        choice = input("Do you want to calculate again? (y/n): ")
        if choice.lower() != 'y':
            print("Thanks for using the IBM calculator!")
            sys.exit()

ibm_calculate()
