import random


def game_upgrade_structure(game, choice, symbol):
    game[int(choice) - 1] = symbol
    return game


def drawing_of_game(game, way_of_win):
    print(way_of_win)
    spot = 0
    v_1 = v_2 = v_3 = ' '
    v_1_d = v_2_d = v_3_d = '_'
    d_1 = d_11 = d_111 = d_2 = d_21 = d_211 = ' '
    d_1_d = d_11_d = d_111_d = d_2_d = d_21_d = d_211_d = '_'
    print('\t\t\t\t\t _________________')
    for x in range(3):
        if way_of_win == 0:
            v_1 = v_1_d = '|'
        elif way_of_win == 1:
            v_2 = v_2_d = '|'
        elif way_of_win == 2:
            v_3 = v_3_d = '|'
        if way_of_win == 6:
            if x == 0:
                d_1 = d_21_d = '\\'
            if x == 1:
                d_111 = d_111_d = '\\'
            if x == 2:
                d_21 = d_1_d = '\\'
        if way_of_win == 7:
            if x == 0:
                d_2 = d_11_d = '/'
            if x == 1:
                d_211 = d_211_d = '/'
            if x == 2:
                d_11 = d_2_d = '/'
        if way_of_win - 3 == x:
            middle = '--'
        else:
            middle = '  '
        print(f'\t\t\t\t\t|{d_1} {v_1} {d_11}|{d_111} {v_2} {d_211}|{d_21} {v_3} {d_2}|')
        print(f'\t\t\t\t\t|', end='')
        for y in range(3):
            symbol = game[spot]
            print(f'{middle}{symbol}{middle}|', end='')
            spot += 1
        print('')
        print(f'\t\t\t\t\t|{d_2_d}_{v_1_d}_{d_21_d}|{d_211_d}_{v_2_d}_{d_111_d}|{d_11_d}_{v_3_d}_{d_1_d}|')
        d_1 = d_11 = d_111 = d_2 = d_21 = d_211 = ' '
        d_1_d = d_11_d = d_111_d = d_2_d = d_21_d = d_211_d = '_'
    print('\n')


def turn(spot_left, my_turn, game):
    if my_turn:
        choice = choosing_spot_player(spot_left)
        symbol = 'O'
        my_turn = False
    else:
        symbol = 'X'
        choice = spot_to_go(symbol, spot_left, game)
        print("Computer's move")
        my_turn = True
    spot_left.remove(int(choice))
    return choice, symbol, my_turn


def spot_to_go(symbol, spot_left, game):
    dict_of_games_next_move = dict_of_next_move(symbol, spot_left, game)
    dict_of_games_opponent_move = dict_of_next_move(symbols_switch(symbol), spot_left, game)
    a = first_or_second_move(spot_left)
    if a:
        return a
    b = win_move(dict_of_games_next_move)
    if b:
        b = list(b)
        for i in b:
            return i
    c = check_dict_for_next_move(dict_of_games_opponent_move)
    if c:
        c = list(c)
        for i in c:
            return i
    d = two_change_test(symbol, spot_left, dict_of_games_next_move)
    if d:
        return random.choice(d)
    e = two_way_block_test(symbols_switch(symbol), spot_left, dict_of_games_next_move, dict_of_games_opponent_move)
    if e:
        return e
    g = random_move(spot_left)
    return g


def win_move(dict_of_games_next_move):
    b = check_dict_for_next_move(dict_of_games_next_move)  # one move win
    if b:
        return b


def check_dict_for_next_move(dict_games):
    for games in dict_games:
        game_on, spot = try_next_move(games)
        if not game_on:
            spot_to_go_ = dict_games[games]
            return spot_to_go_, spot


def try_next_move(games):
    game_on, x = is_game_on(games)
    if game_on == 'F':
        game_on = False
    else:
        game_on = True
    return game_on, x


