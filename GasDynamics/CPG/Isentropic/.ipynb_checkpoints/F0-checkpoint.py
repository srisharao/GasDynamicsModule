import math
def F0(M,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\Isentropic
    Function: F0(M,k)
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
    Inputs: M,k
    Outputs: F0
    Explanantion: Calculates the function F0=1+(k-1)/2*M^2 which appears in several instances of perfect gas gasdynamics relations
    Usage:
        f0=F0(M) # calculates f0 for a perfect diatomic gas including air
        f0=F0(M,k) # calculates f0 for a general perfect gas given M,k
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    return (1+((k-1)/2)*M**2)