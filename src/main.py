#!/usr/bin/python
#James Valente
#CSC500 - Path Planning for Autonomous Mobile Robots

from random import randint

def main():
    numRobots = 10
    size = (50,50) #(Rows, Columns)
    obstacles = []
    Robot.size = size
    roboArray = makeRobots(size,numRobots)
    world = Grid(size, roboArray, obstacles) 
    print world
    for robot in roboArray:
        print robot
        
def makeRobots(size, numRobots):
    height, width = size
    arr = []
    for i in range(numRobots):
        start = (randint(1,height)-1, randint(1,width)-1) #Subtracting 1 because arrays are indexed 0...n-1. 
        goal = (randint(1,height)-1, randint(1,width)-1)
        arr.append(Robot(start,goal))
    return  arr

def getNeighborList(size,point):
    row,col = point
    maxX = size[1] - 1
    maxY = size[0] - 1
    w = (row,col - 1)
    e = (row, col + 1)
    n = (row - 1, col)
    s = (row + 1, col)
    neighbors = [n,w,e,s]
    #Less neighbors if we are checking a node at a north/south edge, a east/west edge
    if row == 0 or row == maxY:
        neighbors.remove(n if row == 0 else s) 
    if col == 0 or col == maxX:
        neighbors.remove(w if col == 0 else e)
    return neighbors


#Create the robot objects
class Robot:
    
    population = 0 #Keep track of how many robots exist, useful for assigning ID.
    #We should keep a list of occupied start and end nodes so we don't give two robots the same point
    startList = []
    goalList = []
    
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.color = self.genColor()
        self.ID = 'R_' + str(Robot.population)
        Robot.population +=1
        
    def __str__(self):
        #Tell me about your mother.
        return "ID : {id!s}\nStart: {st!s}\nGoal: {gl!s}\nColor: {cl!s}\n" \
                .format(id=self.ID, st=self.start, gl=self.goal, cl=self.color)
                
    @staticmethod
    def genColor():
        x = randint(0, 16777215)
        return hex(x)
    
    def wavefront(self, start, goal):
        #Get Neighbors of Goal
        val = 1
        nodesToCheck = getNeighborList(self.size,goal)
        #while not at start
            #Assign values to each of the neighbors
            #Get neighbors of neighbors
            #Remove current neighbors from list
            #value ++
        pass

    
#Create the grid used by all the robots
class Grid():
    
    def __init__(self,size, robotList, obstacleList):
        self.size = size
        self.rows = self.size[0]
        self.cols = self.size[1]
        self.robots = robotList
        self.obstacles = obstacleList
        self.map = [[{} for col in range(self.cols)] for row in range(self.rows)]
        self.populateGrid()
    
    def __str__(self):
        return "The world is a {0[0]!s}x{0[1]!s} grid home to {1!s} robots with {2!s} obstacles\n"\
            .format(self.size, len(self.robots), len(self.obstacles))

    def populateGrid(self):
        #Pre-wavefront grid with start and goals marked
        for robot in self.robots:
            gRow, gCol = robot.goal
            sRow, sCol = robot.start
            for row in range(self.rows):
                for col in range(self.cols):
                    self.map[row][col][robot.ID] = 0
            self.map[gRow][gCol][robot.ID] = 'G'
            self.map[sRow][sCol][robot.ID] = 'S'
            #Block off obstacles 
            for obstacle in self.obstacles:
                oRow, oCol = obstacle
                self.map[oRow][oCol] = 'X'

    def checkPoint(self, row, col):    
        return self.map[row][col] #Find the value of a node after wavefront is run.
    
    def printGrid(self, robot):
        robotID = robot.ID
        gs = ''
        for row in range(self.rows):
            for col in range(self.cols):
                gs+= str(self.map[row][col][robotID])
            gs+='\n'
        return gs
    
if __name__ == '__main__':
    main()    