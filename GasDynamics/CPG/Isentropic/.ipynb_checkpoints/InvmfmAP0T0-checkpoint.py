from .F1 import *
from .InvF1 import *
def InvmfmAP0T0(m,A,P0,T0,R=287,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\Isentropic
    Function: InvmfmAP0T0(m,A,P0,T0,R=287,k=1.4)
    Variables:
        T - Temperature [K]
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
    Formula:
         m=A*(k/R)^0.5*P/(T)^0.5*M
    Abbreviations:
        PG - Perfect Gas
        CPG - Calorically Perfect Gas
        TPG - Thermally Perfect Gas
    Inputs: m,A,P0,T0,R,k
    Outputs: M
    Explanantion: Inverts the mass flow rate through a cross section given mass flow rate m and P0,T0,A, calculates M. Fluid properties k,R must be provided
    Usage:
        M=InvmfmAP0T0(m,A,P0,T0,R=287,k=1.4)
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    f1=(m/(A*(P0/(T0**0.5))*((k/R)**0.5)))
    return InvF1(f1,k)