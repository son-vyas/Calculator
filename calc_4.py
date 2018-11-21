def welcome():
    '''
    A Welcome message to the user
    '''
    print("-"*25+"Welcome to the Calculator"+"-"*25)


num1=raw_input('Enter First number:-')
num2=raw_input('Enter Second number:-')

operation = input('''
Please enter the operation you would like to perform with the numbers:-
+ Addition
- Subtraction
* Multiplication
/ Division
''')
