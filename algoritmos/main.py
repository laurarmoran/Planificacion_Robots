#!/usr/bin/env


from read_csv import read_csv
#from a_star_ import a_star_
from dijkstra import dijkstra


def main():

    graph, start, end = read_csv('map1.csv')
    # path_a_star_ = a_star_(graph, start, end)

    print('\nTHIS IS THE PATH:')

    delta, previous = dijkstra(graph, start)

    path_dijkstra = []
    vertex = end

    while vertex is not None:
        path_dijkstra.append(vertex)
        vertex = previous[vertex]

        path_dijkstra.reverse()
    return path_dijkstra

    # print(path_a_star_)


if __name__ == '__main__':
    main()

