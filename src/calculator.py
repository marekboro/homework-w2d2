### Question: Why did we not need to dedine a class:

# class Calculator:
#     #def __init__(self):

#     def add(self,first_number, second_number):
#         return first_number + second_number

#     def subtract(self, first_number, second_number):
#         return first_number - second_number

#     def divide(self, first_number, second_number):
#         return first_number / second_number

#     def multiply(self, first_number, second_number):
#         return first_number * second_number


def add(first_number, second_number):
    return first_number + second_number


def subtract(first_number, second_number):
    return first_number - second_number


def divide(first_number, second_number):
    return first_number / second_number


def multiply(first_number, second_number):
    return first_number * second_number

def raise_to_power(first_number, second_number):
    return (first_number ** second_number)

def factorial(the_number):
    result = 1
    for i in range(1,the_number+1):
        result = result * i
    return result


