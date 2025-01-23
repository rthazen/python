#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 1/23/2025

Module 5 Assignment

@author: Reed Hazen
"""
from random import randint  #this is python code so follow the case properly and this is the top line with no indentation

TotalPoints = 0
#then here is that GenerateGuess
def GenerateGuess(s,e):
   if ((s < e) and (s >= 0)) : #fill in the blank so we test if s is less than e, and s is a positive number
      if (((e - s) <= 10) or ((s - e) <= 10)): #fill in the blank to check if the distance from s to e is at least 10
          return (randint(1, e)) #this generate a number between 1 and e. 
   return (randint(1, 100))  #if the above does not return, it means one of the if's failed. In that case create a random number between 1 and 100

def CheckGuess(userGuess, secretGuess):
    if (userGuess == secretGuess):
        return 10
    # check whether the difference between the numbers is 5 or less
    elif ((((userGuess - secretGuess) <= 5) and ((userGuess - secretGuess) > 0)) or (((secretGuess - userGuess) <= 5) and ((secretGuess - userGuess) > 0))):
        return 5
    else:
        return 0

def UpdatePoints(points):
    global TotalPoints
    #take existing TotalPoints value and add points value to it
    TotalPoints = TotalPoints + points
    return TotalPoints

def main(): #note this function will always have no parameters by convention
                    print("Let's play the number Guessing Game")      
                    UserGuessRange = int(input("What range do you want to play for? ")) #note you must convert the input to int since the input returns a string
                    ComputerGuess = GenerateGuess(1, UserGuessRange) #Call the GenerateGuess on 1 and UserGuessRange to return a value in this ComputerGuess variable


                    #here get a guess from the user to use next. Call this variable UserGuess
                    UserGuess = int(input("What is your guess? "))


                    Status                = CheckGuess(UserGuess , ComputerGuess)  #Pass CheckGuess the computerGuess and the UserGuess. It will return 10, 5 or 0
                    if   Status == 0: #if 0 it means user did not guess right                          

                         # display a you lost msg.
                         print('You lost')
                    else:  #user guess was right. The value of Status tells us the points they earned   
                        print('You earned', Status, 'points')
                          #activate UpdatePoints on the Status then print the total points
                        UpdatePoints(Status)
                        print('Your total points is', TotalPoints)
                         

               # Ask if the user wants to play again. If user types 'yes', call main. 
                    PlayAgain = input('Want to play again? ')
               
                    if ((PlayAgain == 'yes') or (PlayAgain == 'y')):
                        main()
                   
                    else:
                        print('Goodbye, you are ending with', TotalPoints, 'points')
               # If user does not want to play again, don't call main. The code will end. Just display a good bye msg with the TotalPoints won.
               
main()
    