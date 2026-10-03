
# ============================================================
# PR. 7 - MODULER & PACKAGER
# Project: Multi-Utility Toolkit
# ============================================================

# ---------------- IMPORT MODULES ----------------

import datetime
import time
import math
import random
import string
import uuid
import os


# ============================================================
# 1. DATE AND TIME OPERATIONS
# ============================================================

def date_time_operations():

    while True:

        print("\n----- DATE AND TIME OPERATIONS -----")
        print("1. Current Date and Time")
        print("2. Difference Between Two Dates")
        print("3. Format Current Date")
        print("4. Countdown Timer")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        # Current date and time
        if choice == "1":

            current = datetime.datetime.now()

            print("\nCurrent Date and Time:")
            print(current)

        # Difference between two dates
        elif choice == "2":

            date1 = input("Enter first date (YYYY-MM-DD): ")
            date2 = input("Enter second date (YYYY-MM-DD): ")

            d1 = datetime.datetime.strptime(date1, "%Y-%m-%d")
            d2 = datetime.datetime.strptime(date2, "%Y-%m-%d")

            difference = abs((d2 - d1).days)

            print("Difference:", difference, "days")

        # Format date
        elif choice == "3":

            current = datetime.datetime.now()

            formatted_date = current.strftime("%d-%m-%Y")

            print("Formatted Date:", formatted_date)

        # Countdown
        elif choice == "4":

            seconds = int(input("Enter countdown seconds: "))

            while seconds > 0:

                print("Time left:", seconds)

                time.sleep(1)

                seconds = seconds - 1

            print("Countdown Finished!")

        # Back
        elif choice == "5":

            break

        else:

            print("Invalid choice!")


# ============================================================
# 2. MATHEMATICAL OPERATIONS
# ============================================================

def mathematical_operations():

    while True:

        print("\n----- MATHEMATICAL OPERATIONS -----")
        print("1. Factorial")
        print("2. Compound Interest")
        print("3. Circle Area")
        print("4. Rectangle Area")
        print("5. Trigonometry")
        print("6. Square Root")
        print("7. Back to Main Menu")

        choice = input("Enter your choice: ")

        # Factorial
        if choice == "1":

            number = int(input("Enter a number: "))

            result = math.factorial(number)

            print("Factorial:", result)

        # Compound Interest
        elif choice == "2":

            principal = float(input("Enter principal amount: "))
            rate = float(input("Enter rate of interest (%): "))
            years = float(input("Enter time in years: "))

            amount = principal * (1 + rate / 100) ** years

            print("Final Amount:", round(amount, 2))

        # Circle Area
        elif choice == "3":

            radius = float(input("Enter radius: "))

            area = math.pi * radius * radius

            print("Circle Area:", round(area, 2))

        # Rectangle Area
        elif choice == "4":

            length = float(input("Enter length: "))
            width = float(input("Enter width: "))

            area = length * width

            print("Rectangle Area:", area)

        # Trigonometry
        elif choice == "5":

            angle = float(input("Enter angle in degrees: "))

            radians = math.radians(angle)

            print("Sin:", round(math.sin(radians), 2))
            print("Cos:", round(math.cos(radians), 2))
            print("Tan:", round(math.tan(radians), 2))

        # Square Root
        elif choice == "6":

            number = float(input("Enter a number: "))

            result = math.sqrt(number)

            print("Square Root:", result)

        # Back
        elif choice == "7":

            break

        else:

            print("Invalid choice!")


# ============================================================
# 3. RANDOM DATA GENERATION
# ============================================================

