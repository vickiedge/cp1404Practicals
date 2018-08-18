"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

def main():
    MENU = """C - Convert Celsius to Fahrenheit
            F - Convert Fahrenheit to Celsius
            Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            fahrenheit = calculate_farenheit_from_celcius()
            print("Result: {:.2f} F".format(fahrenheit))
        elif choice == "F":
            celsius = calculate_celsius_from_farenheit()
            print("Result: {:.2f} C".format(celsius))
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")

def calculate_farenheit_from_celcius():
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    return fahrenheit

def calculate_celsius_from_farenheit():
    fahrenheit = float(input("Farenheit:  "))
    celsius = 5 / 9 *(fahrenheit - 32)
    return celsius

main()