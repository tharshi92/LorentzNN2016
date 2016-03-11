# Coded by Tharshi Srikannathasan March 2016
# This is a 4th order Runge-Kutta Scheme to Solve the Lorentz Model with a Neural network to produce values of z

# import all needed libraries 
import numpy as np;
import pylab as pl;
from mpl_toolkits.mplot3d import Axes3D;
from Lorentz import Lorentz

def Lorentz_RK_NN(x0, y0, z0, T, h):

    # define simulation parameters
    # T = 4.0;    # simultion length
    #h = T/N;    # timestep
    N = T/h;   # number of steps

    x = np.zeros(N);
    y = np.zeros(N);
    z = np.zeros(N);

    # parameters for the lorentz model
    sigma = 10.0;
    beta = 8.0/3.0;
    rho = 28;

    # initial conditions
    x[0] = x0;
    y[0] = y0;
    z[0] = z0;

    # define derivative functions

    def x_prime(sigma, x, y, z):
    
        return -sigma*(x - y);
    
    def y_prime(rho, x, y, z):
    
        return x*(rho - z) - y;
    
    def z_prime(beta, x, y, z):
    
        return x*y - beta*z;
    
    # integrate using Runge Kutta Method

    for i in xrange(0, int(N - 1)):
        
        p1 = x_prime(sigma, x[i], y[i], z[i]);
        q1 = y_prime(rho, x[i], y[i], z[i]); 
        r1 = z_prime(beta, x[i], y[i], z[i]);

        p2 = x_prime(sigma, x[i] + h*p1/2.0, y[i] + h*q1/2.0, z[i] + h*r1/2.0);
        q2 = y_prime(rho, x[i] + h*p1/2.0, y[i] + h*q1/2.0, z[i] + h*r1/2.0);
        r2 = z_prime(beta, x[i] + h*p1/2.0, y[i] + h*q1/2.0, z[i] + h*r1/2.0); 

        p3 = x_prime(sigma, x[i] + h*p2/2.0, y[i] + h*q2/2.0, z[i] + h*r2/2.0); 
        q3 = y_prime(rho, x[i] + h*p2/2.0, y[i] + h*q2/2.0, z[i] + h*r2/2.0); 
        r3 = z_prime(beta, x[i] + h*p2/2.0, y[i] + h*q2/2.0, z[i] + h*r2/2.0); 

        p4 = x_prime(sigma, x[i] + h*p3, y[i] + h*q3, z[i] + h*r3);
        q4 = y_prime(rho, x[i] + h*p3, y[i] + h*q3, z[i] + h*r3); 
        r4 = z_prime(beta, x[i] + h*p3, y[i] + h*q3, z[i] + h*r3);

        x[i+1] = x[i] + h*(p1 + 2.0*p2 + 2.0*p3 + p4)/6.0;
        y[i+1] = y[i] + h*(q1 + 2.0*q2 + 2.0*q3 + q4)/6.0;
        z[i+1] = z[i] + h*(r1 + 2.0*r2 + 2.0*r3 + r4)/6.0;

    # return dynamical signal
    
    dynamics = Lorentz(x, y, z);
    
    # plot results
    
    # pl.figure(1);
    # pl.plot(x, '-.', label='x');
    # pl.plot(y, '-.', label='y');
    # pl.plot(z, '-.', label='z');
    # pl.legend();
    # pl.xlabel("timestep");
    #
    # fig = pl.figure();
    # ax = fig.add_subplot(111, projection='3d');
    # ax.scatter(x, y, z);
    #
    # ax.set_xlabel('X');
    # ax.set_ylabel('Y');
    # ax.set_zlabel('Z');
    #
    # pl.show();

    return x, y, z, dynamics;