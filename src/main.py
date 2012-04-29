#!/usr/bin/python
#James Valente
#CSC500 - Path Planning for Autonomous Mobile Robots

from entities.grid import Grid
from entities.robot import Robot
from conversion.jsonf import expJSON
from time import time

def main():
    
    numRobots = 10
    size = (50, 50) #(Rows, Columns)
    obstacles = set([(3, 3), (25, 25), (20, 40)])
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
        
    #Save the output as a JSON file in the format 'robots_%EPOCHTIME%.json
    saveTo = "robots_{0}.json".format((int(time())))
    expJSON(roboArray, obstacles, size, True, saveTo)
    
def makeRobots(size, numRobots, obstacles):
    
    arr = []
    for i in range(numRobots):
        start, goal = Robot.genWaypoints(obstacles)
        arr.append(Robot(start, goal))
    return  arr

    
if __name__ == '__main__':
    main()    
