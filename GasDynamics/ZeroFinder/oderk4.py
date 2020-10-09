import numpy as np
import math
from inspect import signature
def oderk4(funcname,y0,x,x0,args,*arglist,**keyop):
    '''
    The oderk4 function uses the 4th order Runge-Kutta method to evaluate a system of first order ODE.
    
    Explanation:
    The oderk4 needs the a function that calculates the derivative f'(y,x,args)
    where args are additional arguments for the function.
    The initial values y0,x0 must be given.
    x corresponds to the location at which the value of the solution needs to be evaluated.
    
    #################
    Use of the code:
    Inputs : (funcname) the function name, y0,x,x0, args argument list for the function.
    options: Nsteps, use Nsteps=10
    outputs: Solution 
    
    sol=oderk4(funcname,y0,0,x0,args)
    sol=oderk4(funcname,y0,0,x0,args,Nsteps=10)
    
    #########
    
    Example:
    from GasDynamics import *
    import math
    def derivativefn(y,x,args):
        dydx=y
        return dydx
    x0=0
    y0=1
    x=1
    y=oderk4(derivativefn,y0,x,x0,[])
    print(y)
    print(math.e)
    
    ####
    
    Credits:
    Srisha Rao M V, August 2020
    
    ###
    ver 0
    '''
    if 'Nsteps' in keyop:
        Nsteps=keyop['Nsteps']
        pass
    else:
        Nsteps=200
        pass
    dx=(x-x0)/(Nsteps)
    flag=0
    xi=x0
    yi=y0
    c=1
    while flag==0:
        k1=dx*funcname(yi,xi,args)
        k2=dx*funcname(yi+k1/2,xi+dx/2,args)
        k3=dx*funcname(yi+k2/2,xi+dx/2,args)
        k4=dx*funcname(yi+k3,xi+dx,args)
        yi1=yi+(1/6)*k1+(1/3)*k2+(1/3)*k3+(1/6)*k4
        xi1=xi+dx
        if c==Nsteps:
            flag==1
            return yi1
        else:
            xi=xi1
            yi=yi1
            c=c+1
            pass
        pass
    return