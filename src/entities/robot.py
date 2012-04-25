from random import randint
from grid import Grid
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
        self.bestPath = []
        Robot.population += 1
        
    def __str__(self):
        #Tell me about your mother.
        return "ID : {id!s}\nStart: {st!s}\nGoal: {gl!s}\nColor: {cl!s}\n" \
                .format(id=self.ID, st=self.start, gl=self.goal, cl=self.color)
                
    def findPaths(self, graph, start, goal, path=[]):
        path = path + [start]
        paths = []        
        if start == goal:
            return [path]
        if not graph.has_key(str(start)):
            return []

        for node in graph[str(start)]:
            if node not in path:
                newpaths = self.findPaths(graph, node, goal, path)
                for newpath in newpaths:
                    paths.append(newpath)
                    if len(paths) > 9:
                        return paths
        return paths
            
    @staticmethod
    def genColor():
        x = randint(0, 16777215)
        return hex(x)
    
    @staticmethod
    def genWaypoints():
        height, width = Grid.size
        start = (randint(1, height) - 1, randint(1, width) - 1)
        goal = (randint(1, height) - 1, randint(1, width) - 1)
        return start, goal
    
    def pathToDirection(self, path):
        directions = ''
        for step in range(len(path) - 1):
            if path[step][0] > path[step + 1][0]:
                directions += "N"
            elif path[step][0] < path[step + 1][0]:
                directions += "S"
            elif path[step][0] == path[step + 1][0]:
                if path[step][1] > path[step + 1][1]:
                    directions += "W"
                elif path[step][1] < path[step + 1][1]:
                    directions += "E"
                elif path[step][1] == path[step + 1][1]:
                    directions += "H"
        return directions
    
    @staticmethod
    def getCollisionPoint(pathA, pathB):
        if len(pathA) > len(pathB):
            for iNode in range(len(pathB)):
                if pathA[iNode] == pathB[iNode]:
                    return iNode
        else:
            for iNode in range(len(pathA)):
                if pathA[iNode] == pathB[iNode]:
                    return iNode
        return False #If there are no collisions, return False to let us know things are OK.
    
    @staticmethod
    def getBestPath(robotList):
        robotPathPairs = set([(0, 0)]) #Initialize the set of pairs with Robot 0, Path 0
        robotIndex = 1
        pathIndex = 0 
        while robotIndex < len(robotList):
            badPath = False
            while True:
                for pair in robotPathPairs:
                    try:
                        collisionPoint = Robot.getCollisionPoint(robotList[pair[0]].paths[pair[1]], 
                                                                 robotList[robotIndex].paths[pathIndex])
                    except IndexError:
                        print "Resetting path index"
                        pathIndex = 0
                        badPath = False
                        break
                    else:
                        if collisionPoint:
                            print Robot.collisionDetails(pair, (robotIndex, pathIndex), collisionPoint)
                            robotList[robotIndex].paths[pathIndex].insert(collisionPoint, robotList[robotIndex].paths[pathIndex][collisionPoint - 1])
                            #Robot.addWait(robotList[robotIndex], pathIndex, collisionPoint)
                            pathIndex += 1 
                            badPath = True
                            break
                if not badPath:
                    print "No collision, adding Robot {0}, Path {1} to set".format(robotIndex, pathIndex)
                    robotPathPairs.add((robotIndex, pathIndex))
                    pathIndex = 0
                    robotIndex += 1
                    badPath = False
                    break
            
        #Now to update each robot with the best path
        for pair in robotPathPairs:
                r, p = pair
                robotList[r].bestPath = robotList[r].paths[p]
        print "Done"
    @staticmethod
    def collisionDetails(pathA, pathB, point):
        aR, aP = pathA #First robot, path
        bR, bP = pathB #Second robot,path
        message = "***Collision found at step {0} between R_{1}.path[{2}] and R_{3}.path[{4}]. Incrementing path index!***"
        return message.format(point, aR, aP, bR, bP)
    @staticmethod
    def addWait(robot, path, index):
        value = robot.paths[path][index-1]
        robot.paths[path].insert(index, value)