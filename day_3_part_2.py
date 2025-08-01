with open('data/day_3_input.txt', 'r') as data_file:
    houses = {}
    houses[(0, 0)] = True
    current_santa_x: int = 0
    current_santa_y: int = 0
    current_robot_x: int = 0
    current_robot_y: int = 0
    is_santa_turn: bool = True
    while True:
        char = data_file.read(1)          
        if not char: 
            break

        match char:
            case '<':
                if is_santa_turn:
                    current_santa_x -= 1
                else:
                    current_robot_x -= 1
            case '>':
                if is_santa_turn:
                    current_santa_x += 1
                else:
                    current_robot_x += 1
            case 'v':
                if is_santa_turn:
                    current_santa_y -= 1
                else:
                    current_robot_y -= 1
            case '^':
                if is_santa_turn:
                    current_santa_y += 1
                else:
                    current_robot_y += 1

        if is_santa_turn:
            houses[(current_santa_x, current_santa_y)] = True
        else:
            houses[(current_robot_x, current_robot_y)] = True

        is_santa_turn = not is_santa_turn
    print(len(houses))