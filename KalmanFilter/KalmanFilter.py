import numpy as np


class KalmanFilter:
    def __init__(self, mu0, sigma0, A, B, R, C, Q):
        """

        :param mu0: initial mean of bel(x_0)
        :param sigma0: initial sigma of bel(x_0)
        :param A: correlation matrix between x and previous x, used in linear formation of state x. Shape = (n,n)
        :param B: correlation matrix between x and u, used in linear formation of state x. Shape = (m,m)
        :param C: correlation matrix between z and x, used in linear formation of measurement z. Shape = (k,n)
        :param R: variance matrix of Gaussian noise et of x
        :param Q: variance matrix of Gaussian noise dt of z
        """
        self.mu0 = mu0
        self.sigma0 = sigma0
        self.A = A
        self.B = B
        self.C = C
        self.R = R
        self.Q = Q

    def step(self, pre_mu, pre_sigma, u, z):
        """
        :param pre_mu: mean of bel(x) at time step t-1. Shape = (n,1)
        :param pre_sigma: sigma of bel(x) at time step t-1. Shape = (n,n)
        :param u: control data at current time step t. Shape = (m,1)
        :param z: measurement data at current time step t. Shape = (k,1)
        :return:
            current mean & current sigma to represent bel(x_t)
        """
        mu_bar = np.dot(self.A, pre_mu) + np.dot(self.B, u)
        sigma_bar = np.dot(np.dot(self.A, pre_sigma), self.A.T) + self.R
        inv = (np.dot(np.dot(self.C,sigma_bar),self.C.T)+self.Q)**-1 if self.C.shape[0] == 1 \
            else np.linalg.inv(np.dot(np.dot(self.C,sigma_bar),self.C.T)+self.Q)
        K = np.dot(np.dot(sigma_bar, self.C.T), inv)
        mu = mu_bar + np.dot(K, z-np.dot(self.C, mu_bar))
        sigma = np.dot((np.identity(K.shape[0]) - np.dot(K,self.C)), sigma_bar)
        return mu, sigma

