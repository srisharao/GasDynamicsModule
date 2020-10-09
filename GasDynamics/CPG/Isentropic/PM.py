import math
def PM(M,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\Isentropic
    Function: PM(M,k)
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
    Outputs: pm
    Explanantion: Calculates the Prantdtl-Meyer's function 
    Usage:
        pm=PM(M) # calculates pm for a perfect diatomic gas including air
        pm=PM(M,k) # calculates pm for a general perfect gas given M,k
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    return (math.sqrt((k+1)/(k-1))*math.atan(math.sqrt((k-1)/(k+1)*(M**2-1)))-math.atan(math.sqrt(M**2-1)))