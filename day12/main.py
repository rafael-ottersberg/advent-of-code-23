import os
import sys
import pathlib
import re

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper
from itertools import product
from functools import cache

def solution(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()

    for i, line in enumerate(lines):
        spmap, numbers = line.split()
        numbers = numbers.split(',')

        s, q = [], []
        for j, c in enumerate(spmap):
            if c == '#':
                s.append(j)
            elif c == '?':
                q.append(j)

        perm_count = 0
        for p in product(range(2), repeat=len(q)):
            spring = s.copy()
            for i, _p in enumerate(p):
                if _p:
                    spring.append(q[i])

            spring.sort()

            count = 1
            count_i = 0
            for ind in range(1, len(spring)):
                step = spring[ind] - spring[ind-1]
                if step > 1:
                    if count != int(numbers[count_i]):
                        break
                    count_i += 1
                    count = 1
                    if count_i >= len(numbers):
                        break
                else:
                    count += 1
            
            else:
                if count_i == len(numbers) - 1 and count == int(numbers[-1]):
                    perm_count += 1

        result += perm_count

    return result

def solution2(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()

    for i, line in enumerate(lines):
        spmap, numbers = line.split()
        numbers = numbers.split(',')

        numbers = list(map(int, numbers))*5
        spmap_new = spmap
        for _ in range(4):
            spmap_new += f'?{spmap}'

        poss = search_in_string(tuple(numbers), spmap_new)
        result += poss

    return result

@cache
def search_in_string(numbers, string):    
    needed_c = sum(numbers) + len(numbers) - 1
    if needed_c > len(string):
        return 0
    
    possibilities = 0
    if not numbers:
        if '#' not in string:
            possibilities = 1

    else:
        index = int(numbers.index(max(numbers)))
        regex = '(?=((?<!#)[?#]{'+ str(numbers[index]) +'}(?!#)))'
        matches = [match for match in re.finditer(regex, string)]

        for match in matches:
            match_start = match.start()
            ms = match_start
            if ms > 0:
                ms -= 1
            me = match_start + numbers[index]
            if me < len(string):
                me += 1

            p_l = search_in_string(numbers[:index], string[:ms])
            p_r = search_in_string(numbers[index+1:], string[me:])
            possibilities += p_l * p_r
    return possibilities


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