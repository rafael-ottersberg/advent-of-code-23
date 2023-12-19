# 857

import os
import sys
import pathlib
import heapq

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper

grid = []
distances = []
goal = (0,0)
worst_case = float('inf')
heap = []
heapq.heapify(heap)
pushed = set()

def is_on_grid(position):
    global goal
    return 0 <= position[0] <= goal[0] and 0 <= position[1] <= goal[1]

def dist_to_goal(position):
    global goal
    return abs(goal[0] - position[0]) + abs(goal[1] - position[1])

def heuristic(coord):
    global distances
    return distances[coord[1]][coord[0]]


def dijkstra(grid):
    rows, cols = len(grid), len(grid[0])

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    dist = [[float('inf')] * cols for _ in range(rows)]
    dist[rows-1][cols-1] = int(grid[rows-1][cols-1])  # start bottom right

    # Min-heap
    pq = [(int(grid[rows-1][cols-1]), (cols-1, rows-1))]  # (distance, row, col)
    heapq.heapify(pq)

    while pq:
        curr_dist, coord = heapq.heappop(pq)
        c, r = coord

        # If current distance is already greater than the stored distance, skip
        if curr_dist > dist[r][c]:
            continue
        
        # Check all neighbours
        for dx, dy in directions:
            next_coord = (coord[0] + dx, coord[1] + dy)
            nc, nr = next_coord

            if is_on_grid(next_coord):
                new_dist = curr_dist + int(grid[nr][nc])
                
                if new_dist < dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    heapq.heappush(pq, (new_dist, next_coord))

    return dist


def add_next_states(position, direction, count, travelled_before):
    global grid, goal, heap, pushed

    tile_cost = int(grid[position[1]][position[0]])

    travelled = travelled_before + tile_cost
    if position == goal:
        return travelled
    
    next_params = []

    # walk straight
    if count < 3:
        next_position = (position[0] + direction[0], position[1] + direction[1])
        if is_on_grid(next_position):
            next_param = (next_position, direction, count+1, travelled)
            next_params.append(next_param)
    
    # turn left, right
    for d in [-1, 1]:
        if direction[0] == 0:
            next_dir = (d, 0)
        else:
            next_dir = (0, d)
        
        next_position = (position[0] + next_dir[0], position[1] + next_dir[1])
        if is_on_grid(next_position):
            next_param = (next_position, next_dir, 1, travelled)
            next_params.append(next_param)

    for next_param in next_params:
        next_pos, next_dir, next_count, travelled = next_param

        for i in range(0, next_count):
            if (next_pos, next_dir, i + 1, travelled) in pushed:
                break
        else:
            heapq.heappush(heap, (travelled_before + heuristic(next_pos), next_pos, next_dir, next_count, travelled))
            pushed.add(next_param)



def solution(input_file):
    global grid, goal, heap, distances, pushed
    
    grid = open(input_file, 'r').read().splitlines()
    goal = (len(grid[0]) - 1 , len(grid) - 1)

    distances = dijkstra(grid)
    print(distances)

    distance_walked = 0

    heap = []
    heapq.heapify(heap)

    pushed = set()

    heapq.heappush(heap, (dist_to_goal((1,0)), (1,0), (1,0), 1, distance_walked))
    heapq.heappush(heap, (dist_to_goal((0,1)), (0,1), (0,1), 1, distance_walked))

    seen = set()
    while heap:
        min_dist, coord, dir, count, dist = heapq.heappop(heap)
        #if coord not in seen:
        #    print(coord)
        #    seen.add(coord)
        res = add_next_states(coord, dir, count, dist)
        if res is not None:
            return res
        
def add_next_states_2(position, direction, count, travelled_before):
    global grid, goal, heap, pushed

    tile_cost = int(grid[position[1]][position[0]])

    travelled = travelled_before + tile_cost
    if position == goal:
        return travelled
    
    next_params = []

    # walk straight
    if count < 10:
        next_position = (position[0] + direction[0], position[1] + direction[1])
        if is_on_grid(next_position):
            next_param = (next_position, direction, count+1, travelled)
            next_params.append(next_param)
    
    # turn left, right
    for d in [-1, 1]:
        if direction[0] == 0:
            next_dir = (d, 0)
        else:
            next_dir = (0, d)
        
        add_cost = 0
        for i in range(1,4):
            next_position = (position[0] + next_dir[0]*i, position[1] + next_dir[1]*i)
            if is_on_grid(next_position):
                add_cost += int(grid[next_position[1]][next_position[0]])
            else:
                break
        else:
            next_position = (position[0] + next_dir[0]*4, position[1] + next_dir[1]*4)
            if is_on_grid(next_position):
                next_param = (next_position, next_dir, 4, travelled+add_cost)
                next_params.append(next_param)

    for next_param in next_params:
        next_pos, next_dir, next_count, travelled = next_param

        for i in range(3, next_count):
            if (next_pos, next_dir, i + 1, travelled) in pushed:
                break
        else:
            heapq.heappush(heap, (travelled_before + heuristic(next_pos), next_pos, next_dir, next_count, travelled))
            pushed.add(next_param)
       

def solution2(input_file):
    global grid, goal, heap, distances, pushed
    
    grid = open(input_file, 'r').read().splitlines()
    goal = (len(grid[0]) - 1 , len(grid) - 1)

    distances = dijkstra(grid)

    distance_walked = 0

    heap = []
    heapq.heapify(heap)

    pushed = set()

    heapq.heappush(heap, (dist_to_goal((1,0)), (1,0), (1,0), 1, distance_walked))
    heapq.heappush(heap, (dist_to_goal((0,1)), (0,1), (0,1), 1, distance_walked))

    seen = set()
    while heap:
        min_dist, coord, dir, count, dist = heapq.heappop(heap)
        #if coord not in seen:
        #    print(coord)
        #    seen.add(coord)
        res = add_next_states_2(coord, dir, count, dist)
        if res is not None:
            return res

if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    if 1: # run part 1
        print(helper.benchmark(solution)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        #print(helper.benchmark(solution)(file_directory / 'input.txt'))
    if 1: # run part 2
        print('\n----------------part2----------------\n')
        print(helper.benchmark(solution2)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        #print(helper.benchmark(solution2)(file_directory / 'input.txt'))