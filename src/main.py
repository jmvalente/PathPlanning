#!/usr/bin/python
#James Valente
#CSC500 - Path Planning for Autonomous Mobile Robots

#########################
#*Create Arguments for: #
#-Size of Grid          #
#-List of Robots        #
#-List of Obstacles     #
#########################

def main():
    numRobots = 10
    size = (25,25)
    print "Finding paths for " + str(numRobots) + \
        " robots on a grid size of " + str(size)
    y = Robot(2,1)
    print y
    
def makeRobots(size):
    arr = []
    for robot in range():
        arr[robot] = Robot(1,1)
    return  arr

    return    
def wavefront():
    #Placeholder for wavefront algorithm
    return
#Create the robot objects
class Robot:
    def __init__(self, start, goal):
        self.start = start
        self.goal = goal
        self.color = self.genColor()
        self.matrix = 0  # Todo, implement matrix
    def checkPoint(self, row, col):    
            return #
    def __str__(self):
        return "Start: " + str(self.start) + "\nGoal: " + str(self.goal) \
             + "\nColor: " + str(self.color)           
    @staticmethod
    def genColor():
        from random import randint
        x = randint(0, 16777215)
        return hex(x)
class Grid:
    def __init__(self, rows, cols, obst): 
        self.rows = rows
        self.cols = cols
        self.obst = obst      
    
if __name__ == '__main__':
    size = (25,25)
    main()    