#!/usr/bin/env/python

import numpy as np

from read_csv import read_csv
from a_star_ import a_star_
# from a_star_ import Node

# from dijkstra import dijkstra


def main():

    reader, start, end = read_csv('map1.csv')
    path_a_star_ = a_star_(reader, start, end)

    print('PATH:')

    print(path_a_star_)


if __name__ == '__main__':
    main()