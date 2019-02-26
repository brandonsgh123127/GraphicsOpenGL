import glfw
import time
#import PyOpenGL
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.locals import *
import ctypes

class ShapesDraw(object):
    def __init__(self):
        identity = ''#identifies shape

    Vertices = (())
    Edges = (())
    Colors = (())
    pos = (())
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

        self.Colors = ((1,0,0),
                       (0, 1, 0),
                       (0, 0, 1),
                       (0, 1, 0),
                       (1, 1, 1),
                       (0, 1, 1),
                       (1, 0, 0),
                       (0, 1, 0),
                       (0, 0, 1),
                       (1, 0, 0),
                       (1, 1, 1),
                       (0, 1, 1))
        glBegin(GL_LINES)  # Treats as independent line segments
        for edge in self.Edges:  # Loop that will connect vertices and create edges
            x = 0
            for vertex in edge:
                x= x+1
                glColor3fv(self.Colors[x])
                glVertex3fv(self.Vertices[vertex])  # print("vertex: ",vertex)
        glEnd()

    def Rectangle(self, width, height):
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
    def getObjDim(self):
        return (())

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


def drawGLScene(f):
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    #glRotatef(1, -0, f,f)
    print("In here!")
    glPopMatrix()





def main():
    pygame.init()
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    display = (screensize[0], screensize[1])
    isTrue = True
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    # field of view y, x direction fov, closest edge, furthest edge
    glMatrixMode(GL_PROJECTION);
    gluPerspective(90, (display[0] / display[1] + 0.66), 0.3, 50.0)  # fovy, aspect, znear, zfar
    glTranslatef(0.5, -1, -8)

    while isTrue:
        glPushMatrix()
        glLoadIdentity()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    glPopMatrix()
                    glTranslatef(1,0,0)
                    glPushMatrix()
                if event.key == pygame.K_LEFT:
                    glPopMatrix()
                    glTranslatef(-1,0,0)
                    glPushMatrix()
                if event.key == pygame.K_UP:
                    glPopMatrix()
                    glTranslatef(0,1,0)
                    glPushMatrix()
                if event.key == pygame.K_DOWN:
                    glPopMatrix()
                    glTranslatef(0,-1,0)
                    glPushMatrix()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_position = pygame.mouse.get_pos()
                print("mouse pos: ", mouse_position[0],mouse_position[1])
                glPopMatrix()
                glRotatef(2,mouse_position[1]-(display[1]/2),mouse_position[0]-
                          (display[0]/2),1)
                print("rotated:  ",mouse_position[0]-(display[0]/2),
                                    mouse_position[1]-(display[1]/2)),
                glPushMatrix()
        glPopMatrix()
        #glPushMatrix()
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        cube = ShapesDraw()
        cube.Cube()


        rectangle = ShapesDraw()
        rectangle.Rectangle()


        pyramid = ShapesDraw()
        pyramid.Pyramid()

        pygame.display.flip()
        pygame.time.wait(10)

        #print(glGetDoublev(GL_MODELVIEW_MATRIX))


main()
