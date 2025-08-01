with open('data/day_1_input.txt', 'r') as data_file:
    current_floor = 0
    pos = 0
    while True:
        char = data_file.read(1)          
        pos += 1
        if not char: 
            break
        
        if char == '(':
            current_floor += 1
        elif char == ')':
            current_floor -= 1
        
        if current_floor == -1:
            print(pos)
            break