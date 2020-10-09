import math
def soundspeedPrho(P,rho,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\basicFunctions
    Function: soundspeedPrho(P,rho,k)
    Variables:
        T - Temperature [K]
        P - Pressure [Pa]
        rho - Density [kg/m^3]
        R - Gas constant [J/(kgK)], default value 287 J/(kgK) for air
        k - ratio of specific heats gamma=Cp/Cv, default value k=1.4 for diatomic gases
        a - speed of sound [m/s]
    Abbreviations:
        PG - Perfect Gas
        CPG - Calorically Perfect Gas
        TPG - Thermally Perfect Gas
    Inputs: T,R,k
    Outputs: a (sound speed)
    Explanantion: Calculates the speed of sound in a perfect gas given the Pressure, Density and gamma
    Usage:
        a=soundspeedT(P,rho) # Calculates the sound speed in a diatomic PG gas at the given pressure and density
        a=soundspeedT(P,rho,k) # Calculates the sound speed in a Perfect gas at the given pressure,density, and k
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    return (math.sqrt((k*P)/(rho)))