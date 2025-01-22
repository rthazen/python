# -*- coding: utf-8 -*-
"""
Created on 1/19/2025

Module 4 Assignment

@author: Reed Hazen
"""

def tempConversionToCelsius(f):
    # f is for farenheight
    celsius = (f - 32) * 5/9
    print(celsius, ' celsius')

    
def distanceTraveled(s, d):
    # s is fo speed and d is for duration in minutes
    timeHours = d / 60
    distance = s * timeHours
    print(distance, ' miles')
    
    
def menu():
    print('Enter 1 to convert Fahrenheit temperature to Celsius \nEnter 2 to calculate distance travelled \nEnter 3 to exit\n')
    
def main():
    menu()
    
    main_input = int(input('Please choose an option: '))
    
    if  main_input == 1:
        farehnheit = int(input('Please enter a farenheit: '))
        tempConversionToCelsius(farehnheit)
        main()
    elif main_input == 2:
        speed = int(input('Please enter a speed in mph: '))
        duration = int(input('Please enter a duration in minutes: '))
        distanceTraveled(speed, duration)
        main()
    elif main_input == 3:
        print('Adios')
    else:
        print('Invalid choice, please try again')
        main()
        
    
    
main()