import math
def VgivenM(M,a):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\basicFunctions
    Function: VgivenM(M,a)
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
    Inputs: M,a
    Outputs: V
    Explanantion: Calculates the local gas velocity magnitude given the Mach number and speed of sound
    Usage:
        V=VgivenM(M,a)
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    return (M*a)