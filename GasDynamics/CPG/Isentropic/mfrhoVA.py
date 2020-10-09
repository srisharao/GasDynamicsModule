def mfrhoVA(rho,V,A):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\Isentropic
    Function: mfrhoVA(rho,V,A)
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
    Inputs: rho,V,A
    Outputs: m
    Explanantion: Calculates the mass flow rate through a cross section given rho,V,A
    Usage:
        m=mfrrhoVA(rho,V,A)
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    return (rho*V*A)