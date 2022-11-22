# !/user/bin/env.python3
# Created By: Jeremiah omoike
# Date: Nov. 21, 2022
# This program Asks user for a temperature in fahrenheit and then converts it to celsius
# in Celsius to Fahrenheit.


def calculate_fahrenheit():

    # Asks user for a degree in celsius
    temp_c_string = input("Enter the temperature (°C): ")
    print("")

    try:
        # Tries to convert user input to a float
        temp_c_float = float(temp_c_string)
        # calculates the fahrenheit of user integer
        temp_f = (9 / 5) * temp_c_float + 32
        print("{:,.2f}°C is equal to {:,.2f}°F".format(temp_c_float, temp_f))

    # checks if the number is a string
    except Exception:
        print("{} is not a number. Try again.".format(temp_c_string))


def main():
    # call def calculate_fahrenheit
    calculate_fahrenheit()


if __name__ == "__main__":
    main()
