# Bowling Score Counter

STRIKE = 'x'
SPARE = '/'
MISS = '-'


def score(game):

    game = data_processing(game)
    result = 0
    frame = 1
    in_first_half = True
    for i in range(len(game)):
        if game[i] == SPARE:
            result += 10 - last
        else:
            result += get_value(game[i])
        if frame < 10 and get_value(game[i]) == 10:
            if game[i] == SPARE:
                result += get_value(game[i + 1])
            elif game[i] == STRIKE:
                result += get_value(game[i + 1])
                if game[i + 2] == SPARE:
                    result += 10 - get_value(game[i + 1])
                else:
                    result += get_value(game[i + 2])
        last = get_value(game[i])
        if in_first_half is False:
            frame += 1
            in_first_half = True
        elif in_first_half is True:
            in_first_half = False
        if game[i] == STRIKE:
            in_first_half = True
            frame += 1
    return result


def data_processing(data_string):
    return data_string.lower()


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
