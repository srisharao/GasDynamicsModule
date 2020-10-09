def InvNSrho2rho1(rho2rho1,k=1.4):
    '''
    Gasdynamics Module
    Location: GasDynamics\\CPG\\NormalShock
    Function: InvNSrho2rho1
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
    Inputs: rho2rho1,k
    Outputs: M1
    Explanantion: Calculates the upstream Mach number given rho2/rho1 across a shock
    Usage:
        M1=InvNSrho2rho1(rho2rho1,k)
    ###
    ver 0
    August 2020
    ###
    Credits:
    Srisha Rao M V
    '''
    return (((2/(k-1))*rho2rho1)/((k+1)/(k-1)-rho2rho1))