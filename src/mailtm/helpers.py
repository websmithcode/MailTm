import string
import random


def username_gen(length=24, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(length))


def password_gen(length=8, chars=string.ascii_letters + string.digits + string.punctuation):
    return ''.join(random.choice(chars) for _ in range(length))
