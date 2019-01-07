import copy

import game_state

class MancalaBoard():
    def __init__(self, pots, stones, initial_state = None, game_number = 0):
        default_state = [
            [stones] * pots,
            [stones] * pots,
            [0,0]
        ]
        self.current_player = 0
        self.player_turn_number = 0
        self.winning_player = None
        self.game_is_over = False
        self.game_board_log = [ default_state ] if initial_state is None else [ initial_state ]
        self.game_state_log = []
        self.game_number = game_number
        # print(self.game_board_log)

    def check_player_turn_number(self, player_number):
        if player_number != self.current_player:
            self.current_player = player_number
            self.player_turn_number = 1
        else:
            self.player_turn_number += 1

    def validate_turn(self, player_number, pot_number):
        if player_number < 0 or player_number > 1:
            raise ValueError(f"A valid player must be given")

        if self.player_turn_number > 2:
            raise Exception(f"Player {player_number + 1} cannot take another turn")

        try:
            self.game_board_log[-1][player_number][pot_number]
        except IndexError as error:
            raise Exception(f"A valid pot must be selected for play") from error

        if self.game_board_log[-1][player_number][pot_number] is 0:
            raise ValueError(f"Selected pot {pot_number + 1} must not be empty")

    def clear_board(self):
        player_one_clear = False
        self.clear_remaining_stones(player_one_clear)
        player_one_clear = True
        self.clear_remaining_stones(player_one_clear)

    def clear_remaining_stones(self, player_one_already_clear):
        player_to_clear = 1 if player_one_already_clear else 0

        # Add sum of remaining stones to store
        self.game_board_log[-1][2][player_to_clear] += sum(self.game_board_log[-1][player_to_clear])
        # Clear board
        self.game_board_log[-1][player_to_clear] = [0 if x == 1 else 0 for x in self.game_board_log[-1][player_to_clear]]

    def check_for_game_over(self, current_turn):
        player_one_clear = all(pot == 0 for pot in current_turn[0])
        player_two_clear = all(pot == 0 for pot in current_turn[1])

        if player_one_clear or player_two_clear:
            self.game_is_over = True
            self.clear_remaining_stones(player_one_clear)

        if self.game_is_over == True:
            winning_player = 0
            if current_turn[2][0] > current_turn[2][1]:
                winning_player = 1
            elif current_turn[2][0] < current_turn[2][1]:
                winning_player = 2

            self.winning_player = winning_player


    def sow(self, starting_player, current_player, stones_to_sow, starting_pot, new_turn):
        take_another_turn = False
        # sow a stone in all the pots on the current side until out of stones
        for index, pot in enumerate(new_turn[current_player]):
            if stones_to_sow > 0 and index >= starting_pot and index <= len(new_turn[current_player]):

                # opposite capture if last stone, current pot is empty, and player side is the current player
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
            if stones_to_sow == 0:
                take_another_turn = True

        if stones_to_sow > 0:
            # switch sides and continue
            current_player = 0 if current_player == 1 else 1
            return self.sow(starting_player, current_player, stones_to_sow, 0, new_turn)

        # print(f"Player {current_player} new turn: {new_turn}")
        # print("take another turn: " + str(take_another_turn))
        return [new_turn, take_another_turn]

    def generate_turn(self, player_number, starting_pot):
        new_turn = copy.deepcopy(self.game_board_log[-1])
        stones_to_sow = copy.deepcopy(new_turn[player_number][starting_pot])

        new_turn[player_number][starting_pot] = 0
        starting_pot += 1

        return self.sow(copy.deepcopy(player_number), player_number, stones_to_sow, starting_pot, new_turn)

    def check_for_extra_turn(self, extra_turn):
        if extra_turn is True and self.player_turn_number is 2:
            # Prevents taking more than one extra turn
            return False
        else:
            return extra_turn

    def play(self, player_number, pot_number):
        self.check_player_turn_number(player_number)

        player_number = player_number - 1;
        pot_number = pot_number - 1;
        self.validate_turn(player_number, pot_number)

        turn = self.generate_turn(player_number, pot_number)
        self.game_board_log.append(turn[0])
        self.check_for_game_over(turn[0])
        gets_extra_turn = self.check_for_extra_turn(turn[1])

        if len(self.game_board_log) > 1: # If not the initial board set up, add state
            new_game_state = game_state.get_game_state(
                player_number,
                pot_number,
                self.game_board_log,
                gets_extra_turn,
                self.game_is_over,
                self.game_number
            )
            self.game_state_log.append(new_game_state)

        if self.game_is_over == True:
            return False
        else:
            return gets_extra_turn

    def get_legal_moves(self, player_number):
        player_number = player_number - 1
        legal_moves = []
        for i, pot in enumerate(self.game_board_log[-1][player_number]):
            if pot != 0:
                legal_moves.append(i + 1)
        return legal_moves

    def game_over(self):
        return self.game_is_over