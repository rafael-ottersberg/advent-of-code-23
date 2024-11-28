cmake_minimum_required(VERSION 3.31)
project(AOC23 LANGUAGES CXX)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add compiler flags for bounds checking and other debug options in Debug mode
if (CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    set(CMAKE_CXX_FLAGS_DEBUG 
    "${CMAKE_CXX_FLAGS_DEBUG} -fsanitize=undefined -fno-omit-frame-pointer -Wall -Wextra -Wpedantic -Og -fstack-protector -DDEBUG -D_GLIBCXX_DEBUG")
    set(CMAKE_LINKER_FLAGS_DEBUG "${CMAKE_LINKER_FLAGS_DEBUG} -fsanitize=address,undefined")
endif()

set(CMAKE_EXPORT_COMPILE_COMMANDS ON)

find_package(TBB REQUIRED)

include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}
)

add_executable(aoc23 main.cpp)
target_link_libraries( 
    aoc23
    PRIVATE
    day01
    #day02
)


add_subdirectory(day01)
#add_subdirectory(day02)