#!/usr/bin/python
#James Valente
#CSC500 - Path Planning for Autonomous Mobile Robots

#########################
#*Create Arguments for: #
#-Size of Grid          #
#-List of Robots        #
#-List of Obstacles     #
#########################
from random import randint
def main():
    numRobots = 10
    size = (randint(10,51),randint(10,51))
    Robot.size = size
    print "Finding paths for {0} robots on a {1[0]!s}x{1[1]!s} grid.\n".format(numRobots, size)
    roboArray = makeRobots(size,numRobots)
    for robot in roboArray:
        print robot
        
def makeRobots(size, numRobots):
    height, width = size
    arr = []
    for i in range(numRobots):
        start = (randint(0,height), randint(0,width))
        goal = (randint(0,height), randint(0,width))
        arr.append(Robot(start,goal))
    return  arr
   
def wavefront():
    #Placeholder for wavefront algorithm
    pass
#Create the robot objects
class Robot:
    population = 0
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.color = self.genColor()
        self.matrix = self.makeGrid(self.size, self.start, self.goal)  # Todo, implement matrix
        self.ID = Robot.population
        Robot.population +=1
    def checkPoint(self, row, col):    
            return self.matrix[row][col]
    def __str__(self):
        return "ID : {id!s}\nStart: {st!s}\nGoal: {gl!s}\nColor: {cl!s}\n" \
                .format(id=self.ID, st=self.start, gl=self.goal, cl=self.color)                
    @staticmethod
    def genColor():
        x = randint(0, 16777215)
        return hex(x)
    def makeGrid(self, size, start, goal):
        #Create Grid first
        height, width = (size)
        sr, sc = start
        gr, gc = goal
        grid = [['?'] * width for i in range(height)]
        grid[sr-1][sc-1] = "S"
        grid[gr-1][gc-1] = "G"
        return grid
    
if __name__ == '__main__':
    main()    