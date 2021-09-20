# Introduction

### Definition
Kalman Filter is a variant of Bayes Filter which is built to calculate a belief distribution of state of system, given measurement data and control data. 
- Formally, we want to calculate bel(**x**<sub>t</sub>) = p(**x**<sub>t</sub>| **z**<sub>1:t</sub>, **u**<sub>1:t</sub>)
  - Where:
    - **x**<sub>t</sub> is the state at current time
    - **z**<sub>1:t</sub> is the sequence of historical data from sensors, called measurement data
    - **u**<sub>1:t</sub> is the sequence of historical data from actuators, called control data

In Kalman Filter, we try to find a loop to calculate the above probability by using Multivariate Gaussian distribution and Linear expression to represent state transitional probability and measurement probability.

To use the Kalman Filter, we define some assumption:
- The system follows Markov Assumption
- The system must be linear
    1) Transitional probability p(**x**<sub>t</sub>| **u**<sub>t</sub>, **x**<sub>t-1</sub>) must be applied to a state x<sub>t</sub> that can be represented as a linear function of **u**<sub>t</sub> and **x**<sub>t-1</sub>, plus a Gaussian noise:
       - **x**<sub>t</sub> = **A**<sub>t</sub> **x**<sub>t-1</sub> + **B**<sub>t</sub> **u**<sub>t</sub> + **e**<sub>t</sub>
         - Where:
           - **x**<sub>t</sub> is a vector represent state, shape = (n, 1). 
           - **u**<sub>t</sub> is a vector represent control data, shape = (m, 1)
           - **A**<sub>t</sub> is a matrix, shape = (n, n)
           - **B**<sub>t</sub> is a matrix, shape = (m, m)
           - **e**<sub>t</sub> is a Gaussian noise that is a multivariate Gaussian random vector with mean = 0 and covariance = **R**<sub>t</sub>
       - Then,
         - <img src="https://latex.codecogs.com/gif.latex?p(\textbf{x}_{t}|\textbf{u}_{t},\textbf{x}_{t-1})="/> 
           <img src="https://latex.codecogs.com/gif.latex?det(2\pi\textbf{R}_{t})^{-1/2}\ exp(-1/2(\textbf{x}_{t}-\textbf{A}_{t}\textbf{x}_{t-1}-\textbf{B}_{t}\textbf{u}_{t})^{T}\textbf{R}_{t}^{-1}(\textbf{x}_{t}-\textbf{A}_{t}\textbf{x}_{t-1}-\textbf{B}_{t}\textbf{u}_{t}))"/>
    2) Measurement probability p(**z**<sub>t</sub>| **x**<sub>t</sub>) can be represented as a linear function of **x**<sub>t</sub>, plus a Gaussian noise: 
       - **z**<sub>t</sub> = **C**<sub>t</sub> **x**<sub>t</sub> + **d**<sub>t</sub> 
         - Where:
           - **z**<sub>t</sub> is a vector represent measurement data, shape = (k, 1). 
           - **x**<sub>t</sub> is a vector represent state, shape = (n, 1). 
           - **C**<sub>t</sub> is a matrix, shape = (k, n)
           - **d**<sub>t</sub> is a Gaussian noise that is a multivariate Gaussian random vector with mean = 0 and covariance = **Q**<sub>t</sub>
       - Then,
         - <img src="https://latex.codecogs.com/gif.latex?p(\textbf{z}_{t}|\textbf{z}_{t)"/> 
           <img src="https://latex.codecogs.com/gif.latex?=det(2\pi\textbf{Q}_{t})^{-1/2}\ exp(-1/2(\textbf{z}_{t}-\textbf{C}_{t}\textbf{x}_{t})^{T}\textbf{Q}_{t}^{-1}(\textbf{z}_{t}-\textbf{C}_{t}\textbf{x}_{t}))"/>
    3) Belief of state at sthe initial timestep must have a Gaussian distribution with mean **µ**<sub>0</sub> and variance **Σ**<sub>0</sub>:
       - <img src="https://latex.codecogs.com/gif.latex?bel(\textbf{x}_{0})= p(\textbf{x}_{0}) = det(2\pi\Sigma_{0})^{-1/2}\ exp(-1/2(\textbf{x}_{0}-\mathbf{\mu}_{0})^{T}\Sigma_{0}^{-1}(\textbf{x}_{0}-\mathbf{\mu}_{0}))"/>
- We will use moment representation<sup>(*)</sup> to represent bel(**x**<sub>t</sub>). In other way, we represent bel(**x**<sub>t</sub>) by its mean **µ**<sub>t</sub> and **Σ**<sub>t</sub>

Kalman Filter make a step-by-step calculation to update **µ**<sub>t</sub> and **Σ**<sub>t</sub> from previous **µ**<sub>t-1</sub> and  **Σ**<sub>t-1</sub> by using measurement and control data  **u**<sub>t</sub>  and  **z**<sub>t</sub> 

### Pseudocode algorithm
Pseudocode algorithm will be:

<center>

![img.png](kf.png)

</center>

_Sebastian Thrun,, Wolfram Burgard, and Dieter Fox. Probabilistic robotics. MIT press, 2005 (Page 36)_

### Derivation
- TODO

# Experiments
Requirement description: <a href="http://stefanosnikolaidis.net/course-files/CS545/HW/hw2.pdf">Section 2 - CSCI545, USC, Fall 2019 </a> by
<a href="http://www.stefanosnikolaidis.net/"> Prof. Stefanos Nikolaidis </a>

### Test 1:
<center>
Section 2.a

![img_1.png](experiment1.png)

</center>
