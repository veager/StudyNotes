# Traffic Assignment : Stochastic User Equilibrium (SUE) Principle

## 1. Introduction

### 1.1 Motivation

Randomness of Perceived Travel Time

Deterministic user equilibrium (DUE) conditions assumes that all the travelers have **exact/perfect/full** traffic information of network.

However, travelers do not always have full information about road condition and travel time.

Hence, we can assume that there is **uncertainty of travel time** perceived by travelers.

Behavioral analysis of drivers in route choice under stochastic perceived
travel time should be **first investigated**!

### 1.2 Stochastic Perceived Path Travel Time Functions

Relation between Stochastic Perceived Path Travel Time and Traffic Flow

The stochastic perceived travel time between an OD pair consists of two parts:

- (i) Deterministic component;

- (ii) Random term that describes the stochasticity of drivers' perception on travel time

$$
C_k^{rs}(\boldsymbol{f}) = c_k^{rs}(\boldsymbol{f}) + \xi^{rs}_{k},
\quad \forall k \in K_{rs}, \forall \ r\in R, \ \forall  s \in S
$$

where:
- $\boldsymbol{f} = \{f^{rs}_k \ | \ \forall k \in K_{rs}, \forall \ r\in R, \ \forall  s \in S \}$ is path flow vector
- $\displaystyle x_a = \sum_{r\in R} \sum_{s \in S} \sum_{k \in K_{rs}} \delta^{rs}_{ak} f^{rs}_k$ is traffic flow on link $a$
- $\displaystyle c_k^{rs}(\boldsymbol{f}) = \sum_{r\in R} \sum_{s \in S} \sum_{k \in K_{rs}} \delta_{ak}^{rs} \, t_a(x_a)$ is deterministic path travel time/cost functions
- $\xi_{k}^{rs}, \forall k \in K_{rs}, \forall \ r\in R, \ \forall  s \in S$ is random terms

### 1.3 Behavioral Analysis of Travelers in Route Choice

**Path choice set** from origin $r$ to destination $s$ :
$$
K_{rs}, \quad \forall \ r\in R, \ \forall s \in S
$$

**Random disutility function:**
$$
C_k^{rs}(\boldsymbol{f}) = c_k^{rs}(\boldsymbol{f}) + \xi^{rs}_{k},
\quad \forall k \in K_{rs}, \forall \ r\in R, \ \forall  s \in S
$$

Perceived travel time on a path depends on traffic flow and random term that formulates the stochasticity of travelers' perception

- It is reasonable to assume that each traveler tries to minimize her/ his perceived travel time when traveling from origin $r$ to destination $s$

- That is, travelers will aim to travel on the **"shortest path" they perceived** from origin $r$ to destination $s$.

- This does not mean that travelers between the same O-D pair should take the shortest path in terms of the deterministic travel time/cost.

### 1.4 Deterministic Path Travel Time Functions

**Deterministic travel time function of a path** is defined as sum of deterministic travel time function of all links defining the path:
$$
c_k^{rs}(\boldsymbol{f}) = \sum_{a \in A} \delta_{ak}^{rs} \, t_a(x_a),
\quad \forall k \in K_{rs}, \forall \ r\in R, \ \forall  s \in S
$$

## 2. Mathematical Formulation of SUE Principle

"Each traveler will choose a path that she or he perceives to be the shortest one". Namely, the probability that a path is chosen at equilibrium equals the probability perceived to be the shortest one.

**Mathematical Model**

Mathematically, the SUE conditions is formulated as follows:
$$
\begin{array}{ll}
f_{k}^{rs} = q_{rs} \Pr \big(C_{k}^{rs}(\boldsymbol{f}) \leq C_{l}^{rs}(\boldsymbol{f}), \ \forall \ l \neq k, l \in K_{rs} \big) & \forall k \in K_{rs}, \forall r \in R, \forall s \in S
\\
f_{k}^{rs} = q_{rs} \Pr \big(c_{k}^{rs}(\boldsymbol{f}) + \xi_{k}^{rs} \leq c_{l}^{rs}(\boldsymbol{f}) + \xi_{l}^{rs}, \ \forall \ l \neq k, l \in K_{rs} \big) & \forall k \in K_{rs}, \forall r \in R, \forall s \in S
\end{array}
$$

### 2.1 Logit-based SUE Conditions

**Assume :**
- random terms $\{\xi_{k}^{rs} \ | \ k \in K_{rs}, r \in R, s \in S\}$ are **Independent and Identical Distributed** random variables following **Gumbel distribution** with parameters $\eta=0$ and $\mu = \theta$

