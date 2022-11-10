import random
from game.hilo import Draw


class Director:
    '''This class operates the game loop'''


    def __init__(self):
        '''creates the score board and initializes objects'''
        self.score = 300
        self.in_play = True

    def start_game(self):
        '''starts a game loop'''
        while self.in_play:
            self.user_input()
            self.result()
            self.game_respond()
    
    def user_input(self):
        '''gets user input'''
        card1 = Draw.drawn_card
        print(f'The card is: {card1}')
        self.guess = input('higher or lower? [h/l]: ')
        return self.guess

    def result(self):
        '''decides if user wins or loses points'''
        if Draw.drawn_card() < Draw.new_card() and self.guess.lower == 'h':
            self.score = self.score + 100

        elif Draw.drawn_card() > Draw.new_card() and self.guess.lower == 'l':
            self.score = self.score + 100
        
        elif Draw.drawn_card() > Draw.new_card() and self.guess.lower == 'h':
            self.score = self.score - 75

        elif Draw.drawn_card() < Draw.new_card() and self.guess.lower == 'l':
            self.score = self.score - 75

        card2 = Draw.new_card
        print(f'The new card is: {card2}')
        # print(f'Your score is: {self.score}')

    # def update(self):
    #     ''''''

    def game_respond(self):
        '''output for results is displayed'''
        card2 = Draw.new_card
        # print(f'The new card is: {card2}')
        print(f'Your score is: {self.score}')
        if self.score > 0:
            break_case = input('Play again? [y/n]: ')
            self.user_input
            
            if break_case == 'n':
                print('Thanks for playing!')
                self.in_play = False
                self.__init__
                

            elif break_case == 'y':
                self.in_play = True
                self.__init__

            else:
                print("Sorry I don't understand")
                self.game_respond()
        else:
            print('Thanks for playing!')