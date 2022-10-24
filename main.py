car = 'bmw'
print(car == 'audi')
print(car != 'audi')
age = 18
print(age == 18)
# Notice (cond1 and cond2) is true only if
# both cond1 and cond2 are true.
print(True and True)
print(True and False)
print(False and True)
print(False and False)
# Notice (cond1 or cond2) is true if
# cond1 or cond2 or both are true.
cond1 = (3 < 4) or (5 < 3)
print(cond1)
print(((3 < 4) or (5 < 3)) and (6 < 3))
print((3 < 4) or (5 < 3) and (6 < 3))
print(not(car == 'audi'))
print(not(False))
print(not(True))
value = ((3 < 4) or (5 < 3)) and (6 < 3)
print(value)
print(not(value))
print(not(((3 < 4) or (5 < 3)) and (6 < 3)))

print()

# You can enclose a multi-line comment in opening and
# closing triple quotes (''').
'''
print("Do you want to play again? Y/N")
user_response = 'Y'
if user_response == 'Y':
    print("Let's play again.")
'''

print()

'''
print("Do you want to play again? Y/N")
user_response = 'y'
if user_response == 'Y':
    print("Let's play again.")

print("Do you want to play again? Y/N")
user_response = 'y'
if user_response.upper() == 'Y':
    print("Let's play again.")
    print("Here we go!")

print("Do you want to play again? Y/N")
user_response = 'n'
if user_response.upper() == 'Y':
    print("Let's play again.")
    print("Here we go!")

print("Do you want to play again? Y/N")
user_response = 'y'
if user_response.upper() == 'Y':
    print("Let's play again.")
print("Here we go!")

print("Do you want to play again? Y/N")
user_response = 'n'
if user_response.upper() == 'Y':
    print("Let's play again.")
print("Here we go!")

print("Do you want to play again? Y/N")
user_response = 'y'
if user_response.upper() == 'Y':
    print("Let's play again.")
if user_response.upper() != 'Y':
    print("Quitting.")

print("Do you want to play again? Y/N")
user_response = 'n'
if user_response.upper() == 'Y':
    print("Let's play again.")
if user_response.upper() != 'Y':
    print("Quitting.")

print("Do you want to play again? Y/N")
user_response = 'n'
# Try if-else.
if user_response.upper() == 'Y':
    print("Let's play again.")
# Otherwise...
else:
    print("Quitting.")

print("Do you want to play again? Y/N")
user_response = 'y'
# Try if-else.
if user_response.upper() == 'Y':
    print("Let's play again.")
# Otherwise...
else:
    print("Quitting.")

print("Do you want to play again? Y/N")
user_response = 'yes'
# Try if-else.
if user_response.upper() == 'Y':
    print("Let's play again.")
# Otherwise...
else:
    print("Quitting.")
    
'''
print("Do you want to play again? Y/N")
user_response = 'yes'
# Try if-else.
if user_response.upper() == 'Y':
    print("Let's play again.")
# Otherwise if...
elif user_response.upper() == 'N':
    print("Quitting.")
else:
    print("Error.")