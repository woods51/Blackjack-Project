import turtle as t
import random
from time import sleep

#loop constant
GAME_ON = True

print('-----Blackjack-----')
print('\nWelcome to Blackjack!\n')

#win percentage tracking
games_played = 0
wins = 0

#main loop
while GAME_ON:
    games_played += 1

    #defining list
    card_deck = ['A','A','A','A',2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9 \
         ,10,10,10,10,'J','J','J','J','Q','Q','Q','Q','K','K','K','K']

    #defining variabes
    player_cards = []
    player_total = 0
    player_ace = 0
    
    opponent_cards = []
    opponent_total = 0
    opponent_ace = 0
    
    #deals initial cards
    def deal():
        global player_cards
        global opponent_cards

        #deals 2 cards to each
        for i in range(0,2):
            cardDraw(player_cards)
            cardDraw(opponent_cards)
        return
    
    #draws a random card from the deck to argument
    def cardDraw(user):
        global card_deck

        #chooses card, then removes it from deck
        x = random.choice(card_deck)
        user.append(x)
        card_deck.remove(x)
        return
        
    #calcutes sum of hand (and converts facecards to numbers if necessary)
    def handSum(user_cards):
        global player_cards
        global player_total
        global player_ace
        global opponent_cards
        global opponent_total
        global opponent_ace
        
        if user_cards == player_cards:
            player_total = 0
            player_ace = 0

            #calculates totals
            for i in user_cards:
                if i == 'J' or i == 'Q' or i == 'K':
                    i = 10
                elif i == 'A':
                    i = 11
                    player_ace += 1

                #adds together cards for user
                player_total += i
            return

        elif user_cards == opponent_cards:
            opponent_total = 0
            opponent_ace = 0

            #calculates totals
            for i in user_cards:
                if i == 'J' or i == 'Q' or i == 'K':
                    i = 10
                    
                elif i == 'A':
                    i = 11
                    opponent_ace += 1

                #adds together cards for user
                opponent_total += i
            return

    #allows the computer to play
    def opponent_turn():
        global opponent_cards
        global opponent_total
        global opponent_ace

        #calculates current total
        handSum(opponent_cards)

        while True:
            #computer will only hit if its current total is < 16
            if opponent_total < 16:

                #draws again
                cardDraw(opponent_cards)

                #calculates new total
                handSum(opponent_cards)
        
            #changes the computers Ace value (1 or 11) if needed
            elif opponent_ace >= 1 and opponent_total > 21:
                opponent_total += -10
                opponent_ace -= 1
            else:
                break
        return
    
    #allows users ace value to change if needed
    def player_turn():
        global player_cards
        global player_total
        global player_ace

        handSum(player_cards)

        while True:
            if player_ace >= 1 and player_total > 21:
                    player_total += -10
                    player_ace -= 1
            else:
                break
        return
        
    #determines the results
    def results():
        global player_cards
        global player_total
        global opponent_cards
        global opponent_total
        global wins

        #initiates functions
        player_turn()
        opponent_turn()

        #determining results
        print('\n=================')
        print('FINAL RESULTS:')
        if opponent_total == player_total or opponent_total > 21 and player_total > 21:
            print('Opponent\'s Cards: ',opponent_cards)
            print('Your Cards: ',player_cards)
            print()
            print('DRAW! Both players had a total of %s.' % (opponent_total))
            return
        elif opponent_total < 21 and player_total > 21:
            print('Opponent\'s Cards: ',opponent_cards)
            print('Your Cards: ',player_cards)
            print()
            print('YOU LOST! Your opponent won with a total of %s. You went over with a total of %s.' % (opponent_total,player_total))
            return
        elif opponent_total == 21 and player_total != 21 or opponent_total < 21 and player_total < 21 and opponent_total > player_total:
            print('Opponent\'s Cards: ',opponent_cards)
            print('Your Cards: ',player_cards)
            print()
            print('YOU LOST! Your opponent won with a total of %s. You had a total of %s.' % (opponent_total,player_total))
            return
        elif opponent_total > 21 and player_total <= 21:
            print('Opponent\'s Cards: ',opponent_cards)
            print('Your Cards: ',player_cards)
            print()
            print('YOU WON! You won with a total of %s. Your opponent went over with a total of %s' % (player_total,opponent_total))
            wins += 1
            turtleGraphic()
            return
        else:
            print('Opponent\'s Cards: ',opponent_cards)
            print('Your Cards: ',player_cards)
            print()
            print('YOU WON! You won with a total of %s. Your opponent had a total of %s' % (player_total,opponent_total))
            wins += 1
            turtleGraphic()
            return
            
    #calculates win percentage
    def winPercentage():
        global wins
        global games_played

        win_percent = (wins / games_played) * 100
        print()
        print('Win Percentage = ',format(win_percent,',.1f'),end='')
        print('%')
        return

    #turtle animation
    def turtleGraphic():
        global wins
        if wins == 1:
            t.setup(400,400)
            t.speed(2)
            t.penup()
            t.goto(0,-175)
            t.pendown()
            t.pencolor('red')
            t.pensize(5)
            t.fillcolor('yellow')
            t.begin_fill()
            t.circle(175)
            t.end_fill()
            t.hideturtle()
            t.pencolor('black')
            t.speed(10)
            t.penup()
            t.pensize(10)
            t.goto(-75,75)
            t.pendown()
            t.fillcolor('black')
            t.begin_fill()
            t.circle(25)
            t.end_fill()
            t.penup()
            t.goto(75,75)
            t.pendown()
            t.begin_fill()
            t.circle(25)
            t.end_fill()
            t.penup()
            t.goto(-50,0)
            t.pendown()
            t.setheading(-90)
            for x in range(180):
                t.forward(1)
                t.left(1)
            sleep(5)
            t.bye()
        return

    input('Press enter to Deal...')
    deal()
    
    #displays user their inital hand
    print('\nYour Cards are:\n\t',player_cards)
    
    #allows user to hit again
    hit = input('Would you like to Hit? (y or n): ')

    while True:
        if hit == 'y':
            cardDraw(player_cards)

            #displays users new hand
            print('Your Cards are:\n\t',player_cards)

            hit = input('Would you like to Hit? (y or n): ')
        elif hit == 'n':
            break
        else:
            hit = input('Invalid Input. Re-enter: ')
    results()
    winPercentage()
    print('=================\n')

    #allows user to restart the loop
    play = input('Play Again? (y or n): ')

    #breaks loop (ending game)
    if not play == 'y':
        break
    print('\n\n\n')
