# 1317
# 1392 low
# 1391
# 310 low

import os
import sys
import pathlib

from collections import deque

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper

def by_height(block):
    return block.height

class Block:
    def __init__(self, x, y, z, id):
        if type(x) == range:
            self.orientation = 'x'
            self.height = z
        elif type(y) == range:
            self.orientation = 'y'
            self.height = z
        elif type(z) == range:
            self.orientation = 'z'
            self.height = z.start
        else:
            self.orientation = None
            self.height = z

        self.x = x
        self.y = y
        self.z = z
        self.id = id #'ABCDEFGHIJ'[id]

    def __str__(self):
        return f'Block({self.x}, {self.y}, {self.z})'
    
    def __repr__(self):
        return f'{self.orientation}-Block {self.id} ({self.x}, {self.y}, {self.z}) at height {self.height}'
    
    def __contains__(self, item):
        x, y, z = item

        if self.orientation == 'x':
            return x in self.x and y == self.y and z == self.z
        elif self.orientation == 'y':
            return x == self.x and y in self.y and z == self.z
        elif self.orientation == 'z':
            return x == self.x and y == self.y and z in self.z
        else:
            return x == self.x and y == self.y and z == self.z

    def get_bottom_tiles(self):
        if self.orientation == 'x':
            return [(xi, self.y, self.z) for xi in self.x]

        elif self.orientation == 'y':
            return [(self.x, yi, self.z) for yi in self.y]

        elif self.orientation == 'z':
            return [(self.x, self.y, self.z.start)]
        
        else:
            return [(self.x, self.y, self.z)]
        
    def get_top_tiles(self):
        if self.orientation == 'x':
            return [(xi, self.y, self.z) for xi in self.x]

        elif self.orientation == 'y':
            return [(self.x, yi, self.z) for yi in self.y]

        elif self.orientation == 'z':
            return [(self.x, self.y, self.z.stop-1)]
        
        else:
            return [(self.x, self.y, self.z)]
    

    def let_fall(self, fallen, supports, surface):
        supports[self.id] = {'supports': set(), 'supported_by': set()}
        bottom_tiles = self.get_bottom_tiles()

        landed_on_block = False
        i = 0
        while not landed_on_block and bottom_tiles[0][2] - i - 1 > 0:
            for tile in bottom_tiles:
                x, y, z = tile

                # quick check if block is on surface
                if (x, y, z-i-1) in surface:
                    # check which already fallen blocks support the new block
                    for fallen_block in fallen:
                        if (x, y, z-i-1) in fallen_block:
                            supports[self.id]['supported_by'].add(fallen_block.id)
                            supports[fallen_block.id]['supports'].add(self.id)
                            landed_on_block = True

                            surface.remove((x, y, z-i-1))

            if not landed_on_block:
                i += 1

        self.height -= i
        if self.orientation == 'z':
            self.z = range(self.z.start - i, self.z.stop - i)
        else:
            self.z = self.z - i

        for tile in self.get_top_tiles():
            surface.add(tile)
        fallen.append(self)

def cascade(block_id, supports):
    queue = deque()
    falling_blocks = set()
    queue.append(block_id)
    falling_blocks.add(block_id)

    round_1 = True
    while queue:
        current_block_id = queue.popleft()
        block_falls = True
        for supported_by_block_id in supports[current_block_id]['supported_by']:
            if supported_by_block_id not in falling_blocks:
                block_falls = False
                break

        if block_falls or round_1:
            round_1 = False
            falling_blocks.add(current_block_id)
            for supported_block_id in supports[current_block_id]['supports']:
                queue.append(supported_block_id)
        
    return len(falling_blocks)

    

def solution(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()
    blocks = []

    for i, line in enumerate(lines):
        start, end = line.split('~')
        xs, ys, zs = map(int, start.split(','))
        xe, ye, ze = map(int, end.split(','))
        
        block = None
        if xs != xe:
            block = Block(range(xs, xe+1), ys, zs, i)
        elif ys != ye:
            block = Block(xs, range(ys, ye+1), zs, i)
        elif zs != ze:
            block = Block(xs, ys, range(zs, ze+1), i)
        else:
            block = Block(xs, ys, zs, i)

        blocks.append(block)
        
    blocks.sort(key=by_height, reverse=True)

    fallen = []
    supports = {}
    surface = set()

    while blocks:
        block = blocks.pop()
        block.let_fall(fallen, supports, surface)

    unique_supporter = set()
    for block in supports:
        if len(supports[block]['supported_by']) == 1:
            unique_supporter.add(list(supports[block]['supported_by'])[0])

    safely_pop = len(fallen) - len(unique_supporter)

    sum_cascade = 0
    for block in supports:
        sum_cascade = sum_cascade + cascade(block, supports) - 1

    return safely_pop, sum_cascade

def solution2(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()
    for i, line in enumerate(lines):
        pass

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