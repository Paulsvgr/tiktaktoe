import random


class ComputerCalculator:
    def __init__(self, current_game):
        symbol = "X"
        self.game = current_game
        self.spot_left = self.game_spot_left()
        self.dict_of_games_next_move = self.dict_of_next_move(symbol, self.spot_left, self.game)
        self.dict_of_games_opponent_move = self.dict_of_next_move(self.symbol_switch(symbol), self.spot_left, self.game)

    def options(self, symbol="X"):
        # try different options in order to find the next move

        a = self.first_or_second_move()  # chooses the middle or a random corner
        if a:
            return a
        b = self.check_dict_for_next_move(self.dict_of_games_next_move)  # chooses a spot that makes a win
        if b:
            b = list(b)
            for i in b:
                return i
        c = self.check_dict_for_next_move(self.dict_of_games_opponent_move)  # chooses a spot that block a loss
        if c:
            c = list(c)
            for i in c:
                return i
        d = self.two_change_test(symbol, self.spot_left, self.dict_of_games_next_move)  # looks for spot with 2 win next
        if d:
            return random.choice(d)
        e = self.two_way_block_test(self.symbol_switch(symbol), self.spot_left, self.dict_of_games_next_move,
                                    self.dict_of_games_opponent_move)
        if e:
            return e
        g = self.random_move()
        return g

    @staticmethod
    def symbol_switch(symbol):
        # return the other symbol
        switch = {"X": "O", "O": "X"}
        return switch[symbol]

    @staticmethod
    def dict_of_next_move(symbol, spot_left, game):
        dict_games = {}
        for spot in spot_left:
            game_try_spot = list(game)
            a = game_try_spot[spot - 1]
            game_try_spot[spot - 1] = symbol
            dict_games[tuple(game_try_spot)] = spot
            game_try_spot[spot - 1] = a
        return dict_games

    def two_way_block_test(self, symbol, spot_left, dict_game, dict_of_games_opponent_move):
        list_spot = self.two_change_test(symbol, spot_left, dict_of_games_opponent_move)
        for games in dict_game:
            spot_left.remove(dict_game[games])
            games = list(games)
            dict_games2 = self.dict_of_next_move(self.symbol_switch(symbol), spot_left, games)
            for games2 in dict_games2:
                game_on, x = self.try_next_move(games2)
                if not game_on and dict_games2[games2] not in list_spot:
                    games = tuple(games)
                    return dict_game[games]
            games = tuple(games)
            spot_left.append(dict_game[games])

    def two_change_test(self, symbol, spot_left, dict_games):
        list_of_spot = []
        for games in dict_games:
            games = list(games)
            dict_games2 = self.dict_of_next_move(symbol, spot_left, games)
            spot_to_go_ = dict_games[tuple(games)]
            way_to_win = 0
            for games2 in dict_games2:
                game_on, x = self.try_next_move(games2)
                if not game_on:
                    way_to_win += 1
                if way_to_win > 1 and spot_to_go_ not in list_of_spot:
                    list_of_spot.append(spot_to_go_)
        return list_of_spot

    def check_dict_for_next_move(self, dict_games):
        for games in dict_games:
            game_on, spot = self.try_next_move(games)
            if not game_on:
                spot_to_go_ = dict_games[games]
                return spot_to_go_, spot

    def try_next_move(self, games):
        game_on, x = self.is_game_on(games)
        if game_on == 'F':
            game_on = False
        else:
            game_on = True
        return game_on, x

    def game_spot_left(self):
        spot_left = []
        for place, spot in enumerate(self.game):
            if spot not in ["X", "O"]:
                spot_left.append(place + 1)
        return spot_left

    def first_or_second_move(self):
        random_corner = random.choice(['1', '3', '7', '9'])
        if 5 in self.spot_left:
            return 5
        elif len(self.spot_left) == 8:
            return random_corner

    def random_move(self):
        corner_left = [1, 3, 7, 9]
        corner_lefts = list(set(corner_left) & set(self.spot_left))
        if corner_lefts:
            spot = random.choice(corner_lefts)
        else:
            spot = random.choice(self.spot_left)
        return spot

    @staticmethod
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


def go(game):
    s = ComputerCalculator(game)
    return s.options()
