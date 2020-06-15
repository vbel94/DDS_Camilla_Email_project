import random
import string
def randomString(stringLength=16):
    letters = string.printable
    return ''.join(random.choice(letters) for i in range(stringLength))
