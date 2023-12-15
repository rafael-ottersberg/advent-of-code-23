import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper

def calc_hash(string):
    r=0
    for c in string:
        if c == '\n':
            continue
        r += ord(c)
        r *= 17
        r = r % 256
    return r

def solution(input_file):
    result = 0
    lines = open(input_file, 'r').read().split(',')

    for i, line in enumerate(lines):
        result += calc_hash(line)

    return result

def solution2(input_file):
    result = 0
    lines = open(input_file, 'r').read().split(',')
    boxes = [([],[]) for _ in range(256)]

    for i, line in enumerate(lines):
        if '-' in line:
            label, focal_length = line.split('-')
            h = calc_hash(label)
            if label in boxes[h][0]:
                i = boxes[h][0].index(label)
                boxes[h][0].pop(i)
                boxes[h][1].pop(i)
            
        else:
            label, focal_lenght = line.split('=')
            h = calc_hash(label)

            if label in boxes[h][0]:
                index = boxes[h][0].index(label)
                boxes[h][1][index] = int(focal_lenght)
            else:
                boxes[h][0].append(label)
                boxes[h][1].append(int(focal_lenght))

    for i, box in enumerate(boxes):
        label, focal = box
        for j, focal in enumerate(focal):
            result += (1 + i) * (1 + j) * focal

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