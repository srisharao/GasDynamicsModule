from GasDynamics.CPG.NormalShock import *
from GasDynamics.CPG.ObliqueShock import *
from GasDynamics.ZeroFinder.secant import *
import math
def residual_OSP2P1th(B,th,b,k):
    '''Residual to calculate the oblique shock properties given only P2P1 and th'''
    return (math.tan(B-th)/math.tan(th)-b)
def OSP2P1th(P2P1,th,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\ObliqueShock
    Function: OSMP2P1(M,P2P1,k=1.4)
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
    Inputs: M,P2P1,k
    Outputs: [M,M2,P2/P1,T2/T1,rho2/rho1,P02/P01,dS/R,th,B]
    Explanantion: Calculates the downstream shock properties of an attached oblique shock given M and P2P1
    Usage:
        B=OSMP2P1(M,P2P1,k=1.4)
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    M1n=InvNSP2P1(P2P1,k)
    M1max=InvOSthmax(th,k)
    Bmax=OSBmax(M1max[0],k)
    M2n=NSM1M2(M1n,k)
    T2T1n=NST2T1(M1n,k)
    b=M2n/M1n*math.sqrt(T2T1n)
    B1=secant(residual_OSP2P1th,[0.99*Bmax,0.80*Bmax],th,b,k)
    M=M1n/math.sin(B1[0])
    M2=M2n/math.sin(B1[0]-th)
    out=[M,M2,NSP2P1(M1n,k),NST2T1(M1n,k),NSrho2rho1(M1n,k),NSP02P01(M1n,k),NSdSbyR(M1n,k),th,B1[0]]
    return out