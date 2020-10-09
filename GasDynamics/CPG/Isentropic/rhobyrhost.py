import math
from .rhobyrho0 import *
def rhobyrhost(M,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\Isentropic
    Function: PbyP0(M,k)
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
    Outputs: rhorhost
    Explanantion: Calculates the rho/rhost for an isentropic star process
    Usage:
        rhorhost=rhobyrhost(M) # calculates rho/rhost for a perfect diatomic gas including air
        rhorhost=rhobyrhost(M,k) # calculates rho/rhost for a general perfect gas given M,k
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''    
    return (rhobyrho0(M,k)/rhobyrho0(1,k))