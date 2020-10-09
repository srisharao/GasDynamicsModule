from GasDynamics.ZeroFinder.secant import *
from GasDynamics.CPG.basicFunctions.machangle import *
from .OSthmax import *
from .OSBmax import *
import math
from .OSMBth import *
import numpy as np
from scipy import interpolate
def residual_MthB(B,M,th,k):
    return (OSMBth(M,B,k)-th)
def OSMthB(M,th,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\ObliqueShock
    Function: OSMthB(M,th,k=1.4)
    Variables:
        T - Temperature[K]
        P - Pressure [Pa]
        P0 - Stagnation Pressure [Pa]
        T0 - Stagnation Temperature [K]
        rho - Density [kg/m^3]
        R - Gas constant [J/(kgK)], default value 287 J/(kgK) for air
        k - ratio of specific heats gamma=Cp/Cv, default value k=1.4 for diatomic gases
        a - speed of sound [m/s]
        V - local magnitude of gas velocity [m/s]
        M - Mach number
        A - Area of cross section
        m - mass flow rate
        B - beta the shock angle for a given flow deflection angle theta
        th - theta the flow defelection angle
    Numbers:
        1 - upstream of the shock
        2 - downstream of the shock
    Abbreviations:
        PG - Perfect Gas
        CPG - Calorically Perfect Gas
        TPG - Thermally Perfect Gas
    Inputs: M1,k
    Outputs: Bmax
    Explanantion: Calculates the shock angle for attached solutions given M, th and k
    Usage:
        B=OSMthB(M,th,k=1.4)
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    thmax=OSthmax(M,k)
    Bmax=OSBmax(M,k)
    mu=machangle(M)
    if th==thmax:
        return ([Bmax,Bmax,1])
    elif th>thmax:
        print('error the angle is greater than the maximum flow deflection angle for attached shock solutions')
        return ([0,0,0])
    elif th==0:
        return ([mu,math.pi/2,1])
    else:
        Btemp1=np.linspace(mu,Bmax,100)
        Btemp2=np.linspace(Bmax,math.pi/2,100)
        thtemp1=np.empty_like(Btemp1)
        thtemp2=np.empty_like(Btemp2)
        for i in range(0,len(Btemp1)):
            thtemp1[i]=OSMBth(M,Btemp1[i],k)
            thtemp2[i]=OSMBth(M,Btemp2[i],k)
            pass
        interpfn1=interpolate.interp1d(thtemp1,Btemp1)
        Bestw1=0.999*interpfn1(th)
        Bestw2=0.995*interpfn1(th)
        interpfn2=interpolate.interp1d(thtemp2,Btemp2)        
        Bests1=0.999*interpfn2(th)
        Bests2=0.995*interpfn2(th)
        B1=secant(residual_MthB,[Bestw1,Bestw2],M,th,k)
        B2=secant(residual_MthB,[Bests1,Bests2],M,th,k)
        return ([B1[0],B2[0],1])