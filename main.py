import string

my_alphabet = list (string.ascii_uppercase)

my_list = iter(my_alphabet)

try:
    while True:
        print(next(my_list))

except StopIteration:
    pass



