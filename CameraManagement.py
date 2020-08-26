import numpy as np
from OpenGL.GL import *

"""
* Class that manages manipulations of camera angles.
*
* * * * * * * * * * * * * * * * * * * * * * * * * 
* STILL A WORK IN PROGRESS
* * * * * * * * * * * * * * * * * * * * * * * * *
*
"""
class Camera(object):
    """
    Default variables necessary in class are
    a.) matrix- original view matrix camera
    b.) dotResult- where the resulted manipulation is stored...
    c.) fullAngle- Rotation angles stored here in degrees...
    """
    dotResult =[]
    matrix = None
    fullAngle = [0,0,0]
    mapped =[]
    def __init__(self,matrix):
        self.matrix=matrix
        glPushMatrix()
        glPushMatrix()
        self.dotResult=np.array((self.matrix[0,0],self.matrix[1,1],self.matrix[2,2],1))
    """"
    ###########################
    Rotate along x axis...
    ############################
    """
    def rotateXY(self,angle):
        self.fullAngle[0] += angle
        #self.matrix=glGetFloatv(GL_PROJECTION_MATRIX)
        #self.fullAngle=360 % self.fullAngle
        matrixManip = np.array(self.matrix.copy())
        """ In order to manipulate rotation, use cos/sin manipulations"""
        # Manipulate Data, then transform into dotResult...
        angleToRadians = np.deg2rad(float(self.fullAngle[0]))
        """
        
        CHECKS TO SEE IF w VALUE IS 0.  IF NOT, THEN MULTIPLY RESULT BY IT.
        """
        if matrixManip[1,3] == 0:
            matrixManip[1,1] = float(np.cos(angleToRadians))
            matrixManip[1,2] = float(-(np.sin(angleToRadians)))
            matrixManip[0,2]=float(-(np.sin(angleToRadians))/4)
            # matrixManip[0,3]=matrixManip[0,2]
        else:
            matrixManip[1, 1] = float(np.cos(angleToRadians) * matrixManip[1,3])
            matrixManip[1, 2] = float(-(np.sin(angleToRadians))* matrixManip[1,3])
        #matrixManip[1,3] = float(-(np.sin(angleToRadians)))
        if matrixManip[2,3]==0:
            matrixManip[2,1] = float((np.sin(angleToRadians)))
            matrixManip[2,2] = float(np.cos(angleToRadians))
        else:
            matrixManip[2,1] = float((np.sin(angleToRadians))* matrixManip[2,3])
            matrixManip[2,2] = float(np.cos(angleToRadians)* matrixManip[2,3])
            """
            Manipulation of w values still not working...
            W value is supposed to go up to 360 degree value of sin/cos
            """
        matrixManip[1,3]+=float(-(np.sin(angleToRadians)))
        matrixManip[2,3]=matrixManip[2,2]
        self.dotResult[1] = (matrixManip[1,1] *self.dotResult[1]) + matrixManip[1,2] * self.dotResult[2]
        self.dotResult[2] = (matrixManip[2,1] *self.dotResult[1]) + matrixManip[2,2] * self.dotResult[2]
        self.dotResult[3] = 1
        # Flatten array for use in glMatrix
        self.matrix=matrixManip
        matrixManip = matrixManip.flatten()
        singleDMatrix = np.zeros((16))
        # Populate a new array with elements from old array
        for i in range(0,len(matrixManip)):
            singleDMatrix[i]=(float(matrixManip[i]))
        # Mapping values of matrix to m...
        m = map(float, singleDMatrix)
        self.mapped = (GLfloat * 16)(*m)
        glMatrixMode(GL_PROJECTION)
        ## Where the magic happens, manipulation happens here...
        glLoadMatrixf(self.mapped)
        """"
        # Just in case matrix stack is empty...
        # Push the matrix to stack...
        """
        try:
            glPopMatrix()
            glPushMatrix()
        except:
            glPushMatrix()
        print(self.dotResult)
        print (self.matrix)
    """
        ###########################
        Rotate along Z axis...
        ############################
    """
    def rotateXZ(self,angle):
        try:
            glLoadMatrixf(self.mapped)
        except:
            print("No value for mapped!")
        self.fullAngle[2] += angle
        matrixManip = np.array(self.matrix.copy())
        """ In order to manipulate rotation, use cos/sin manipulations"""
        # Manipulate Data, then transform into dotResult...
        angleToRadians = np.deg2rad(float(self.fullAngle[2]))
        """
        CHECKS TO SEE IF w VALUE IS 0.  IF NOT, THEN MULTIPLY RESULT BY IT.
        """
        if matrixManip[0, 3] == 0:
            matrixManip[0, 0] = float(np.cos(angleToRadians)/2)
            matrixManip[0, 1] = float((np.sin(angleToRadians)))

        else:
            matrixManip[0, 0] = float(np.cos(angleToRadians) * matrixManip[0, 3])
            matrixManip[0,1] = float((np.sin(angleToRadians)) * matrixManip[0, 3])
        # matrixManip[1,3] = float(-(np.sin(angleToRadians)))
        if matrixManip[1, 3] == 0:
            matrixManip[1, 0] = float((np.sin(angleToRadians)/2))
            matrixManip[1, 1] = float(np.cos(angleToRadians))
        else:
            matrixManip[1, 0] = float((np.sin(angleToRadians)) * matrixManip[1, 3])
            matrixManip[1, 1] = float(np.cos(angleToRadians) * matrixManip[1, 3])
            """
            Manipulation of w values still not working...
            W value is supposed to go up to 360 degree value of sin/cos
            """
        self.dotResult[0] = (matrixManip[0, 0] * self.dotResult[0]) + matrixManip[0, 1] * self.dotResult[1]
        self.dotResult[1] = (matrixManip[1, 1] * self.dotResult[0]) + matrixManip[1, 2] * self.dotResult[1]
        self.dotResult[3] = 1
        # Flatten array for use in glMatrix
        # self.matrix=matrixManip
        self.matrix=matrixManip
        matrixManip = matrixManip.flatten()
        singleDMatrix = np.zeros((16))
        # Populate a new array with elements from old array
        for i in range(0, len(matrixManip)):
            singleDMatrix[i] = (float(matrixManip[i]))
        # Mapping values of matrix to m...
        m = map(float, singleDMatrix)
        self.mapped = (GLfloat * 16)(*m)
        glMatrixMode(GL_PROJECTION)
        ## Where the magic happens, manipulation happens here...
        glLoadMatrixf(self.mapped)
        """"
        # Just in case matrix stack is empty...
        # Push the matrix to stack...
        """
        try:
            glPopMatrix()
            glPushMatrix()
        except:
            glPushMatrix()
    def rotateXU(self,angle):
        matrixManip = np.zeros((4,4))
    def rotateYZ(self,angle):
        matrixManip = np.zeros((4,4))

    def getDot(self):
        print("Dot Values...",self.dotResult,"\n\n")
    """
    Allows matrix to be set by external class.
    """
    def updateMatrix(self,m):
        self.matrix=m
    def setDot(self,d):
        self.dotResult=d
        print(d)
    def getDot(self):
        return self.dotResult
    def getMapped(self):
        return self.mapped
    def setMatrix(self,m):
        self.matrix=m
        print(self.matrix)