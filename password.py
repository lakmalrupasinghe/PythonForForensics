import os
import random
import sys
import string


# q: I need password generator created what are the classes i need to use?
# a: random, string, os, sys

# q: what are the functions i need to use?
# a: random.choice, random.shuffle, string.ascii_letters, string.digits, string.punctuation, os.urandom, sys.exit

# q: how to comment in python
# a: #, ''' '''

''' I will be using the random module to generate random passwords'''

total = string.ascii_letters + string.digits + string.punctuation
length = 20


password = "".join(random.sample(total, length))

print(password)








