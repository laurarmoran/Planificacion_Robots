#!/usr/bin/env/python

import csv
import numpy


def read_csv(choice):

    mapa = 'map'+str(choice)+'.csv'
    with open(mapa) as myFile:
        reader = csv.reader(myFile)
        reader = list(reader)   # convert tuple to list (list of strings)
        maze = []       # list of lists

        print('\nMAP: ')

        for row in reader:   # -------> row pone columnas, line pone filas
            maze.append(list(map(int, row)))        # convert to list of lists (lists of integers instead of strings)
        print(numpy.array(maze))

        start, end = set_origin(maze)

    return maze, start, end


def set_origin(maze):

    while 1:
        print('\nSet origin: ')
        x_orig = int(input('X_orig: '))
        y_orig = int(input('Y_orig: '))

        if maze[x_orig][y_orig] != 0:
            input('\nInvalid origin coordinates. Press any key to select new ones... ')
            continue
        else:
            start = (x_orig, y_orig)
            print('start: ', start)

        print('\nSet destination: ')
        x_dest = int(input('X_dest: '))
        y_dest = int(input('Y_dest: '))

        if maze[x_dest][y_dest] != 0:
            input('\nInvalid destination coordinates. Press any key to select new ones... ')
            continue
        else:
            end = (x_dest, y_dest)
            print('end: ', end)

        return start, end