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
    
    