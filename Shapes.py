import math

import time
#import PyOpenGL
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
#import pygame
#from pygame.examples.prevent_display_stretching import user32
#from pygame.locals import *
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
                glColor3fv(self.Colors[x])
                glVertex3fv(self.Vertices[vertex])  # print("vertex: ",vertex)
        glEnd()
    def movePixels(self):
        glBegin(GL_LINES)



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
        self.updateColor()
class Rectangle(Shapes):
    def __init__(self, len, width, height):
        self.identity = 'Rectangle'
        self.Vertices = np.array([[len/2, height/2, -(width/2)],  # 0, x 2, y -2 to 2, z -2  BOTTOM CORNER
                    [len/2, -(height/2), -(width/2)],  # 1 TOP CORNER
                    [-(len/2), height/2, -(width/2)],  # 2 TOP CORNER
                    [len/2, -(height/2), (width/2)],  # 3 BOTTOM CORNER
                    [-(len/2), -(height/2), -(width/2)],  # 4 BOTTOM CORNER
                    [len/2, (height/2), (width/2)],  # 5  TOP CORNER
                    [-(len/2), -(height/2), (width/2)],  # 6  BOTTOM CORNER
                    [-(len/2), (height/2), (width/2)]]  # 7   TOP CORNER
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
        self.update()
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
                     [1, 2],  # 3 to 2

                     [4, 3],  #
                     [4, 2]],  #
                      )

        self.update()




