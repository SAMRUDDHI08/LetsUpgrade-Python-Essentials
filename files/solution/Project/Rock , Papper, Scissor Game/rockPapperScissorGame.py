# -*- coding: utf-8 -*-
"""
Created on Tue Sep  8 21:21:30 2020

@author: Samruddhi Patil
"""

import random

def takePlayerInput():
    player = 'blank'
    while not(player.lower() == 'r' or player.lower() == 's' or player.lower() == 'p'):
        player = input("Enter your choice (R|S|P):")
    return player

def Enterbot_choice():
    choices = ['r','p','s']
    return random.choice(choices)

def comparisonOfChoices(player,bot):
    if player.lower() == 'r' and bot.lower() == 'r':
        return "draw"
    elif player.lower() == 'r' and bot.lower() == 's':
        return "player"
    elif player.lower() == 'r' and bot.lower() == 'p':
        return "bot"
    elif player.lower() == 's' and bot.lower() == 's':
        return "draw"
    elif player.lower() == 's' and bot.lower() == 'p':
        return "player"
    elif player.lower() == 's' and bot.lower() == 'r':
        return "bot"
    elif player.lower() == 'p' and bot.lower() == 's':
        return "bot"
    elif player.lower() == 'p' and bot.lower() == 'r':
        return "player"
    elif player.lower() == 'p' and bot.lower() == 'p':
        return "draw"
    else:
        return "draw"

def score_board():
    player_score = 0
    bot_score = 0 
    doYouWanttoendtheGame = 'n'
    while doYouWanttoendtheGame.lower()=='n' and doYouWanttoendtheGame.lower() != 'y':
        player_choice =  takePlayerInput()
        botChoice = Enterbot_choice()
        winner = comparisonOfChoices(player_choice,botChoice)
        print("Bot's choice is:",botChoice)
        print("Winner of this round is:",winner)
        if winner == 'player':
            player_score += 2
        elif winner == 'bot':
            bot_score += 2
        else:
            player_score += 1
            bot_score += 1
        print()
        print("--SCORE BOARD--")
        print("Player",player_score)
        print("Bot",bot_score)
        doYouWanttoendtheGame = input("Do you want to quit the game (Y|N):")
        
score_board()

        

   
    