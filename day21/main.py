import os
import sys
import pathlib
from collections import deque

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper

def solution(input_file, n=65):
    start = 0
    lines = open(input_file, 'r').read().splitlines()
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == 'S':
                start = x + y * 1j

    dim = len(lines[0]) + len(lines)*1j

    seen = set()
    seen.add(start)
    even_odd_count = [1, 0]

    queue = deque()
    queue.append((start, 0))
    directions = [1,-1,1j,-1j]
    while queue:
        coord, steps = queue.popleft()
        if steps >= n:
            break
        for d in directions:
            new_coord = coord + d
            if new_coord in seen:
                continue
            
            if 0 <= new_coord.real < dim.real and 0 <= new_coord.imag < dim.imag:
                seen.add(new_coord)
                c = lines[int(new_coord.imag)][int(new_coord.real)]
                if c == '#':
                    continue
                else:
                    queue.append((new_coord, steps + 1))
                    even_odd_count[(steps + 1) % 2] += 1
    
    return even_odd_count[n % 2]

def solution2(input_file, number_of_steps=525, brute_force=False):
    start = 0
    lines = open(input_file, 'r').read().splitlines()

    dim = len(lines[0]) + len(lines)*1j

    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            if c == 'S':
                start = x + y *1j

    dim = len(lines[0]) + len(lines)*1j

    seen = set()
    seen.add(start)
    even_odd_count = [1, 0]

    queue = deque()
    queue.append((start, 0))
    directions = [1,-1,1j,-1j]

    last_steps = 0
    dist = {}
    max_steps = 4 * dim.real

    if brute_force:
        max_steps = number_of_steps

    while queue:
        coord, steps = queue.popleft()
        if steps > last_steps:
            dist[last_steps] = even_odd_count[last_steps % 2]

        last_steps = steps

        if steps > max_steps:
            break

        for d in directions:
            new_coord = coord + d
            if new_coord in seen:
                continue
            
            if not brute_force:
                if not start.real-2*dim.real < new_coord.real < start.real+2*dim.real:
                    continue

                if not start.imag-2*dim.imag < new_coord.imag < start.imag+2*dim.imag:
                    continue
            
            seen.add(new_coord)
            r, c = int(new_coord.imag % dim.imag), int(new_coord.real % dim.real)

            ch = lines[r][c]
            if ch == '#':
                continue
            else:
                queue.append((new_coord, steps + 1))
                even_odd_count[(steps + 1) % 2] += 1

    d = 2*dim.real

    if brute_force:
        return dist[number_of_steps]

    remainder = number_of_steps % d
    cube_dist = number_of_steps // d

    print(f'{number_of_steps=}')
    print(f'{remainder=}')
    print(f'{cube_dist=}')

    number_of_n_1 = cube_dist + 1
    number_of_n_2 = cube_dist
    fields_complete = even_odd_count[number_of_steps % 2] + 2

    nr = cube_dist - 1
    number_complete = (nr**2 + nr) / 2

    fields_1 = dist[remainder]
    if remainder + d in dist:
        fields_2 = dist[remainder+d]
    else:
        fields_2 = fields_complete

    increment = int(number_of_n_1 * (fields_1 + 4 * (remainder+1) / 2) - 4 * (remainder+1)/2)
    total_number = increment
    print('1:')
    print(f'{int(number_of_n_1)}x ({int(fields_1)} + {int(remainder+1)} x 4 / 2) - 4 x {int(remainder+1)}/2 = {increment}')
    if number_of_n_2 > 0:
        increment = int(number_of_n_2 * (fields_2 + 4 * d / 2 + 1) - 4 * d/2) # + 1 from S square
        total_number += increment
        print('2: ')
        print(f'{int(number_of_n_2)}x ({int(fields_2)} + 4 x {int(d)} / 2) - 4 x {int(d)}/2 = {increment}')

    if nr > 0:
        increment = int(number_complete * (fields_complete + 4 * d / 2) - nr * 4 * d / 2)
        total_number += increment
        print('complete: ')
        print(f'{int(number_complete)}x ({int(fields_complete)} + {nr} x 4 x {int(d)} / 2) - 4 x {int(d)}/2 = {increment}')
        
    return total_number

if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    if 1: # run part 1
        print(helper.benchmark(solution)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(helper.benchmark(solution)(file_directory / 'input.txt'))
    if 1: # run part 2
        print('\n----------------part2----------------\n')
        number = 26501365
        #bf = helper.benchmark(solution2)(file_directory / 'input.txt', number, True)
        #print(bf)
        print('\n*******************************\n')
        ex = helper.benchmark(solution2)(file_directory / 'input.txt', number, False)
        print(int(ex))

        #print(int(ex - bf))