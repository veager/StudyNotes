# Traffic Assignment - System Optimum (SO) Principle and Extension of DUE Principle

## 1. System Optimum (SO) Principle

### 1.1 Wardrop's Second Principle (SO Principle)

> The average journal travel time is minimal (Wardrop, 1952)

Average journey travel time:

$$
\frac{
  \displaystyle \sum_{r \in R} \sum_{s \in S} \sum_{k \in K_{r s}}\left(c_{k}^{r s} \times f_{k}^{r s}\right)
  }{
  \displaystyle \sum_{r \in R} \sum_{s \in S} q_{r s}
}
$$

Total system travel time
$$
\begin{align*}
\tilde{z}(\boldsymbol{x}) &= \sum_{r \in R} \sum_{s \in S} \sum_{k \in K_{r s}} \left(c_{k}^{r s} \times f_{k}^{r s} \right)
\\
&= \sum_{r \in R} \sum_{s \in S} \sum_{k \in K_{r s}} \left\{ \left[ \sum_{a \in A} \delta_{ak}^{rs} \cdot t_a(x_a) \right] \times f_{k}^{r s} \right \}
\\
&= \sum_{r \in R} \sum_{s \in S} \sum_{k \in K_{r s}} \sum_{a \in A} \delta_{ak}^{rs} \cdot t_a(x_a) \cdot  f_{k}^{r s}
\\
&= \sum_{a \in A} t_a(x_a) \left[\sum_{r \in R} \sum_{s \in S} \sum_{k \in K_{r s}} \delta_{ak}^{rs} \cdot t_a(x_a) \right]
\\
&= \sum_{a \in A} \left[ t_a(x_a) \cdot x_a \right]
\end{align*}
$$

### 1.2 System Optimum Formulation

A Convex Programming Model
$$
\begin{array}{rll}
\displaystyle \min_{\boldsymbol{x}} \tilde{z}(\boldsymbol{x}) =& \sum \limits_{a \in A} x_{a} \cdot t_{a} \left(x_{a}\right)
\\
\text{s.t.} \quad & x_a = \sum \limits_{r \in R} \sum \limits_{s \in S} \sum \limits_{k \in K_{rs}} \delta_{ak}^{rs} \cdot f_{k}^{rs},
& \forall \ a \in A
\\
& \sum \limits_{k \in K_{rs}}f_{k}^{rs} = q_{rs} \ ,
& \forall r \in R, \ \forall s \in S
\\
& \displaystyle f_{k}^{rs} \geq 0 \ ,
& \forall k \in K_{rs}, \ \forall \ r \in R, \ \forall \ s \in S
\end{array}
$$


- The link flow pattern that minimizes the total system travel time (i.e., the objective function of the previous convex programming model) **does not** generally represent an 'equilibrium' situation.

- SO can result only from **joint decisions** by all travelers to act so as to minimize the total system travel time rather than their own.

- At the SO flow pattern, some travelers may be able to **increase** their travel time by **unilaterally** changing routes.

- This situation is unlikely to sustain itself and consequently the SO flow pattern is not able and **should not** be used as a model for actual route choice behavior.

- However, the total system travel time may serve as a yardstick to evaluate different flow patterns

- **Total system travel time** is a common measurement of effectiveness upon networks.

## 2. SO Solution

### 2.1 SO Solution vs. DUE Solution

#### (1) Marginal time of Link Travel Time
$$
t^{\prime}\left(x_{a}\right)=\frac{\mathrm{d} \,   t_{a} \left(x_{a}\right)}{\mathrm{d} \, x_{a}}, \ a \in A
$$

#### (2) Generalized Link Travel Time Function
$$
\tilde{t}_{a}\left(x_{a}\right) = t_{a}\left(x_{a}\right)+x_{a} \ t^{\prime}\left(x_{a}\right), \ a \in A
\quad \Rightarrow \quad \tilde{t}_{a}\left(x_{a}\right) = \frac{\mathrm{d}\left[x_{a} t_{a} (x_{a}) \right]}{\mathrm{d} \ x_{a} }
$$

