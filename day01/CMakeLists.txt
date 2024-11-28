add_library( day01 day01.cpp )

target_include_directories(day01 PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries( day01 TBB::tbb )