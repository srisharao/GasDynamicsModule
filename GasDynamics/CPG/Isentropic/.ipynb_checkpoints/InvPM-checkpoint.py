import math
from GasDynamics.ZeroFinder.secant import secant
from .PM import *
def residual_pm(M,pm,k):
    '''residual function for inverse of PM'''
    return (PM(M,k)-pm)
def InvPM(pm,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\Isentropic
    Function: InvPM(M,k=1.4)
    Variables:
        T - Temperature [K]
        R - Gas constant [J/(kgK)], default value 287 J/(kgK) for air
        k - ratio of specific heats gamma=Cp/Cv, default value k=1.4 for diatomic gases
        a - speed of sound [m/s]
        V - local magnitude of gas velocity [m/s]
        M - Mach number
        F0 - 1+(k-1)/2*M^2
    Abbreviations:
        PG - Perfect Gas
        CPG - Calorically Perfect Gas
        TPG - Thermally Perfect Gas
    Inputs: pm,k
    Outputs: M
    Explanantion: Inverts the Prantdtl-Meyer's function and gives M, k must be given 
    Usage:
        M=InvPM(M) # calculates M for a perfect diatomic gas including air
        M=InvPM(M,k) # calculates M for a general perfect gas given pm,k
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    return (secant(residual_pm,[1.1,3.0],pm,k))