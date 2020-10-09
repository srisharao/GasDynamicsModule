def NSM1M2(M1,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\NormalShock
    Function: NSM1M2(M1,k)
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
    Numbers:
        1 - upstream of the shock
        2 - downstream of the shock
    Abbreviations:
        PG - Perfect Gas
        CPG - Calorically Perfect Gas
        TPG - Thermally Perfect Gas
    Inputs: M1,k
    Outputs: A
    Explanantion: Calculates the Mach number downstream of the shock given the upstream Mach number and k
    Usage:
        M2=NSM1M2(M1,k)
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    return (((M1*M1+2/(k-1))/(((2*k)/(k-1))*M1*M1-1))**0.5)