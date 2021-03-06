from random import randint
from grid import Grid
import logging
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
        self.bestPath = ''
        Robot.population += 1
        
    def __str__(self):
        #Tell me about your mother.
        return "ID : {id!s}\nStart: {st!s}\nGoal: {gl!s}\nColor: {cl!s}\nBest Path: {bp}\n" \
                .format(id=self.ID, st=self.start, gl=self.goal, cl=self.color, bp=self.bestPath)
                
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
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        return str((r, g, b))
    
    @staticmethod
    def genWaypoints(obstacles):
        start = Robot.genWaypoint("start", obstacles)
        goal = Robot.genWaypoint("goal", obstacles)
        return start, goal
    
    @staticmethod
    def genWaypoint(kind, obstacles):
        height, width = Grid.size
        p = (randint(1, height) - 1, randint(1, width) - 1)
        if kind == "start":
            if p in Robot.startNodes or p in obstacles:
                return Robot.genWaypoint("start", obstacles)
            else: return p
        elif kind == "goal":
            if p in Robot.goalNodes or p in obstacles:
                return Robot.genWaypoint("goal", obstacles)
            else: return p
            
    @staticmethod
    def pathToDirection(path):
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
    def getCollisionPoint(pathA, pathB, kind=1):
        if kind == 1:
            if len(pathA) > len(pathB):
                for iNode in range(len(pathB)):
                    if pathA[iNode] == pathB[iNode]:
                        return iNode
                    else:
                        for iNode in range(len(pathA)):
                            if pathA[iNode] == pathB[iNode]:
                                return iNode
            return False #If there are no collisions, return False to let us know things are OK.
        if kind == 2:
            if len(pathA) > len(pathB):
                for iNode in range(len(pathB) - 1):
                    if pathA[iNode] == pathB[iNode + 1] and pathA[iNode + 1] == pathB[iNode]:
                        return iNode + 1
            else:
                for iNode in range(len(pathA) - 1):
                    if pathA[iNode] == pathB[iNode + 1] and pathA[iNode + 1] == pathB[iNode]:
                        return iNode + 1
            return False
    
    @staticmethod
    def getBestPath(robotList):
        robotPathPairs = set([(0, 0)]) #Initialize the set of pairs with Robot 0, Path 0
        robotIndex = 1
        pathIndex = 0 
        while robotIndex < len(robotList):
            badPath = False
            while True:
                badPath = False
                for pair in robotPathPairs:
                    try:
                        collisionPoint = Robot.getCollisionPoint(robotList[pair[0]].paths[pair[1]],
                                                                 robotList[robotIndex].paths[pathIndex])
                    except IndexError:
                        pathIndex = 0
                        badPath = False
                        break
                    else:
                        if collisionPoint:
                            logging.warning(Robot.collisionDetails(pair, (robotIndex, pathIndex), collisionPoint))
                            Robot.addWait(robotList[robotIndex], pathIndex, collisionPoint)
                            pathIndex += 1 
                            badPath = True
                            break
                if not badPath:
                    logging.info("No collision, adding Robot {0}, Path {1} to set".format(robotIndex, pathIndex))
                    robotPathPairs.add((robotIndex, pathIndex))
                    pathIndex = 0
                    robotIndex += 1
                    badPath = False
                    break
            
        #Now to update each robot with the best path
        for pair in robotPathPairs:
                r, p = pair
                robotList[r].bestPath = Robot.pathToDirection(robotList[r].paths[p])
        
    @staticmethod
    def collisionDetails(pathA, pathB, point):
        aR, aP = pathA #First robot, path
        bR, bP = pathB #Second robot,path
        message = "***Collision found at step {0} between R_{1}.path[{2}] and R_{3}.path[{4}]. Incrementing path index!***"
        return message.format(point, aR, aP, bR, bP)
    
    @staticmethod
    def addWait(robot, path, index):
        value = robot.paths[path][index - 1]
        robot.paths[path].insert(index, value)
        
    @staticmethod
    
    ###Walk Around function that will probably never be implemented
    def addWalkAround(robot, path, index):
        value = robot.paths[path][index - 1]
        prev = robot.paths[path][index - 2]
        direction = Robot.pathToDirection([prev, value])
        if direction == "N" or direction == "S":
            #Add east or west wait
            pass
        elif direction == "E" or direction == "W":
            #Add North or South wait
            pass
        elif direction == "H":
            #Try to move one direction
            pass
