import hashlib

input: str = 'yzbqklnj'
modified_input: str = input

i = 1
while True:
    modified_input = input + str(i)
    hash_value = hashlib.md5(modified_input.encode()).hexdigest()
    if hash_value.startswith('000000'):
        print(i)
        break
    i += 1