import numpy as np
import matplotlib.pyplot as plt
from KalmanFilter import KalmanFilter


def plotTract(track):
    time_step = [x[0] for x in track]
    real_p = [x[1] for x in track]
    predicted_p = [x[2] for x in track]
    avg_mse = [x[3] for x in track]
    plt.plot(time_step, real_p, label="real position")
    plt.plot(time_step, predicted_p, label="predicted position")
    plt.plot(time_step, avg_mse, label="mse")
    plt.legend()
    plt.show()


def testA():
    n = 4
    k = 1
    m = 0
    A = np.array([[1, 0.1, 0, 0], [0, 1, 0.1, 0], [0, 0, 1, 0.1], [0, 0, 0, 1]])
    B = 0
    R = 0
    C = np.array([1, 0, 0, 0]).reshape((1,4))
    Q = 1.0
    mu0 = np.array([5,1,0,0]).reshape((4,1))
    sigma0 = np.array([[10, 0, 0, 0], [0, 10, 0, 0], [0, 0, 10, 0], [0, 0, 0, 10]])

    #a.1)
    track = []
    kf = KalmanFilter(mu0, sigma0, A, B, R, C, Q)
    mu = mu0
    sigma = sigma0
    for t in range(100):
        p = np.sin(0.1*t)
        u = 0
        z = p + np.random.normal(0, Q)
        mu, sigma = kf.step(mu, sigma, u, z)

        predicted_x = np.random.multivariate_normal(mu.T.reshape(-1), sigma)
        avg_position_mse = 0
        for i in range(1000):
            predicted_x_i = np.random.multivariate_normal(mu.T.reshape(-1), sigma)
            avg_position_mse += np.abs(predicted_x_i[0]-p)
        avg_position_mse /= 1000
        track.append((t, p, predicted_x[0], avg_position_mse))
        print(t, avg_position_mse)
    plotTract(track)

testA()










