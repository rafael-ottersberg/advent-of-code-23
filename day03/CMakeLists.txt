add_library( day03 day03.cpp )

target_include_directories(day03 PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries( day03 TBB::tbb )