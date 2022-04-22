cmake_minimum_required(VERSION 3.17)
project(Helix C)


file(GLOB_RECURSE SRCS real/*.c pub/*.c)

set(CMAKE_C_STANDARD 99)
include_directories(real)
add_executable(Helix main.c mp3tabs.c mp3dec.c ${SRCS} pre/play.c pre/play.h)