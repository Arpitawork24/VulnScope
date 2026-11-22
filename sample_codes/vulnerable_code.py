import os

user_input = input("Enter command: ")

os.system(user_input)

result = eval(user_input)

print(result)