The generalized link travel time $t_{a}\left(x_{a}\right)$ can be interpreted as considering marginal contribution of an additional traveler on the link to the total travel time on this link.

It is the sum of two components:
- $t_{a}\left(x_{a}\right)$ : the travel time experienced by that additional traveler when the total link flow is $x_A$
- $t^{\prime}\left(x_{a}\right)$ : the additional travel-time burden that this traveler inflicts on each one of the travelers already using link a (there are $x_a$ of them)

#### (3) DUE solution v.s. SO solution

DUE solution is identical to SO solution provided that **link travel time function** is a constant

**Assumption:** $t_a(x_a) = t_a^0, \ \forall a \in A$, where $t_a^0$ is the free-flow travel time on link $a$.

$$
\begin{align*}
z(x)&=\sum_{a \in A} \int_{0}^{x_{a}} t_{a}(\omega) \ \mathrm{d} \omega
  = \sum_{a \in A} \int_{0}^{x_{a}} t_{a}^{0} \mathrm{d} \omega
  = \sum_{a \in A} x_{a} t_{a}^{0}
\\
\tilde{z}(x) &= \sum_{a \in A} x_{a} t_{a}\left(x_{a}\right)
  =\sum_{a \in A} x_{a} t_{a}^{0}
\end{align*}
$$

**SO solution** is a special case of the UE solution corresponding to network with the marginal cost functions.

Note that:
$$
x_{a} \ t_{a} (x_{a}) = \int_{0}^{x_{a}}\left[t_{a}(\omega)+\omega \, t_{a}^{\prime}(\omega) \right] \, \mathrm{d} \omega = \int_{0}^{x_{a}} \tilde{t}_{a}(\omega) \, \mathrm{d} \omega
$$

Thus, we have
$$
\min_{\boldsymbol{x}} \tilde{z}(\boldsymbol{x}) = \sum_{a \in A} x_{a} \ t_{a} (x_{a})
= \sum_{a \in A} \int_0^{x_a} \tilde{t}_{a} (\omega) \, \mathrm{d} \omega
$$
with constraints:
$$
\begin{array}{ll}
x_a = \sum \limits_{r \in R} \sum \limits_{s \in S} \sum \limits_{k \in K_{rs}} \delta_{ak}^{rs} \cdot f_{k}^{rs}, & \forall a \in A
\\
\displaystyle \sum_{k \in K_{rs}}f_{k}^{rs} = q_{rs} \ ,
& \forall r \in R, \ \forall s \in S
\\
\displaystyle f_{k}^{rs} \geq 0 \ ,
& \forall k \in K_{rs}, \ \forall r \in R, \ \forall s \in S
\end{array}
$$

### 2.2 Uniqueness of SO Solution

Hessian Matrix of Objective Function of SO Formulation
$$
\nabla^{2} \tilde{z}(x) = \begin{bmatrix}
  \tilde{t}^{\prime}\left(v_{1}\right) & 0 & 0 & \cdots \\
  0 & \ddots & 0 & \cdots \\
  0 & 0 & \tilde{t}^{\prime}\left(v_{a}\right) & \cdots \\
  \vdots & \vdots & \vdots & \ddots
\end{bmatrix}
= \begin{bmatrix}
2 t^{\prime}\left(x_{1}\right)+x_{1} t^{\prime \prime}\left(x_{1}\right) & 0 & 0 & \cdots \\
0 & \ddots & 0 & \cdots \\
0 & 0 & 2 t^{\prime}\left(x_{a}\right)+x_{1} t^{\prime \prime}\left(x_{a}\right) & \cdots \\
\vdots & \vdots & \vdots & \ddots
\end{bmatrix}
$$
is positive semi-definite.

The SO solution is unique provided the generalized link travel time functions are **strictly increasing** , namely:
$$
\tilde{t}_{a}' = 2 \, \tilde{t}_{a}'(x_a)
+ x_a \, \tilde{t}_{a}''(x_a) > 0, \ a \in A
$$

