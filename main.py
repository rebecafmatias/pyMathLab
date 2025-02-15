flg_error_choice = True
flg_error_value = True

while flg_error_choice:
    try:
        choice = int(input("""Choose one of the operations below:
        
        1. Add two numbers
        2. Calculate the remainder of a division
        3. Multiply two given numbers
        4. Divide two numbers
        5. Calculate the square of a number
        6. Calculate the average of two numbers
        7. Calculate the power of a number
        8. Convert temperature from Celsius to Fahrenheit
        9. Calculate the area of a circle from its radius

        Which operation would you like to perform?
        """))

        if choice > 9 or choice < 1:
            print('You have to choose a number between 1 and 9.')
            flg_error_choice = True
    except ValueError:
        print('You entered an invalid value. Choose a number between 1 and 9.')
        flg_error_choice = True
    else: 
        flg_error_choice = False

while flg_error_value:
    try:
        if choice == 1:
            num01 = float(input('Enter the first number: '))
            num02 = float(input('Enter the second number: '))

            result = num01 + num02

        elif choice == 2:
            num01 = int(input('Enter the number to be divided: '))
            num02 = int(input('Enter the divisor: '))

            result = num01 % num02

        elif choice == 3:
            num01 = int(input('Enter the first number: '))
            num02 = int(input('Enter the second number: '))

            result = num01 * num02

        elif choice == 4:
            num01 = int(input('Enter the number to be divided: '))
            num02 = int(input('Enter the divisor: '))

            result = num01 / num02

        elif choice == 5:
            num01 = int(input('Enter the number to be squared: '))

            result = num01 ** 2

        elif choice == 6:
            num01 = float(input('Enter the first number: '))
            num02 = float(input('Enter the second number: '))

            result = (num01 + num02) / 2

        elif choice == 7:
            num01 = float(input('Enter the base: '))
            num02 = float(input('Enter the exponent: '))

            result = num01 ** num02

        elif choice == 8:
            num01 = float(input('Enter the temperature in Celsius: '))
            result = (num01 * 9/5) + 32

        elif choice == 9:
            num01 = float(input('Enter the radius of the circle: '))
            num02 = 3.14159265359
            result = num02 * (num01 ** 2)
    except ValueError:
        print('You entered an incorrect value. Try again.')
        flg_error_value = True
    except ZeroDivisionError:
        print('Division by zero is not allowed. Try again.')
        flg_error_value = True
    else:
        flg_error_value = False
        print(f'Your result is {result}')
