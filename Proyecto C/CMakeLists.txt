cmake_minimum_required(VERSION 3.14)
project(badplat LANGUAGES C CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_path(RAYLIB_INCLUDE_DIR raylib.h PATHS /usr/local/include)
find_library(RAYLIB_LIBRARY NAMES raylib PATHS /usr/local/lib)

add_executable(${PROJECT_NAME} main.cpp)

target_include_directories(${PROJECT_NAME} PRIVATE ${RAYLIB_INCLUDE_DIR})


target_link_libraries(${PROJECT_NAME} PRIVATE 
    ${RAYLIB_LIBRARY} 
    GL       # OpenGL
    m        # Math library
    pthread  # POSIX threads
    dl       # Dynamic linking
    rt       # Real-time POSIX
    X11      # X11 Windowing system
)