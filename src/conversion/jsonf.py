import tocartesian
def expJSON(robotList, obstacleList, size, writeFile=True):
    import json
    rJSON = ''
    oJSON = ''
    #Create JSON for size
    sJSON = ''
    for robot in robotList:
        cStart = str(tocartesian.convertPoint(robot.start, size))
        cGoal = str(tocartesian.convertPoint(robot.goal, size))
        #Create JSON for Robot, write to rJSON
    for obstacle in obstacleList:
        cObst = str(tocartesian.convertPoint(obstacle, size))
        #Create JSON for Osbtacles
    #Combine JSON for size, robot list, and obstacle list
    output = ''
    if writeFile:
        #write to file
        pass
    return output

def importJSON(fp):
    import json
    rawJSON = json.load(open(fp))
    robotList = rawJSON["Robots"]
    obstList = rawJSON["Obstacles"]
    verticalSize = rawJSON["Size"]["Rows"] / 2  # Size includes -n...n
    horizontalSize = rawJSON["Size"]["Cols"] / 2
    return [robotList, obstList, verticalSize, horizontalSize]
