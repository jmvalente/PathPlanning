import tocartesian
def expJSON(robotList, obstacleList, size, writeFile=True):
    import json
    rJSON = "Robots: "
    oJSON = "Obstacles: "
    #Create JSON for size
    sJSON = "Size: " + str(dict([("Rows", size[0]), ("Cols", size[1])]))
    for robot in robotList:
        cStart = str(tocartesian.convertPoint(robot.start, size))
        cGoal = str(tocartesian.convertPoint(robot.goal, size))
        #Create JSON for Robot, write to rJSON
    cObsticles = []
    for obstacle in obstacleList:
        cObst = str(tocartesian.convertPoint(obstacle, size))
        cObsticles.append(cObst)
    oJSON += str(cObsticles)
    #Combine JSON for size, robot list, and obstacle list
    output = ''
    if writeFile:
        #write to file
        pass
    return output

def importJSON(fp):
    """Read in a JSON file.
    
    Arguments:
    fp -- The file being imported
    
    Return a list containing a dictionary, a list, and two integers:
    robotDict -- Dictionary containing the ID, start, goal, color, and path of each robot.
    obstList -- List containing the coordinates of each obstacle.
    verticalSize -- Integer identifying the magnitude of the y-axis.
    horizontalSize -- Integer identifying the magnitude of the x-axis."""
    import json
    rawJSON = json.load(open(fp))
    robotDict = rawJSON["Robots"]
    obstList = rawJSON["Obstacles"]
    verticalSize = rawJSON["Size"]["Rows"] / 2  # Size includes -n...n
    horizontalSize = rawJSON["Size"]["Cols"] / 2
    return [robotDict, obstList, verticalSize, horizontalSize]
