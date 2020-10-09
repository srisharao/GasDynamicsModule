import math
def MMstar(Mst,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\Isentropic
    Function: MMstar(Mst,k=1.4)
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
    Inputs: Mst,k
    Outputs: M
    Explanantion: Calculates the Mach number given the star Mach number and k
    Usage:
        M=MMstar(Mst) # calculates M for a perfect diatomic gas including air
        M=MMstar(Mst,k) # calculates M for a general perfect gas given M,k
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    return ((2/(((k+1)/Mst**2)-(k-1)))**0.5)