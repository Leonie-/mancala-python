import copy

class Mancala():

    is_new = True

    def __init__(self, pots, stones):
        # create game log
        self.game_log = [[
            [stones] * pots,
            [stones] * pots,
            [0,0]
        ]]

    def validate_turn(self, player_number, pot_number):
        if player_number < 0 or player_number > 1:
            raise ValueError("A valid player must be given")

        try:
            self.game_log[-1][player_number][pot_number]
        except IndexError as error:
            raise Exception("A valid pot must be selected for play") from error

    def generate_turn(self, player_number, pot_number):
        current_player = player_number
        new_turn = copy.deepcopy(self.game_log[-1])
        stones_to_sow = copy.deepcopy(new_turn[current_player][pot_number]) #pick up stones

        new_turn[current_player][pot_number] = 0; #current pot is now empty

        while stones_to_sow:
            pot_number += 1
            while pot_number < len(new_turn[current_player]):
                new_turn[current_player][pot_number] += 1
                pot_number += 1
                stones_to_sow -= 1
            if stones_to_sow > 0:
                new_turn[2][current_player] += 1
                stones_to_sow -= 1
        print(new_turn)
        return new_turn

    def play(self, player_number, pot_number):
        player_number = player_number - 1;
        pot_number = pot_number - 1;

        self.validate_turn(player_number, pot_number)
        self.game_log.append(self.generate_turn(player_number, pot_number))











