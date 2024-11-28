#include <string>
#include <iostream>
#include "day01/day01.hpp"
#include "util.hpp"

int main() {
    std::string folder_path = "/home/rafael/advent-of-code-23/day01/";

    std::cout << time_function(d01pt1, folder_path, "test.txt") << std::endl;
    std::cout << time_function(d01pt1, folder_path, "input.txt") << std::endl;
    std::cout << time_function(d01pt2, folder_path, "test2.txt") << std::endl;
    std::cout << time_function(d01pt2, folder_path, "input.txt") << std::endl;
    return 0;
}