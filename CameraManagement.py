import Shapes
import numpy as np
import math
from OpenGL.GL import *

class Camera:

    """
    # Rotate along x axis --> YZ rotate
    # [[ 1            0.          0.                 0.        ]
    #  [ 0.          xcos(a)  -sin(a)         -sin(a)]
    #  [ 0.         -sin(a)       1         -ycos(a) ]
    #  [ 0.          0.         1         0.        ]]
    #
    #
    """



    def __init__(self,matrix=None):
        self.projection=matrix
    #COS [(0,0),(0,1)] SIN((0,1)) -SIN((1,0))
    def rotateXY(self,angle):
        matrixManip = self.projection
        print(matrixManip)
        #glBindVertexArray(matrixManip)
        matrixManip[2,1] = -(math.sin(angle))
        matrixManip[1,2] = -np.math.sin(angle)
        matrixManip[1,3] = -np.math.sin(angle)
        matrixManip[2,1] = -np.math.sin(angle)
        matrixManip[2,3] = -matrixManip[1,1]*np.math.sin(angle)
        matrixManip[1,1] = matrixManip[0,0]*np.math.cos(angle)
        print(matrixManip)
        glDrawArrays(GL_TRIANGLES, 0, 3)
        #glRotatef(angle,1,1,0)

    def rotateXZ(self,angle):
        matrixManip = np.zeros((4,4))
    def rotateXU(self,angle):
        matrixManip = np.zeros((4,4))
    def rotateXZ(self,angle):
        matrixManip = np.zeros((4,4))
    def rotateYZ(self,angle):
        matrixManip = np.zeros((4,4))