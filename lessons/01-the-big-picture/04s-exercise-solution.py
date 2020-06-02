# Don't look at this until you've attempted a solution on your own...

# Part 1
a = 1
b = False
c = 'Some kinda string...'
d = 5

# Part 2
result_of_addition = a + d
print(result_of_addition)

# Part 3
c += ' with some additional text'
print(c)

# Part 4
print(b)
print(not b)

# Part 5

# This works, and bool_plus_number is equal to 2
# ... kinda weird right? Read more: https://blog.rmotr.com/those-tricky-python-booleans-2100d5df92c
bool_plus_number = True + 1
print(bool_plus_number)

# These two both throw errors.
string_plus_number = '1' + 1
string_plus_bool = 'True' + False
