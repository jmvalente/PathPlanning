#!/usr/bin/python
#James Valente
#CSC500 - Path Planning for Autonomous Mobile Robots

from entities.grid import Grid
from entities.robot import Robot


def main():
    
    numRobots = 10
    size = (5,5) #(Rows, Columns)
    obstacles = set()
    Grid.size = size
    roboArray = makeRobots(size,numRobots)
    world = Grid(size, roboArray, obstacles) 
    print world
    for robot in roboArray:
        print robot
        print world.printGrid(robot)
        
def makeRobots(size, numRobots):
    
    arr = []
    for i in range(numRobots):
        start, goal = Robot.genWaypoints()
        arr.append(Robot(start,goal))
    return  arr

    
if __name__ == '__main__':
    main()    