#!/usr/bin/env/python

import time
from read_csv import read_csv
from a_star_ import a_star_
from dijkstra import dijkstra
from best_first import best_first
from best_first_ import best_first_


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
            # Any integer inputs other than values 1-5 we print an error message
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

    if algorithm_chosen == 1:
        path = a_star_(mapa, start, end)
    elif algorithm_chosen == 2:
        path = dijkstra(mapa, start, end)
    elif algorithm_chosen == 3:
        path = best_first(mapa, start, end)
    elif algorithm_chosen == 4:
        path = best_first_(mapa, start, end)

    print('PATH:')
    print(path)


if __name__ == '__main__':
    start_time = time.time()
    main()
    print("\n--- RUN TIME: ---")
    print("--- %s seconds ---" % (time.time() - start_time))

    # PATH:
    # [(2, 2), (3, 2), (4, 2), (5, 2), (6, 2), (7, 2), (8, 2)]
    #
    # --- RUN TIME: ---
    # --- 4.510892629623413 seconds ---

    # --- RUN TIME: ---
    # --- 5.804784059524536 seconds ---