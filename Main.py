import glfw
import time
#import PyOpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *


class vals:
    # vertex has 3 points, x, y and z, so 0, 2, 6, and 5 are starting edges for line

    #  *******************************
    #  BROKEN INIT NO WORKING MATRICES
    #  *******************************
    def __init__(this):
        cubeVertices = ((2, -2, -2),  # 0, x 2, y -2 to 2, z -2  BOTTOM CORNER
                        (2, 2, -2),  # 1 TOP CORNER
                        (-2, 2, -2),  # 2 TOP CORNER
                        (-2, -2, -2),  # 3 BOTTOM CORNER
                        (2, -2, 2),  # 4 BOTTOM CORNER
                        (2, 2, 2),  # 5  TOP CORNER
                        (-2, -2, 2),  # 6  BOTTOM CORNER
                        (-2, 2, 2)  # 7   TOP CORNER
                        )
        # Will be used to draw specific vertices, position in array...0,1... 0 , 3...
        cubeEdges = ((0, 1),  # bottom to top
                     (0, 3),  # bottom to bottom
                     (0, 4),  # bottom to bottom

                     (2, 1),  # top to top
                     (2, 3),  # top to bottom
                     (2, 7),  # top to top

                     (6, 3),  # bottom to bottom
                     (6, 4),  # bottom to bottom
                     (6, 7),  # bottom to top

                     (5, 1),  # top to top
                     (5, 4),  # top to bottom
                     (5, 7)  # top to top
                     )
        triangleVertices = ((0, 1.5, 0),  # 1  TOP
                            (2, -2, -2),  # 3
                            (2, -2, 2),  # 2
                            (-2, -2, -2),  # 4
                            (-2, -2, 2),  # 5
                            )
        triangleEdges = ((0, 1),  # Top connecting down
                         (0, 2),  #
                         (0, 3),
                         (0, 4),  #

                         (1, 3),  # 3 to 4
                         (1, 2),  # 3 to 2

                         (4, 3),  #
                         (4, 2),  #
                         )
        #  Used to get viewpoint of vertices...  To be implemented...
        viewPoint = []

        viewPoint=[-5,2,-1,1]
        for edge in cubeEdges:
            for vertex in edge:
                for point in vertex:
                    print(point)
                    cubeVertices[vertex[point]]= cubeVertices[vertex[point]] * viewPoint[0]
    def Cube(this):
        glBegin(GL_LINES)  # Treats as independent line segments
        for edge in this.cubeEdges:  # Loop that will connect vertices and create edges
            for vertex in edge:
                glVertex3fv(this.cubeVertices[vertex])  # print("vertex: ",vertex)
        glEnd()
    def Triangle(this):
        glBegin(GL_LINES)  # Treats as independent line segments
        for edge in this.triangleEdges:
            for vertex in edge:
                glVertex3fv(this.triangleVertices[vertex])  # print("vertex: ",vertex)
        glEnd()


class runner:
    @staticmethod
    def main(this):
        pygame.init()
        display = (1200, 900)
        pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

        # field of view y, x direction fov, closest edge, furthest edge
        gluPerspective(90, (display[0] / display[1] + 0.66), 0.3, 50.0)  # fovy, aspect, znear, zfar
        glTranslatef(0.5, -1, -8)
        #glRotatef(30, 5, 10, 3)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            # glRotatef(1, 0, 1, 1)
            # glRotatef(1, 0, 0, 0)# slowly gets further away
            # glRotatef(1, 2, 0, 0)#rotates y
            # glRotatef(1, 0, 2, 0)#rotates x
            glRotatef(1, 0, 1, 0)
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            vals.Cube()
            vals.Triangle()
            pygame.display.flip()
            pygame.time.wait(2)


runner.main(None)
