def welcome_msg():
    '''
    A Welcome message to the user
    '''
    print("-"*25+"Welcome to the Calculator"+"-"*25)

def menu():
    number1=raw_input('Enter First number:-')
    number2=raw_input('Enter Second number:-')

    operation = raw_input('''
    Please enter the operation you would like to perform with the numbers:-
    + Addition
    - Subtraction
    * Multiplication
    / Division
    ''')
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
        print(div(number1,number2))

    else:
        menu()


def add(number1,number2):
    print (int(number1)+int(number2))
    continue_msg()

def sub(number1,number2):
    print(int(number1)-int(number2))
    continue_msg()

def mul(number1,number2):
    print(int(number1)*int(number2))
    continue_msg()

def div(number1,number2):
    print(int(number1)/int(number2))
    continue_msg()

def continue_msg():
    print('Do you want to continue(y) or exit(n)[y/n]')
    ans=raw_input()
    if ans =='y' or ans =='Y' :
        menu()
    else:
        print ('Thank You')
welcome_msg()
menu()
