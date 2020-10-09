import math
def OSthBM(th,B,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\ObliqueShock
    Function: OSthBM(M,B,k=1.4)
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
    Inputs: th,B,k
    Outputs: B
    Explanantion: Calculates the Mach number given the flow deflection angle and the shock wave angle for attached solutions given M, B and k
    Usage:
        M=OSthBM(th,B,k=1.4)
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    temp=(1+math.tan(th)*math.tan(B))/(math.sin(B)**2-(math.tan(th)*math.tan(B)/2)*(k+math.cos(2*B)))
    if temp<0:
        print('error: the combination of theta and beta is inaddmissable')
        return 0
    else:
        return math.sqrt(temp)