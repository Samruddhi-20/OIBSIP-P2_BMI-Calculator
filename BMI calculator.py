def calculate_bmi(weight, height):
    # Check if weight and height are within reasonable ranges
    if weight <= 0 or height <= 0:
        return None  # Invalid input

    # Calculate BMI using the formula: BMI = weight (kg) / (height (m) ^ 2)
    bmi = weight / (height ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi is None:
        return "Invalid input"
    elif bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25.0 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    try:
        # Get user input for weight and height
        weight = float(input("Enter your weight in kilograms: "))
        height = float(input("Enter your height in meters: "))

        # Calculate BMI
        bmi = calculate_bmi(weight, height)

        # Classify BMI and display the result
        category = classify_bmi(bmi)
        if category == "Invalid input":
            print("Invalid input. Please enter valid weight and height values.")
        else:
            print(f"Your BMI is: {bmi:.2f}")
            print(f"You are classified as '{category}'.")

    except ValueError:
        print("Invalid input. Please enter numeric values for weight and height.")

if __name__ == "__main":
    main()
