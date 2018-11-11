#!/usr/bin/env/python

import time
from read_csv import read_csv
from a_star_ import a_star_
from dijkstra import dijkstra
from best_first import best_first


def choose_algorithm():
    print('Please choose an algorithm: ')
    print('1. A* (A star)')
    print('2. Dijkstra')
    print('3. Best_first')
    choice = int(input("Enter your choice [1-3]: "))

    while 1:
        if choice == 1:
            print('A* selected')
        elif choice == 2:
            print('Dijkstra selected')
        elif choice == 3:
             print('Best-First selected')
        else:
            # Any integer inputs other than values 1-3 we print an error message
            input("Wrong option selection. Enter any key to try again..")
        break
    return choice


def choose_map():
    choice = int(input('What map do yoy want to use? [1-11]: '))
    return choice


def main():
    algorithm_chosen = choose_algorithm()
    map_chosen = choose_map()
    mapa, start, end = read_csv(map_chosen)
    path = []
    num_visited_nodes = 0

    start_time = time.time()
    if algorithm_chosen == 1:
        path, num_visited_nodes = a_star_(mapa, start, end)
    elif algorithm_chosen == 2:
        path, num_visited_nodes = dijkstra(mapa, start, end)
    elif algorithm_chosen == 3:
        path, num_visited_nodes = best_first(mapa, start, end)
    end_time = time.time()

    print('\nAlgorithm has checked: %s nodes' %(num_visited_nodes))
    print('\nPATH:')
    print(path)
    print('\nPATH has: %s nodes' % (len(path)))

    print("\n--- RUN TIME: ---")
    print("--- %s ms ---\n" % ((end_time - start_time) * 1000))



if __name__ == '__main__':
    main()
    input()