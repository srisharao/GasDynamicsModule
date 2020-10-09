import math
def machangle(M):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\basicFunctions
    Function: machangle(M)
    Variables:
        T - Temperature [K]
        R - Gas constant [J/(kgK)], default value 287 J/(kgK) for air
        k - ratio of specific heats gamma=Cp/Cv, default value k=1.4 for diatomic gases
        a - speed of sound [m/s]
        V - local magnitude of gas velocity [m/s]
        M - Mach number
        mu - mach angle = sin^(-1)(1/M)
    Abbreviations:
        PG - Perfect Gas
        CPG - Calorically Perfect Gas
        TPG - Thermally Perfect Gas
    Inputs: M
    Outputs: mu
    Explanantion: Calculates the Mach angle given M
    Usage:
        mu=machangle(M)
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    if M<1:
        print('error: flow should be supersonic M>1')
        return 0
        pass
    return (math.asin(1/M))