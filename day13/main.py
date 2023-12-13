import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper

def solution(input_file):
    result = 0
    patterns = open(input_file, 'r').read().split('\n\n')
    solved = set()
    for pp, pattern in enumerate(patterns):
        tiles = set()
        dots = set()
        lines = pattern.splitlines()
        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                if c == '#':
                    tiles.add(j+i*1j)
                else:
                    dots.add(j+i*1j)


        for k in range(1, len(lines[0])):
            error_tile = False
            for t in tiles:
                if t.real >= k:
                    mirrored_index = 2*(k-1) - t.real + 1
                    if complex(mirrored_index, t.imag) not in tiles and mirrored_index >= 0:
                        error_tile = True
                        break

            error_dot = False
            for d in dots:
                if d.real >= k:
                    mirrored_index = 2*(k-1) - d.real + 1
                    if complex(mirrored_index, d.imag) not in dots and mirrored_index >= 0:
                        error_dot = True
                        break

            if not error_tile and not error_dot:
                if pp in solved: print(pp, '\n', pattern)
                solved.add(pp)
                print(pp, 'fin-c', k)
                result += k
                break     

        for k in range(1, len(lines)):
            error_tile = False
            for t in tiles:
                if t.imag >= k:
                    mirrored_index = 2*(k-1) - t.imag + 1
                    if complex(t.real, mirrored_index) not in tiles and mirrored_index >= 0:
                        error_tile = True
                        break
            error_dot = False
            for d in dots:
                if d.imag >= k:
                    mirrored_index = 2*(k-1) - d.imag + 1
                    if complex(d.real, mirrored_index) not in dots and 2*(k-1) - d.imag + 1 >= 0:
                        error_dot = True
                        break

            if not error_tile and not error_dot:
                if pp in solved: print(pp, '\n', pattern)
                solved.add(pp)
                print(pp, 'fin-r', k)
                result += k * 100
                break


                

    return result

def solution2(input_file):
    result = 0
    patterns = open(input_file, 'r').read().split('\n\n')
    for pp, pattern in enumerate(patterns):
        tiles = set()
        dots = set()
        lines = pattern.splitlines()
        for i, line in enumerate(lines):
            for j, c in enumerate(line):
                if c == '#':
                    tiles.add(j+i*1j)
                else:
                    dots.add(j+i*1j)


        found = False
        for k in range(1, len(lines[0])):
            faults = set()
            for t in tiles:
                if t.real >= k:
                    if complex(2*(k-1) - t.real + 1, t.imag) not in tiles and 2*(k-1) - t.real + 1 >= 0:
                        faults.add(complex(2*(k-1) - t.real + 1, t.imag))

            for d in dots:
                if d.real >= k:
                    if complex(2*(k-1) - d.real + 1, d.imag) not in dots and 2*(k-1) - d.real + 1 >= 0:
                        faults.add(complex(2*(k-1) - d.real + 1, d.imag))
            
            if len(faults) == 1:
                result += k

        for k in range(1, len(lines)):
            faults = set()
            for t in tiles:
                if t.imag >= k:
                    if complex(t.real, 2*(k-1) - t.imag + 1) not in tiles and 2*(k-1) - t.imag + 1 >= 0:
                        faults.add(complex(t.real, 2*(k-1) - t.imag + 1))
            for d in dots:
                if d.imag >= k:
                    if complex(d.real, 2*(k-1) - d.imag + 1) not in dots and 2*(k-1) - d.imag + 1 >= 0:
                        faults.add(complex(d.real, 2*(k-1) - d.imag + 1))
            
            if len(faults) == 1:
                result += k * 100
                

    return result

if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    if 1: # run part 1
        print(helper.benchmark(solution)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(helper.benchmark(solution)(file_directory / 'input.txt'))
    if 0: # run part 2
        print('\n----------------part2----------------\n')
        print(helper.benchmark(solution2)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(helper.benchmark(solution2)(file_directory / 'input.txt'))