### 2.3 Solution Method Finding SO Solution

Any methods solving DUE can be used to solve SO

## 3. Marginal-Cost Pricing Principle

Achieve a SO solution by implementing a proper traffic management strategy

### 3.1 Congestion pricing

Let $\{x_a^{\text{SO}}, a \in A \}$ be a SO link flow solution.

**Congestion pricing**: Charge the following **toll in terms of time** for each link in the network
$$
Toll_a = x_a^{\text{SO}} \ t'(x_a^{\text{SO}}) , \ a \in A
$$

Link travel time functions with the toll
$$
\tilde{t}_a (x_a) = t_a(x_a) + x_a^{\text{SO}} \ t'(x_a^{\text{SO}}), \ a \in A
$$

Travelers follow DUE principle to choose their routes by taking into account the toll, namely,
$$
z(\boldsymbol{x})=\sum_{a \in A} \int_{0}^{x_{a}} \left[ t_{a}(\omega) + x_a^{\text{SO}} \ t'(x_a^{\text{SO}}) \right] \, \mathrm{d} \omega
$$
with the above constraints.

Its optimal solution is: $\{x_a^{\text{SO}}, a \in A \}$

#### 3.1 Braess's paradox (布雷斯悖论)

Total system travel time is a **key performance indicator (KPI)** to measure the effectiveness of a transport management or control strategy

After building a new road, the total travel time could be increased. Try to avoid constructing such road.

### 4. DUE Problem with Elastic Demand

**Assumption:**

- Previous DUE (Beckmann's model) assume the trip rate between every origin and every destination is **fixed and known**.

- **Travel demand function:** The travel demand (i.e., trip rate) from origin $r$ to destination $s$, $q_{rs}$, is a function (generally is a **monotonically decreasing function**, or at least nonincreasing)) of the travel time/cost from the origin to the destination denoted by $u_{rs}$

  $$
  q_{rs} = D_{rs}(u_{rs}),
  \qquad
  u_{rs} = D^{-1}_{rs}(q_{rs}) \ (\text{inverse function})
  $$

  where $u_{rs}$ is the minimum travel time (i.e., shortest path travel time/cost) between $r$ and $s$.

### 4.1 Formulation

- **Strictly convex programming model**

- $q_{rs}$ is a **variable** in this formulation, rather than a constant.

$$
\begin{array}{rll}
\min z(\boldsymbol{x}, \boldsymbol{q})
= & \displaystyle \sum_{a \in A} \int_0^{x_a} t_a (\omega) \, \mathrm{d} \omega
- \sum_{r \in R} \sum_{s \in S} \int_0^{q_{rs}} D_{rs}^{-1} (\omega) \ \mathrm{d} \omega
\\
\text{s.t.} \quad & x_a = \sum \limits_{r \in R} \sum \limits_{s \in S} \sum \limits_{k \in K_{rs}} \delta_{ak}^{rs} \cdot f_{k}^{rs}, & \forall a \in A
\\
& \sum \limits_{k \in K_{rs}}f_{k}^{rs} = q_{rs} \ ,
  & \forall r \in R, \ \forall s \in S
\\
& f_{k}^{rs} \geq 0 \ ,
  & \forall k \in K_{rs}, \ \forall r \in R, \ \forall s \in S
\\
& q_{rs} \geq 0, & \forall r \in R, \ \forall s \in S
\end{array}
$$

The mode has unique solution in terms of link flow $\{ x_a, a \in A \}$ and O-D demand $\{q_{rs}, r \in R, s \in S \}$

Transform the formulation in terms of path flow $f^{rs}_{k}$ and travel demand $q_{rs}$ :
$$
\begin{align*}
& \min z(\boldsymbol{f}, \boldsymbol{q})
  = \displaystyle \sum_{a \in A} \int_0^{x_a(\boldsymbol{f})} t_a (\omega) \, \mathrm{d} \omega
  - \sum_{r \in R} \sum_{s \in S} \int_0^{q_{rs}} D_{rs}^{-1} (\omega) \ \mathrm{d} \omega
\\
& \quad \ \ \ \begin{array}{lll}
  \text{s.t.} \quad & \sum \limits_{k \in K_{rs}}f_{k}^{rs} = q_{rs} \ ,
    & \forall r \in R, \ \forall s \in S \\
  & f_{k}^{rs} \geq 0, & \forall k \in K_{rs}, \ \forall r \in R, \ \forall s \in S \\
  & q_{rs} \geq 0, & \forall r \in R, \ \forall s \in S
\end{array}
\end{align*}
$$

where $x_a(\boldsymbol{f})$:
$$
x_a(\boldsymbol{f}) = \sum_{r \in R} \sum_{s \in S} \sum_{k \in K_{rs}} \delta_{ak}^{rs} \, f_{k}^{rs}
$$

#### KKT conditions

The Lagrangian Funtion is:
$$
\begin{align*}
L(\boldsymbol{f}, \boldsymbol{q}, \boldsymbol{u}, \boldsymbol{\mu}, \boldsymbol{\lambda})
\ = \ & z(\boldsymbol{f}, \boldsymbol{q}) + \sum_{r} \sum_{s} u_{rs} \left( \sum_{k \in K_{rs}}f_{k}^{rs} - q_{rs} \right) + \\
& \sum_{r} \sum_{s} \sum_{k} \big[\mu^{rs}_{k} \cdot (-f_{k}^{rs}) \big] + \sum_{r} \sum_{s} \big[\lambda_{rs} \cdot (-q_{rs}) \big]
\end{align*}
$$

where $\boldsymbol{u}$, $\boldsymbol{\mu} \geq \boldsymbol{0}$, $\boldsymbol{\lambda} \geq \boldsymbol{0}$ are Lagrangian multipliers.

The optimal solution satisfying the following DUE conditions:
$$
\begin{array}{rl}
f_k^{rs} (c_k^{rs} - u_{rs}) = 0, & \forall k \in K_{rs}, \ \forall r \in R, \ \forall s \in S \\
c_k^{rs} - u_{rs} \geq 0, & \forall k \in K_{rs}, \ \forall r \in R, \ \forall s \in S \\
q_{rs} \left[u_{rs} - D_{rs}^{-1}(q_{rs}) \right] = 0, & \forall r \in R, \ \forall s \in S \\
u_{rs} - D_{rs}^{-1}(q_{rs}) \geq 0, & \forall r \in R, \ \forall s \in S \\
\displaystyle \sum_{k \in K_{rs}} f_{k}^{rs} = q_{rs}, & \forall r \in R, \ \forall s \in S \\
 f_{k}^{rs} \geq 0, & \forall k \in K_{rs}, \ \forall r \in R, \ \forall s \in S \\
q_{rs} \geq 0, & \forall r \in R, \ \forall s \in S
\end{array}
$$

#### Uniqueness Conditions

The objective function
$$
z(\boldsymbol{x}, \boldsymbol{q}) = z_1(\boldsymbol{x}) - z_2(\boldsymbol{q})
$$
is the sum of two strictly convex functions. Thus, z(\boldsymbol{x}, \boldsymbol{q}) is strictly convex.

### 4.2 Solution Algorithm

$$
\begin{align*}
& \min z(\boldsymbol{x}, \boldsymbol{q})
  = \displaystyle \sum_{a \in A} \int_0^{x_a} t_a (\omega) \, \mathrm{d} \omega
  - \sum_{r \in R} \sum_{s \in S} \int_0^{q_{rs}} D_{rs}^{-1} (\omega) \ \mathrm{d} \omega
\\
& \qquad \quad \begin{array}{lll}
  \text{s.t.} \quad & \displaystyle x_a = \sum_{r \in R} \sum_{s \in S} \sum_{k \in K_{rs}} \delta_{ak}^{rs} \cdot f_{k}^{rs}, & \forall a \in A \\
  & \displaystyle \sum_{k \in K_{rs}}f_{k}^{rs} = q_{rs}, & \forall r \in R, \ \forall s \in S \\
  & q_{rs} \leq \bar{q}_{rs}, & \forall r \in R, \ \forall s \in S \\
  & \displaystyle f_{k}^{rs} \geq 0, & \forall k \in K_{rs}, \ \forall r \in R, \ \forall s \in S \\
  & q_{rs} \geq 0, & \forall r \in R, \ \forall s \in S
\end{array}
\end{align*}
$$

where $\bar{q}_{rs}$ is the upper bound of travel demand $q_{rs}$. This constraint is added for compu tational reasons.

Transform the formulation in terms of path flow $f^{rs}_{k}$ :
$$
\begin{align*}
& \min z(\boldsymbol{f})
  = \displaystyle \sum_{a \in A} \int_0^{x_a(\boldsymbol{f})} t_a (\omega) \, \mathrm{d} \omega
  - \sum_{r \in R} \sum_{s \in S} \int_0^{q_{rs}(\boldsymbol{f}^{rs})} D_{rs}^{-1} (\omega) \ \mathrm{d} \omega
\\
& \quad \ \ \ \begin{array}{lll}
  \text{s.t.} \quad & \displaystyle \sum_{k \in K_{rs}}f_{k}^{rs} \leq \bar{q}_{rs}, & \forall r \in R, \ \forall s \in S \\
  & \displaystyle f_{k}^{rs} \geq 0, & \forall k \in K_{rs}, \ \forall r \in R, \ \forall s \in S \\
  & q_{rs} \geq 0, & \forall r \in R, \ \forall s \in S
\end{array}
\end{align*}
$$

where $x_a(\boldsymbol{f})$ and $q_{rs}(\boldsymbol{f^{rs})}$:
$$
\begin{align*}
x_a(\boldsymbol{f}) & = \sum_{r \in R} \sum_{s \in S} \sum_{k \in K_{rs}} \delta_{ak}^{rs} \, f_{k}^{rs}\\
q_{rs}(\boldsymbol{f}^{rs}) &= \sum_{k \in K_{rs}}f_{k}^{rs}
\end{align*}
$$

**Step 0 :** *Initialization.* Find an initial feasible flow pattern $\big\{ x_a^{(0)} \big\}$, $\big\{ q_{rs}^{(0)} \big\}$. Set $n:= 1$.

**Step 1:** *Update.* Set $t_a^{(n)}=t_a(x_a^{(n)}), \forall \, a$ ; compute $D_{rs}^{-1}(q_{rs}^{(n)}), \forall \, r, s$

**Step 2:** *Direction finding.* For each O-D pair $r\text{-}s$:

**Step 2.1:** Compute the shortest path, $m$, between each based on $\big\{ t_a^{(n)} \big\}$. Then get:
$$
c_{m}^{rs^{(n)}} = \min_{\forall \, k} \left\{c_k^{rs^{(n)}} \right\}
$$
where $c_{m}^{rs^{(n)}}$ is the minimal travel time of the O-D pair $r\text{-}s$ at the $n$th iteration

**Step 2.2:** Execute the assignment rule according to:
$$
\begin{align*}
& \text{If } \ c_{m}^{rs^{(n)}} < D^{-1}(q_{rs}^{(n)}), \quad
  \text{ set } \ g^{rs^{(n)}}_{m} = \bar{q}_{rs}
  \text{ and } \ g^{rs^{(n)}}_{k}, \ \forall \, k \neq m
\\
& \text{If } \ c_{m}^{rs^{(n)}} \geq D^{-1}(q_{rs}^{(n)}), \quad
  \text{ set } \ g^{rs^{(n)}}_{k} = 0, \ \forall \, k
\end{align*}
$$
where $g^{rs^{(n)}}_{k}$ are auxiliary **path flow**

This assignment yields an auxiliary flow pattern: **link flow** $\big\{ y_a^{n} \big\}$ and **travel demand** $\big\{ v_{rs}^{n} \big\}$
$$
\begin{array}{ll}
y_a^{(n)} = \sum \limits_{r} \sum \limits_{s} \sum \limits_{k} g^{rs^{(n)}}_{k} \, \delta_{ak}^{rs},
  & \forall \, a
\\
v_{rs}^{(n)} = \sum \limits_{k} g_{k}^{rs^{(n)}},
  & \forall \, r,s
\end{array}
$$

**Step 3:** *Move size.* Find $\alpha_n$ that solves program
$$
\begin{align*}
& \min_{\alpha} z(\alpha)
  = \displaystyle \sum_{a \in A} \int_0^{x_a^{(n)} + \alpha \left(y_{a}^{(n)} - x_{a}^{(n)} \right)} t_a (\omega) \, \mathrm{d} \omega
  - \sum_{r \in R} \sum_{s \in S} \int_0^{q_{rs}^{(n)} + \alpha \left(v_{rs}^{(n)} - q_{rs}^{(n)}\right)} D_{rs}^{-1} (\omega) \ \mathrm{d} \omega
\\
& \quad \text{s.t.} \qquad \quad 0 \leq \alpha \leq 1
\end{align*}
$$

**Step 4:** *Flow update.* Find $\big\{ x_a^{(n+1)} \big\}$ and $\big\{ q_{rs}^{(n+1)} \big\}$
$$
\begin{align*}
x_a^{(n+1)} &= x_a^{(n)} + \alpha_n (y_{a}^{(n)} - x_{a}^{(n)}), \quad \forall \, a
\\
q_{rs}^{(n+1)} &= q_{rs}^{(n)} + \alpha_n (v_{rs}^{(n)} - q_{rs}^{(n)}), \quad \ \forall \, r,s
\end{align*}
$$

**Step 5:** *Convergence criterion.* If the criterion
$$
\sum_{r} \sum_{s} \frac{ \left|D^{-1}_{rs}(q_{rs}^{(n)} )- u_{rs}^{(n)} \right|}{u_{rs}^{(n)}} + \sum_{r} \sum_{s} \frac{ \left|u_{rs}^{(n)} - u_{rs}^{(n-1)} \right|}{u_{rs}^{(n)}} \leq \varepsilon
$$
is satisfied, terminate.

Otherwise, set $n := n + 1$ and go to **Step 1**.


## 5. Solution By Network Representation

### 5.1 The Zero-Cost Overflow Formulation

### 5.2 Excess-Demand Formulation

#### (1) Excess Demand

By introdcing the **upper bound** of travel demand $\bar{q}_{rs}$, namely, $\bar{q}_{rs} = D_{rs}(u_{rs}=0)$. Then the objective function $z(\boldsymbol{x}, \boldsymbol{q})$ can be rewritten as:

$$
\begin{align*}
z(\boldsymbol{x}, \boldsymbol{q})
&= \sum_{a \in A} \int_0^{x_a} t_a (\omega) \, \mathrm{d} \omega
- \sum_{r \in R} \sum_{s \in S} \int_0^{q_{rs}} D_{rs}^{-1} (\omega) \ \mathrm{d} \omega
\\
&= \sum_{a \in A} \int_0^{x_a} t_a (\omega) \, \mathrm{d} \omega
- \sum_{r \in R} \sum_{s \in S} \left[ \int_0^{q_{rs}} D_{rs}^{-1} (\omega) \ \mathrm{d} \omega + \int_{q_{rs}}^{\bar{q}_{rs}} D_{rs}^{-1} (\omega) \ \mathrm{d} \omega \right]
\\
&= \sum_{a \in A} \int_0^{x_a} t_a (\omega) \, \mathrm{d} \omega
- \sum_{r \in R} \sum_{s \in S} \left[ \int_0^{\bar{q}_{rs}} D_{rs}^{-1} (\omega) \ \mathrm{d} \omega - \int_{q_{rs}}^{\bar{q}_{rs}} D_{rs}^{-1} (\omega) \ \mathrm{d} \omega \right]
\end{align*}
$$

where $\displaystyle \int_0^{\bar{q}_{rs}} D_{rs}^{-1} (\omega) \ \mathrm{d} \omega$ is a constant item.

Then, by introducing the **excess demand** with a simple change of variable : $e_{rs} = \bar{q}_{rs} - q_{rs}$. The new variable of integration is $v = \bar{q}_{rs} - \omega$, then we will have:

$$
\begin{align*}
z(\boldsymbol{x}, \boldsymbol{q})
&= \sum_{a \in A} \int_{0}^{x_{a}} t_{a}(\omega) \, \mathrm{d} \omega-\sum_{r \in R} \sum_{s \in S} \left[\int_{0}^{\bar{q}_{r s}} D^{-1}(\omega) \, \mathrm{d} \omega-\int_{\bar{q}_{r s}-q_{r s}}^{0} D_{r s}^{-1} (\bar{q}_{r s}-v) \, \mathrm{d} (\bar{q}_{r s}-v) \right]
\\
&=\sum_{a \in A} \int_{0}^{x_{a}} t_{a}(\omega) \, \mathrm{d} \omega
  - \sum_{r \in R} \sum_{s \in S} \left[\int_{0}^{\bar{q}_{r s}} D^{-1}(\omega) \, \mathrm{d} \omega-\int_{0}^{\bar{q}_{r s}-q_{r s}} D_{r s}^{-1}\left(\bar{q}_{r s}-v\right) \, \mathrm{d} v\right]
\\
&=\sum_{a \in A} \int_{0}^{x_{a}} t_{a}(\omega) \, \mathrm{d} \omega
  + \sum_{r \in R} \sum_{s \in S} \int_{0}^{\bar{q}_{r s}-q_{r s}} D_{r s}^{-1} \left(\bar{q}_{r s}-v\right) \, \mathrm{d} v
  - \sum_{r \in R} \sum_{s \in S} \left[\int_{0}^{\bar{q}_{r s}} D^{-1}(\omega) \, \mathrm{d} \omega \right]
\end{align*}
$$

By introducing **excess-demand function**, defined as:
$$
W_{rs}(e_{rs}) = D^{-1}_{rs} (\bar{q}_{rs} - e_{rs})
$$

#### (2) Formulation

Then, we will have the following **formulations**:
$$
\begin{array}{rll}
\min z_1(\boldsymbol{x}, e)
= & \displaystyle \sum_{a \in A} \int_0^{x_a} t_a (\omega) \, \mathrm{d} \omega
  + \sum_{r \in R} \sum_{s \in S} \int_0^{e_{rs}} W_{rs} (v) \ \mathrm{d} v
\\
\text{s.t.} \quad & \displaystyle x_a = \sum_{r \in R} \sum_{s \in S} \sum_{k \in K_{rs}} f_{k}^{rs} \delta_{ak}^{rs}, & \forall a \in A
\\
& \displaystyle \sum_{k \in K_{rs}} f_{k}^{rs} + e_{rs} = \bar{q}_{rs} \ ,
  & \forall r \in R, \ \forall s \in S
\\
& f^{rs}_k \geq 0, & \forall k \in K_{rs}, r \in R, \ \forall s \in S
\\
& e_{rs} \geq 0, & \forall r \in R, \ \forall s \in S
\end{array}
$$

It can be regarded as the **DUE formulation** by intrducing a **directly dummy link** between every O-D pairs with travel time function (excess-demand function): $W_{rs}(e_{rs}) = D^{-1}_{rs} (\bar{q}_{rs} - e_{rs})$.

#### (3) Solutions

Any algorithms that can solve the DUE problem with fixed demand can be directly used to solve the DUE problem with elastic demand based on the reformulated network with dummy links.
