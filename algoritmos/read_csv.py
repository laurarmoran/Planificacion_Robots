#!/usr/bin/env/python

import csv
import numpy


def read_csv(mapa):

    with open(mapa) as myFile:
        reader = csv.reader(myFile)
        reader = list(reader)   # convert tuple to list (list of strings)
        maze = []       # list of lists

        start = (1, 1)
        end = (7, 3)

        print('\nMAP: ')

        for row in reader:
            maze.append(list(map(int, row)))        # convert to list of lists (lists of integers instead of strings)
        print(numpy.array(maze))

    return maze, start, end