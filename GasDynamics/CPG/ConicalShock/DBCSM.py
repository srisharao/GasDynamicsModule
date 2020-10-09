from .CSMB import *
from GasDynamics.CPG.basicFunctions import *
import numpy as np
import math
def DBCSM(M,k=1.4,Nmax=100):
    '''
    Creates a database of conical shock properties giving a numpy array as an output
    Inputs: M,k
    output: numpy array of values arranged as follows M,Mc,Pc/P1,Tc/T1,rhoc/rho1,P0c/P01,dSbyR,th,B
    Usage:
        DB=DBCSM(M,k=1.4)
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    mu=machangle(M)
    DB=CSMB(M,mu,k)    
    dB=1*math.pi/180
    flag=0
    c=1
    dBdth=1
    while flag==0:
        temp=np.empty_like(DB)
        B=mu+c*dB
        temp=CSMB(M,B,k)
        if c>2:
            dBdth=(DB[(c-1),-1]-DB[(c-2),-1])/(DB[(c-1),-2]-DB[(c-2),-2])
            pass
        if temp[0]==0:
            flag=1
            return DB
        elif B>(math.pi/2-dB):
            flag=1
            return DB
        elif c>Nmax:
            flag=1
            return DB
        elif dBdth<0:            
            flag=1
            return DB
        else:
            DB=np.vstack((DB,temp))
            c=c+1
            #print(c)
            pass
        pass
    return
        