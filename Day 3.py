print("******* SIGN-UP PAGE *******")
user_name1 = str(input("Create your username (min. 5 characters) : "))
password1 = str(input("Create your password (min. 5 characters): "))

if len(user_name1) >= 5 and len(password1) >= 5:
    print("You're successfully signed up!")
elif len(user_name1) < 5 and len(password1) >= 5:
    print("Invalid username!")
elif len(user_name1) >= 5 and len(password1) < 5:
    print("Invalid password!")
else:
    print("Invalid username and password")

thisdict = {
    "username": user_name1,
    "password": password1
}

print("******* LOG IN PAGE *******")
user_name = str(input("Enter your username : "))
password = str(input("Enter your password : "))

if user_name == thisdict["username"] and password == thisdict["password"]:
    print("You are successfully logged in!")
elif user_name == thisdict["username"] and password != thisdict["password"]:
    print("Invalid password!")
elif user_name != thisdict["username"] and password == thisdict["password"]:
    print("Invalid username and/or password")
else:
    print("Invalid username and password")
