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

print(txt[0::2], txt[1::2], sep='\n')


# 3.



                                
  
