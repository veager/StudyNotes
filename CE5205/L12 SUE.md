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

**Path choice set** from origin $r$ to destination $s$ : $$
K_{rs} \quad \forall \ r\in R, \ \forall  s \in S
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

Deterministic travel time function of a path is defined as sum of deterministic travel time function of all links defining the path

## 2. Mathematical Formulation of SUE Principle

### 2.1 Logit-based SUE Conditions

### 2.2 Probit-Based SUE Conditions

## 3. Fisk's Model

Fisk's model (Fisk, & Caroline, 1980) is a strictly convex programming model


### 3.1 Equivalence with Logi-based SUE conditions

### 3.2 Proof using KKT conditions

## 4. Stochastic User Equilibrium Loading Methods
