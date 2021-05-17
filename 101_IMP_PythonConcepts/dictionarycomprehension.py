users = [
    (0, "bob", "password"),
    (1, "Rolf", "56845"),
    (2, "Jose", "56789"),
    (3, "Username", "1234")
]

# //----------- DICTIOANRIES COMPHRENSIONS------------------//
user_mapping = {user[1] : user for user in users}

print(user_mapping["bob"])


username_input = input("Enter your username: ")
userpass_input = input("Enter your passwrod: ")
_, username,password = user_mapping[username_input]

if userpass_input == password:
    print("welcome to Takebook")
else:
    print("wrong password")