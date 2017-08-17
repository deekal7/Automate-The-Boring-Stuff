#! /usr/bin/python3

import re

def pwdRegex():
    passwordRegex = re.compile(r'^(?=.*?[0-9])(?=.*?[A-Z])(?=.*?[a-z]).{8,}$')

    print("Enter your password")
    password = raw_input("> ")

    pass_w = passwordRegex.search(password)

    if pass_w != None:
        print("Success")

    else:
        print("Try again")

pwdRegex()


