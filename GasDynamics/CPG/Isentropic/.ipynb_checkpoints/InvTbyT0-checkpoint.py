import math
from .InvF0 import *
def InvTbyT0(TT0,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\Isentropic
    Function: InvTbyT0(TT0,k)
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
    Inputs: TT0,k
    Outputs: M
    Explanantion: Inverts the T/T0 relation for an isentropic stagnation process to give M given T/T0 and k
    Usage:
        M=InvTbyT0(TT0) # calculates M for a perfect diatomic gas including air
        M=InvTbyT0(TT0,k) # calculates M for a general perfect gas given TT0,k
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    return (InvF0(1/TT0,k))