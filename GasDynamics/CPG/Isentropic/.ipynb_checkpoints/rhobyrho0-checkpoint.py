import math
from .TbyT0 import *
def rhobyrho0(M,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\Isentropic
    Function: rhobyrho0(M,k)
    Variables:
        T - Temperature [K]
        T0 - Stagnation Temperature [K]
        rho - Density [kg/m^3]
        rho0 - Stagnation Density        
        R - Gas constant [J/(kgK)], default value 287 J/(kgK) for air
        k - ratio of specific heats gamma=Cp/Cv, default value k=1.4 for diatomic gases
        a - speed of sound [m/s]
        V - local magnitude of gas velocity [m/s]
        M - Mach number
    Formula:
         rho/rho0 =1/(1+(k-1)/2*M^2)^(1/k-1)
    Abbreviations:
        PG - Perfect Gas
        CPG - Calorically Perfect Gas
        TPG - Thermally Perfect Gas
    Inputs: M,k
    Outputs: rhorho0
    Explanantion: Calculates the rho/rho0 for an isentropic stagnation process
    Usage:
        rhorho0=rhobyrho0(M) # calculates rho/rho0 for a perfect diatomic gas including air
        rhorho0=rhobyrho0(M,k) # calculates rho/rho0 for a general perfect gas given M,k
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    expo=1/(k-1)
    return (TbyT0(M,k)**expo)