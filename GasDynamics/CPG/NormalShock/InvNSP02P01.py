from GasDynamics.ZeroFinder.secant import *
from .NSP02P01 import *
def residual_P02P01(M1,P02P01,k):
    '''Residual function for claculateing M1 given P02P01 across the shock'''
    return (NSP02P01(M1,k)-P02P01)
def InvNSP02P01(P02P01,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\NormalShock
    Function: InvNSP02P01(P02P01,k)
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
    Inputs: P02P01,k
    Outputs: M1
    Explanantion: Calculates the upstream Mach number given P02/P01 across a shock
    Usage:
        M1=InvNSP02P01(P02P01,k)
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    return secant(residual_P02P01,[1.1,3.0],P02P01,k)