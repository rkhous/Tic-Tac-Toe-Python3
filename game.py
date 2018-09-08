project_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

def setplayer():
    player1 = ''
    player2 = ''
    while player1 == '' and player2 == '':
        ques = input('Player1, do you want to be X or O?').upper()
        if ques == 'X':
            player1 = 'X'
            player2 = 'O'
        elif ques == 'O':
            player1 = 'O'
            player2 = 'X'
    return (player1,player2)

def printboard():
    print('\n'*50)
    print(project_board[0] + '|' + project_board[1] + '|' + project_board[2])
    print('- - -')
    print(project_board[3] + '|' + project_board[4] + '|' + project_board[5])
    print('- - -')
    print(project_board[6] + '|' + project_board[7] + '|' + project_board[8])
    print('\n')

player1,player2 = setplayer()

def game():
    x = 0
    o = 0
    while True:
        try:
            if x == o:
                ques = int(input('Player1, where would you like to place your letter?\n'))
                if ques <= 9 and ques >= 1:
                    check = (ques - 1)
                    if project_board[check] == ' ':
                        project_board[check] = player1
                        x += 1
                    else:
                        print(f'{player2} is already in that location! Try another.')
                        continue
                else:
                    print('Please choose a number between 1-9')
                    continue
            else:
                ques = int(input('Player2, where would you like to place your letter?\n'))
                if ques <= 9 >= 1:
                    check = (ques - 1)
                    if project_board[check] == ' ':
                        project_board[check] = player2
                        x -= 1
                    else:
                        print(f'{player1} is already in that location! Try another.')
                        continue
                else:
                    print('Please choose a number between 1-9')
                    continue
        except ValueError:
            print('Please choose a number between 1-9')
            continue
        if project_board[0] == project_board[1] == project_board[2] and project_board[0] != ' ':
            winner = f'{project_board[0]} is the winner!'
            break
        elif project_board[6] == project_board[7] == project_board[8] and project_board[6] != ' ':
            winner = f'{project_board[6]} is the winner!'
            break
        elif project_board[0] == project_board[1] == project_board[6] and project_board[0] != ' ':
            winner = f'{project_board[0]} is the winner!'
            break
        elif project_board[2] == project_board[5] == project_board[8] and project_board[2] != ' ':
            winner = f'{project_board[2]} is the winner!'
            break
        elif project_board[0] == project_board[4] == project_board[8] and project_board[0] != ' ':
            winner = f'{project_board[0]} is the winner!'
            break
        elif project_board[2] == project_board[4] == project_board[6] and project_board[2] != ' ':
            winner = f'{project_board[2]} is the winner!'
            break
        elif project_board[3] == project_board[4] == project_board[5] and project_board[3] != ' ':
            winner = f'{project_board[3]} is the winner!'
            break
        elif ' ' not in project_board:
            winner = 'Nobody won. Tie game!'
            print('Nobody won. Tie game!')
            break
        printboard()
    printboard()
    print(winner)
game()
