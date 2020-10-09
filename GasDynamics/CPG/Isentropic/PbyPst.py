import math
from .PbyP0 import *
def PbyPst(M,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\Isentropic
    Function: PbyPst(M,k)
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
         P/Pst =P/P0*P0/Pst
    Abbreviations:
        PG - Perfect Gas
        CPG - Calorically Perfect Gas
        TPG - Thermally Perfect Gas
    Inputs: M,k
    Outputs: P/Pst
    Explanantion: Calculates the P/Pst for an isentropic stagnation process
    Usage:
        PPst=PbyPst(M) # calculates P/Pst for a perfect diatomic gas including air
        PPst=PbyPst(M,k) # calculates P/Pst for a general perfect gas given M,k
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    return (PbyP0(M,k)/PbyP0(1,k))