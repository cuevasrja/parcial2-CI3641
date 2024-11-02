# Variables
CXX = g++
CXXFLAGS = -Wall -Wextra -std=c++17

PART_B = partb.cpp
PART_C = partc.cpp

# Targets
all: partb partc

partb: $(PART_B)
	$(CXX) $(CXXFLAGS) $(PART_B) -o partb.out

partc: $(PART_C)
	$(CXX) $(CXXFLAGS) $(PART_C) -o partc.out

clean:
	rm -f *.out

# Phony targets
.PHONY: all partb partc clean
