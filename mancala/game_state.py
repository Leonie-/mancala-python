# Current player
# Pot number played
# Turn number
# Stones captured
# Gets extra turn
# Is final move
# Number of empty pots on own side at start (array)
# Number of empty pots on own side at end (array)
# Number of empty pots on opponent's side at start (array)
# Number of empty pots on opponent's  side at end (array)
# Number of moves available at start
# Number of moves available at end

# Seeds sown on native side
# Seeds sown on opponent's side


# Number of Kroos (array)
# Current score

# Pots threatened at start (array)
# Pots threatened at end (array)
# Pots attacking at start (array)
# Pots attacking at end (array)

def get_opposite_player(current_player):
    return 1 if current_player is 2 else 2

def get_stones_captured(player_number, board_log):
    return board_log[-1][2][player_number - 1] - board_log[-2][2][player_number - 1]

def get_empty_pots(player, turn):
    return [index + 1 for index, item in enumerate(turn[player - 1]) if item == 0]

def get_non_empty_pots(player, turn):
    return [index + 1 for index, item in enumerate(turn[player - 1]) if item > 0]

def get_stones_sown_on_own_side(board_log, player, pot_number):
    stones_in_played_pot = board_log[-2][player -1][pot_number -1]
    stones_difference = sum(board_log[-2][player -1]) - sum(board_log[-1][player -1])
    return stones_in_played_pot - stones_difference

def get_stones_sown_on_opponents_side(board_log, opponent):
    stones_difference =  sum(board_log[-1][opponent -1]) - sum(board_log[-2][opponent -1])
    return stones_difference

def get_game_state(player, pot_number, board_log, gets_extra_turn, game_over):
    opponent = get_opposite_player(player)
    return {
        "current_player": player,
        "pot_played": pot_number,
        "turn_number": len(board_log) -1,
        "stones_captured": get_stones_captured(player, board_log),
        "get_extra_turn": gets_extra_turn,
        "is_final_turn": game_over,
        "empty_pots_on_own_side_start": get_empty_pots(player, board_log[-2]),
        "empty_pots_on_own_side_end": get_empty_pots(player, board_log[-1]),
        "empty_pots_on_opponents_side_start": get_empty_pots(opponent, board_log[-2]),
        "empty_pots_on_opponents_side_end": get_empty_pots(opponent, board_log[-1]),
        "moves_available_on_own_side_at_start":  get_non_empty_pots(player, board_log[-2]),
        "moves_available_on_own_side_at_end": get_non_empty_pots(player, board_log[-1]),
        "moves_available_on_opponents_side_at_start": get_non_empty_pots(opponent, board_log[-2]),
        "moves_available_on_opponents_side_at_end": get_non_empty_pots(opponent, board_log[-1]),
        "stones_sown_on_own_side": get_stones_sown_on_own_side(board_log, player, pot_number),
        "stones_sown_on_opponents_side": get_stones_sown_on_opponents_side(board_log, opponent)
    }