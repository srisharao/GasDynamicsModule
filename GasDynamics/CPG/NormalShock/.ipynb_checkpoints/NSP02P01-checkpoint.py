from GasDynamics.CPG.Isentropic.PbyP0 import *
from .NSM2M1 import *
from .NSP2P1 import *
def NSP02P01(M1,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\NormalShock
    Function: NSP02P01(M1,k)
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
    Numbers:
        1 - upstream of the shock
        2 - downstream of the shock
    Abbreviations:
        PG - Perfect Gas
        CPG - Calorically Perfect Gas
        TPG - Thermally Perfect Gas
    Inputs: M1,k
    Outputs: P02/P01
    Explanantion: Calculates the ratio of the downstream and upstream stagnation pressures across a shock
    Usage:
        P02P01=MSP02P01(M1,k)
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    M2=NSM2M1(M1,k)
    return (NSP2P1(M1,k)*PbyP0(M1,k)/PbyP0(M2,k))