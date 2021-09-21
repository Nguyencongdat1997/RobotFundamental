import numpy as np


class ExtendedKalmanFilter:
    def __init__(self, mu0, sigma0, g, G, R, h, H, Q):
        """

        :param mu0: initial mean of bel(x_0)
        :param sigma0: initial sigma of bel(x_0)
        :param g: function g(u,x). input u and previous x. return new x
        :param G: slope of G
        :param R: variance matrix of Gaussian noise et of x
        :param h: function h(x). input x. return z
        :param H: slop of H
        :param Q: variance matrix of Gaussian noise et of z
        """
        pass

    def step(self, pre_mu, pre_sigma, u, z):
        """
        :param pre_mu: mean of bel(x) at time step t-1. Shape = (n,1)
        :param pre_sigma: sigma of bel(x) at time step t-1. Shape = (n,n)
        :param u: control data at current time step t. Shape = (m,1)
        :param z: measurement data at current time step t. Shape = (k,1)
        :return:
            current mean & current sigma to represent bel(x_t)
        """
        pass

