import os
import getpass

if not os.path.exists('record.txt'):
    open('record.txt', 'w').close()


def register():
    print("=============User Registration Page=============")
    username = input('Enter Username: ')
    if username in open('record.txt').read():
        print('Username already exists')
        exit()
    password = getpass.getpass('Enter Password: ')
    confirm_password = getpass.getpass('Confirm Password: ')
    if password != confirm_password:
        print('Password does not match')
        exit()

    file = open('record.txt', 'a')
    file.write(username)
    file.write(' ')
    file.write(password)
    file.write('\n')
    print("Registration Successful")
    exit()


def login():
    print("=============User Login Page=============")
    username = input('Enter Username: ')
    password = getpass.getpass('Enter Password: ')
    get_data = open('record.txt', 'r')
    users = get_data.readlines()
    data = []
    for user in users:
        data.append(user.split())

    total_users = len(data)
    increment = 0
    login_success = False
    while increment < total_users:
        uname = data[increment][0]
        p_word = data[increment][1]
        if username == uname and password == p_word:
            login_success = True

        increment += 1

    if login_success == True:
        print(f'Welcome:  {username}')
    else:
        print('Login Failed')


question = input('Do you have an account y/n ')
if question == 'y':
    login()

else:
    register()



# s.n   name  password
# 1     ram     ram

