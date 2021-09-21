# Introduction

### Definition
- Extended Kalman Filter (EKF) has the same process with Kalman Filter (KF) with only an alteration in the assumption.
- Instead of assuming that the system is linear, EKF tries to construct a linear approximation from it.
  - Assume the system can be expressed in non-linear functions:
    - ![img_2.png](doc_imgs/img_2.png)
  - We can do linear approximation as:
    - ![img_1.png](doc_imgs/img_1.png)
    - ![img_3.png](doc_imgs/img_3.png)
  - Then, 
    - The approximation for state transition probability will be:
      - ![img_4.png](doc_imgs/img_4.png)
    - The approximation for measurement probability will be:
      - ![img_5.png](doc_imgs/img_5.png)

### Pseudocode algorithm
Pseudocode algorithm will be:

<center>

![img_6.png](doc_imgs/ekf.png)

</center>

_Sebastian Thrun, Wolfram Burgard, and Dieter Fox. Probabilistic robotics. MIT press, 2005. Page 51_

### Derivation
- TOWRITE

# Experiments
Requirement description: <a href="http://stefanosnikolaidis.net/course-files/CS545-Fall2020/Slides_7.pdf">USC - CSCI54 5- Fall 2020 - Lecture 7</a> by <a href="http://www.stefanosnikolaidis.net/"> Prof. Stefanos Nikolaidis </a>
![](doc_imgs/img_6.png)

### Problem
In this situation, we want to estimate the position of a flying airplane given the radar data.
Consider the following situation:
 - The plane flies with a constant velocity v: v<sub>t</sub> = v<sub>t-1</sub>
 - The plane flies in a constant height h: h<sub>t</sub> = h<sub>t-1</sub>
 - The position of the plane is scaled in one dimension: p<sub>t</sub> = p<sub>t-1</sub> + v<sub>t</sub>*Δ<sub>t</sub>
 - The range from the radar to the plane is
   - <img src="https://latex.codecogs.com/png.latex?r_{t}=\sqrt{p_{t}^{2}+h_{t}^{2}}"/> 
 - But due to the error in the measurement, our detected range data will be
   - <img src="https://latex.codecogs.com/png.latex?r_{t}=\sqrt{p_{t}^{2}+h_{t}^{2}} + \delta"/> 
   - where 𝛿 is a Gaussian noise

We want to estimate the position of the airplane w.r.t our range data

### Solution
- State transition model:
  - We consider the state **x**<sub>t</sub> to be:
    - **x**<sub>t</sub> = [p<sub>t</sub> v<sub>t</sub> h<sub>t</sub>]<sup>T</sup>
  - Here, we only consider a simple case, where state is in a linear form and using no control data.
  - Then,
    - <img src="https://latex.codecogs.com/png.latex?%5Ctextbf%7Bx%7D_%7Bt%2B1%7D%20%3D%20%5Cbegin%7Bbmatrix%7Dp_%7Bt%2B1%7D%5C%5Cv_%7Bt%2B1%7D%20%5C%5Ch_%7Bt%2B1%7D%5Cend%7Bbmatrix%7D%20%3D%20%5Cbegin%7Bbmatrix%7D%0A1%20%26%20%5CDelta%20_%7Bt%7D%20%26%200%20%5C%5C%0A0%20%26%201%20%26%200%20%5C%5C%0A0%20%26%200%20%26%201%20%5C%5C%0A%5Cend%7Bbmatrix%7D%20%5Cbegin%7Bbmatrix%7D%0Ap_%7Bt%7D%20%5C%5C%0Av_%7Bt%7D%20%5C%5C%0Ah_%7Bt%7D%20%0A%5Cend%7Bbmatrix%7D%20%3D%20%5Cbegin%7Bbmatrix%7D%0A1%20%26%20%5CDelta%20_%7Bt%7D%20%26%200%20%5C%5C%0A0%20%26%201%20%26%200%20%5C%5C%0A0%20%26%200%20%26%201%20%5C%5C%20%5Cend%7Bbmatrix%7D%20%5Ctextbf%7Bx%7D_%7Bt%7D"/> 
  - Or,
    - <img src="https://latex.codecogs.com/png.latex?g(%5Ctextbf%7Bx%7D_%7Bt%7D%2C%20%5Ctextbf%7Bu%7D_%7Bt%7D)%20%3A%3D%20%5Cbegin%7Bbmatrix%7D%0A1%20%26%20%5CDelta%20_%7Bt%7D%20%26%200%20%5C%5C%0A0%20%26%201%20%26%200%20%5C%5C%0A0%20%26%200%20%26%201%20%5C%5C%20%5Cend%7Bbmatrix%7D%20%5Ctextbf%7Bx%7D_%7Bt%7D"/>
- Measurement model:
  - We consider z<sub>t</sub> = r<sub>t</sub>
    - <img src="https://latex.codecogs.com/png.latex?z_{t}=r_{t}=\sqrt{p_{t}^{2}+h_{t}^{2}} + \delta"/> 
  - Then,
    - <img src="https://latex.codecogs.com/png.latex?h(\textbf{x}_{t})=\sqrt{p_{t}^{2}+h_{t}^{2}}=\sqrt{\textbf{x}_{t,1}^{2}+\textbf{x}_{t,3}^{2}}"/>
  - Hear h(**x**<sub>t</sub>) is not linear. Therefore, we do linear approximation for h() as:
    - ![](doc_imgs/img_7.png)
  - Where 
    - ![](doc_imgs/img_8.png)
- With above models, we can apply EKF to estimate the position of the airplane
  
### Result
- TOWRITE