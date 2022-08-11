# Variable for store token
token = 'Bearer '

# Write token to file (token.txt)
with open('token.txt', 'r') as file:
    token += file.read()