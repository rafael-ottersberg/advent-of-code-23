add_library( day02 day02.cpp )

target_include_directories(day02 PRIVATE ${CMAKE_CURRENT_LIST_DIR})

target_link_libraries( day02 TBB::tbb )