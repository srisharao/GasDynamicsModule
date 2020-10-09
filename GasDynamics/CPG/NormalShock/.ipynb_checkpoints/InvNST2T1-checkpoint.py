from GasDynamics.ZeroFinder.secant import *
from .NST2T1 import *
def residual_T2T1(M1,T2T1,k):
    '''Residual function for claculateing M1 given T2T1 across the shock'''
    return (NST2T1(M1,k)-T2T1)
def InvNST2T1(T2T1,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\NormalShock
    Function: InvNST2T1(T2T1,k)
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
    Inputs: T2T1,k
    Outputs: A
    Explanantion: Calculates the upstream Mach number given T2/T1 across a shock
    Usage:
        M1=InvNST2T1(T2T1,k)
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    return secant(residual_T2T1,[1.1,3.0],T2T1,k)