# Function to calculate BMI
def calculate_bmi(weight, height):
    try:
        # Convert height from centimeters to meters
        height_in_meters = height / 100.0

        # Calculate BMI using the formula: weight (kg) / height (m)^2
        bmi = weight / (height_in_meters ** 2)

        return bmi
    except ZeroDivisionError:
        return None


# Function to get user input and validate it
def get_user_input():
    while True:
        try:
            # Get weight input from the user
            weight = float(input("Enter your weight in kilograms (kg): "))

            # Get height input from the user
            height = float(input("Enter your height in centimeters (cm): "))

            # Check if weight and height are valid
            if weight <= 0 or height <= 0:
                print("Height and weight must be greater than zero. Please try again.")
                continue

            return weight, height
        except ValueError:
            print("Invalid input! Please enter numeric values.")


# Function to display the BMI result and category
def display_bmi_result(bmi):
    if bmi is None:
        print("Error: Unable to calculate BMI due to invalid input.")
    else:
        print(f"Your BMI is: {bmi:.2f}")

        # Determine BMI category
        if bmi < 18.5:
            print("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            print("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            print("You are overweight.")
        else:
            print("You are obese.")


# Main function to run the BMI calculator
def bmi_calculator():
    print("Welcome to the BMI Calculator!")

    # Get valid weight and height from the user
    weight, height = get_user_input()

    # Calculate BMI
    bmi = calculate_bmi(weight, height)

    # Display BMI result and category
    display_bmi_result(bmi)


while True:
    bmi_calculator()