Thus, we have:

$$
\begin{align*}
& \Pr \big(c_{k}^{rs}(\boldsymbol{f}) + \xi_{k}^{rs} \leq c_{l}^{rs}(\boldsymbol{f}) + \xi_{l}^{rs}, \ \forall \ l \neq k, l \in K_{rs} \big)
= \frac{
    \exp \big[-\theta \,  c_{k}^{rs}(\boldsymbol{f}) \big]
  }{
    \displaystyle \sum_{l \in K_{rs}} \exp \big[-\theta \,  c_{l}^{rs}(\boldsymbol{f}) \big]
  }
\\
& \qquad \forall k \in K_{rs}, \forall r \in R, \forall s \in S
\end{align*}
$$

Thus, The logit-based SUE conditions can be **analytically** expressed by
$$
f^{rs}_k = q_{rs} \cdot \frac{
    \exp \big[-\theta \,  c_{k}^{rs}(\boldsymbol{f}) \big]
  }{
    \displaystyle \sum_{l \in K_{rs}} \exp \big[-\theta \,  c_{l}^{rs}(\boldsymbol{f}) \big]
  }
\qquad \forall k \in K_{rs}, \forall r \in R, \forall s \in S
$$

### 2.2 Probit-Based SUE Conditions

**Assume :**
- random terms $\{\xi_{k}^{rs} \ | \ k \in K_{rs}, r \in R, s \in S\}$ follow a multivariant normal distribution with a mean vector $\boldsymbol{\mu} = \boldsymbol{0}$ and a covariance matrix $\mathbf{\Sigma}$

The joint probability density function:
$$
\phi(\boldsymbol{x} \ | \ \boldsymbol{\mu}, \mathbf{\Sigma})
= \left( \frac{1}{2 \pi} \right)^{\frac{n}{2}} |\mathbf{\Sigma}|^{-\frac{1}{2}} \exp \left[ -\frac{1}{2} (\boldsymbol{x}-\boldsymbol{\mu})^{\top} \mathbf{\Sigma}^{-1} (\boldsymbol{x}-\boldsymbol{\mu}) \right],
\qquad - \infty < \boldsymbol{x} < + \infty
$$
where $n$ is the total number of paths in the network.

The probit-based SUE conditions can be expressed by
$$
f_{k}^{rs} = q_{rs} \Pr \big(c_{k}^{rs}(\boldsymbol{f}) + \xi_{k}^{rs} \leq c_{l}^{rs}(\boldsymbol{f}) + \xi_{l}^{rs},
\quad \ \forall \ l \neq k, l \in K_{rs} \big)
\forall k \in K_{rs}, \forall r \in R, \forall s \in S
$$
and this model doesn't have a analytical expression.


## 3. Fisk's Model

Fisk's model (Fisk, & Caroline, 1980) is a strictly convex programming model:
$$
\begin{array}{rll}
\displaystyle \min_{\boldsymbol{f}} z(\boldsymbol{f}) =& \displaystyle \frac{1}{\theta} \sum_{r \in R} \sum_{s \in S} \sum_{k \in K_{rs}} (f_{k}^{rs} \ln f_{k}^{rs} - f_{k}^{rs}) \ \ +
  & \displaystyle \sum_{a \in A} \int_{0}^{x_a} t_a(\omega) \ \mathrm{d} \omega
\\
\text{s.t.} \quad & \displaystyle x_a = \sum_{r \in R} \sum_{s \in S} \sum_{k \in K_{rs}} \delta_{ak}^{rs} \cdot f_{k}^{rs},
& \forall \ a \in A
\\
& \displaystyle \sum_{k \in K_{rs}}f_{k}^{rs} = q_{rs} \ ,
& \forall r \in R, \ \forall s \in S
\\
& \displaystyle f_{k}^{rs} \geq 0 \ ,
& \forall k \in K_{rs}, \ \forall \ r \in R, \ \forall \ s \in S
\end{array}
$$

The Hessian Matrix $\nabla^2 z(\boldsymbol{f})$ of objective function is a positive definite matrix.

### 3.1 Equivalence with Logit-based SUE conditions

$$
\begin{array}{rll}
\displaystyle \min_{\boldsymbol{f}} z(\boldsymbol{f}) =
  & \displaystyle \frac{1}{\theta} \sum_{r \in R} \sum_{s \in S} \sum_{k \in K_{rs}} (f_{k}^{rs} \ln f_{k}^{rs} - f_{k}^{rs}) \ \ +
  & \displaystyle \sum_{a \in A} \int_0 ^{
    \textstyle { \sum \limits_{r \in R}} \ {\sum \limits_{s \in S}} \ {\sum \limits_{k \in K_{rs}}
    } \delta_{ak}^{rs} \cdot f_{k}^{rs} }
