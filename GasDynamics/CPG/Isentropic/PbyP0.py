import math
from .TbyT0 import *
def PbyP0(M,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\Isentropic
    Function: PbyP0(M,k)
    Variables:
        T - Temperature [K]
        T0 - Stagnation Temperature [K]
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
    Explanantion: Calculates the P/P0 for an isentropic stagnation process
    Usage:
        PP0=PbyP0(M) # calculates P/P0 for a perfect diatomic gas including air
        PP0=PbyP0(M,k) # calculates P/P0 for a general perfect gas given M,k
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    expo=k/(k-1)
    return (TbyT0(M,k)**expo)