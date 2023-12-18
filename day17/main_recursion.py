import os
import sys
import pathlib

sys.setrecursionlimit(3000)

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper

grid = []
goal = (0,0)

worst_case = float('inf')
cache = dict()

def is_on_grid(position):
    global goal
    return 0 <= position[0] <= goal[0] and 0 <= position[1] <= goal[1]

def dist_to_goal(position):
    global goal
    return abs(goal[0] - position[0]) + abs(goal[1] - position[1])

def is_worth_exploring(position, travelled):
    global worst_case
    return travelled + dist_to_goal(position) <= worst_case

def walk(position, direction, count, history):
    global grid, goal, cache

    param = (position, direction, count)
    if param in history:
        return float('inf'), []

    if param in cache:
        return cache[param]
    
    if position == goal:
        result = (int(grid[position[1]][position[0]]), [(position, direction)])
        cache[param] = result
        return result

    next_params = []

    # walk straight
    if count < 3:
        next_position = (position[0] + direction[0], position[1] + direction[1])
        if is_on_grid(next_position):
            next_param = (next_position, direction, count+1)
            next_params.append(next_param)
    
    # turn left, right
    #assert direction[0] == 0 or direction[1] == 0
    for d in [-1, 1]:
        if direction[0] == 0:
            next_dir = (d, 0)
        else:
            next_dir = (0, d)
        
        next_position = (position[0] + next_dir[0], position[1] + next_dir[1])
        if is_on_grid(next_position):
            next_param = (next_position, next_dir, 1)
            next_params.append(next_param)

    best_dist = float('inf')
    best_backlog = []

    for next_param in next_params:
        next_pos, next_dir, next_count = next_param
        dist, backlog = walk(next_pos, next_dir, next_count, history + [param])
        if dist < best_dist:
            best_dist = dist
            best_backlog = backlog

    result = best_dist + int(grid[position[1]][position[0]])
    
    new_backlog =  best_backlog + [(position, direction)]
    cache[param] = (result, new_backlog)

    return result, new_backlog

def print_result(result):
    global grid
    coords = [r[0] for r in result[1]]
    dirs = [r[1] for r in result[1]]

    for j in range(goal[0]+1):
        for i in range(goal[1]+1):
            if (i,j) in coords:
                match dirs[coords.index((i,j))]:
                    case (1,0):
                        print('>', end='')
                    case (-1,0):
                        print('<', end='')
                    case (0,-1):
                        print('^', end='')
                    case (0,1):
                        print('v', end='')
            else:
                print(grid[j][i], end='')
        print()

def solution(input_file):
    global grid, goal, cache
    grid = open(input_file, 'r').read().splitlines()
    goal = (len(grid[0]) - 1 , len(grid) - 1)

    cache = dict()
    history = []

    result = walk((1,0), (1,0), 1, history.copy())
    result2 = walk((0,1), (0,1), 1, history.copy())

    if result2[0] < result[0]:
        result = result2

    print_result(result)    

    return result[0]

def solution2(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()
    for i, line in enumerate(lines):
        pass

    return result

if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    if 1: # run part 1
        print(helper.benchmark(solution)(file_directory / 'test_.txt'))
        print('\n*******************************\n')
        #print(helper.benchmark(solution)(file_directory / 'input.txt'))
    if 0: # run part 2
        print('\n----------------part2----------------\n')
        print(helper.benchmark(solution2)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(helper.benchmark(solution2)(file_directory / 'input.txt'))