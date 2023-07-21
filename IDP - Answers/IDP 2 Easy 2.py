def check_possibility_to_strike_left(game_board, index):
    while index >= 0:
        if game_board[index] == 'S':
            return False
        elif game_board[index] == 'X':
            return True
        index -= 1
    return False
        
def main():
    game_board = input()
    
    index_of_S = []
    for each_index in range(len(game_board)):
        if game_board[each_index] == 'S':
            index_of_S.append(each_index)
            
    for index in index_of_S:
        can_strike_left = check_possibility_to_strike_left(game_board, index - 1)
        print('S ' + str(can_strike_left))

main()