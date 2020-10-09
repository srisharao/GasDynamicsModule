from GasDynamics.CPG.ObliqueShock import *
from GasDynamics.CPG.Isentropic import *
from GasDynamics.CPG.basicFunctions import *
from GasDynamics.ZeroFinder import *
from scipy.integrate import odeint
import math
def derivative_CSMB(y,xi,args):
    k=args[0]
    Mst=math.sqrt(y[0]**2+y[1]**2)
    aast=((k+1)/2)-((k-1)/2)*Mst**2
    dustdxi=y[1]
    dvstdxi=-y[0]+(aast*(y[0]+y[1]/math.tan(xi)))/(y[1]**2-aast)
    return np.array([dustdxi,dvstdxi])
def residual_CSMB(xi,x0,yini,k):
    args=[k]
    sol=oderk4(derivative_CSMB,yini,xi,x0,args)
    return sol[1]
def CSMB(M,B,k=1.4):
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
    mu=machangle(M)
    if B==mu:
        out=[M,M,1,1,1,1,0,0,mu]
        return out
    elif B>mu:
        OSprop=OSMB(M,B,k)
        OSM2=OSprop[1]
        M2stini=MstarM(OSM2,k)
        ustini=M2stini*math.cos(OSprop[-1]-OSprop[-2])
        vstini=-M2stini*math.sin(OSprop[-1]-OSprop[-2])
        yini=np.array([ustini,vstini])
        xi1=0.99*OSprop[-1]
        xi2=0.95*OSprop[-1]
        xisol=secant(residual_CSMB,[xi1,xi2],B,yini,k)
        if xisol[1]==1:
            th=xisol[0]
            rk4sol=oderk4(derivative_CSMB,yini,th,B,[k])
            ustc=rk4sol[0]
            vstc=rk4sol[1]
            Mstc=math.sqrt(ustc**2+vstc**2)
            Mc=MMstar(Mstc,k)
            PcP1=PbyP0(Mc,k)/PbyP0(OSM2,k)*OSprop[2]
            TcT1=TbyT0(Mc,k)/TbyT0(OSM2,k)*OSprop[3]
            rhocrho1=rhobyrho0(Mc,k)/rhobyrho0(OSM2,k)*OSprop[4]
            P0cP01=OSprop[5]
            dSbyR=OSprop[6]
            out=[M,Mc,PcP1,TcT1,rhocrho1,P0cP01,dSbyR,th,B]
            return out
        else:
            return [0,0,0,0,0,0,0,0,0]
        pass
    else:
        print('error:value of B is impermissible')
        return [0,0,0,0,0,0,0,0,0]
    pass
        
        
    
        