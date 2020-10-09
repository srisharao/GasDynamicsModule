def InvmfmAPT(m,A,P,T,R=287,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\Isentropic
    Function: InvmfmAPT(m,A,P,T,R=287,k=1.4)
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
    Inputs: m,A,P,T,R,k
    Outputs: M
    Explanantion: Inverts the mass flow rate through a cross section given mass flow rate m and P,T,A, calculates M. Fluid properties k,R must be provided
    Usage:
        m=InvmfmPTA(m,A,P,T,R,k)
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    return (m/(A*((k/R)**0.5)*P/(T**0.5)))