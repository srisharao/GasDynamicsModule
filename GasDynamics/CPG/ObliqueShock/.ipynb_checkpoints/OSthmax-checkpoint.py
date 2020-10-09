from .OSBmax import *
from .OSMBth import *
def OSthmax(M,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\ObliqueShock
    Function: OSthmax(M,k=1.4)
    Variables:
        T - Temperature[K]
        P - Pressure [Pa]
        P0 - Stagnation Pressure [Pa]
        T0 - Stagnation Temperature [K]
        rho - Density [kg/m^3]
        R - Gas constant [J/(kgK)], default value 287 J/(kgK) for air
        k - ratio of specific heats gamma=Cp/Cv, default value k=1.4 for diatomic gases
        a - speed of sound [m/s]
        V - local magnitude of gas velocity [m/s]
        M - Mach number
        A - Area of cross section
        m - mass flow rate
        B - beta the shock angle for a given flow deflection angle theta
        th - theta the flow defelection angle
    Numbers:
        1 - upstream of the shock
        2 - downstream of the shock
    Abbreviations:
        PG - Perfect Gas
        CPG - Calorically Perfect Gas
        TPG - Thermally Perfect Gas
    Inputs: M1,k
    Outputs: thmax
    Explanantion: Calculates the maximum flow deflection angle for attached solutions given M and k
    Usage:
        thmax=OSBmax(M,k=1.4)
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''    
    return OSMBth(M,OSBmax(M,k),k)