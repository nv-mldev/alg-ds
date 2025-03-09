import string 
import random 
char_dictionary = string.ascii_lowercase+' '
target = 'hello world'

def genrate_random_string(length):
    random_string = ''
    for i in range(length):
        random_string += random.choice(char_dictionary)
    return random_string

def infinite_monkey(target):
    target_length = len(target)
    iteration = 0
    while True:
        random_string = genrate_random_string(target_length)
        iteration += 1
        print(iteration)
        if random_string == target:
            return iteration
    

# def generate_random_string(length):
#     return ''.join(random.choice(char_dictionary) for i in range(length))
attempts = infinite_monkey(target)