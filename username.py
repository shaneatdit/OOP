__author__ = 'Shane'
# asks for user's name, then generates a username

a = input("Enter user's first name: ")
b = input("Enter user's second name: ")
username = b[:12] + a[0] + "1"

print(username)
