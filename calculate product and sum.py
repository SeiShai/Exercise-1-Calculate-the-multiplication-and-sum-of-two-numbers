# Given two integer numbers
# return their product only if the product is equal to or lower than 1000.
# Otherwise, return their sum.

# inputs
first_number = int(input('first number = '))
second_number = int(input('second number = '))


# def function
def product_or_sum(first_number,second_number):
    product = first_number * second_number

    if product =< 1000:
        return product
    else:
        return first_number + second_number

# printing
