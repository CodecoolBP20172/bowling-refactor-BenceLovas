# Bowling Score Counter

STRIKE = 'x'
SPARE = '/'
MISS = '-'
BASE_GAME_FRAME_AMOUNT = 9

def score(game):

    game = data_processing(game)
    result = 0
    frame = 1
    roll_in_frame = 1
    for index, current_roll in enumerate(game):

        if frame <= BASE_GAME_FRAME_AMOUNT:
            result += base_game(game, index, current_roll)
        else:
            result += last_frame(game, index, current_roll)
        
        frame, roll_in_frame = frame_progression(frame, roll_in_frame, current_roll)

    return result


def data_processing(data_string):

    return data_string.lower()


def base_game(game, index, current_roll):

    if current_roll == SPARE:
        return get_value(SPARE, game[index - 1]) + spare_bonus_points(game, index)
    elif current_roll == STRIKE:
        return get_value(STRIKE) + strike_bonus_points(game, index)
    else:
        return get_value(current_roll)


def last_frame(game, index, current_roll):

    if current_roll == SPARE:
        return get_value(SPARE, game[index - 1])
    else:
        return get_value(current_roll)


def spare_bonus_points(game, index):

    return get_value(game[index + 1])


def strike_bonus_points(game, index):

    if game[index + 2] == SPARE:
        return get_value(game[index + 1]) + get_value(SPARE, game[index + 1])
    else:
        return get_value(game[index + 1]) + get_value(game[index + 2])


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


def get_value(current_roll, last_roll=""):
    if current_roll == STRIKE:
        return 10
    elif current_roll == SPARE:
        return 10 - get_value(last_roll)
    elif current_roll == MISS:
        return 0
    try:
        current_roll_int = int(current_roll)
        if 1 <= current_roll_int and current_roll_int <= 9:
            return current_roll_int
        else:
            raise ValueError("Integer is out of range.")
    except ValueError:
        raise ValueError("Invalid input.")
