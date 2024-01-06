import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper

arrows = {
    '^': (0, -1),
    'v': (0, 1),
    '<': (-1, 0),
    '>': (1, 0)
}

def is_vertice(x, y, grid):
    neighbour_count = 0
    for dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        dx, dy = dc
        if grid[y + dy][x + dx] != '#':
            neighbour_count += 1

    return neighbour_count > 2

def find_next_vertices(x, y, dir, grid, vertices, test_direction = True):
    for dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        dx, dy = dc

        if dx == -dir[0] and dy == -dir[1]:
            continue

        tile = grid[y + dy][x + dx]

        if tile == '#':
            continue
        
        if test_direction:
            if tile in arrows:
                if arrows[tile] != dc:
                    return None
        
        if (x + dx, y + dy) in vertices:
            return (x + dx, y + dy), 1
        
        re = find_next_vertices(x + dx, y + dy, dc, grid, vertices, test_direction=test_direction)

        if re is None:
            return None
        else:
            coor, rest_distance = re
            return coor, rest_distance + 1
    
    return None

def find_all_vertices(grid):
    vertices = []
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == '#':
                continue

            if y == 0 or y == len(grid) - 1:
                vertices.append((x, y))
                continue

            if is_vertice(x, y, grid):
                vertices.append((x, y))
    return vertices

def build_graph(grid, vertices, test_direction = True):
    graph = {}

    for v in vertices:
        x, y = v
        graph[v] = {}
        for dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            dx, dy = dc

            if x + dx < 0 or x + dx >= len(grid[0]) or y + dy < 0 or y + dy >= len(grid):
                continue

            tile = grid[y + dy][x + dx]

            if tile == '#':
                continue
            
            if test_direction:
                if tile in arrows:
                    if arrows[tile] != dc:
                        continue

            re = find_next_vertices(x + dx, y + dy, dc, grid, vertices, test_direction=test_direction)
            if re is not None:
                coor, distance = re
                graph[v][coor] = distance + 1

    return graph

def traverse(current_vertice, graph, visited, vertices):
    max_distance = 0
    for next_vertice in graph[current_vertice]:
        if next_vertice == vertices[-1]:
            return graph[current_vertice][next_vertice]

        if next_vertice in visited:
            continue

        new_visited = visited.copy()
        new_visited.add(next_vertice)

        max_distance = max(traverse(next_vertice, graph, new_visited, vertices) + graph[current_vertice][next_vertice], max_distance)

    return max_distance


def solution(input_file):
    grid = open(input_file, 'r').read().splitlines()

    vertices = find_all_vertices(grid)

    graph = build_graph(grid, vertices)
    start = vertices[0]
    visited = set()

    result = traverse(start, graph, visited, vertices)

    return result

def solution2(input_file):
    grid = open(input_file, 'r').read().splitlines()

    vertices = find_all_vertices(grid)

    graph = build_graph(grid, vertices, test_direction=False)
    start = vertices[0]
    visited = set()

    result = traverse(start, graph, visited, vertices)

    return result

if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    if 1: # run part 1
        print(helper.benchmark(solution)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(helper.benchmark(solution)(file_directory / 'input.txt'))
    if 1: # run part 2
        print('\n----------------part2----------------\n')
        print(helper.benchmark(solution2)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(helper.benchmark(solution2)(file_directory / 'input.txt'))