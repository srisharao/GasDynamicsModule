import math
def soundspeedT(T,R=287,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\basicFunctions
    Function: soundspeedT(T,R,k)
    Variables:
        T - Temperature [K]
        R - Gas constant [J/(kgK)], default value 287 J/(kgK) for air
        k - ratio of specific heats gamma=Cp/Cv, default value k=1.4 for diatomic gases
        a - speed of sound [m/s]
    Abbreviations:
        PG - Perfect Gas
        CPG - Calorically Perfect Gas
        TPG - Thermally Perfect Gas
    Inputs: T,R,k
    Outputs: a (sound speed)
    Explanantion: Calculates the speed of sound in a perfect gas given the Temperature, Gas constant and gamma
    Usage:
        a=soundspeedT(T) # Calculates the sound speed in PG air at the given Temperature
        a=soundspeedT(T,R) # Calculates the sound speed in a diatomic PG gas given T and R
        a=soundspeedT(T,R,k) # Calculates the sound speed in a Perfect gas geven, T,R, and k
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    return (math.sqrt(k*R*T))