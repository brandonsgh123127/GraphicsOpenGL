import Shapes
import numpy as np
import math
from OpenGL.GL import *

"""
* Class that manages manipulations of camera angles.
*
* * * * * * * * * * * * * * * * * * * * * * * * * 
* STILL A WORK IN PROGRESS
* * * * * * * * * * * * * * * * * * * * * * * * *
*
"""
class Camera:
    dotResult = ''
    matrix = None

    def __init__(self,matrix):
        self.matrix=matrix
    ###########################
    # Rotate along x axis...
    ############################
    def rotateXY(self,angle):
        matrixManip = np.array(self.matrix)
        print("Original: \n",matrixManip,"\n")
        """ In order to manipulate rotation, use cos/sin manipulations"""
        if len(self.dotResult) == 0:
            self.dotResult = np.array((matrixManip[0,0],matrixManip[1,1],matrixManip[2,2],
               1))
            print("SET DOT RESULT")
        # Manipulate Data, then transorm into dotResult...
        angleToRadians = np.deg2rad(angle)
        matrixManip[1,1] = float(np.cos(angleToRadians))
        matrixManip[1,2] = float(-(np.sin(angleToRadians)))
        matrixManip[2,1] = float((np.sin(angleToRadians)))
        matrixManip[2,2] = float(np.cos(angleToRadians))
        #cosy - sinz
        self.dotResult[1] = matrixManip[1,1] *self.dotResult[1] + matrixManip[1,2] * self.dotResult[2]
        #siny + cosz
        self.dotResult[2] = matrixManip[2,1] *self.dotResult[1] + matrixManip[2,2] * self.dotResult[2]
        # Flatten array for use in glMatrix
        self.matrix=matrixManip.copy()
        print("Modified: \n",self.matrix)
        matrixManip = matrixManip.flatten()
        singleDMatrix = np.zeros((16))
        # Populate a new array with elements from old array
        for i in range(0,len(matrixManip)):
            singleDMatrix[i]=(float(matrixManip[i]))
        # Mapping values of matrix to m...
        m = map(float, singleDMatrix)
        m1 = (GLfloat * 16)(*m)

        glMatrixMode(GL_MODELVIEW)
        ## Where the magic happens, manipulation happens here...
        glLoadMatrixf(m1)
        # Just in case matrix stack is empty...
        try:
            glPopMatrix()
            glPushMatrix()
        except:
            glPushMatrix()
        self.getDot()

    ###########################
    # Rotate along x axis to ...
    ############################
    def rotateXZ(self,angle):
        matrixManip = np.zeros((4,4))
    def rotateXU(self,angle):
        matrixManip = np.zeros((4,4))
    def rotateXZ(self,angle):
        matrixManip = np.zeros((4,4))
    def rotateYZ(self,angle):
        matrixManip = np.zeros((4,4))

    def getDot(self):
        print("Dot Values...",self.dotResult,"\n\n")
    """
    Allows matrix to be set by external class.
    """
    def setMatrix(self,m):
        self.matrix=m
        print(self.matrix)