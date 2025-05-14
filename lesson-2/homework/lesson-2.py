# 1.

from datetime import datetime


def calculate_age():
    name = input("Enter your name").strip()          # Asks the user to enter their name and trims the accidental spaces before and after the name.
    
    year_of_birth = int(input("Enter your year of birth").strip())       # Asks the user to enter their year of birth and trims the accidental spaces before and after the entered year.
    
    current_year = datetime.now().year                    # Retrieves current year from the current date.
    
    age = current_year - year_of_birth          # Calcualtes the age.

    return f"Hello {name}, your age is {age}."      # Output message "Hello [name of the user], your age is [year of birth of the user]."
    
print(calculate_age())


# 2.

txt = 'LMaasleitbtui'

print(txt[0::2], txt[1::2], sep='\n')               # prints two car models, separated by a new line with "sep='\n'".


# 3.

txt = 'MsaatmiazD'

print(txt[0::2], txt[::-2], sep='\n')

# 4.

import re

txt = "I'am John. I am from London"

pattern = r'\b(?:in|at|from|to|on)\s+([A-Z][a-z]+)'        # Regular expression pattern to match words that start with a capital letter and are preceded by the words "in", "at", "from", "to", or "on".
matches = re.search(pattern, txt)                          # Searches for the pattern in the given text.

if matches:
    print(matches.group(1))                                # If a match is found, it prints the first group of the match (the capitalized word).
else:
    print("No match found")

# 5.

def myFunc():
    name = input("Enter a text: ")
    
    print(name[::-1])          # Prints the reversed string.

myFunc()


# 6.

def vowel_count(string):
    vowels = "aeiou"
    
    print(sum(1 for char in string.lower() if char in vowels))   # Counts the number of vowels in the string. lower() converts the string to lowercase to ensure that the comparison is case-insensitive.
    

vowel_count("I know you count the vowels in this sentence correctly")

# 7.

def max_value(numbers):
    print(max(numbers))     # Prints the maximum value from the list of numbers.
    
my_num = [1, 3, 5, 0]
    

max_value(my_num)       

# 8.

def polidrome_check(txt):
    
    if txt[::].lower() == txt[::-1].lower():       # Checks if the string is equal to its reverse.
        print("Polidrome!")
    else:
        print("Not polidrome!")
        
polidrome_check("Ramar")


# 9.

import re

def domain_extract(email):
    
    pattern = r'@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})'    
    # Regular expression pattern to match the domain part of an email address.
    # The pattern looks for an '@' symbol followed by one or more alphanumeric characters, dots, or hyphens, and then a dot followed by two or more alphabetic characters.
    
    matches = re.search(pattern, email)
    
    if matches:                                   # If a match is found, it retrieves the domain part of the email address.
        return matches.group(1)
    else:
        return "Domain not found"                 # If no match is found, it returns "Domain not found".
        
print(domain_extract("timaxrus@gmail.com"))


# 10.

import random                                                  # importing random library to work with random selection of letters, digits and special characters
import string                                                  # importing string library to get the list of lower and upper letters, digits and special characters

def generate_password(length=12):                              # default length of the password is 12, user can also specify the length of the password. It should be at least 8 characters length
    if length < 8:
        raise ValueError("Password length should be at least 8 characters for security reasons.")          # raise error message in case the user gives less amount than expected
    
    lowercase_letters = string.ascii_lowercase                 # assigning all the lowercase letters to the varaible
    uppercase_letters = string.ascii_uppercase                 # assigning all the uppercase letters to the varaible
    digits = string.digits                                     # assigning all the digits to the varaible
    special_characters = string.punctuation                    # assigning special characters to the varaible
    
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters               # assigning all the characters to the varaible
    
    password = [                                                                                       # password variable contains at least one of the four types of character in list datatype
        random.choice(lowercase_letters),
        random.choice(uppercase_letters),
        random.choice(digits),
        random.choice(special_characters)
    ]
    
    password += random.choices(all_characters, k=length - 4)                                          # appending the random length - 4 character to password list
    random.shuffle(password)                                                                          # shuffles the password variable in place
    
    return ''.join(password)                                                                          # joining the list values together without a space in between, changing the datatype to string

print(generate_password())
