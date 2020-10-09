import math
from .InvTbyT0 import *
def Invrhobyrho0(rhorho0,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\Isentropic
    Function: Invrhobyrho0(rhorho0,k)
    Variables:
        T - Temperature [K]
        T0 - Stagnation Temperature [K]
        R - Gas constant [J/(kgK)], default value 287 J/(kgK) for air
        k - ratio of specific heats gamma=Cp/Cv, default value k=1.4 for diatomic gases
        a - speed of sound [m/s]
        V - local magnitude of gas velocity [m/s]
        M - Mach number
    Formula:
         rho/rho0 =1/(1+(k-1)/2*M^2)^(1/(k-1))
    Abbreviations:
        PG - Perfect Gas
        CPG - Calorically Perfect Gas
        TPG - Thermally Perfect Gas
    Inputs: M,k
    Outputs: rho/rho0
    Explanantion: Inverts the rho/rho0 relation for an isentropic stagnation process
    Usage:
        M=Invrhobyrho0(M) # calculates M for a perfect diatomic gas including air
        M=Invrhobyrho0(M,k) # calculates M for a general perfect gas given rhorho0,k
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    expo=(k-1)
    TT0=rhorho0**expo
    return (InvTbyT0(TT0,k))