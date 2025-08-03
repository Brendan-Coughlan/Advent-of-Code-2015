with open('data/day_5_input.txt', 'r') as data_file:
    nice_str_count: int = 0
    while True:
        line = data_file.readline()
        if not line:
            break

        if line.find('ab') != -1 or line.find('cd') != -1 or line.find('pq') != -1 or line.find('xy') != -1:
            continue

        appears_twice: bool = False
        vowel_count: int = 0
        last_char: str = None
        for char in line:
            if char in 'aeiou':
                vowel_count += 1
            if last_char == char:
                appears_twice = True
            last_char = char
        
        if appears_twice and vowel_count >= 3:
            nice_str_count += 1
    print(nice_str_count)