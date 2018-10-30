#!/usr/bin/env/python

import sys


from read_csv import read_csv
from a_star_ import a_star_
# from a_star_ import Node

# from dijkstra import dijkstra


def choose_algorithm():  ## Your menu design here
    print('Please choose an algorithm: ')
    print('1. A* (A star)')
    print('2. Dijkstra')

    choice = int(input("Enter your choice [1-2]: "))

    while 1:
        if choice == 1:
            print('A* selected')
        elif choice == 2:
            print('Dijkstra selected')
        else:
            # Any integer inputs other than values 1-5 we print an error message
            input("Wrong option selection. Enter any key to try again..")
        break


def choose_map():

    print('What map do yoy want to use? [1-9]')

    choice = int(input('Enter your choice [1-9]: '))
    mapa = ''

    while 1:  # While loop which will keep going until loop = False

        if choice == 1:
            print('Map 1 selected')
            mapa = 'map1.csv'
        elif choice == 2:
            print('Map 2 selected')
            mapa = 'map2.csv'
        elif choice == 3:
            print('Map 3 selected')
            mapa = 'map3.csv'
        elif choice == 4:
            print('Map 4 selected')
            mapa = 'map4.csv'
        elif choice == 5:
            print('Map 5 selected')
            mapa = 'map5.csv'
        elif choice == 6:
            print('Map 6 selected')
            mapa = 'map6.csv'
        elif choice == 7:
            print('Map 7 selected')
            mapa = 'map7.csv'
        elif choice == 8:
            print('Map 8 selected')
            mapa = 'map8.csv'
        elif choice == 9:
            print('Map 9 selected')
            mapa = 'map9.csv'
        else:
            # Any integer inputs other than values 1-5 we print an error message
            input('Wrong option selection. Enter any key to try again...')
        break

    return mapa


def main():
    choose_algorithm()
    mapa = choose_map()
    reader, start, end = read_csv(mapa)
    path_a_star_ = a_star_(reader, start, end)

    print('PATH:')

    print(path_a_star_)


if __name__ == '__main__':
    main()