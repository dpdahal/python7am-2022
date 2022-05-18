import os
import getpass

if not os.path.exists('record.txt'):
    open('record.txt', 'w').close()


def register():
    username = input('Enter Username: ')
    if username in open('record.txt').read():
        print('Username already exists')
        exit()
    password = getpass.getpass('Enter Password: ')
    confirm_password = getpass.getpass('Confirm Password: ')
    if password != confirm_password:
        print('Password does not match')
        exit()

    with open('record.txt', 'a') as file:
        file.write(username + ' ' + password + '\n')
    print('Registration Successful')
    exit()


def login():
    username = input('Enter Username: ')
    password = getpass.getpass('Enter Password: ')
    get_data = open('record.txt','r')
    users = get_data.readlines()
    data = []
    for user in users:
        data.append(user.split(' '))

    total_users = len(data)
    increment = 0
    while increment < total_users:
        uname = data[increment][0]
        pword = data[increment][1]
        if username == uname and password == pword:
            print('Login Successful')

        increment += 1

login()
