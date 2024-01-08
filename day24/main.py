import os
import sys
import pathlib

parent_directory = os.path.abspath('.')
sys.path.append(parent_directory)

import helper

from itertools import combinations

class Point:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __str__(self):
        return f'P: ({self.x}, {self.y}, {self.z})'

    def __add__(self, v):
        return Point(self.x + v.x, self.y + v.y, self.z + v.z)

class Vector:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def __str__(self):
        return f'V: ({self.x}, {self.y}, {self.z})'

    def __mul__(self, k):
        return Vector(self.x * k, self.y * k, self.z * k)

    def scalar_product(self, v):
        return self.x * v.x + self.y * v.y + self.z * v.z
    
    def is_parallel(self, v):
        return self.x * v.y - self.y * v.x == 0
    
    def is_parallel_3d(self, v):
        return self.x * v.y - self.y * v.x == 0 and self.x * v.z - self.z * v.x == 0 and self.y * v.z - self.z * v.y == 0
    
class Trajectory:
    def __init__(self, p, v):
        self.p, self.v = p, v

    def __str__(self):
        return f'T: {self.p} + t * {self.v}'

    def point_on_trajectory(self, t):
        return self.p + self.v * t

def intersect(t1, t2):
    if t1.v.is_parallel(t2.v):
        return None
    
    s = (t2.p.y * t1.v.x - t1.p.y * t1.v.x - t2.p.x * t1.v.y + t1.p.x * t1.v.y) / (t2.v.x * t1.v.y - t1.v.x * t2.v.y)
    t = (t2.p.x + t2.v.x * s - t1.p.x) / t1.v.x

    return t, s, t2.point_on_trajectory(s)


def solution(input_file, limits):
    result = 0
    lines = open(input_file, 'r').read().splitlines()

    trajectories = []

    for i, line in enumerate(lines):
        pos, vel = line.split(' @ ')
        px, py, pz = map(int, pos.split(', '))
        vx, vy, vz = map(int, vel.split(', '))

        trajectories.append(Trajectory(Point(px, py, pz), Vector(vx, vy, vz)))

    for t1, t2 in combinations(trajectories, 2):
        re = intersect(t1, t2)
        if re is not None:
            t, s, p = re
            if t > 0 and s > 0 and limits[0] <= p.x <= limits[1] and limits[0] <= p.y <= limits[1]:
                result += 1

    return result

def solution2(input_file):
    result = 0
    lines = open(input_file, 'r').read().splitlines()
    for i, line in enumerate(lines):
        pass

    return result

if __name__ == '__main__':
    file_directory = pathlib.Path(__file__).parent.absolute()
    if 1: # run part 1
        print(helper.benchmark(solution)(file_directory / 'test.txt', limits=(7,27)))
        print('\n*******************************\n')
        print(helper.benchmark(solution)(file_directory / 'input.txt', limits=(200000000000000, 400000000000000)))
    if 0: # run part 2
        print('\n----------------part2----------------\n')
        print(helper.benchmark(solution2)(file_directory / 'test.txt'))
        print('\n*******************************\n')
        print(helper.benchmark(solution2)(file_directory / 'input.txt'))