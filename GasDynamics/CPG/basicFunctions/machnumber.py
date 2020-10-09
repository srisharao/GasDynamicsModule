import math
def machnumber(V,a):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\basicFunctions
    Function: machnumber(V,a)
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
    Inputs: V,a
    Outputs: M
    Explanantion: Calculates the Mach number given local magnitude of velocity and speed of sound 
    Usage:
        M=machnumber(V,a) # Calculates the Mach number given V and a
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    return (V/a)