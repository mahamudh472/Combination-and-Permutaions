
"""
###########################################
# Project Name: Combination-and-Permutaions python command line project
# Author: Md Mahmud Hasan
# Email: mahadymahamudh472@gmail.com
# GitHub: https://github.com/mahamudh472
# Description: This project is a practice for me. I was reading the chapters Permutation and combinations. So I Just used the formulla here to get the permutations and combinations. I know python have built-in packages for these operations. But it was fun😄..
# Created On: 23 Aug 2022
###########################################
"""

import os, sys

def factorial(num): 
    '''
    Calculate the factorial of a given number
    Args:
        num(int): The number to calculate the factorial for
    Returns:
        int: The factorial of the number
    '''                        
    result = 1                              
    for i in range (1, num+1):
        result = result * i
    return result

def comb(num1, num2):    
    '''
    Calcualte the combinations
    Args:
        num1(int): The value of n in the combination formulla (nCr)
        num2(int): The value of r in the combination formulla (nCr)
    Returns:
        int: The combinations of num1 and num2
    '''                  
    result = factorial(num1)//(factorial(num2)*factorial(num1 - num2))
    return result

def permut(num1, num2):
    '''
    Calculate the permutaion
    Args:
        num1(int): The value of n in the permutation formulla (nPr)
        num2(int): The value of r in the permutation formulla (nPr)
    Returns:
        int: The Permutation of num1 and num2
    '''
    result = factorial(num1)//(factorial(num1 - num2))
    return result

def clear_terminal():
    '''
    This function is used for clearing the terminal for a clean inteface
    by running this function, the termial will be cleared
    '''
    os.system('clear' if os.name == 'posix' else 'cls')



# Global variable for storing error message
ERROR_MESSAGE = None

def display_error():
    '''
    This function use the global variable ERROR_MESSAGE and print the error
    message with a formating color. 
    '''
    global ERROR_MESSAGE
    # if ERROR_MESSAGE:
    #     print(f'\033[31m {ERROR_MESSAGE}\033[0m')
    if ERROR_MESSAGE:
        print('\033[31m'+ ERROR_MESSAGE + '\033[0m')
        ERROR_MESSAGE = ""


