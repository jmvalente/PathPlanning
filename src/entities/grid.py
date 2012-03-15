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
        #If a neighbor is an obstacle then it really isn't a good neighbor, is it?
        for neighbor in set(neighbors):
            nRow, nCol = neighbor
            if self.map[nRow][nCol] == 'X':
                neighbors.remove(neighbor)
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