import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run
class CardGame:

    def __init__(self):
        self.cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        self.dealer=[]
        self.player=[]
    def supply_cards(self):
        # 	Deal both user and computer a starting hand of 2 random card values
        for i in range(2):
            rand=random.choice(self.cards)
            self.player.append(rand)
        for i in range(2):
            rand=random.choice(self.cards)
            self.dealer.append(rand)
    """def display(self):
        #displays palyers all but dealers one card
        print(f"Players cards are : {self.player}")
        print(f"Dealer card is {self.dealer[0]}")"""
    def displayall(self):
        #Print out the player's and computer's final hand and their scores at the end of the game.
        player_Score=sum(self.player)

        dealer_Score=sum(self.dealer)

        print(f"The players cards are: {self.player} and his score is : {player_Score}\n"
              f"The Dealers cards are {self.dealer} and his score is: {dealer_Score}")
    def blackjack(self):
        #Detect when computer or user has a blackjack. (Ace + 10 value card).
        #If computer gets blackjack, then the user loses (even if the user also has a blackjack)
        # If the user gets a blackjack, then they win (unless the computer also has a blackjack).
        sum_player= sum(self.player)
        sum_dealer= sum(self.dealer)
        if sum_player==21 and sum_dealer !=21:
            return 1
        elif sum_dealer == 21 :
            return 0
    def calcScore(self):
         #Calculate the user's and computer's scores based on their card values
         print(f"The score of the player for cards: {self.player} is {sum(self.player)}  "
               f"The score for the Dealer for the card is {self.dealer[0]} is {self.dealer[0]}")
    def aceDrawn(self,user):
        #If an ace is drawn, count it as 11. But if the total goes over 21, count the ace as 1 instead.
        if sum(user)+11 > 21:
            user.append(1)
        else:
            user.append(11)

    def DrawCard(self,num):
        #Ask the user if they want to get another card
        if num==0:
            rand=random.choice(self.cards)
            if rand==11:
                if sum(self.dealer)+rand >21:

                    self.dealer.append(1)
                else:
                    self.dealer.append(11)
            else:
                self.dealer.append(rand)

        elif num==1:
            rand = random.choice(self.cards)
            if rand == 11:
                if sum(self.player) + rand > 21:
                    self.player.append(1)
                else:
                    self.player.append(11)
            else:
                self.player.append(rand)

    def winner(self):
        #Compare user and computer scores and see if it's a win, loss, or draw
        pass
        if sum(self.player) <=21 and sum(self.dealer)<=21 and sum(self.player) > sum(self.dealer):
            print("Player won and Dealer lost")
            self.displayall()
        if sum(self.player) <=21 and sum(self.dealer)<=21 and sum(self.player) < sum(self.dealer):
            print("Dealer won and player lost")
            self.displayall()
    def main(self):
        print(logo)
        mygame = CardGame()
        mygame.supply_cards()
        mygame.calcScore()
        blackJ = mygame.blackjack()
        if blackJ == 1:
            print("Player 1 Won the game")
            mygame.displayall()
            inp = input(print("Do you want to play (Y / N)"))
            if inp =="Y":
                self.main()
            else:
                exit("Exiting the Game")
        elif blackJ==0:
            print("Dealer Won the game")
            mygame.displayall()
            inp = input(print("Do you want to play (Y / N)"))
            if inp == "Y":
                self.main()
                exit("Exiting the Game")
        while(True):
            inp=input("Player Do you want to draw a card (Y / N)")
            if inp=="Y":
                mygame.DrawCard(1)
                mygame.calcScore()
                if sum(mygame.player)>21:
                    print("Busst !! you lost the game")
                    inp = input(print("Do you want to play (Y / N)"))
                    if inp == "Y":
                        self.main()
                        exit("Exiting the Game")
            else:
                break
        while (True):
            temp=sum(mygame.dealer)
            if temp <16:

                mygame.DrawCard(0)
                mygame.displayall()
            else:
                break
        mygame.winner()









if __name__=="__main__":
    CardGame().main()





