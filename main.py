from passwordverification import *

pwd = password_validation()

input = input("Enter your password  :")

valid_pass =pwd.validate_password(input)

print(valid_pass)