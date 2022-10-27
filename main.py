from Player import HumanPlayer, RandomComputerPlayer, GeniusComputerPlayer
from Game import TicTacToe, play

if __name__ == '__main__':
    x_wins = 0
    o_wins = 0
    ties = 0
    for _ in range(1000):
        # x_player = HumanPlayer('X')
        x_player = RandomComputerPlayer('X')
        o_player = GeniusComputerPlayer('O')
        t = TicTacToe()
        result = play(t, x_player, o_player, print_game=False)
        if result == 'X':
            x_wins += 1
        elif result == 'O':
            o_wins += 1
        else:
            ties += 1

    print(f'After 1000 iterations, we see {x_wins} X wins, {o_wins} O wins and {ties} ties.')
