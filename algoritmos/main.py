#!/usr/bin/env/python

from read_csv import read_csv
from a_star_ import a_star_

# from dijkstra import dijkstra


def choose_algorithm():
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
    choice = int(input('What map do yoy want to use? [1-9]: '))
    return choice


def main():
    choose_algorithm()
    mapa = choose_map()
    reader, start, end = read_csv(mapa)
    path_a_star_ = a_star_(reader, start, end)

    print('PATH:')
    print(path_a_star_)


if __name__ == '__main__':
    main()