import math
def F1(M,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\Isentropic
    Function: F1(M,k)
    Variables:
        T - Temperature [K]
        R - Gas constant [J/(kgK)], default value 287 J/(kgK) for air
        k - ratio of specific heats gamma=Cp/Cv, default value k=1.4 for diatomic gases
        a - speed of sound [m/s]
        V - local magnitude of gas velocity [m/s]
        M - Mach number
        F1 - M*(1+(k-1)/2*M^2)^(-(k+1)/(2*(k-1)))
    Abbreviations:
        PG - Perfect Gas
        CPG - Calorically Perfect Gas
        TPG - Thermally Perfect Gas
    Inputs: M,k
    Outputs: F0
    Explanantion: Calculates the function F1=M*(1+(k-1)/2*M^2)^(-(k+1)/(2*(k-1))) which appears in isentropic area relations of perfect gas gasdynamics relations
    Usage:
        f1=F1(M) # calculates f1 for a perfect diatomic gas including air
        f1=F1(M,k) # calculates f1 for a general perfect gas given M,k
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    return (M*(1+((k-1)/2)*M**2)**(-0.5*(k+1)/(k-1)))