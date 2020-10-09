import numpy as np
import math
from inspect import signature

def secant(funcname,maxmin,*arglist,**keyop):
    '''
    The secant function uses the secant method to evaluate the zero of a generic function.
    
    Explanation:
    The secant method is a modification of the newton-raphsons method to find the zeros of a function.
    The update formula for the secant method can be written as
    x_3=x_1-y_1*(x_2-x_1)/(y_2-y_1).
    The secant method requires two initial guess values to progress the iterations.
    At each iteration the set of values (x,y) are updated such that y_3 approaches zero.
    Details of the method can be inferred from the code below and is described in textbooks on numerical methods
    
    #################
    Use of the code:
    Inputs : (funcname) the function name, (maxmin) the upper and lower initial estimates passed in as a list, 
    other arguments of the function passed in as variable arguments.
    options: keyword arguments tol=1e-10 and Max_iter=1e6 values can be varied
    outputs: Solution and the flag (1 if solution is achieved, 0 otherwise)
    
    [x,flag]=secant(funcname,[x_init_nax x_init_min],[other variables required for the function])
    [x,flag]=secant(funcname,[x_init_nax x_init_min],[other variables required for the function],tol=1e-6)
    [x,flag]=secant(funcname,[x_init_nax x_init_min],[other variables required for the function],tol=1e-6,Max_iter=1e6)
    [x,flag]=secant(funcname,[x_init_nax x_init_min],[other variables required for the function],Max_iter=1e6)
    
    #########
    
    Example:
    
    Solve the equation tan(x)=x
    First define a residual function that goes to zero as the solution approaches.
    def residual_func(x):
        res=math.tan(x)-x
        return x
    Then use the secant function on the residual function.
    [x,flag]=secant(residual_func,[math.pi/6,math.pi/3])
    
    ####
    
    Credits:
    Srisha Rao M V, August 2020
    
    ###
    ver 0
    '''
    # in python the function itself can be passed by its name into funcname and funcname can be called like a normal function.
    sig = signature(funcname)
    n_arg_func=len(sig.parameters) # check the number of arguments required by the function 
    #(do not use variable number of arguments in the function)
    #	print(arglist)
    #	print(arglist[0:(n_arg_func-2)])
    #	print(n_arg_func)
    if n_arg_func>1:
        arglist_temp0=[maxmin[0]]+list(arglist[0:(n_arg_func-1)]) # create a list of arguments 
        #(pyhton behaviour of counting - exclusive (does not include thelast number given))
        arglist_temp1=[maxmin[1]]+list(arglist[0:(n_arg_func-1)])
    else:
        if n_arg_func==1:
            arglist_temp0=[maxmin[0]]
            arglist_temp1=[maxmin[1]]
#	print(arglist_temp0)
#	print(arglist_temp1)
    arg_array=np.array([[maxmin[0],0],[maxmin[1],0],[0,0]])
    arg_array[0,1]=funcname(*arglist_temp0) # way of passing the values by expanding a list
    arg_array[1,1]=funcname(*arglist_temp1)
#	print(arg_array)
    flag_completion=0
    iterator=1
    if 'tol' in keyop:
        tol=keyop['tol']
        pass
    else:
        tol=1e-10 # This is hard coded will be made optional in the next version
        pass
    if 'Max_iter' in keyop:
        Max_iter=keyop['Max_iter']
    else:
        Max_iter=1e6 # This is hard coded will be made optional in the next version
        pass
    while flag_completion==0:
        arg_array[2,0]=arg_array[0,0]-arg_array[0,1]*((arg_array[1,0]-arg_array[0,0])/(arg_array[1,1]-arg_array[0,1])) # formula of secant iterations
        if n_arg_func>1:
            arglist_temp=[arg_array[2,0]]+list(arglist[0:(n_arg_func-1)])
        else:
            if n_arg_func==1:
                arglist_temp=[arg_array[2,0]]
        arg_array[2,1]=funcname(*arglist_temp)
        #print(arg_array)
        if math.fabs(arg_array[2,1])<tol:
            flag_completion=1
            return [arg_array[2,0],flag_completion]
        else:
            if iterator>Max_iter:
                print("Function has no converged solution in maximum number of iterations")
                return [0,flag_completion]
            else:
                ind=np.argsort(np.abs(arg_array[:,1])) # sorting is not as straight forward as matlab
                temp_array=np.array([arg_array[ind,0],arg_array[ind,1]])
                arg_array=np.transpose(temp_array)
                #print(arg_array)
                iterator=iterator+1

