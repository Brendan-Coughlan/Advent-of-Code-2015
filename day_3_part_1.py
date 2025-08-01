with open('data/day_3_input.txt', 'r') as data_file:
    houses = {}
    houses[(0, 0)] = True
    current_x: int = 0
    current_y: int = 0
    while True:
        char = data_file.read(1)          
        if not char: 
            break

        match char:
            case '<':
                current_x -= 1
            case '>':
                current_x += 1
            case 'v':
                current_y -= 1
            case '^':
                current_y += 1
        
        houses[(current_x, current_y)] = True
    print(len(houses))