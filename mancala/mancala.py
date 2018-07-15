import copy

class Mancala():

    is_new = True

    def __init__(self, pots, stones):
        play_board = [stones] * pots
        self.game_log = [[play_board, play_board, [0,0]]]

    def validate_turn(self, player_number, pot_number):
        if player_number < 0 or player_number > 1:
            raise ValueError("A valid player must be given")

        try:
            self.game_log[-1][player_number][pot_number]
        except IndexError as error:
            raise Exception("A valid pot must be selected for play") from error

    def generate_turn(self, player_number, pot_number):
        new_turn = copy.deepcopy(self.game_log[-1])
        stones_to_sow = new_turn[player_number][pot_number]

        new_turn[player_number][pot_number] = 0;

        count = 1

        while count <= stones_to_sow:
            pot = pot_number + count
            try:
                new_turn[player_number][pot]
            except IndexError:
                print("out of bounds")
            else:
                print("pot exists " + str(pot))
                new_turn[player_number][pot] += 1

            count += 1

        return new_turn

    def play(self, player_number, pot_number):
        player_number = player_number - 1;
        pot_number = pot_number - 1;

        self.validate_turn(player_number, pot_number)
        self.game_log.append(self.generate_turn(player_number, pot_number))











