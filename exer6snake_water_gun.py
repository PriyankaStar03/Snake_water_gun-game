# snake water gun

import random

game=['snake', 'water', 'gun']

print('This is a game named "SNAKE, WATER, GUN". \nIn this game you have total 10 chance to play the game.\nSo, let play the game, enter what you choose\n')

computer=0
you=0
chance=0
while(chance<10):
    a=str(input())
    c = random.choice(game)
    chance=chance+1
    if c==a:
        print('Computer also choose', c, '. So, Game is tie \nYou can play', 10-chance, 'time more')
        computer=computer+1
    elif c=="snake" and a=='water':
        print('Computer choose', c, '. So, Computer Wins \nYou can play', 10-chance, 'time more')
        computer = computer + 1
    elif c=='water' and a=='gun':
        print('Computer choose', c, '. So, Computer Wins \nYou can play', 10-chance, 'time more')
        computer = computer + 1
    elif c=='gun' and a=='snake':
        print('Computer choose', c,'.So, Computer Wins \nYou can play', 10-chance, 'time more')
        computer = computer + 1

    elif c == "water" and a == 'snake':
        print('Computer choose', c, '. So, You Wins \nYou can play', 10 - chance, 'time more')
        you=you+1
    elif c == 'gun' and a == 'water':
        print('Computer choose', c, '. So, You Wins \nYou can play', 10 - chance, 'time more')
        you=you+1
    elif c == 'snake' and a == 'gun':
        print('Computer choose', c, '.So, You Wins \nYou can play', 10 - chance, 'time more')
        you=you+1
    else:
        print('You enter wrong input, please enter correct input\n''Now you can play', 10-chance, 'time more')



if computer==you:
    print('\nGame is tie, play the game one more time \nyou win', you, 'time and computer win', computer, 'time')
elif computer>you:
    print('\nThe game is win by COMPUTER, try your luck next time \nyou win', you, 'time and computer win', computer, 'time')
else:
    print('\nCONGRATULATIONS! The game is win by YOU \nyou win', you, 'time and computer win', computer, 'time')