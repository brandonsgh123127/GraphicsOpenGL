import math

import glfw
import time
#import PyOpenGL
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
import pygame
from pygame.examples.prevent_display_stretching import user32
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
    def Cube(self, x):
        self.identity = 'Cube'
        self.Vertices = ((x, x, -x),  # 0, x 2, y -2 to 2, z -2  BOTTOM CORNER
                    (x, -x, -x),  # 1 TOP CORNER
                    (-x, x, -x),  # 2 TOP CORNER
                    (-x, -x, -x),  # 3 BOTTOM CORNER
                    (x, -x, x),  # 4 BOTTOM CORNER
                    (x, x, x),  # 5  TOP CORNER
                    (-x, -x, x),  # 6  BOTTOM CORNER
                    (-x, x, x)  # 7   TOP CORNER
                    )
        self.Edges = ((1, 0),  # bottom to top
                 (1, 3),  # bottom to bottom
                 (1, 4),  # bottom to bottom

                 (2, 0),  # top to top
                 (2, 3),  # top to bottom
                 (2, 7),  # top to top

                 (6, 3),  # bottom to bottom
                 (6, 4),  # bottom to bottom
                 (6, 7),  # bottom to top

                 (5, 0),  # top to top
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

    def Rectangle(self, len, width, height):
        self.identity = 'Rectangle'

        self.Vertices = ((len/2, height/2, -(width/2)),  # 0, x 2, y -2 to 2, z -2  BOTTOM CORNER
                    (len/2, -(height/2), -(width/2)),  # 1 TOP CORNER
                    (-(len/2), height/2, -(width/2)),  # 2 TOP CORNER
                    (len/2, -(height/2), (width/2)),  # 3 BOTTOM CORNER
                    (-(len/2), -(height/2), -(width/2)),  # 4 BOTTOM CORNER
                    (len/2, (height/2), (width/2)),  # 5  TOP CORNER
                    (-(len/2), -(height/2), (width/2)),  # 6  BOTTOM CORNER
                    (-(len/2), (height/2), (width/2))  # 7   TOP CORNER
                    )
        self.Edges = ((1, 0),  # bottom to top
                 (1, 4),  # bottom to bottom
                 (1, 3),  # bottom to bottom

                 (2, 0),  # top to top
                 (2, 4),  # top to bottom
                 (2, 7),  # top to top

                 (6, 4),  # bottom to bottom
                 (6, 3),  # bottom to bottom
                 (6, 7),  # bottom to top

                 (5, 0),  # top to top
                 (5, 3),  # top to bottom
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
    def Pyramid(self,len,width,height):
        self.identity = 'Pyramid'

        self.Vertices = ((0, height, 0),  # 1  TOP
                        (len/2, 0, -(width/2)),  # 3
                        (len/2, 0, width/2),  # 2
                        (-(len/2), 0, -(width/2)),  # 4
                        (-(len/2), 0, (width/2)),  # 5
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

    def getDimensions(self):#  length, width, height
        return ((abs(self.Vertices[0][0])+abs(self.Vertices[4][0])),(abs(self.Vertices[0][2])+(abs(self.Vertices[4][2]))),(abs(self.Vertices[0][1])+(abs(self.Vertices[4][1]))))

    def checkClick(self):
        mpos = pygame.mouse.get_pos()
        z = 2
        ndc = [2.0 * mpos[0] / user32.GetSystemMetrics(0) - 1.0, 1.0 - 2.0 * mpos[1] / user32.GetSystemMetrics(1)]
        tanFov = math.tan(90 * 0.5 * math.pi / 180)
        aspect = user32.GetSystemMetrics(0) / user32.GetSystemMetrics(1)
        viewPos = [z * ndc[0] * aspect * tanFov, z * ndc[1] * tanFov]

        onRect1 = 1 if (
                    viewPos[0] >= self.Vertices[0][0] and viewPos[0] <= self.Vertices[1][0] and viewPos[1] >= self.Vertices[0][1] and viewPos[
                1] <= self.Vertices[2][1]) else 0
        onRect2 = 1 if (
                    viewPos[0] >= self.Vertices[0][0] and viewPos[0] <= self.Vertices[1][0] and viewPos[1] >= self.Vertices[0][1] and viewPos[
                1] <= self.Vertices[2][1]) else 0
        glColor3f(1, 1 - onRect1, 1 - onRect1)
        glBegin(GL_LINES)
        for edge in self.Edges:
            for vertex in edge:
                glVertex3fv(self.Vertices[vertex])
        glEnd()

        glColor3f(1, 1 - onRect2, 1 - onRect2)
def zoomOut():
    glTranslatef(0,0,-.5)
def zoomIn():
    glTranslatef(0,0,0.5)






#calculate angle of 2 vectors
def angle_calculation(a,b):
    cos_a = np.dot(a, b) / (np.linalg.norm(a)*np.linalg.norm(b))
    r = math.degrees(math.acos(min(1, max(cos_a,-1)) ))
    return r
ground_surfaces = (0, 1, 2, 3)

ground_vertices = (
    (-10, -0.1, 50),
    (10, -0.1, 50),
    (-10, -0.1, -300),
    (10, -0.1, -300),

    )

def Ground():
    glBegin(GL_QUADS)
    x = 0
    for vertex in ground_vertices:
        x += 1
        glColor3fv((0, 1, 1))
        glVertex3fv(vertex)
    glEnd()

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
    gluPerspective(45, (display[0] / display[1] + 0.66), 0.3, 50.0)  # fovy, aspect, znear, zfar
    glTranslatef(0.5, -1, -8)

    while isTrue:
        Ground()
        glPushMatrix()
        mv_matrix = glGetFloatv(GL_MODELVIEW_MATRIX) #  GETS MATRIX VALUES AND STORES THEM IN VAR
        left, up, forward, position = [v / (np.linalg.norm(v)) for v in mv_matrix[:, :3]]
        print("left ",left)
        print("up ",up)
        print("forward ",forward)
        print("pos ",position)
        glLoadIdentity()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            elif event.type == pygame.KEYDOWN:
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
                #  used to test z rotate, x rotate, y rotate
                if event.key == pygame.K_z:
                    glPopMatrix()
                    glRotatef(1,0,0,1)
                    glPushMatrix()
                if event.key == pygame.K_x:
                    glPopMatrix()
                    glRotatef(1,1,0,0)
                    glPushMatrix()
                if event.key == pygame.K_y:
                    glPopMatrix()
                    glRotatef(1,0,1,0)
                    glPushMatrix()
                if event.key == pygame.K_LCTRL:
                    glPopMatrix()
                    zoomOut()
                    glPushMatrix()
                if event.key == pygame.K_LSHIFT:
                    glPopMatrix()
                    zoomIn()
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
        cube.Cube(25)
        print("CUBE DIMENSIONS: ",cube.getDimensions())
        print("CUBE angle dim.",angle_calculation(cube.Vertices[0],cube.Vertices[3]))
        #cube.checkClick()

        rectangle = ShapesDraw()
        rectangle.Rectangle(3,5,8)
        print("RECTANGLE DIMENSIONS: ",rectangle.getDimensions())


        pyramid = ShapesDraw()
        pyramid.Pyramid(6,2,3)
        print("PYRAMID DIMENSIONS: ",pyramid.getDimensions())

        pygame.display.flip()
        pygame.time.wait(100)

        #print(glGetDoublev(GL_MODELVIEW_MATRIX))


main()
