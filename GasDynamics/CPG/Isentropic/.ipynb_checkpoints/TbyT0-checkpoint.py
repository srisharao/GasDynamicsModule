import math
from .F0 import *
def TbyT0(M,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\Isentropic
    Function: TbyT0(M,k)
    Variables:
        T - Temperature [K]
        T0 - Stagnation Temperature [K]
        R - Gas constant [J/(kgK)], default value 287 J/(kgK) for air
        k - ratio of specific heats gamma=Cp/Cv, default value k=1.4 for diatomic gases
        a - speed of sound [m/s]
        V - local magnitude of gas velocity [m/s]
        M - Mach number
    Formula:
         T/T0 =1/(1+(k-1)/2*M^2)
    Abbreviations:
        PG - Perfect Gas
        CPG - Calorically Perfect Gas
        TPG - Thermally Perfect Gas
    Inputs: M,k
    Outputs: T/T0
    Explanantion: Calculates the T/T0 for an isentropic stagnation process
    Usage:
        TT0=TbyT0(M) # calculates T/T0 for a perfect diatomic gas including air
        TT0=TbyT0(M,k) # calculates T/T0 for a general perfect gas given M,k
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    return (1/F0(M,k))