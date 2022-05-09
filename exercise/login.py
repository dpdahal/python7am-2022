users = [
    ['admin', 'admin002'],
    ['ram', 'ram002'],
    ['sita', 'sita002']
]
username = input("Enter username: ")
password = input("Enter password: ")
total_users = len(users)
increment = 0
login_success = False
while increment < total_users:
    uname = users[increment][0]
    upass = users[increment][1]
    if username == uname and password == upass:
        login_success = True
    increment += 1

if login_success:
    print(f"Welcome {username}")
else:
    print("Username & password not found")
