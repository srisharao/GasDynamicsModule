import math
from .TbyT0 import *
from .InvTbyT0 import *
def InvTbyTst(TTst,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\Isentropic
    Function: InvTbyT0(TT0,k)
    Variables:
        T - Temperature [K]
        T0 - Stagnation Temperature [K]
        Tst - star temperature corresponding to temperature at sonic condition achieved using an isentropic process Tst=TbyT0(1,k)
        R - Gas constant [J/(kgK)], default value 287 J/(kgK) for air
        k - ratio of specific heats gamma=Cp/Cv, default value k=1.4 for diatomic gases
        a - speed of sound [m/s]
        V - local magnitude of gas velocity [m/s]
        M - Mach number
    Formula:
         T/T0 =T/Tst =T/T0*T0/Tst
    Abbreviations:
        PG - Perfect Gas
        CPG - Calorically Perfect Gas
        TPG - Thermally Perfect Gas
    Inputs: TTst,k
    Outputs: M
    Explanantion: Inverts the T/Tst relation for an isentropic stagnation process to give M given T/T0 and k
    Usage:
        M=InvTbyTst(TTst) # calculates T/T0 for a perfect diatomic gas including air
        M=InvTbyTst(TTst,k) # calculates T/T0 for a general perfect gas given M,k
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''    
    return (InvTbyT0((TTst*TbyT0(1,k)),k))