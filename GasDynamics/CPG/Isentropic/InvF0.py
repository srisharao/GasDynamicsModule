import math
def InvF0(f0,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\Isentropic
    Function: InvF0(f0,k)
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
    Inputs: f0,k
    Outputs: k
    Explanantion: Inverts the function F0=1+(k-1)/2*M^2 which appears in several instances of perfect gas gasdynamics relations, and gives Mach number for a given f0 and k
    Usage:
        M=InvF0(f0) # calculates M for a perfect diatomic gas including air
        f0=InvF0(f0,k) # calculates M for a general perfect gas given M,k
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    return (math.sqrt((f0-1)*(2/(k-1))))