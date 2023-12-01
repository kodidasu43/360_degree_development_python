import os
from calculator_art import logo

#print(logo)

def clear():
    os.system('cls')
    
def add(n1,n2):
    return n1+n2
    
def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide (n1,n2):
    return n1/n2
    
operations ={
    '+':add,
    '-':subtract,
    '*':multiply,
    '/':divide  
}

def calculator():
    print(logo)
    first_number=float(input("What's the first number?: "))
    should_continue=True
    while should_continue:
        for operator in operations:
            print(operator)
        user_operation = input("Pick an operation: ")
        second_number=float(input("What's the next number?: "))
        number_function=operations[user_operation]
        result=number_function(first_number,second_number)
        print(f"{first_number} {user_operation} {second_number} = {result}")
        user_choice=input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation:")
        if user_choice == 'y':
            first_number=result
        elif user_choice == 'n':
            should_continue=False
            clear()
            calculator()
    
calculator()
    
  
  