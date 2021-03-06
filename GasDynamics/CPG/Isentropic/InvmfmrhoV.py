def InvmfmrhoV(m,rho,V):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\Isentropic
    Function: InvmfmrhoV(m,rho,V)
    Variables:
        T - Temperature [K]
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
         m=rho*V*A
    Abbreviations:
        PG - Perfect Gas
        CPG - Calorically Perfect Gas
        TPG - Thermally Perfect Gas
    Inputs: m,rho,V
    Outputs: A
    Explanantion: Inverts the mass flow rate formula through a cross section and calculates A given m,rho,V
    Usage:
        A=InvmfmrhoV(m,rho,V)
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    return (m/(rho*V))