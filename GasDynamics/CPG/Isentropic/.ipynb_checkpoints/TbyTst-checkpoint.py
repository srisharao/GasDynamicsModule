import math
from .TbyT0 import *
def TbyTst(M,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\Isentropic
    Function: TbyTst(M,k)
    Variables:
        T - Temperature [K]
        T0 - Stagnation Temperature [K]
        Tst - star temperature corresponding to temperature at sonic condition achieved using an isentropic process
        R - Gas constant [J/(kgK)], default value 287 J/(kgK) for air
        k - ratio of specific heats gamma=Cp/Cv, default value k=1.4 for diatomic gases
        a - speed of sound [m/s]
        V - local magnitude of gas velocity [m/s]
        M - Mach number
    Formula:
         T/Tst =T/T0*T0/Tst
    Abbreviations:
        PG - Perfect Gas
        CPG - Calorically Perfect Gas
        TPG - Thermally Perfect Gas
    Inputs: M,k
    Outputs: T/Tst
    Explanantion: Calculates the T/Tst for an isentropic star process
    Usage:
        TTst=TbyTst(M) # calculates T/Tst for a perfect diatomic gas including air
        TTst=TbyTst(M,k) # calculates T/Tst for a general perfect gas given M,k
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    return (TbyT0(M,k)/TbyT0(1,k))