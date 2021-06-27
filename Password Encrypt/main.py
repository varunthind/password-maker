
#  This Program will change plain and simple password to complex password(Which is not easy to get)
#  Just remember the simple password and  use it as complex password with this software

import getpass
#  This is dictionary
encrypt = {'a': 'P%*7G', 'b': '`kj#@Q6', 'c': 'n7N@', 'd': '#Hl2', 'e': '!W?8e', 'f': 'h{C6e', 'g': '(J89#f', 'h': 'Y6gd%', 'j': 'd4o$N', 'k': '*f#56Y', 'l': '@G4o#',  'm': 'SD!Gf8h',
           'n': '#^G576d', 'o': ')hEgT0', 'p': 'n)8@', 'q': '@7g()F', 'r': 'n^lkK7"', 's': 'Y,./.34.>t!', 't': 'K2J|3j@', 'u': '&^E7/G', 'v': '||n>0)~j', 'w': '<J!d&8', 'x': 'n)8deG', 'y': '&E#fJ9', 'z': '+9Yn',
           '1': '7vN~', '2': '*(b`6',  '3': 'HJ*6f', '4': 'YU%$b8', '5': '*&7"J"6', '6': '*(f_-76', '7': 'nG*(j', '8': 'g#=7!8', '9': 'B^bI', '0': '_R$}j', ' ': '&-R_#b^k'}  # => plain alphabets, symobols etc. in complex form

start = True
while start:
    i = ''
    # Takes password input from user
    password = getpass.getpass(prompt='Enter your password: ', stream=None)
    confirm_password = getpass.getpass(
        prompt='Confirm password: ', stream=None)

    if password == confirm_password:                # This piece of code will confirm the password
        # This piece of code  will change the plain password to complex password
        for value in password:
            for enc in encrypt.keys():
                if value == enc:
                    m = (encrypt.get(enc))
                    i += m
                    start = False
    # If password does matches than this piece of code will be executed
    else:
        print("Password does not match! Please Enter again.")


print(i)
input("Press Enter to exit........")

#  Author: Varunt Thind
