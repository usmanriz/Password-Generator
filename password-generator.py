print("PASSWORD MANAGER")
import random
import string
#A function do shuffle all the characters of a string
def shuffle(string):
  tempList = list(string)
  random.shuffle(tempList)
  return ''.join(tempList)

user_length = int(input("Enter a lenght of password: "))

uppercaseLetter1=chr(random.randint(65,90))    #Generate a random Uppercase letter (based on ASCII code)
lowercaseLetter1=chr(random.randint(97,122))    #Generate a random Lowercase Letter  (based on ASCII code
number1=str(random.randint(48,57))               #Generate a Random Number between [0-9]
specialCharacter1=chr(random.randint(33,47))+chr(random.randint(58,64))+chr(random.randint(91,96))+chr(random.randint(123,126))  # special characters
all_characters = uppercaseLetter1 + lowercaseLetter1 + number1 + specialCharacter1

if user_length < 4:
    print("Password length must be at least 4 characters.")
else:
    # Generate password using characters from all_categories
    password = random.choices(all_characters, k=user_length)
    # Shuffle the characters in the password
    password = ''.join(password)
    password = shuffle(password)

    print("Generated Password:", password) 



   