t_a(\omega) \ \mathrm{d} \omega
\\
\text{s.t.} \quad & \displaystyle \sum_{k \in K_{rs}}f_{k}^{rs} = q_{rs} \ ,
& \forall r \in R, \ \forall s \in S
\\
& \displaystyle f_{k}^{rs} \geq 0 \ ,
& \forall k \in K_{rs}, \ \forall \ r \in R, \ \forall \ s \in S
\end{array}
$$

### 3.2 Proof using KKT conditions

(1) Build the Lagrangian function for the equivalent minimization model
$$
L \left(\boldsymbol{f}, \boldsymbol{v}, \boldsymbol{\nu} \right)
= z(\boldsymbol{f}) + \sum_{r \in R} \sum_{s \in S} u_{rs} \left(q_{rs} - \sum_{k \in K_{rs}}f_{k}^{rs} \right)
+ \sum_{r \in R} \sum_{s \in S} \sum_{k \in K_{rs}} \nu^{kr}_{s} \cdot \left( - f_{k}^{rs} \right)
$$
where $u_{rs}$ and $\nu^{kr}_{s}$ are Lagrangian multipliers.

(2) Assume that $\left\{ f_{k}^{*rs} \ | \ \forall  k \in K_{rs}, r \in R, s \in S \right\}$ is the optimal solution. There exist Lagrangian multipliers $\left\{u_{rs}^* \in R \ | \  r \in R, s \in S\right\}$, $\left\{ \nu^{*rs}_k \geq 0 \ | \ \forall  k \in K_{rs}, r \in R, s \in S \right\}$ such that:

$$\begin{array}{lr}
\displaystyle \frac{\partial L \left(\boldsymbol{f}^*, \boldsymbol{u}, \boldsymbol{\nu} \right)}{\partial f^{*rs}_k} = \frac{\partial z(\boldsymbol{f^*})}{f^{*rs}_k} - u_{rs}^* - \nu^{*rs}_k =0,
  & \forall k \in K_{rs}, \ \forall \ r \in R, \ \forall \ s \in S
\\
\nu^{*rs}_k \geq 0,
  & \forall k \in K_{rs}, \ \forall \ r \in R, \ \forall \ s \in S
\\
\displaystyle \nu^{*rs}_k \cdot \frac{\partial L \left(\boldsymbol{f}^*, \boldsymbol{u}, \boldsymbol{\nu} \right)}{\nu^{*rs}_k} = \nu^{*rs}_k \times (-f^{*rs}_k) = 0,
  & \forall k \in K_{rs}, \ \forall \ r \in R, \ \forall \ s \in S
\\
\displaystyle \sum_{k \in K_{rs}} f^{*rs}_k = q_{rs}
  & \forall \ r \in R, \ \forall \ s \in S
\\
f^{*rs}_k \geq 0,
  & \forall k \in K_{rs}, \ \forall \ r \in R, \ \forall \ s \in S
\end{array}$$

where:
$$
\frac{\partial z(\boldsymbol{f})}{f^{rs}_k}
= \frac{1}{\theta} \ln (f_{k}^{rs}) + \sum_{a \in A} t_a (x_a) \ \delta^{rs}_{ak}
= \frac{1}{\theta} \ln (f_{k}^{rs}) + c_k^{rs}
$$

Because $f_k^{*rs} \neq 0$, thus, $\nu_{k}^{*rs} = 0$.

Then, we can get
$$
f^{*rs}_{k} = \exp(-\theta \, c_{k}^{*rs}) \cdot \exp(-\theta \, u_{rs}^{*}),
\quad \forall k \in K_{rs}, \ \forall \ r \in R, \ \forall \ s \in S
$$

Thus, we have the SUE principle:
$$
\frac{f^{*rs}_{k}}{q_{rs}} = \frac{\exp(-\theta \, c_{k}^{*rs})}{\displaystyle \sum_{l \in K_{rs}} \exp(-\theta \, c_l^{*rs})}
$$

## 4. Stochastic User Equilibrium Loading Methods

### 4.1 SUE Loading Methods

