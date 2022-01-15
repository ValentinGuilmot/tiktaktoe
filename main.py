


input1=' '
input2=' '
input3=' '
input4=' '
input5=' '
input6=' '
input7=' '
input8=' '
input9=' '


places={'1':input1,'2':input2,'3':input3,'4':input4,'5':input5,'6':input6,'7':input7,'8':input8,'9':input9}


 

def display_board():
    board=f"|{places['7']}|{places['8']}|{places['7']}|\n-------\n|{places['4']}|{places['5']}|{places['6']}|\n-------\n|{places['1']}|{places['2']}|{places['3']}|"
    print(board)

def start_game():
    while  True:
        l=input('Hey do you wanna play OXO ? yes or no: ')
        if l.lower()=='yes':
            break
        elif l.lower()=='no':
            print('Ok see you later!')
            quit()
        else:
            print('Answer not valid!')

playerA=''
playerB=''

def player_one():
    playerA=input('Player 1, do you want to be X or O ?: ')
    display_board()
    # r=input(('The grid u see is representing your numpad click the number of the place were you want to set your ')+ playerA(': '))
    # places[r]=playerA.upper()
    display_board()
    
def player_two():
    if playerA.lower=='x':
        playerB='O'
    else:
        playerB='X'
    print(playerB)

        


    

display_board()
# start_game()
player_one()
player_two()