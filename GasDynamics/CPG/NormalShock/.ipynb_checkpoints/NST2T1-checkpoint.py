from .NSP2P1 import *
from .NSrho2rho1 import *
def NST2T1(M1,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\NormalShock
    Function: NST2T1(M1,k)
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
    Numbers:
        1 - upstream of the shock
        2 - downstream of the shock
    Abbreviations:
        PG - Perfect Gas
        CPG - Calorically Perfect Gas
        TPG - Thermally Perfect Gas
    Inputs: M1,k
    Outputs: T2/T1
    Explanantion: Calculates the ratio of the downstream and upstream temperatures across a shock
    Usage:
        T2T1=NST2T1(M1,k)
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    return (NSP2P1(M1,k)/NSrho2rho1(M1,k))