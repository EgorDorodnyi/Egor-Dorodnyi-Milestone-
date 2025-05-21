Strong_length = 8
Letters_lowercase = "abcdefghijklmnopqrstuvwxyz"
Letters_uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"

print("Welcome to the password checker")
print("We do not store your password or save it anywhere. We also do not store any of your data.")

Password = input("Please enter your password: ")

# Check length
if len(Password) >= Strong_length:
    Length_check = "Has enougth letters"
    length_fact = 1
else:
    Length_check = "Does not have enough and needs at least 8,"
    length_fact = 0

# Check for lowercase
if any(char in Letters_lowercase for char in Password):
    Lowercase_check = "password has enough lowercase letters"
    low_fact = 1
else:
    Lowercase_check = "does not have enough lowercase letters"
    low_fact = 0

# Check for uppercase
if any(char in Letters_uppercase for char in Password):
    Uppercase_check = "Includes the needed amount of uppercase letters to be safe"
    up_fact = 1
else:
    Uppercase_check = "It does not have enough uppercase letters"
    up_fact = 0

# Check for numbers
if any(char in numbers for char in Password):
    num_check = "have enough numbers wich makes it safe"
    Num_fact = 1
else:
    num_check = "dosint have enough numbers"
    Num_fact = 0

if Num_fact == 1 and up_fact == 1 and low_fact == 1 and length_fact == 1:
    Passed = ". Your password is very sucure!!!"
else:
    Passed = ". Your password is weak you will need to change it."






print("your password {} as well your {} and the {} you password also {}{}".format(
    Length_check, Lowercase_check, Uppercase_check, num_check, Passed))
