import math
def agivenM(M,V):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\basicFunctions
    Function: agivenM(M,V)
    Variables:
        T - Temperature [K]
        R - Gas constant [J/(kgK)], default value 287 J/(kgK) for air
        k - ratio of specific heats gamma=Cp/Cv, default value k=1.4 for diatomic gases
        a - speed of sound [m/s]
        V - local magnitude of gas velocity [m/s]
        M - Mach number
    Abbreviations:
        PG - Perfect Gas
        CPG - Calorically Perfect Gas
        TPG - Thermally Perfect Gas
    Inputs: M,V
    Outputs: a
    Explanantion: Calculates the speed of sound given Mach number and local gas velocity magnitude
    Usage:
        a=agivenM(M,V)
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    return (V/M)