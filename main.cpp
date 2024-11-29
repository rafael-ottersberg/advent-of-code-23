#include <string>
#include <iostream>
#include "util.hpp"
#include "day03/day03.hpp"

int main() {
    std::string folder_path = "C:\\Users\\rafae\\\Documents\\code\\advent-of-code-23\\\\day03\\";

    std::cout << time_function(d03pt1, folder_path, "test.txt") << std::endl;
    std::cout << time_function(d03pt1, folder_path, "input.txt") << std::endl;
    std::cout << time_function(d03pt2, folder_path, "test.txt") << std::endl;
    std::cout << time_function(d03pt2, folder_path, "input.txt") << std::endl;
    return 0;
}