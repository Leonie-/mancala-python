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

    def sow(self, starting_player, current_player, stones_to_sow, starting_pot, new_turn):
        # sow a stone in all the pots on the current side until out of stones
        for index, pot in enumerate(new_turn[current_player]):
            if stones_to_sow > 0 and index >= starting_pot and index <= len(new_turn[current_player]):

                # opposite capture if last stone, current pot is empty, and player is current player
                if stones_to_sow == 1 and new_turn[current_player][index] == 0 and current_player == starting_player:
                    opposite_player = 0 if current_player == 1 else 1
                    opposite_pot_number = len(new_turn[opposite_player]) - index - 1
                    captured_stones = new_turn[opposite_player][opposite_pot_number] + stones_to_sow

                    new_turn[opposite_player][opposite_pot_number] = 0
                    new_turn[2][starting_player] += captured_stones
                    stones_to_sow -= 1
                else:
                    new_turn[current_player][index] += 1
                    stones_to_sow -= 1

        if stones_to_sow > 0 and current_player == starting_player:
            # put a stone in the store
            new_turn[2][starting_player] += 1
            stones_to_sow -= 1

        if stones_to_sow > 0:
            # switch sides and continue
            current_player = 0 if current_player == 1 else 1
            self.sow(starting_player, current_player, stones_to_sow, 0, new_turn)

        print(new_turn)
        return new_turn

    def generate_turn(self, player_number, starting_pot):
        new_turn = copy.deepcopy(self.game_log[-1])
        stones_to_sow = copy.deepcopy(new_turn[player_number][starting_pot])

        new_turn[player_number][starting_pot] = 0
        starting_pot += 1

        self.sow(copy.deepcopy(player_number), player_number, stones_to_sow, starting_pot, new_turn)
        return new_turn

    def play(self, player_number, pot_number):
        player_number = player_number - 1;
        pot_number = pot_number - 1;

        self.validate_turn(player_number, pot_number)
        self.game_log.append(self.generate_turn(player_number, pot_number))











