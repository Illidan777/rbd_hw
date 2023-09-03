# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# sum
number1 = input('Enter first number: ')
number2 = input('Enter first number2: ')

print('Sum: ', float(number1) + float(number2))

# temperature converting

temperature_value = float(input('Enter temperature value: '))
temperature_type = input('Enter temperature type(C/F): ').upper()

if temperature_type == 'F':
    print('Your temperature was converted to Celsius. Value:', (temperature_value - 32) / 1.8)
elif temperature_type == 'C':
    print('Your temperature was converted to Fahrenheit. Value:', temperature_value * 1.8 + 32)
else:
    print("Unsupported temperature type")
