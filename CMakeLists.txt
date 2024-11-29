cmake_minimum_required(VERSION 3.29)

# Activate Sie Hot Reload for MSVC-Compiler.
if (POLICY CMP0141)
  cmake_policy(SET CMP0141 NEW)
  set(CMAKE_MSVC_DEBUG_INFORMATION_FORMAT "$<IF:$<AND:$<C_COMPILER_ID:MSVC>,$<CXX_COMPILER_ID:MSVC>>,$<$<CONFIG:Debug,RelWithDebInfo>:EditAndContinue>,$<$<CONFIG:Debug,RelWithDebInfo>:ProgramDatabase>>")
endif()

project(AOC23)

set(CMAKE_CXX_STANDARD 23)
set(CMAKE_CXX_STANDARD_REQUIRED True)

# Add compiler flags for bounds checking and other debug options in Debug mode
if (CMAKE_CXX_COMPILER_ID STREQUAL "GNU")
    set(CMAKE_CXX_FLAGS_DEBUG 
    "${CMAKE_CXX_FLAGS_DEBUG} -fsanitize=undefined -fno-omit-frame-pointer -Wall -Wextra -Wpedantic -Og -fstack-protector -DDEBUG -D_GLIBCXX_DEBUG")
    set(CMAKE_LINKER_FLAGS_DEBUG "${CMAKE_LINKER_FLAGS_DEBUG} -fsanitize=address,undefined")
#elseif (CMAKE_CXX_COMPILER_ID STREQUAL "MSVC")
#    set(CMAKE_CXX_FLAGS_DEBUG 
#    "${CMAKE_CXX_FLAGS_DEBUG} /ZI /INCREMENTAL /Od /Wall /DDEBUG")
#    set(CMAKE_LINKER_FLAGS_DEBUG "${CMAKE_LINKER_FLAGS_DEBUG} /DEBUG")
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
    day02
    day03
)


add_subdirectory(day01)
add_subdirectory(day02)
add_subdirectory(day03)