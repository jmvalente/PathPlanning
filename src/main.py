#!/usr/bin/python
#James Valente
#CSC500 - Path Planning for Autonomous Mobile Robots

from entities.grid import Grid
from entities.robot import Robot
from conversion.jsonf import expJSON
from random import randint
from time import time

def main():
    
    numRobots = 10
    numObstacles = 15
    size = (50, 50) #(Rows, Columns)
    obstacles = makeObstacles(size, numObstacles)
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
def makeObstacles(size, numObstacles):
    height, width = size
    oSet = set()
    for i in range(numObstacles):
        o = (randint(1, height) - 1, randint(1, width) - 1)
        oSet.add(o)
    return oSet 
    
if __name__ == '__main__':
    main()    
