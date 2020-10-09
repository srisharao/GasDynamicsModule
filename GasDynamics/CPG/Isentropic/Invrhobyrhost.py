import math
from .rhobyrho0 import *
from .Invrhobyrho0 import *
def Invrhobyrhost(rhorhost,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\Isentropic
    Function: Invrhobyrhost(rhorhost,k)
    Variables:
        T - Temperature [K]
        T0 - Stagnation Temperature [K]
        rho - Density [kg/m^3]
        rho0 - Stagnation Density
        rhost - Star Density
        R - Gas constant [J/(kgK)], default value 287 J/(kgK) for air
        k - ratio of specific heats gamma=Cp/Cv, default value k=1.4 for diatomic gases
        a - speed of sound [m/s]
        V - local magnitude of gas velocity [m/s]
        M - Mach number
    Formula:
         rho/rhost =rho/rho0*rho0/rhost
    Abbreviations:
        PG - Perfect Gas
        CPG - Calorically Perfect Gas
        TPG - Thermally Perfect Gas
    Inputs: M,k
    Outputs: rho/rhost
    Explanantion: Inverts the rho/rhost relation for an isentropic stagnation process
    Usage:
        M=Invrhobyrhost(rhorhost) # calculates M for a perfect diatomic gas including air
        M=Invrhobyrhost(rhorhost,k) # calculates M for a general perfect gas given rhorhost,k
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    return (Invrhobyrho0((rhorhost*rhobyrho0(1,k)),k))