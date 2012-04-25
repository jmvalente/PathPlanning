#!/usr/bin/python
#James Valente
#CSC500 - Path Planning for Autonomous Mobile Robots

from entities.grid import Grid
from entities.robot import Robot

def main():
    
    numRobots = 10
    size = (50, 50) #(Rows, Columns)
    obstacles = set()
    Grid.size = size
    roboArray = makeRobots(size, numRobots, obstacles)
    world = Grid(size, roboArray, obstacles) 
    print world
    for robot in roboArray:
        robot.graph = world.buildGraph(robot)
        robot.paths = robot.findPaths(robot.graph, robot.start, robot.goal)
    Robot.getBestPath(roboArray)
    for robot in roboArray:
        print robot
          
def makeRobots(size, numRobots, obstacles):
    
    arr = []
    for i in range(numRobots):
        start, goal = Robot.genWaypoints(obstacles)
        arr.append(Robot(start, goal))
    return  arr

    
if __name__ == '__main__':
    main()    
