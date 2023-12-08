import os
import sys
import pathlib
import math

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper

def solution(input_file):
    instructions = 'LR'
    lines = open(input_file, 'r').read().splitlines()

    commands = lines[0]

    nodes = dict()

    for i, line in enumerate(lines[2:]):
        now, right_left = line.split(' = ')
        right, left = right_left.strip('(').strip(')').split(', ')

        nodes[now] = (right, left)

    node = 'AAA'
    count = 0
    while True:
        instr = commands[count % len(commands)]
        i = instructions.index(instr)
        node = nodes[node][i]
        count += 1


        if node == 'ZZZ':
            return count

def solution2(input_file):
    instructions = 'LR'
    result = 0
    lines = open(input_file, 'r').read().splitlines()

    commands = lines[0]

    nodes = dict()
    a_nodes = []
    for i, line in enumerate(lines[2:]):
        now, right_left = line.split(' = ')
        right, left = right_left.strip('(').strip(')').split(', ')

        nodes[now] = (right, left)

        if now.endswith('A'):
            a_nodes.append(now)

    count = 0

    found_first_time = dict()
    found_second_time = dict()
    while a_nodes:
        instr = commands[count % len(commands)]
        i = instructions.index(instr)
        
        a_nodes = [nodes[node][i] for node in a_nodes]
        count += 1

        for n in a_nodes:
            if n.endswith('Z'):
                if n not in found_first_time.keys():
                    found_first_time[n] = count
                else:
                    found_second_time[n] = count
                    a_nodes.remove(n)

    starts = []
    diffs = []
    for i, k in enumerate(found_first_time):
        starts.append(found_first_time[k])
        diffs.append(found_second_time[k] - found_first_time[k])

    print(starts, diffs)

    lcm = 1
    for i in starts:
        lcm = lcm*i//math.gcd(lcm, i)
    
    return lcm


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