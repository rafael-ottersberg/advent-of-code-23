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
    result = 0
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

    def full_cycle(stones):
        print_=False
        stones = list(stones)        
        #print('start')
        #print(sorted(stones, key=lambda x: x[0].real + x[0].imag*1000))

        # north
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
                
        stones = new_stones
        if print_:
            print('after north')
            print(sorted(stones, key=lambda x: x[0].real + x[0].imag*1000))
        # west
        stones = sorted(stones, key=lambda x: x[0].real)
        last_limits = [0]*len(lines[0])
        new_stones = []
        for stone in stones:
            pos = int(stone[0].imag)
            if stone[1]:
                new_stones.append((complex(last_limits[pos], pos), 1))
                last_limits[pos] += 1
            else:
                last_limits[pos] = stone[0].real + 1
                new_stones.append(stone)

        stones = new_stones
        if print_:
            print('after west')
            print(sorted(stones, key=lambda x: x[0].real + x[0].imag*1000))
        # south
        stones = sorted(stones, key=lambda x: x[0].imag)[::-1]
        last_limits = [len(lines)-1]*len(lines)
        new_stones = []
        for stone in stones:
            pos = int(stone[0].real)
            if stone[1]:
                new_stones.append((complex(pos, last_limits[pos]), 1))
                last_limits[pos] -= 1
            else:
                last_limits[pos] = stone[0].imag - 1
                new_stones.append(stone)

        stones = new_stones
        if print_:
            print('after south')
            print(sorted(stones, key=lambda x: x[0].real + x[0].imag*1000))
        # east
        stones = sorted(stones, key=lambda x: x[0].real)[::-1]
        last_limits = [len(lines)-1]*len(lines)
        new_stones = []
        for stone in stones:
            pos = int(stone[0].imag)
            if stone[1]:
                new_stones.append((complex(last_limits[pos], pos), 1))
                last_limits[pos] -= 1
            else:
                last_limits[pos] = stone[0].real - 1
                new_stones.append(stone)

        stones = new_stones
        if print_:
            print('after west')
            print(sorted(stones, key=lambda x: x[0].real + x[0].imag*1000))

        return tuple(stones)
    

    stones = tuple(stones)
    count = 0
    history = []
    while count < 1000000000:
        if stones in history:
            break
        else:
            history.append(stones)
            stones = full_cycle(stones)
            count += 1
            
    start = history.index(stones)
    step = count - start

    solution_index = (1000000000 - start) % step + start

    return eval_rank(history[solution_index], len(lines))


if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    if 0: # run part 1
        print(helper.benchmark(solution)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(helper.benchmark(solution)(file_directory / 'input.txt'))
    if 1: # run part 2
        print('\n----------------part2----------------\n')
        print(helper.benchmark(solution2)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(helper.benchmark(solution2)(file_directory / 'input.txt'))