import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper

def solution(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()
    lines = list(zip(*lines))
    for i, line in enumerate(lines):
        stones = []
        for j, c in enumerate(line):
            if c == "#":
                stones.append((j, 0))
            elif c == "O":
                stones.append((j, 1))

        last_limit = 0
        for stone in stones:
            if stone[1]:
                result += len(lines[0]) - last_limit
                last_limit += 1
            else:
                last_limit = stone[0] + 1
            
    return result

def solution2(input_file):
    lines = open(input_file, 'r').read().splitlines()
    lines = list(zip(*lines))
    stones = []
    for i, line in enumerate(lines):
        for j, c in enumerate(line):
            if c == "#":
                stones.append((i+j*1j, 0))
            elif c == "O":
                stones.append((i+j*1j, 1))

    def eval_rank(stones, lines):
        result = 0
        for stone in stones:
            if stone[1]:
                result += lines - stone[0].imag

        return int(result)
    
    def shift_north(stones):    
        stones = sorted(stones, key=lambda x: x[0].imag)
        last_limits = [0]*len(lines[0])
        new_stones = []
        for stone in stones:
            pos = int(stone[0].real)
            if stone[1]:
                new_stones.append((complex(pos, last_limits[pos]), 1))
                last_limits[pos] += 1
            else:
                last_limits[pos] = stone[0].imag + 1
                new_stones.append(stone)
                
        return new_stones
    
    def rotate(stones, grid_size):
        return [(complex(grid_size - stone[0].imag - 1, stone[0].real), stone[1]) for stone in stones]


    def full_cycle(stones):
        stones = list(stones)        
        for _ in range(4):
            stones = shift_north(stones)
            stones = rotate(stones, len(lines))

        return tuple(stones)
    
    n = 1000000000
    stones = tuple(stones)
    count = 0
    history = []
    while count < n:
        if stones in history:
            break
        else:
            history.append(stones)
            stones = full_cycle(stones)
            count += 1
            
    start = history.index(stones)
    step = count - start

    solution_index = (n - start) % step + start

    return eval_rank(history[solution_index], len(lines))


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