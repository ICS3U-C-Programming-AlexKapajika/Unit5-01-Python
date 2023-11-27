#!/usr/bin/env python3
# Created by: Alex Kapajika
# Created on: Nov 24, 2023
# This program convert a the temperature from celsius to fahrenheit using
# a function named fahrenheit.


def fahrenheit():
    # Getting the user input
    temperature_cel_str = input("Enter the temperature : ")
    # catching anything that is not integer.

    try:
        temperature_cel_int = int(temperature_cel_str)
    except ValueError:
        print("{} is not a valid input".format(temperature_cel_str))
    # If we successfully try and catch we would convert the temperature to
    # fahrenheit.

    else:
        temperature_fahrenheit = 9 / 5 * (temperature_cel_int) + 32
        # We display the converted temperature
        print(
            "{} celsius in fahrenheit is {}".format(
                temperature_cel_int, temperature_fahrenheit
            )
        )


def main():
    fahrenheit()


if __name__ == "__main__":
    main()
