from GasDynamics.CPG.ObliqueShock import *
from GasDynamics.CPG.Isentropic import *
from GasDynamics.CPG.basicFunctions import *
from GasDynamics.ZeroFinder import *
from .DBCSM import *
from .CSMB import *
from scipy import interpolate
import math
def residual_CSMPcP1(B,PcP1,M,k):
    CSprop=CSMB(M,B,k)
    res=CSprop[2]-PcP1
    return res
def CSMPcP1(M,PcP1,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\ConicalShock
    Function: CSMB(M,B,k=1.4)
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
    Inputs: M,B,k
    Outputs: [M,Mc,Pc/P1,Tc/T1,rhoc/rho1,P02/P01,dS/R,th,B]
    Explanantion: Calculates the properties at cone surface of an attached conical shock given M and B
    Usage:
        B=OSMB(M,B,k=1.4)
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    DBcs=DBCSM(M,k)
    if PcP1==1:
        out=[M,M,1,1,1,1,0,0,mu]
        return out
    elif PcP1<1:
        print('error:value of PcP1 is impermissible')
        return [0,0,0,0,0,0,0,0,0]
    elif PcP1<=DBcs[-1,2]:
        interpfn=interpolate.interp1d(DBcs[:,2],DBcs[:,-1])
        Best1=interpfn(1.01*PcP1)
        Best2=interpfn(0.99*PcP1)
        B=secant(residual_CSMPcP1,[Best1,Best2],PcP1,M,k)
        out=CSMB(M,B[0],k)
        return out
    else:
        print('error:value of PcP1 is impermissible')
        return [0,0,0,0,0,0,0,0,0]
    pass
        
        
    
        