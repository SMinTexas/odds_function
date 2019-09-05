# Write a function that accepts a list of numbers as an argument.
# Return a new list that includes only the odd numbers.
#
# only_odds([11, 20, 42, 97, 23, 10]) # Returns [11, 97, 23]
#
# Hint: use your is_odd_func function to determine which numbers to 
#       include in your new list.
import is_odd_func

def only_odds(list_of_numbers):
        odds = []
        for number in list_of_numbers:
                if is_odd_func.is_odd(number):
                        odds.append(number)

        return odds



numbers = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

print('')
print(f'Original List: {numbers}')
print('')
print(f'New List: {only_odds(numbers)}')
print('')