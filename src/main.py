#!/usr/bin/python
#James Valente
#CSC500 - Path Planning for Autonomous Mobile Robots

from random import randint

def main():
    numRobots = 10
    size = (9,9) #(Rows, Columns)
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



#Create the robot objects
class Robot:
    
    population = 0 #Keep track of how many robots exist, useful for assigning ID.
    #We should keep a list of occupied start and end nodes so we don't give two robots the same point
    startNodes = ()
    goalNodes = ()
    
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.color = self.genColor()
        self.ID = 'R_' + str(Robot.population)
        self.paths = []
        Robot.population +=1
        
    def __str__(self):
        #Tell me about your mother.
        return "ID : {id!s}\nStart: {st!s}\nGoal: {gl!s}\nColor: {cl!s}\n" \
                .format(id=self.ID, st=self.start, gl=self.goal, cl=self.color)
                
    def findPaths(self):
        pass
            
    @staticmethod
    def genColor():
        x = randint(0, 16777215)
        return hex(x)
    @staticmethod
    def genWaypoints():
        height, width = Grid.size
        start = (randint(1,height)-1, randint(1,width)-1)
        goal = (randint(1,height)-1, randint(1,width)-1)
        return start,goal
    
    
#Create the grid used by all the robots
class Grid():
    
    def __init__(self, size, robotList, obstacleList):
        self.size = size
        self.rows = self.size[0]
        self.cols = self.size[1]
        self.robots = robotList
        self.obstacles = obstacleList
        self.map = [[{} for col in range(self.cols)] for row in range(self.rows)]
        self.populateGrid()
        self.wavefront()
    
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
    
    def getNeighborList(self, point):
        row,col = point
        maxX = self.size[1] - 1
        maxY = self.size[0] - 1
        w = (row,col - 1)
        e = (row, col + 1)
        n = (row - 1, col)
        s = (row + 1, col)
        neighbors = set([n,w,e,s])
        #Remove neighbors if we are checking a node at a north/south edge, a east/west edge
        if row == 0 or row == maxY:
            neighbors.remove(n if row == 0 else s) 
        if col == 0 or col == maxX:
            neighbors.remove(w if col == 0 else e)
        return neighbors
    
    def wavefront(self):
        for robot in self.robots:
            #In our implementation we start at the goal node and work back to start
            nodesToCheck = self.getNeighborList(robot.goal) 
            self.markNode(robot.goal, robot, 1)
            val = 2
            tempNeighbor = set()
            visited= set([robot.goal])
            
            while not set([robot.start]).issubset(nodesToCheck):
                for node in nodesToCheck:
                    self.markNode(node, robot, val)
                    tempNeighbor = tempNeighbor.union(self.getNeighborList(node)) 
                    visited.add(node)
                    
                nodesToCheck = set(tempNeighbor)
                nodesToCheck.difference_update(visited) #Remove any visited nodes from the list to check
                tempNeighbor = set() #Remove all elements from the running list for the next iteration
                val +=1
        
    def markNode(self, node, robot, value):
        nodeRow, nodeCol = node
        robotID = robot.ID
        self.map[nodeRow][nodeCol][robotID] = value
    
if __name__ == '__main__':
    main()    