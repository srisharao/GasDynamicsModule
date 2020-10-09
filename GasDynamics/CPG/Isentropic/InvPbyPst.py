import math
from .PbyP0 import *
from .InvPbyP0 import *
def InvPbyPst(PPst,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\Isentropic
    Function: InvPbyPst(PPst,k)
    Variables:
        T - Temperature [K]
        T0 - Stagnation Temperature [K]
        R - Gas constant [J/(kgK)], default value 287 J/(kgK) for air
        k - ratio of specific heats gamma=Cp/Cv, default value k=1.4 for diatomic gases
        a - speed of sound [m/s]
        V - local magnitude of gas velocity [m/s]
        M - Mach number
    Formula:
         P/Pst =P/P0*P0/Pst
    Abbreviations:
        PG - Perfect Gas
        CPG - Calorically Perfect Gas
        TPG - Thermally Perfect Gas
    Inputs: M,k
    Outputs: P/Pst
    Explanantion: Inverts the P/Pst relation for an isentropic stagnation process
    Usage:
        M=InvPbyPst(PPst) # calculates M for a perfect diatomic gas including air
        M=InvPbyPst(PPst,k) # calculates M for a general perfect gas given PPst,k
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    return (InvPbyP0((PPst*PbyP0(1,k)),k))