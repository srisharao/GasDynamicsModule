import math
def MstarM(M,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\Isentropic
    Function: MstarM(M,k=1.4)
    Variables:
        T - Temperature [K]
        R - Gas constant [J/(kgK)], default value 287 J/(kgK) for air
        k - ratio of specific heats gamma=Cp/Cv, default value k=1.4 for diatomic gases
        a - speed of sound [m/s]
        V - local magnitude of gas velocity [m/s]
        M - Mach number
        Mstar - star Mach Number
        F1 - M*(1+(k-1)/2*M^2)^(-(k+1)/(2*(k-1)))
    Abbreviations:
        PG - Perfect Gas
        CPG - Calorically Perfect Gas
        TPG - Thermally Perfect Gas
    Inputs: M,k
    Outputs: Mstar
    Explanantion: Calculates the star Mach number given the Mach number and k
    Usage:
        Mst=MstarM(M) # calculates f1 for a perfect diatomic gas including air
        Mst=MstarM(M,k) # calculates f1 for a general perfect gas given M,k
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    return ((((k+1)/2)*(M**2/(1+((k-1)/2*M**2))))**0.5)