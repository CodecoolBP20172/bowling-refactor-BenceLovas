# Bowling Score Counter

STRIKE = 'x'
SPARE = '/'
MISS = '-'


def score(game):

    game = data_processing(game)
    result = 0
    frame = 1
    roll_in_frame = 1
    for index, current_roll in enumerate(game):
        if current_roll == SPARE:
            result += 10 - last
        else:
            result += get_value(current_roll)
        if frame < 10 and get_value(current_roll) == 10:
            if current_roll == SPARE:
                result += get_value(game[index + 1])
            elif current_roll == STRIKE:
                result += get_value(game[index + 1])
                if game[index + 2] == SPARE:
                    result += 10 - get_value(game[index + 1])
                else:
                    result += get_value(game[index + 2])
        last = get_value(current_roll)
        
        frame, roll_in_frame = frame_progression(frame, roll_in_frame, current_roll)
        
    return result


def data_processing(data_string):

    return data_string.lower()


def is_frame_over(roll_in_frame, current_roll):

    if roll_in_frame == 2 or current_roll == STRIKE:
        return True
    else:
        return False


def frame_progression(frame, roll_in_frame, current_roll):

    if is_frame_over(roll_in_frame, current_roll):
        roll_in_frame = 1
        return frame + 1, roll_in_frame
    else:
        return frame, roll_in_frame + 1


def get_value(char):
    if char == '1' or char == '2' or char == '3' or \
       char == '4' or char == '5' or char == '6' or \
       char == '7' or char == '8' or char == '9':
        return int(char)
    elif char == STRIKE:
        return 10
    elif char == SPARE:
        return 10
    elif char == MISS:
        return 0
    else:
        raise ValueError()
