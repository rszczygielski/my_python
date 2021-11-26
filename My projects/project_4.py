from random import choice
from losowanie_fragmentow import losuj_fragment


def f_password(n):
    password = ''
    last_pass = ''
    while len(password) != n:
        if len(password) < n-1:
            last_pass = password
            password += losuj_fragment()
        else:
            password = last_pass
    return password


for _ in range(10):
    print(f_password(8))

for _ in range(10):
    print(f_password(12))