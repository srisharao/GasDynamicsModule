import math
from GasDynamics.CPG.basicFunctions import *
def OSMBth(M,B,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\ObliqueShock
    Function: OSMBth(M,B,k=1.4)
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
    Inputs: M1,B,k
    Outputs: th
    Explanantion: Calculates the flow deflection angle for attached solutions given M, B and k
    Usage:
        B=OSMBth(M,B,k=1.4)
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    mu=machangle(M)
    if B==mu:
        return 0
    elif B==math.pi/2:
        return 0
    else:
        tanth=2/math.tan(B)*((M*math.sin(B))**2-1)/(M**2*(k+math.cos(2*B))+2)
        th=math.atan(tanth)
        return th