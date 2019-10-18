import math
import time
#import PyOpenGL
import numpy as np
from OpenGL.GL import *
import ctypes



#**************************
#Class gives each object
# Main methods, such as:
#init values
#updating graphics
#updating color
#**************************
class Shapes:
    def __init__(self):
        print("New Shape Created!")
    def update(self):
        glBegin(GL_LINES)  # Treats as independent line segments
        for edge in self.Edges:
            for vertex in edge:
                glVertex3fv(self.Vertices[vertex])

        glEnd()

    def updateColor(self):
        glBegin(GL_LINES)  # Treats as independent line segments
        for edge in self.Edges:  # Loop that will connect vertices and create edges
            x = 0
            for vertex in edge:
                x = x + 1
                try:
                    glColor3fv(self.Colors[x])
                    glVertex3fv(self.Vertices[vertex])  # print("vertex: ",vertex)
                except:
                    glVertex3fv(self.Vertices[vertex])
        glEnd()
    def getIdentity(self):
        return self.identity
    def getVertices(self):
        return self.Vertices
    def getEdges(self):
        return self.Edges
    def setIdentity(self,name):
        self.identity = name
    def manipulateShape(self,arg1=None,arg2=None,arg3=None): # Manipulate the Position of Shape
        for vertex in self.Vertices:
            for i in range(0,1):
                vertex[i]+=arg1
                vertex[i+1] += arg2
                vertex[i+2] += arg3

class Cube(Shapes):
    #,xpos,ypos,zpos,(width,height)
    def __init__(self, x):
        self.identity = 'Cube'
        self.Vertices = np.array([[x, x, -x],  # 0, x 2, y -2 to 2, z -2  BOTTOM CORNER
                    [x, -x, -x],  # 1 TOP CORNER
                    [-x, x, -x],  # 2 TOP CORNER
                    [-x, -x, -x],  # 3 BOTTOM CORNER
                    [x, -x, x],  # 4 BOTTOM CORNER
                    [x, x, x],  # 5  TOP CORNER
                    [-x, -x, x],  # 6  BOTTOM CORNER
                    [-x, x, x]]  # 7   TOP CORNER
                    )
        self.Edges = np.array([[1, 0],  # bottom to top
                 [1, 3],  # bottom to bottom
                 [1, 4],  # bottom to bottom
                 [2, 0],  # top to top
                 [2, 3],  # top to bottom
                 [2, 7],  # top to top
                 [6, 3],  # bottom to bottom
                 [6, 4],  # bottom to bottom
                 [6, 7],  # bottom to top
                 [5, 0],  # top to top
                 [5, 4],  # top to bottom
                 [5, 7]  # top to top
                 ])

        self.Colors = np.array([[100,0,0],
                       [0, 100, 0],
                       [0, 0, 100],
                       [0, 100, 0],
                       [155, 155, 100],
                       [0, 155, 155],
                       [144, 0, 0],
                       [0, 144, 0],
                       [0, 0, 144],
                       [1, 0, 0],
                       [100, 1, 100],
                       [0, 100, 100]])
class Rectangle(Shapes):
    def __init__(self, len, width, height,x=None,y=None,z=None):
        self.identity = 'Rectangle'
        self.Vertices = np.array([[len/2+x, height/2+y, -(width/2)+z],  # 0, x 2, y -2 to 2, z -2  BOTTOM CORNER
                    [len/2+x, -(height/2)+y, -(width/2)+z],  # 1 TOP CORNER
                    [-(len/2)+x, height/2+y, -(width/2)+z],  # 2 TOP CORNER
                    [len/2+x, -(height/2)+y, (width/2)+z],  # 3 BOTTOM CORNER
                    [-(len/2)+x, -(height/2)+y, -(width/2)+z],  # 4 BOTTOM CORNER
                    [len/2+x, (height/2)+y, (width/2)+z],  # 5  TOP CORNER
                    [-(len/2)+x, -(height/2)+y, (width/2)+z],  # 6  BOTTOM CORNER
                    [-(len/2)+x, (height/2)+y, (width/2)+z]]  # 7   TOP CORNER
                    )
        self.Edges = np.array([[1, 0],  # bottom to top
                 [1, 4],  # bottom to bottom
                 [1, 3],  # bottom to bottom

                 [2, 0],  # top to top
                 [2, 4],  # top to bottom
                 [2, 7],  # top to top

                 [6, 4],  # bottom to bottom
                 [6, 3],  # bottom to bottom
                 [6, 7],  # bottom to top

                 [5, 0],  # top to top
                 [5, 3],  # top to bottom
                 [5, 7]]  # top to top
                 )
        self.Colors = np.array([[100, 200, 0],
                                [0, 100, 200],
                                [200, 0, 100],
                                [0, 100, 0],
                                [155, 0, 100],
                                [100, 155, 155],
                                [144, 0, 100],
                                [0, 144, 0],
                                [100, 100, 144],
                                [1, 0, 0],
                                [100, 1, 100],
                                [0, 0, 100]])
class Pyramid(Shapes):
    def __init__(self,len,width,height):
        self.identity = 'Pyramid'
        self.Vertices = np.array([[0, height, 0],  # 1  TOP
                        [len/2, 0, -(width/2)],  # 3
                        [len/2, 0, width/2],  # 2
                        [-(len/2), 0, -(width/2)],  # 4
                        [-(len/2), 0, (width/2)]],  # 5
                        )
        self.Edges = np.array([[0, 1],  # Top connecting down
                     [0, 2],  #
                     [0, 3],
                     [0, 4],  #
                     [1, 3],  # 3 to 4
                     [1, 2],  # 3 to
                     [4, 3],  #
                     [4, 2]],  #
                      )
class axes():
    def __init__(self):

        glBegin(GL_LINES)
        glLineWidth(4)