A SUE loading method aims to find a SUE link flow solution when the deterministic link or path travel times are given. Namely: for the given link travel time pattern $\{t_a, a \in A\}$, we need to obtain fulfiling the following SUE conditions:
$$
x^*_a = \sum_{r \in R} \sum_{s \in S} \sum_{k \in K_{rs}} \delta_{ak}^{rs} \, f_{k}^{*rs},
\ a \in A
\quad \text{and} \quad
f_{k}^{*rs}, \ \quad f_{k}^{*rs}, \ \forall k \in K_{rs}, \forall r \in R, \forall s \in S
$$
fulfiling the following SUE conditions:
$$
f_{k}^{rs} = q_{rs} \Pr \big(c_{k}^{rs}(\boldsymbol{f}) + \xi_{k}^{rs} \leq c_{l}^{rs}(\boldsymbol{f}) + \xi_{l}^{rs}, \ \forall \ l \neq k, l \in K_{rs} \big),
\quad \forall k \in K_{rs}, \forall r \in R, \forall s \in S
$$

where:
$$
c_{k}^{rs} = \sum_{r \in R} \sum_{s \in S} \sum_{k \in K_{rs}} \delta_{ak}^{rs} \, t_a,
\quad \forall k \in K_{rs}, \forall r \in R, \forall s \in S
$$
and $t_a$ is a fixed value.

### 4.2 Logit-based SUE Loading Method

### 4.3 Probit-based SUE Loading Method

### 4.4 Monte Carlo Simulation based SUE Loading Method

**Step 0: (Initialization)** Set $n:=1$.

**Step 1: (Sampling)** Sample $T_a^n$ from random variable $T_a$ for each link $a \in A$.

**Step 2: (All-or-nothing assignment)** Based on $\{T_a^n, \ a \in A\}$, assign $\{q_{rs}\}$ to the shortest path connecting each O-D pair $r\text{-}s$. This step yields the set of **link flows** $\{X_a^n, \ a \in A\}$

**Step 3: (Flow averaging)** Let
$$
x_a^n = \frac{1}{n} \big[(n-1) x_a^{n-1} + X_a^n \big], \quad \forall a \in A
$$
**Note** that when $n=1$, $x_a^n = X_a^n$

**Step 4: (Stopping test)** Let maximum relative error
$$
\sigma := \max_{a \in A} \left\{ \frac{|x_a^n - x_{a}^{n-1}|}{x_a^n} \right\}
$$
If $n>1$ and $\sigma \leq \varepsilon$, stop, and the solution is $\{x_a^n, \ a \in A\}$. Otherwise, set $n:= n+1$ and go to **Step 1**.

Where $\varepsilon$ is the stopping tolerance, it is a given constant.

### 4.5 MSA Algorithmic Steps

**Step 0 (Initialization) :** Perform an SUE loading method based on $\{t_a = t_a(0), a \in A\}$. This yields $\{x_a^{(1)}, a \in A \}$. Set counter $n:=1$

**Step 1: (Update) :** Set $t_a^{(n)} = t_a(x_a^{(n)}), \forall \, a \in A$

**Step 2: (Direction finding) :** Perform an SUE loading based on $\left\{t_a^{(n)}, a \in A \right\}$. This yields a set of (auxiliary) flows $\left\{y_a^{(n)}, a \in A \right\}$

**Step 3: (Move) :**
$$
x_a^{(n+1)} = x_a^{(n)} + \frac{1}{n} \left( y_a^{(n)} - x_a^{(n)} \right), \ \forall a \in A
$$

**Step 4: (Convergence test) :** If a convergence criterion is met, then stop. The current solution,
$$
\{x_a^{(n+1)}, a \in A \} \ ,
$$
is the set of equilibrium flows.

Otherwise set $n := n+1$ and go to **Step 1**.

The convergence criterion is:
$$
\frac{\displaystyle \sqrt{\sum_{a \in A}\left(x_{a}^{(n+1)}-x_{a}^{(n)}\right)^{2}}}{\displaystyle \sum_{a \in A} x_{a}^{(n)}} \leq \varepsilon
$$

## References

[1] J. de D. Ortúzar S. and L. G. Willumsen, "Chapter 11 Equilibrium and Dynamic Assignment", in *Modelling Transport, Fourth edition*. Chichester, West Sussex, United Kingdom: John Wiley & Sons, 2011.

[2] Y. Sheffi, "Section 10.1-10.2, Chapter 11", in *Urban Transportation Networks: Equilibrium Analysis with Mathematical Programming Methods*, Englewood Cliffs, N.J: Prentice-Hall, 1984. Free download from this [website](https://sheffi.mit.edu/book/urban-transportation-networks)

[3] C. Fisk, "Some developments in equilibrium traffic assignment", *Transportation Research Part B: Methodological*, vol. 14, no. 3, pp. 243–255, Sep. 1980, doi: 10.1016/0191-2615(80)90004-1.
