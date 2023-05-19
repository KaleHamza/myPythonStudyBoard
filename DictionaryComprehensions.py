users = [
  (0, "Hamza", "password")
  (1, "Kim", "123")
  (2, "Zuka", "456")
  (3, "Ddeneme", "789")
]
                    #            #
username_mapping = {user[1]: user
                    for user in users}

print(username_mapping["Hamza"])

for user in users:
  if user[1] == "Hamza":
    print(user)
  
username_input = input("username:")
password_input = input("password:")
_, username, password = username_mapping[username_input]

if password_input == password:
  print("Correct")
else:
  print("False")