def random_operations():

    while True:

        print("\n----- RANDOM DATA GENERATION -----")
        print("1. Random Number")
        print("2. Random List")
        print("3. Random Password")
        print("4. Random OTP")
        print("5. Random Sample")
        print("6. Simple Dice Game")
        print("7. Back to Main Menu")

        choice = input("Enter your choice: ")

        # Random number
        if choice == "1":

            number = random.randint(1, 100)

            print("Random Number:", number)

        # Random list
        elif choice == "2":

            numbers = []

            for i in range(5):

                number = random.randint(1, 100)

                numbers.append(number)

            print("Random List:", numbers)

        # Random password
        elif choice == "3":

            length = int(input("Enter password length: "))

            characters = (
                string.ascii_letters
                + string.digits
                + "!@#$"
            )

            password = ""

            for i in range(length):

                password = password + random.choice(characters)

            print("Generated Password:", password)

        # Random OTP
        elif choice == "4":

            otp = ""

            for i in range(6):

                otp = otp + str(random.randint(0, 9))

            print("Generated OTP:", otp)

        # Random sample
        elif choice == "5":

            data = [
                "Apple",
                "Banana",
                "Mango",
                "Orange",
                "Grapes"
            ]

            sample = random.sample(data, 3)

            print("Random Sample:", sample)

        # Dice game
        elif choice == "6":

            user = int(input("Choose a number between 1 and 6: "))

            computer = random.randint(1, 6)

            print("Your Number:", user)
            print("Computer Number:", computer)

            if user == computer:

                print("You got the same number!")

            else:

                print("Numbers are different.")

        # Back
        elif choice == "7":

            break

        else:

            print("Invalid choice!")


# ============================================================
# 4. UUID OPERATIONS
# ============================================================

def generate_uuid():

    print("\n----- UUID GENERATOR -----")

    unique_id = uuid.uuid4()

    print("Generated UUID:")
    print(unique_id)


# ============================================================
# 5. FILE OPERATIONS
# ============================================================

def file_operations():

    while True:

        print("\n----- FILE OPERATIONS -----")
        print("1. Create File")
        print("2. Write to File")
        print("3. Read File")
        print("4. Append to File")
        print("5. Check File Exists")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        # Create file
        if choice == "1":

            file_name = input("Enter file name: ")

            with open(file_name, "w"):

                pass

            print("File created successfully!")

        # Write file
        elif choice == "2":

            file_name = input("Enter file name: ")
            data = input("Enter data to write: ")

            with open(file_name, "w") as file:

                file.write(data)

            print("Data written successfully!")

        # Read file
        elif choice == "3":

            file_name = input("Enter file name: ")

            if os.path.exists(file_name):

                with open(file_name, "r") as file:

                    data = file.read()

                print("\nFile Content:")
                print(data)

            else:

                print("File does not exist!")

        # Append file
        elif choice == "4":

            file_name = input("Enter file name: ")
            data = input("Enter data to append: ")

            with open(file_name, "a") as file:

                file.write("\n" + data)

            print("Data added successfully!")

        # Check file
        elif choice == "5":

            file_name = input("Enter file name: ")

            if os.path.exists(file_name):

                print("File exists.")

            else:

                print("File does not exist.")

        # Back
        elif choice == "6":

            break

        else:

            print("Invalid choice!")


# ============================================================
# 6. MODULE EXPLORER USING dir()
# ============================================================

def explore_module():

    print("\n----- MODULE EXPLORER -----")

    print("Available modules:")
    print("1. math")
    print("2. random")
    print("3. datetime")
    print("4. uuid")
    print("5. time")

    choice = input("Choose module: ")

    if choice == "1":

        print("\nAttributes of math module:")
        print(dir(math))

    elif choice == "2":

        print("\nAttributes of random module:")
        print(dir(random))

    elif choice == "3":

        print("\nAttributes of datetime module:")
        print(dir(datetime))

    elif choice == "4":

        print("\nAttributes of uuid module:")
        print(dir(uuid))

    elif choice == "5":

        print("\nAttributes of time module:")
        print(dir(time))

    else:

        print("Invalid choice!")


# ============================================================
# 7. MAIN MENU
# ============================================================

def main():

    while True:

        print("\n")
        print("==========================================")
        print("       WELCOME TO MULTI-UTILITY TOOLKIT")
        print("==========================================")

        print("1. Date and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique ID (UUID)")
        print("5. File Operations")
        print("6. Explore Module using dir()")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":

            date_time_operations()

        elif choice == "2":

            mathematical_operations()

        elif choice == "3":

            random_operations()

        elif choice == "4":

            generate_uuid()

        elif choice == "5":

            file_operations()

        elif choice == "6":

            explore_module()

        elif choice == "7":

            print("\nThank you for using Multi-Utility Toolkit!")
            print("Program Ended.")

            break

        else:

            print("Invalid choice!")
            print("Please enter a number from 1 to 7.")


# ============================================================
# 8. __name__ AND __main__
# ============================================================

if __name__ == "__main__":

    main()
