#Panda's grid uses a Cartesian coordinate system with the origin, (0,0), being in the center.
#Because of this points must be converted from list indices of (row,col) to (x,y).
def convertPoint(point, size):
    
    row, col = point
    #We must output the points for use on a Cartesian coordinate system
    x = col - size[1]/2.0  # A grid with n columns spans from -(n/2) to (n/2)
    y = row - size[0]/2.0  # A grid with m rows spans from -(m/2) to (m/2)
    return (x,y)

def convertPath(path):
    pass