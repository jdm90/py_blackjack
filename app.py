############### Blackjack Project #####################

# Blackjack created with Python

############### Our Blackjack House Rules #####################

# The deck is unlimited in size. 
# There are no jokers. 
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Cards are not removed from the deck as they are drawn.

import random
import os
from art import logo

clear = lambda: os.system('cls')

# Return random card from deck of cards
# Using 11 as Ace
def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    score = sum(cards)
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and score > 21:
        cards.remove(11)
        cards.append(1)
    return score

def compare_scores(player_score, dealer_score):
    if player_score > 21 and dealer_score > 21:
        return "You went over 21. You lose."

    if player_score == dealer_score:
        return "Draw"
    elif player_score == 0:
        return "BLACKJACK! You win!"
    elif dealer_score == 0:
        return"BLACKJACK! The dealer wins."
    elif player_score > 21:
        return"You went over 21. You lose."
    elif dealer_score > 21:
        return"The dealer has gone over 21. You win!"
    elif player_score > dealer_score:
        return"You win!"
    else:
        return "You lose."        

def play_game():
    print(logo)

    player_cards = []
    dealer_cards = []
    is_game_over = False
    
    for i in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_game_over:
        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"Your cards: {player_cards}.\nCurrent score: {player_score}")
        print(f"\nDealer's first card: {dealer_cards[0]}.")


        if player_score == 0 or dealer_score == 0 or player_score > 21:
            is_game_over = True
        else:
            hit_or_stand = input("\nType 'h' to hit, or 's' to stand: ")
            if hit_or_stand == "h":
                clear()
                print("\nYou chose to hit...\n")
                player_cards.append(deal_card())
            else:
                clear()
                print("\nYou chose to stand...")
                is_game_over =  True
    
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)
        print(f"\nYour final hand: {player_cards}.\nYour final score: {player_score}")
        print(f"\nDealer's final hand: {dealer_cards}.\nDealer final score: {dealer_score}\n")
        print(compare_scores(player_score, dealer_score))

while input("\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    play_game()