#!/usr/bin/env

import csv


def read_csv(mapa):

    with open(mapa) as myFile:
        reader = csv.reader(myFile)
        reader = list(reader)   # convert tuple to list

        start = (0, 0)
        end = (7, 8)

        print('THIS IS THE MAP: ')

        for row in reader:
            print(row)

    return reader, start, end

