#!/usr/bin/python
#James Valente
#CSC500 - Path Planning for Autonomous Mobile Robots

from random import randint

def main():
    numRobots = 10
    size = (50,50) #(Rows, Columns)
    Robot.size = size
    print "Finding paths for {0} robots on a {1[0]!s}x{1[1]!s} grid.\n".format(numRobots, size)
    roboArray = makeRobots(size,numRobots)
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
    
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.color = self.genColor()
        self.matrix = self.initGrid(self.size, self.start, self.goal)
        self.ID = Robot.population
        Robot.population +=1
        
    def checkPoint(self, row, col):    
            return self.matrix[row][col] #Find the value of a node after wavefront is run.
        
    def __str__(self):
        #Tell me about your mother.
        return "ID : {id!s}\nStart: {st!s}\nGoal: {gl!s}\nColor: {cl!s}\n" \
                .format(id=self.ID, st=self.start, gl=self.goal, cl=self.color)
                
    @staticmethod
    def genColor():
        x = randint(0, 16777215)
        return hex(x)
    
    def initGrid(self, size, start, goal):
        #Create Grid first
        height, width = (size)
        sr, sc = start
        gr, gc = goal
        grid = [[0] * width for i in range(height)]
        grid[sr][sc] = "S"
        grid[gr][gc] = "G"
        return grid
    
    def gridText(self):
        height = self.size[0]
        width = self.size[1]
        grid = self.matrix
        gs = ''
        for row in range(height):
            for col in range(width):
                gs+= str(grid[row][col])
            gs+="\n"
        return gs
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

if __name__ == '__main__':
    main()    