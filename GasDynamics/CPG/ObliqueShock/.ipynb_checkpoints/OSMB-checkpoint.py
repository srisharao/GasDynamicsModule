from GasDynamics.CPG.NormalShock import *
from GasDynamics.CPG.basicFunctions import *
from .OSMBth import *
import math
def OSMB(M,B,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\ObliqueShock
    Function: OSMB(M,B,k=1.4)
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
    Inputs: M,th,k
    Outputs: [M,M2,P2/P1,T2/T1,rho2/rho1,P02/P01,dS/R,th,B]
    Explanantion: Calculates the downstream shock properties of an attached oblique shock given M and B
    Usage:
        B=OSMB(M,B,k=1.4)
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    mu=machangle(M)
    if B==mu:        
        out=[M,M,1,1,1,1,0,0,mu]
        return out
    elif B==math.pi/2:
        out=[M,NSM1M2(M,k),NSP2P1(M,k),NST2T1(M,k),NSrho2rho1(M,k),NSP02P01(M,k),NSdSbyR(M,k),0,math.pi/2]
        return out
    else:
        th=OSMBth(M,B,k)
        M1n=M*math.sin(B)
        M2n=NSM1M2(M1n,k)
        M2=M2n/math.sin(B-th)
        out=[M,M2,NSP2P1(M1n,k),NST2T1(M1n,k),NSrho2rho1(M1n,k),NSP02P01(M1n,k),NSdSbyR(M1n,k),th,B]
        return out