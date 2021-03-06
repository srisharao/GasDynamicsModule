import math
from .F1 import *
def AbyAstar(M,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\Isentropic
    Function: AbyAstar(M,k)
    Variables:
        T - Temperature [K]
        T0 - Stagnation Temperature [K]
        AAst - Star Area Ratio, A/Astar wher Astar is the area corresponding to the location at which M=1
        R - Gas constant [J/(kgK)], default value 287 J/(kgK) for air
        k - ratio of specific heats gamma=Cp/Cv, default value k=1.4 for diatomic gases
        a - speed of sound [m/s]
        V - local magnitude of gas velocity [m/s]
        M - Mach number
    Formula:
         A/Astar =1/M*((1+(k-1)/2*M^2)/((k+1)/2))^((k+1)/(2(k-1)))
    Abbreviations:
        PG - Perfect Gas
        CPG - Calorically Perfect Gas
        TPG - Thermally Perfect Gas
    Inputs: M,k
    Outputs: AAst
    Explanantion: Calculates the A/Astar for an isentropic stagnation process
    Usage:
        AAst=AbyAstar(M) # calculates A/Astar for a perfect diatomic gas including air
        AAst=AbyAstar(M,k) # calculates A/Astar for a general perfect gas given M,k
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    return (F1(1,k)/F1(M,k))