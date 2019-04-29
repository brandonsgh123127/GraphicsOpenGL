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
import Shapes


display = [0,0]
def init():
    pygame.init()
    user32 = ctypes.windll.user32
    screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
    display = (screensize[0], screensize[1])

    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    # field of view y, x direction fov, closest edge, furthest edge
    glMatrixMode(GL_PROJECTION);
    gluPerspective(90, (display[0] / display[1] + 0.66 ), 0.3, 50.0)  # fovy, aspect, znear, zfar
    glTranslatef(0.5, -1, -8)

def getKeys():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                glTranslatef(1, 0, 0)
            if event.key == pygame.K_LEFT:
                glTranslatef(-1, 0, 0)
            if event.key == pygame.K_UP:
                glTranslatef(0, -1, 0)
            if event.key == pygame.K_DOWN:
                glTranslatef(0, 1, 0)
            #  used to test z rotate, x rotate, y rotate
            if event.key == pygame.K_z:
                glRotatef(1, 0, 0, 1)
            if event.key == pygame.K_x:
                glRotatef(1, 1, 0, 0)
            if event.key == pygame.K_y:
                glRotatef(1, 0, 1, 0)
            if event.key == pygame.K_LCTRL:
                zoomOut()
            if event.key == pygame.K_LSHIFT:
                zoomIn()
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_position = pygame.mouse.get_pos()
            glRotatef(2, mouse_position[1] - (display[1] / 2), mouse_position[0] -
                      (display[0] / 2), 1)
    glPushMatrix
    glLoadIdentity
    glPopMatrix

def main():
    init()
    projection = glGetFloatv(GL_PROJECTION_MATRIX)  # MATRICES VALUES....
    print(projection)
    cube = Shapes.Cube(5)
    rectangle = Shapes.Rectangle(3, 5, 4)
    pyramid = Shapes.Pyramid(3, 4, 5)

    while True:
        print(projection)
        glLoadIdentity
        getKeys()
        mv_matrix = glGetFloatv(GL_MODELVIEW_MATRIX) #  GETS MATRIX VALUES AND STORES THEM IN VAR
        projection = glGetFloatv(GL_PROJECTION_MATRIX)
        left, up, forward, position = [v / (np.linalg.norm(v)) for v in mv_matrix[:, :3]]
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        #UPDATES DIMENSIONS OF EACH OBJECT
        cube.updateColor()
        rectangle.update()
        pyramid.update()

        print(projection)#Print Matrix values out
        pygame.display.flip()
        pygame.time.wait(100)
        #print(glGetDoublev(GL_MODELVIEW_MATRIX))



#GETS DIMENSIONS OF OBJECT
def getDimensions(obj):#  length, width, height
    return ((abs(obj.Vertices[0][0])+abs(obj.Vertices[4][0])),(abs(obj.Vertices[0][2])+(abs(obj.Vertices[4][2]))),(abs(obj.Vertices[0][1])+(abs(obj.Vertices[4][1]))))
#CHECKS TO SEE IF MOUSE CLICK, ROTATES CAMERA...
def checkClick(obj):
    mpos = pygame.mouse.get_pos()
    z = 2
    ndc = [2.0 * mpos[0] / user32.GetSystemMetrics(0) - 1.0, 1.0 - 2.0 * mpos[1] / user32.GetSystemMetrics(1)]
    tanFov = math.tan(90 * 0.5 * math.pi / 180)
    aspect = user32.GetSystemMetrics(0) / user32.GetSystemMetrics(1)
    viewPos = [z * ndc[0] * aspect * tanFov, z * ndc[1] * tanFov]
    onRect1 = 1 if (
                viewPos[0] >= obj.Vertices[0][0] and viewPos[0] <= obj.Vertices[1][0] and viewPos[1] >= obj.Vertices[0][1] and viewPos[
            1] <= obj.Vertices[2][1]) else 0
    onRect2 = 1 if (
                viewPos[0] >= obj.Vertices[0][0] and viewPos[0] <= obj.Vertices[1][0] and viewPos[1] >= obj.Vertices[0][1] and viewPos[
            1] <= obj.Vertices[2][1]) else 0
    glColor3f(1, 1 - onRect1, 1 - onRect1)
    glBegin(GL_LINES)
    for edge in obj.Edges:
        for vertex in edge:
            glVertex3fv(obj.Vertices[vertex])
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



main()
