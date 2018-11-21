def welcome_msg():
    '''
    A Welcome message to the user
    '''
    print("-"*25+"Welcome to the Calculator"+"-"*25)

def menu():
    num1=raw_input('Enter First number:-')
    num2=raw_input('Enter Second number:-')

    operation = input('''
    Please enter the operation you would like to perform with the numbers:-
    + Addition
    - Subtraction
    * Multiplication
    / Division
    ''')

def add(number1,number2):
    return number1+number2

if operation == '+':
    print ('{} + {}'.format(number1,number2))
    print (add(number1,number2))

elif operation =='-':
    print('{} - {}'.format(number1,number2))
    print (sub(number1,number2))

elif operation =='*':
    print('{} * {}'.format(number1,number2))
    print(mul(number1,number2))

elif operation =='/':
    print('{} / {}'.format(number1,number2))
    print(div(number1/number2))

else:
    again()
