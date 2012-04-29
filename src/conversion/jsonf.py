import tocartesian
def expJSON(robotList, obstacleList, size, writeFile=False, fileName='robots.json'):
    import json
    rJSON = {}
    #Create JSON for size
    sJSON = dict([("Rows", int(size[0])), ("Columns", int(size[1]))])
    for robot in robotList:
        cStart = str(tocartesian.convertPoint(robot.start, size))
        cGoal = str(tocartesian.convertPoint(robot.goal, size))
        rJSON[str(robot.ID)] = {}
        rJSON[str(robot.ID)]['start'] = cStart
        rJSON[str(robot.ID)]['goal'] = cGoal
        rJSON[str(robot.ID)]['color'] = robot.color
        rJSON[str(robot.ID)]['path'] = robot.bestPath
        #Create JSON for Robot, write to rJSON
    cObstacles = []
    for obstacle in obstacleList:
        cObst = str(tocartesian.convertPoint(obstacle, size))
        cObstacles.append(cObst)
    #Combine JSON for size, robot list, and obstacle list
    outputDict = dict([("Size", sJSON), ("Robots", rJSON), ("Obstacles", cObstacles)])
    outputJSON = json.dumps(outputDict, sort_keys=True, indent=4)
    if writeFile:
        outputFile = open(fileName, "w")
        outputFile.writelines(outputJSON)
        outputFile.close
        #write to file
        pass
    print outputJSON

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
    #For these next few lines we need to convert the strings back into tuples
    robotDict = rawJSON["Robots"]
    for robot in robotDict:
        robotDict[robot]['start'] = eval(robotDict[robot]['start'])
        robotDict[robot]['goal'] = eval(robotDict[robot]['goal'])
        robotDict[robot]['color'] = eval(robotDict[robot]['color'])
    obstList = [eval(obs) for obs in rawJSON["Obstacles"]]
    
    verticalSize = rawJSON["Size"]["Rows"] / 2  # Size includes -n...n
    horizontalSize = rawJSON["Size"]["Columns"] / 2
    return [robotDict, obstList, verticalSize, horizontalSize]
