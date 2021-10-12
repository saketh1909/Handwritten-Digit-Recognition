import string
import secrets
from random import *
password = ""
SYMBOLS = ['@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>',
           '*', '(', ')', '<']
for _ in range(randint(6, 16)):
    password += secrets.choice(string.ascii_lowercase)
password += secrets.choice(SYMBOLS)
password += secrets.choice(string.ascii_uppercase)
password += secrets.choice(string.digits)
print(password)
if password.lower()== password or password.upper()==password or password.isalnum()==password:
    print ('password is weak')

elif password.lower()== password and password.upper()==password or password.isalnum()==password:
    print ('password is medium')

else:
    password.lower()== password and password.upper()==password and password.isalnum()==password
    print ('password is strong')