def random_move(spot_left):
    print('random')
    corner_left = ['1', '3', '7', '9']
    for i in corner_left:
        if i in spot_left:
            corner_left.remove(i)
        return random.choice(corner_left)
    else:
        random.choice(spot_left)


def two_change_test(symbol, spot_left, dict_games):
    list_of_spot = []
    for games in dict_games:
        games = list(games)
        dict_games2 = dict_of_next_move(symbol, spot_left, games)
        spot_to_go_ = dict_games[tuple(games)]
        way_to_win = 0
        for games2 in dict_games2:
            game_on, x = try_next_move(games2)
            if not game_on:
                way_to_win += 1
            if way_to_win > 1:
                list_of_spot.append(spot_to_go_)
    return list_of_spot


def two_way_block_test(symbol, spot_left, dict_game, dict_of_games_opponent_move):
    list_spot = two_change_test(symbol, spot_left, dict_of_games_opponent_move)
    if list_spot:
        list_spot = clear_list(list_spot)
        for games in dict_game:
            dict_of_games_opponent_move = dict_of_next_move(symbols_switch(symbol), spot_left, games)
            game_on = win_move(dict_of_games_opponent_move)
            if game_on:
                return dict_game[games]


def clear_list(list_):
    new_list = []
    for i in list_:
        if i not in new_list:
            new_list.append(i)
    return new_list


def first_or_second_move(spot_left):
    random_corner = random.choice(('1', '3', '7', '9'))
    if 5 in spot_left:
        return 5
    elif len(spot_left) == 8:
        return random_corner


def dict_of_next_move(symbol, spot_left, game):
    dict_games = {}
    for spot in spot_left:
        game_try_spot = list(game)
        a = game_try_spot[spot - 1]
        game_try_spot[spot - 1] = symbol
        dict_games[tuple(game_try_spot)] = spot
        game_try_spot[spot - 1] = a
    return dict_games


def symbols_switch(symbol):
    if symbol == 'X':
        symbol = 'O'
    else:
        symbol = 'X'
    return symbol


def is_game_on(game):
    list_of_way_to_win = [[0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6]]
    for spots in list_of_way_to_win:
        if game[spots[0]] == game[spots[1]] == game[spots[2]]:
            game_on = 'F'
            way_of_win = list_of_way_to_win.index(spots)
            return game_on, way_of_win
    game_on = 'T'
    spots = 123
    return game_on, spots


def choosing_spot_player(spot_left):
    while True:
        choice = input('Where do you wanna to put it?')
        if choice in str(spot_left) and choice != '':
            break
        else:
            print('Choose another spot')
    return choice


def choose_to_play_again(answer):
    while answer.lower() != 'yes' and answer.lower() != 'no':
        answer = input('Write yes or no')
    return answer


def game_reset():
    game = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    spot_left = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    game_on = True
    return game, spot_left, game_on


def game_end(my_turn, spot_left, game_on):
    if not game_on:
        if my_turn:
            print('You lost!,')
        elif not my_turn:
            print('You won!')
    elif len(spot_left) == 0:
        print('No winners!')


def choosing_turn():
    answer = choose_to_play_again(input('Do you wanna have the first move? Yes/ No'))
    return answer.lower() == 'yes'


def main():
    play_again = True
    while play_again:
        my_turn = choosing_turn()
        game, spot_left, game_on = game_reset()
        drawing_of_game(game, 123)
        while game_on:
            choice, symbol, my_turn = turn(spot_left, my_turn, game)
            game = game_upgrade_structure(game, choice, symbol)
            game_on, way_of_win = is_game_on(game)
            if game_on == 'F':
                game_on = False
            else:
                game_on = True
            if not game_on or len(spot_left) == 0:
                game_end(my_turn, spot_left, game_on)
                game_on = False
            drawing_of_game(game, way_of_win)
        answer = choose_to_play_again(input('Do you wanna play again? Yes/ No'))
        if answer.lower() == 'no':
            print('Thank you by')
            break
        else:
            print('New game')


main()
