import glfw
import time
#import PyOpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *

class ShapesDraw(object):
    def __init__(self):
        print("")
        identity = ''#identifies shape

    Vertices = (())
    Edges = (())
    #  Used to get viewpoint of vertices...  To be implemented...
    viewPoint = []

    viewPoint = [-5, 2, -1, 1]
    for edge in Edges:
        for vertex in edge:
            for point in vertex:
                print(point)
                Vertices[vertex[point]] = Vertices[vertex[point]] * viewPoint[0]

#,xpos,ypos,zpos,(width,height)
    def Cube(self):
        self.identity = 'Cube'
        self.Vertices = ((2, -2, -2),  # 0, x 2, y -2 to 2, z -2  BOTTOM CORNER
                    (2, 2, -2),  # 1 TOP CORNER
                    (-2, 2, -2),  # 2 TOP CORNER
                    (-2, -2, -2),  # 3 BOTTOM CORNER
                    (2, -2, 2),  # 4 BOTTOM CORNER
                    (2, 2, 2),  # 5  TOP CORNER
                    (-2, -2, 2),  # 6  BOTTOM CORNER
                    (-2, 2, 2)  # 7   TOP CORNER
                    )
        self.Edges = ((0, 1),  # bottom to top
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
        glBegin(GL_LINES)  # Treats as independent line segments
        for edge in self.Edges:  # Loop that will connect vertices and create edges
            for vertex in edge:
                glVertex3fv(self.Vertices[vertex])  # print("vertex: ",vertex)
        glEnd()
        glPushMatrix()

    def Rectangle(self):
        self.identity = 'Rectangle'

        self.Vertices = ((4, -1, -2),  # 0, x 2, y -2 to 2, z -2  BOTTOM CORNER
                    (4, 1, -2),  # 1 TOP CORNER
                    (-4, 1, -2),  # 2 TOP CORNER
                    (-4, -1, -2),  # 3 BOTTOM CORNER
                    (4, -1, 2),  # 4 BOTTOM CORNER
                    (4, 1, 2),  # 5  TOP CORNER
                    (-4, -1, 2),  # 6  BOTTOM CORNER
                    (-4, 1, 2)  # 7   TOP CORNER
                    )
        self.Edges = ((0, 1),  # bottom to top
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
        glBegin(GL_LINES)  # Treats as independent line segments
        for edge in self.Edges:  # Loop that will connect vertices and create edges
            for vertex in edge:
                glVertex3fv(self.Vertices[vertex])  # print("vertex: ",vertex)
        glEnd()

    #xpos, ypos, zpos, (base, width, height)
    def Pyramid(self):
        self.identity = 'Pyramid'

        self.Vertices = ((0, 1.5, 0),  # 1  TOP
                        (2, -2, -2),  # 3
                        (2, -2, 2),  # 2
                        (-2, -2, -2),  # 4
                        (-2, -2, 2),  # 5
                        )
        self.Edges = ((0, 1),  # Top connecting down
                     (0, 2),  #
                     (0, 3),
                     (0, 4),  #

                     (1, 3),  # 3 to 4
                     (1, 2),  # 3 to 2

                     (4, 3),  #
                     (4, 2),  #
                      )
        glBegin(GL_LINES)  # Treats as independent line segments
        for edge in self.Edges:
            for vertex in edge:
                glVertex3fv(self.Vertices[vertex])
        glEnd()

    def rotRight(self):
        if (self.identity == 'Cube'):
            self.drawGLScene(3)
    def drawGLScene(self,int):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        glRotatef(3, -3, 3,3)
        print("In here!")
        glPopMatrix()





def main():
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
        cube = ShapesDraw()
        cube.Cube()
        rectangle = ShapesDraw()
        rectangle.Rectangle()
        pyramid = ShapesDraw()
        pyramid.Pyramid()

        cube.rotRight()
        pygame.display.flip()
        pygame.time.wait(2)


main()
