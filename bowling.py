# Bowling Score Counter

STRIKE = 'x'
SPARE = '/'
MISS = '-'
BASE_GAME_FRAME_AMOUNT = 9
MAX_ROLL_IN_FRAME = 2


def score(data_string):

    game_data_string = data_processing(data_string)
    result = 0
    frame = 1
    roll_in_frame = 1

    for index, current_roll in enumerate(game_data_string):
        if frame <= BASE_GAME_FRAME_AMOUNT:
            result += base_game(game_data_string, index, current_roll)
        else:
            result += last_frame(game_data_string, index, current_roll)
        frame, roll_in_frame = frame_progression(frame, roll_in_frame, current_roll)

    return result


def data_processing(data_string):

    return data_string.lower()


def base_game(game_data_string, index, current_roll):

    if current_roll == SPARE:
        return get_value(SPARE, game_data_string[index - 1]) + spare_bonus_points(game_data_string, index)
    elif current_roll == STRIKE:
        return get_value(STRIKE) + strike_bonus_points(game_data_string, index)
    else:
        return get_value(current_roll)


def last_frame(game_data_string, index, current_roll):

    if current_roll == SPARE:
        return get_value(SPARE, game_data_string[index - 1])
    else:
        return get_value(current_roll)


def spare_bonus_points(game_data_string, index):

    return get_value(game_data_string[index + 1])


def strike_bonus_points(game_data_string, index):

    if game_data_string[index + 2] == SPARE:
        return get_value(game_data_string[index + 1]) + get_value(SPARE, game_data_string[index + 1])
    else:
        return get_value(game_data_string[index + 1]) + get_value(game_data_string[index + 2])


def is_frame_over(roll_in_frame, current_roll):

    if roll_in_frame == MAX_ROLL_IN_FRAME or current_roll == STRIKE:
        return True
    else:
        return False


def frame_progression(frame, roll_in_frame, current_roll):

    if is_frame_over(roll_in_frame, current_roll):
        roll_in_frame = 1
        return frame + 1, roll_in_frame
    else:
        return frame, roll_in_frame + 1


def is_value_int(current_roll):

    try:
        int(current_roll)
        return True
    except ValueError:
        return False


def is_value_in_range(current_roll):

    return 1 <= int(current_roll) and int(current_roll) <= 9


def get_value(current_roll, last_roll=""):

    if current_roll == STRIKE:
        return 10
    elif current_roll == SPARE:
        return 10 - get_value(last_roll)
    elif current_roll == MISS:
        return 0
    elif is_value_int(current_roll) and is_value_in_range(current_roll):
        return int(current_roll)
    else:
        raise ValueError("Invalid input.")
