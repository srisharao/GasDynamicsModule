def mfMAPT(M,A,P,T,R=287,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\Isentropic
    Function: mfPTAM(M,A,P,T,R,k)
    Variables:
        T - Temperature [K]
        P - Pressure [Pa]
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
    Inputs: M,A,P,T,R,k
    Outputs: m
    Explanantion: Calculates the mass flow rate through a cross section given M,P,T,A should be given and fluid properties k,R must be provided
    Usage:
        m=mfPTAM(M,A,P,T,R,k)
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    return(A*M*((k/R)**0.5)*P/(T**0.5))