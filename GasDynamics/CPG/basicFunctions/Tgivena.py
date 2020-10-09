import math
def Tgivena(a,R=287,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\basicFunctions
    Function: Tgivena(a,R,k)
    Variables:
        T - Temperature [K]
        R - Gas constant [J/(kgK)], default value 287 J/(kgK) for air
        k - ratio of specific heats gamma=Cp/Cv, default value k=1.4 for diatomic gases
        a - speed of sound [m/s]
    Abbreviations:
        PG - Perfect Gas
        CPG - Calorically Perfect Gas
        TPG - Thermally Perfect Gas
    Inputs: a,R,k
    Outputs: T
    Explanantion: Calculates the temperature in a perfect gas given the sound speed, Gas constant and gamma
    Usage:
        T=Tgivena(a) # Calculates the temperature in PG air at the given speed of sound
        T=Tgivena(a,R) # Calculates the temperature in a diatomic PG gas given a and R
        T=Tgivena(a,R,k) # Calculates the temperature in a Perfect gas given, a,R, and k
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    return (a**2/(R*k))