#ifndef UTIL_H
#define UTIL_H

#include <vector>
#include <string>
#include <functional>
#include <chrono>
#include <iostream>

inline std::vector<std::string> split(const std::string& line, const std::string delimiter) {
    std::vector<std::string> splitted;
    
    size_t start = 0;
    size_t end = line.find(delimiter);

    size_t del_size = delimiter.size();

    while (end != std::string::npos) {
        splitted.push_back(line.substr(start, end - start));
        start = end + del_size;
        end = line.find(delimiter, start);
    }
    splitted.push_back(line.substr(start));

    return splitted;
}

template<typename Func, typename... Args>
inline auto time_function(Func func, Args&&... args) {
    auto start = std::chrono::high_resolution_clock::now();
    auto ret = func(std::forward<Args>(args)...);
    auto end = std::chrono::high_resolution_clock::now();
    
    std::chrono::duration<double> dur = end - start;
    std::cout << dur.count() << " ms" << std::endl;
    return ret;
}

#endif //UTIL_H