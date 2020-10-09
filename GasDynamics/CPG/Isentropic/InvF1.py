import math
from GasDynamics.ZeroFinder.secant import *
from .F1 import *
def residualF1(M,f1,k):
    '''This functions gives the difference between the function F1 for a given M and the target value of f1. This function is meant to be used in the solution of the inverse to the function F1.'''
    return (F1(M,k)-f1)

def InvF1(f1,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\Isentropic
    Function: InvF1(f1,k)
    Variables:
        T - Temperature [K]
        R - Gas constant [J/(kgK)], default value 287 J/(kgK) for air
        k - ratio of specific heats gamma=Cp/Cv, default value k=1.4 for diatomic gases
        a - speed of sound [m/s]
        V - local magnitude of gas velocity [m/s]
        M - Mach number
        F1 - M*(1+(k-1)/2*M^2)^(-(k+1)/(2*(k-1)))
    Abbreviations:
        PG - Perfect Gas
        CPG - Calorically Perfect Gas
        TPG - Thermally Perfect Gas
    Inputs: f1,k
    Outputs: M [Msub,Msuper,f]
    Explanantion: Inverts the function F1=M*(1+(k-1)/2*M^2)^(-(k+1)/(2*(k-1))) which appears in isentropic area relations of perfect gas gasdynamics relations to give Mach number given f1 and k. For any given f1, there are two possible Mach numbers one subsonic and the other supersonic, accordingly the output is a list containing the two Mach numbers and a flag indicating the success of the operation.
    Usage:
        M=InvF1(f1) # calculates M for a perfect diatomic gas including air
        M=InvF1(f1,k) # calculates M for a general perfect gas given M,k
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    # The subsonic solution
    maxminsub=[0.1,0.2]
    sol1=secant(residualF1,maxminsub,f1,k)
    # The supersonic solution
    maxminsup=[1.1,3.0]
    sol2=secant(residualF1,maxminsup,f1,k)
    # Check for solutions
    if (sol1[1]>0)and(sol2[1]>0):
        return ([sol1[0],sol2[0],1])
    else:
        print('error: The function could not be solved, check the inputs given')
        return