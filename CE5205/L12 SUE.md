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



### 2.2 Probit-Based SUE Conditions

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

$$\begin{array}{lrl}
\displaystyle \frac{\partial z(\boldsymbol{f^*})}{f^{*rs}_k} - u_{rs}^* - \nu^{*rs}_k =0,
  & \forall k \in K_{rs}, \ \forall \ r \in R, \ \forall \ s \in S
  & \quad \Rightarrow \quad \nu^{*rs}_k =  c^{*rs}_k - u^{*rs}_k
\\
\nu^{*rs}_k \geq 0,
  & \forall k \in K_{rs}, \ \forall \ r \in R, \ \forall \ s \in S
  & \quad \Rightarrow \quad c^{*rs}_k \geq u^{*rs}_k
\\
\nu^{*rs}_k \times (-f^{*rs}_k) = 0,
  & \forall k \in K_{rs}, \ \forall \ r \in R, \ \forall \ s \in S
  & \quad \Rightarrow \quad (c^{*rs}_k - u^{*rs}_k) f^{*rs}_k = 0
\\
\displaystyle \sum_{k \in K_{rs}} f^{*rs}_k = q_{rs}
  & \forall \ r \in R, \ \forall \ s \in S
\\
f^{*rs}_k >0,
  & \forall \ r \in R, \ \forall \ s \in S
\end{array}$$

Then we can get
$$
\begin{align*}
\frac{f^{*rs}_{k}}{q_{rs}} = \frac{\exp(-\theta C_{k}^{*rs})}{\sum_{r \in R}\sum_{s \in S} \exp(-\theta)}
\end{align*}
$$
d
where:
$$
\frac{\partial z(\boldsymbol{f^*})}{f^{*rs}_k} = c^{*rs}_k= \sum_{a \in A} t_a (x_a^*) \ \delta^{rs}_{ak}
$$

## 4. Stochastic User Equilibrium Loading Methods


## References

[1] C. Fisk, "Some developments in equilibrium traffic assignment", *Transportation Research Part B: Methodological*, vol. 14, no. 3, pp. 243–255, Sep. 1980, doi: 10.1016/0191-2615(80)90004-1.

[2]
