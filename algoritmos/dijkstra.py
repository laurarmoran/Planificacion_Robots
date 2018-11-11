#!/usr/bin/env/python
from typing import List, Any

import numpy

"""
    Para convertirloi a dijkstra, eliminar la H y continuar el algoritmo no 
    hasta que encuentra el destino, sino hasta que analiza todos los puntos
"""""


class Node():

    def __init__(self, g=0, parent=None, position=None):
        self.parent = parent
        self.position = position
        self.g = g

    def __eq__(self, other):
        return self.position == other.position


def take_g(node):
    return node.g


def dijkstra(map, start, end):

    # Create start and end node
    start_node = Node(0, None, start)
    start_node.g = 0
    end_node = Node(0, None, end)
    end_node.g = 0

    # Initialize stack
    stack = []  # pila con posiciones
    visited_nodes = []  # nodes already checked
    pass    # does nothing. Just to avoid previous line's complaints

    # Calculates map size
    w, h = len(map), len(map)
    map_size = w * h

    node_matrix = []

    node_matrix.append(start_node)

    # Add the start node
    current_node = start_node

    for node in range(0, map_size):
        # Found the goal
        if current_node == end_node:
            path = []
            current = current_node
            path.append(current.position)
            while current.parent is not None:
                for fp in node_matrix:
                    if fp.position == current.parent:
                        path.append(fp.position)
                        current = fp

            return path[::-1],len(visited_nodes)  # Return reversed path

        visited_nodes.append(current_node)

        # Generate new_nodes
        movements = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
        for new_position in movements:  # Adjacent squares
            # Get node position
            new_node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

            # Make sure within range
            if new_node_position[0] > (len(map) - 1) or new_node_position[0] < 0 or new_node_position[1] > (    # x dentro del mapa
                    len(map[len(map) - 1]) - 1) or new_node_position[1] < 0:  # y dentro del mapa
                continue

            # Make sure walkable terrain
            if map[new_node_position[0]][new_node_position[1]] != 0:  # si coincide con obstáculo vuelve a empezar el for
                continue

            stack.append(new_node_position)

            # Check if node is on the visited_node list
            for visited_node in visited_nodes:
                if new_node_position == visited_node.position:
                    stack.pop()
                else:
                    # Get node cost
                    if abs(new_position[0] + new_position[1]) == 1:  # posiciones 0, 2, 4 y 6
                        cost = 10  # movimiento recto
                    elif abs(new_position[0] + new_position[1]) == 0 or 2:  # posiciones 1, 3, 5 y 7
                        cost = 14  # movimiento diagonal

                    # Convert stack items from positions to nodes
                    new_node_cost = current_node.g + cost
                    new_node = Node(new_node_cost, current_node.position, new_node_position)

                    j = 0
                    for i in range(0, len(node_matrix)):
                        if node_matrix[i].position == new_node_position:
                            j = j+1
                            if node_matrix[i].g > new_node_cost:
                                node_matrix[i] = new_node
                    if j == 0:
                        node_matrix.append(new_node)


        # Choose next node
        sorted_matrix = node_matrix.copy()
        quit_index = []
        for visited in visited_nodes:
            for index in range(0, len(sorted_matrix)):
                if sorted_matrix[index].position == visited.position:
                    quit_index.append(index)

        """ Ordenar para que al quitar un objeto de la sorted_matrix quite de mayor
        a menor, porque si quit_index es [6,7,0] y el for está hasta la longitud de
        quit_index, en cuanto popea el 6, la longitud es menor, y se sale de rango el
        acceso a la posición 7"""
        quit_index.sort(reverse=True)

        for k in range(0, len(quit_index)):
            sorted_matrix.pop(quit_index[k])
        sorted_matrix.sort(key=take_g)
        current_node = sorted_matrix[0]
