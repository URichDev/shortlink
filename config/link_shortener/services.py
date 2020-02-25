import string
import random

def short_link_generator(size=6, chars=string.digits+string.ascii_uppercase):
    return ''.join(random.choice(chars) for _ in range(size))

# short_link_generator()