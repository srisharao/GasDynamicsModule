import math
from .InvTbyT0 import *
def InvPbyP0(PP0,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\Isentropic
    Function: InvPbyP0(PP0,k)
    Variables:
        T - Temperature [K]
        T0 - Stagnation Temperature [K]
        P0 - Stagnation Pressure [Pa]
        Tst - Star Temperature [K]
        Pst - Star Pressure [Pa]
        R - Gas constant [J/(kgK)], default value 287 J/(kgK) for air
        k - ratio of specific heats gamma=Cp/Cv, default value k=1.4 for diatomic gases
        a - speed of sound [m/s]
        V - local magnitude of gas velocity [m/s]
        M - Mach number
    Formula:
         P/P0 =1/(1+(k-1)/2*M^2)^(k/k-1)
    Abbreviations:
        PG - Perfect Gas
        CPG - Calorically Perfect Gas
        TPG - Thermally Perfect Gas
    Inputs: M,k
    Outputs: P/P0
    Explanantion: Inverts the P/P0 relation for an isentropic stagnation process
    Usage:
        M=InvPbyP0(PP0) # calculates M for a perfect diatomic gas including air
        M=InvPbyP0(PP0,k) # calculates M for a general perfect gas given PP0,k
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    expo=(k-1)/k
    TT0=PP0**expo
    return (InvTbyT0(TT0,k))