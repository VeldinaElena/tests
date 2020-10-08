import string
import random


def generate_value(length=200, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(length))


def generate_email(length=10):
    return generate_value(length=length) + '@gmail.com'