def op():
    '''
    Main entry point for the application.

    This function defines and manages nested execution functions:
        - `execute_factorial`: Handles factorial calculations.
        - `execute_comb`: Handles combination calculations (nCr).
        - `execute_permut`: Handles permutation calculations (nPr).
        - `execute_main_menu`: Manages the main menu navigation.

    All functions handle user input, output, and exceptions.
    '''
    def execute_factorial():
        '''
        Handles the calculation of factorials based on user input.

        Process:
        - Prompts the user to input a number to calculate its factorial.
        - Allows the user to press Enter to exit.
        - Clears the terminal screen before each input prompt.
        - Displays errors for invalid input (e.g., non-numeric or negative values).

        Side Effects:
        - Prints the calculated factorial for valid input.
        - Updates the global `ERROR_MESSAGE` for invalid input.
        - Displays error messages in the terminal.

        Exceptions Handled:
        - `ValueError`: Raised for invalid input; replaced with a user-friendly message.
            '''
        while True:
            clear_terminal()
            print('Factorial:')
            print('Press enter to exit')
            global ERROR_MESSAGE
            display_error()
            
            try:
                n = input('Enter your number: ')
                if n == "":
                    return
                print(factorial(int(n)))
                input('<press enter>')
                
            except ValueError as e:
                ERROR_MESSAGE="Please enter number!"

    def execute_comb():
        '''
        Handles the calculation of combinations (nCr) based on user input.

        Process:
        - Prompts the user to input two integers, `n` and `r`, separated by a space.
        - Validates the input: 
        - Ensures `n >= r` (n should be greater than or equal to r).
        - Ensures `r > 0`.
        - Prints the calculated combination value for valid input.
        - Allows the user to press Enter to exit the combination operation.
        - Clears the terminal before displaying each prompt.

        Side Effects:
        - Updates the global `ERROR_MESSAGE` variable for input validation errors.
        - Displays error messages in the terminal.
        - Exits the loop and returns to the main menu when no input is provided.

        Exceptions Handled:
        - `Exception`: Catches general exceptions to manage input errors.
            - If no input is provided, the function exits gracefully.
            - If invalid input is provided (e.g., non-numeric or insufficient arguments), an error message is displayed.
        '''
        while True:
            clear_terminal()
            print("Combination:")
            print('Press enter to exit')
            global ERROR_MESSAGE
            display_error()
            try:
                num1,num2 = map(int,input("Enter n, r value: ").split())
                if num1<=num2 or num2 <= 0:
                    ERROR_MESSAGE="n should be greater than or equal r and r must grater than 0 "
                    continue
                print(comb(num1, num2))
                input('<press enter>')
            except Exception as e:
                print(str(e))    
                if 'expected 2, got 0' in str(e):
                    return
                else:
                    ERROR_MESSAGE='Please enter two integers separated by a space. For example: 5 3'

    def execute_permut():
        '''
        Handles the calculation of permutations (nPr) based on user input.

        Process:
        - Prompts the user to input two integers, `n` and `r`, separated by a space.
        - Validates the input:
        - Ensures `n >= r` (n should be greater than or equal to r).
        - Ensures `r > 0`.
        - Prints the calculated permutation value for valid input.
        - Allows the user to press Enter to exit the permutation operation.
        - Clears the terminal before displaying each prompt.

        Side Effects:
        - Updates the global `ERROR_MESSAGE` variable for input validation errors.
        - Displays error messages in the terminal.
        - Exits the loop and returns to the main menu when no input is provided.

        Exceptions Handled:
        - `Exception`: Catches general exceptions to manage input errors.
            - If no input is provided, the function exits gracefully.
            - If invalid input is provided (e.g., non-numeric or insufficient arguments), an error message is displayed.
        '''
        while True:
            clear_terminal()
            print("Permutation")
            print('Press enter to exit')
            global ERROR_MESSAGE
            display_error()
            try:
                num1,num2 = map(int,input("Enter n, r value: ").split())
                if num1<=num2 or num2 <= 0:
                    ERROR_MESSAGE="n should be greater than or equal r and r must grater than 0 "
                    continue
                print(permut(num1, num2))
                input('<press enter>')
            
            except Exception as e:
                print(str(e))    
                if 'expected 2, got 0' in str(e):
                    return
                else:
                    ERROR_MESSAGE='Please enter two integers separated by a space. For example: 5 3'
    menu_options = {
        '1': execute_factorial,
        '2': execute_comb,
        '3': execute_permut,
        '4': sys.exit
    }
    '''
    Dictionary mapping user menu choices to corresponding functions.

    Keys:
    - '1': Maps to the `execute_factorial` function for factorial calculations.
    - '2': Maps to the `execute_comb` function for combination calculations.
    - '3': Maps to the `execute_permut` function for permutation calculations.
    - '4': Maps to the `sys.exit` function to exit the application.

    Purpose:
    - Simplifies menu handling by associating each choice with a function.
    - Facilitates dynamic function calls based on user input.
    '''


    def execute_main_menu():

        '''
        Manages the main menu navigation and user interactions.

        Process:
        - Displays a list of operations to the user:
        1. Factorial
        2. Combination
        3. Permutation
        4. Exit
        - Prompts the user to select an option by entering a number corresponding to a menu item.
        - Executes the function mapped to the selected option using the `menu_options` dictionary.
        - Clears the terminal before displaying the menu and handling each input.

        Side Effects:
        - Calls one of the nested functions (`execute_factorial`, `execute_comb`, `execute_permut`) or exits the application.
        - Updates the global `ERROR_MESSAGE` variable for invalid menu choices.
        - Displays error messages in the terminal.

        Exceptions:
        - None explicitly raised or handled.
        - Input validation is performed to ensure the choice exists in `menu_options`.

        Note:
        - If an invalid choice is entered, the user is prompted again until a valid option is selected.
    
        '''
        while True:
            global ERROR_MESSAGE
            clear_terminal()
            display_error()
            print("Operations:\n1: Factorial\n2: Combination\n3: Permutation\n4: Exit")
            choice = input('--')
            if choice in menu_options.keys():
                menu_options[choice]()
            
            else:
                ERROR_MESSAGE = 'Invalid option selected'
    
    execute_main_menu()


if __name__ == '__main__':
    op()
   