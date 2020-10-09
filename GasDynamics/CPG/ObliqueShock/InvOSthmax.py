import math
from GasDynamics.ZeroFinder.secant import *
from .OSthmax import *
import numpy as np
from scipy import interpolate
def residual_thmax(M,thmax,k):
    '''residual function to calculate inverse of thmax'''
    return (OSthmax(M,k)-thmax)
def InvOSthmax(thmax,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\ObliqueShock
    Function: InvOSthmax(thmax,k=1.4)
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
    Inputs: thmax,k
    Outputs: M
    Explanantion: Calculates the upstream Mach number given the maximum flow deflection angle for attached solutions given M and k
    Usage:
        M=InvOSthmax(thmax,k=1.4)
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    M=np.arange(1.01,20.01,0.01)
    f=np.empty_like(M)
    for i in range(0,len(M)):
        f[i]=OSthmax(M[i],k)
        pass
    interpfn=interpolate.interp1d(f,M)
    M_in1=1.001*interpfn(thmax)
    M_in2=0.999*interpfn(thmax)
    return secant(residual_thmax,[M_in1,M_in2],thmax,k)