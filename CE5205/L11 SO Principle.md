# Traffic Assignment - System Optimum (SO) Principle and Extension of DUE Principle

## 1. System Optimum (SO) Principle

### 1.1 Wardrop's Second Principle (SO Principle)

> The average journal travel time is minimal (Wardrop, 1952)

Average journey travel time:

$$
\frac{
  \displaystyle \sum_{r \in R} \sum_{s \in S} \sum_{k \in K_{r s}}\left[c_{k}^{r s} \times f_{k}^{r s}\right]
  }{
  \displaystyle \sum_{r \in R} \sum_{s \in S} q_{r s}
}
$$

Total system travel time
$$
\tilde{z}(\boldsymbol{x})=\sum_{a \in A}\left[t_{a}\left(x_{a}\right) \times x_{a}\right]
$$

### 1.2 System Optimum Formulation

A Convex Programming Model
$$
\begin{array}{rll}
\displaystyle \min_{\boldsymbol{x}} \tilde{z}(\boldsymbol{x}) =& \displaystyle \sum_{a \in A} x_{a} \cdot t_{a} \left(x_{a}\right)
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
\displaystyle x_a = \sum_{r \in R} \sum_{s \in S} \sum_{k \in K_{rs}} \delta_{ak}^{rs} \cdot f_{k}^{rs}, & \forall a \in A
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

**Assumption:** The travel demand (i.e., trip rate) from origin $r$ to destination $s$, $q_{rs}$, is a decreasing function of the travel time/cost from the origin to the destination denoted by $u_{rs}$
$$
q_{rs} = D_{rs}(u_{rs}),
\qquad
u_{rs} = D^{-1}_{rs}(q_{rs}) \ (\text{inverse function})
$$
where $q_{rs}$ usually is a decrease function with respect to $u_{rs}$.

### 4.1 Formulation

**Strictly convex programming model**
$$
\begin{array}{rll}
\min z(\boldsymbol{x}, \boldsymbol{q})
= & \displaystyle \sum_{a \in A} \int_0^{x_a} t_a (\omega) \, \mathrm{d} \omega
- \sum_{r \in R} \sum_{s \in S} \int_0^{q_{rs}} D_{rs}^{-1} (\omega) \ \mathrm{d} \omega
\\
\text{s.t.} \quad & \displaystyle x_a = \sum_{r \in R} \sum_{s \in S} \sum_{k \in K_{rs}} \delta_{ak}^{rs} \cdot f_{k}^{rs}, & \forall a \in A
\\
&\displaystyle \sum_{k \in K_{rs}}f_{k}^{rs} = q_{rs} \ ,
  & \forall r \in R, \ \forall s \in S
\\
& \displaystyle f_{k}^{rs} \geq 0 \ ,
  & \forall k \in K_{rs}, \ \forall r \in R, \ \forall s \in S
\\
& q_{rs} \geq 0, & \forall r \in R, \ \forall s \in S
\end{array}
$$
The mode has unique solution in terms of link flow $\{ x_a, a \in A \}$ and O-D demand $\{q_{rs}, r \in R, s \in S \}$

The optimal solution satisfying the following DUE conditions:
$$
\begin{array}{rl}
f_k^{rs} (c_k^{rs} - u_{rs}) = 0, & \forall k \in K_{rs}, \ \forall r \in R, \ \forall s \in S \\
c_k^{rs} - u_{rs} \geq 0, & \forall k \in K_{rs}, \ \forall r \in R, \ \forall s \in S \\
q_{rs} \left(u_{rs} - D_{rs}^{-1}(q_{rs}) \right) = 0, & \forall r \in R, \ \forall s \in S \\
u_{rs} - D_{rs}^{-1}(q_{rs}) \geq 0, & \forall r \in R, \ \forall s \in S \\
\displaystyle \sum_{k \in K_{rs}} f_{k}^{rs} = q_{rs}, & \forall r \in R, \ \forall s \in S \\
 f_{k}^{rs} \geq 0, & \forall k \in K_{rs}, \ \forall r \in R, \ \forall s \in S \\
q_{rs} \geq 0, & \forall r \in R, \ \forall s \in S
\end{array}
$$

### 4.2 Solution by Excess-Demand Network Representation

$$
\begin{align*}
\min z(\boldsymbol{x}, \boldsymbol{q})
&= \sum_{a \in A} \int_0^{x_a} t_a (\omega) \, \mathrm{d} \omega
- \sum_{r \in R} \sum_{s \in S} \int_0^{q_{rs}} D_{rs}^{-1} (\omega) \ \mathrm{d} \omega
\\
&= \sum_{a \in A} \int_0^{x_a} t_a (\omega) \, \mathrm{d} \omega
- \sum_{r \in R} \sum_{s \in S} \left[ \int_0^{\bar{q}_{rs}} D_{rs}^{-1} (\omega) \ \mathrm{d} \omega - \int_{q_{rs}}^{\bar{q}_{rs}} D_{rs}^{-1} (\omega) \ \mathrm{d} \omega \right]
\end{align*}
$$

where $\bar{q}_{rs}$ is the **upper bound** of travel demand from origin $r$ to destination $s$, namely, $\bar{q}_{rs} = D_{rs}(u_{rs}=0.0)$. And $\displaystyle \int_0^{\bar{q}_{rs}} D_{rs}^{-1} (\omega) \ \mathrm{d} \omega$ is a constant item.

Let $v = \bar{q}_{rs} - \omega$, we have:
$$
\begin{align*}
z(\boldsymbol{x}, \boldsymbol{q})
&= \sum_{a \in A} \int_{0}^{x_{a}} t_{a}(\omega) \, \mathrm{d} \omega-\sum_{r \in R} \sum_{s \in S} \left[\int_{0}^{\bar{q}_{r s}} D^{-1}(\omega) \, \mathrm{d} \omega-\int_{\bar{q}_{r s}-q_{r s}}^{0} D_{r s}^{-1} (\bar{q}_{r s}-v) \, \mathrm{d} (\bar{q}_{r s}-v) \right]
\\
&=\sum_{a \in A} \int_{0}^{x_{a}} t_{a}(\omega) \, \mathrm{d} \omega-\sum_{r \in R} \sum_{s \in S} \left[\int_{0}^{\bar{q}_{r s}} D^{-1}(\omega) \, \mathrm{d} \omega-\int_{0}^{\bar{q}_{r s}-q_{r s}} D_{r s}^{-1}\left(\bar{q}_{r s}-v\right) \, \mathrm{d} v\right]
\\
&=\sum_{a \in A} \int_{0}^{x_{a}} t_{a}(\omega) \, \mathrm{d} \omega+\int_{0}^{\bar{q}_{r s}-q_{r s}} D_{r s}^{-1} \left(\bar{q}_{r s}-v\right) \, \mathrm{d} v-\sum_{r \in R} \sum_{s \in S} \left[\int_{0}^{\bar{q}_{r s}} D^{-1}(\omega) \, \mathrm{d} \omega \right]
\end{align*}
$$

**Excess-demand function** is defined as:
$$
W_{rs}(e_{rs}) = D^{-1}_{rs} (\bar{q}_{rs} - e_{rs})
$$

Formulation:

$$
\begin{array}{rll}
\min z_1(\boldsymbol{x}, e)
= & \displaystyle \sum_{a \in A} \int_0^{x_a} t_a (\omega) \, \mathrm{d} \omega
- \int_0^{e_{rs}} W_{rs} (v) \ \mathrm{d} v
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

**Conclusion:** Any algorithms that can solve the DUE problem with fixed demand can be directly used to solve the DUE problem with elastic demand based on the reformulated network with dummy links.

## 5. Combined Trip Distribution and Traffic Assignment Model

### 5.1 Formulation

$$
\begin{array}{rll}
\min z(\boldsymbol{x}, \boldsymbol{q})
= & \displaystyle \sum_{a \in A} \int_0^{x_a} t_a (\omega) \, \mathrm{d} \omega
- \frac{1}{\beta} \sum_{r \in R} \sum_{s \in S} \big[ q_{rs} \times (\ln q_{rs} - 1) \big]
\\
\text{s.t.} \quad & \displaystyle \sum_{s \in S} q_{rs} = D_r, & r \in R
\\
& \displaystyle \sum_{r \in R} q_{rs} = D_s, & s \in S
\\
& \displaystyle x_a = \sum_{r \in R} \sum_{s \in S} \sum_{k \in K_{rs}} \delta_{ak}^{rs} \cdot f_{k}^{rs}, & \forall a \in A
\\
&\displaystyle \sum_{k \in K_{rs}}f_{k}^{rs} = q_{rs} \ ,
  & \forall r \in R, \ \forall s \in S
\\
& \displaystyle f_{k}^{rs} \geq 0 \ ,
  & \forall k \in K_{rs}, \ \forall r \in R, \ \forall s \in S
\\
& q_{rs} \geq 0, & \forall r \in R, \ \forall s \in S
\end{array}
$$

- It is a strictly convex programming model

- The optimal solution of the above model is unique.

- The optimal link flow and trip distribution solution:
$$
\begin{align*}
&x_a^{\text{DUE}}, \qquad \forall a \in A \\
&q_{rs}^{\text{DUE}}, \qquad \forall r \in R, s \in S
\end{align*}
$$
where $q_{rs}^{\text{DUE}} = \alpha_r \gamma_s \exp(-\beta c_{rs}^{\text{DUE}})$

### 5.1 Proof using the KKT conditions

The Lagrangian function is:
$$
L\left(\boldsymbol{x}, \boldsymbol{q}, \right)
$$

The derivatives of the Lagrangian function with respect to the O-D flow variable $q_{rs}$ are given by:
$$
\frac{1}{\beta} \, \ln q_{rs} + \mu_{rs} - \mu_r - \lambda_s =0, \quad \forall r \in R, \forall s \in S
$$

These equations imply that:
$$
\begin{align*}
q_{rs} &= \exp \big[ -\beta (\mu_{rs} - \mu_r - \lambda_s) \big]
\\
&= \exp \big( -\beta \mu_{rs} \big) \cdot \exp \big( \beta \mu_r \big) \cdot \exp \big( \beta \lambda_s \big),
\quad \forall r \in R, \forall s \in S
\end{align*}
$$

When these expressions are substituted into the flow conservation constraints, the result is:
$$
\exp(\beta \mu_r) = \frac{O_r}{\displaystyle \sum_{s \in S} \exp \big[ -\beta \, (\mu_{rs} - \lambda_s) \big]}, \ \forall r \in R
\qquad
\exp(\beta \lambda_s) = \frac{D_s}{\displaystyle \sum_{r\in R} \exp \big[ -\beta \, (\mu_{rs} - \mu_r) \big]}, \ \forall s \in S
$$

According to UE condition:
$$
c_{rs}^{\text{DUE}} = \mu_{rs}, \quad \text{If} \ \  f_k^{rs}>0
$$

Using the above equations, trip distribution can be written as
$$
q_{rs}^{\text{DUE}} = \alpha_r \gamma_s \exp \left(-\beta \, c_{rs}^{\text{DUE}} \right)
$$
where $\alpha_r = O_r \, A_r$ and $\gamma_s = D_s \, B_s$

$$
A_r = \frac{1}{\displaystyle \sum_{s \in S} B_s D_s \exp \left(-\beta \, c_{rs}^{\text{DUE}} \right)},
\qquad
B_s = \frac{1}{\displaystyle \sum_{r \in R} A_r O_r \exp \left(-\beta \, c_{rs}^{\text{DUE}} \right)}
$$

### 5.2 Frank-Wolfe Method

**Step 0: Initialization :** Find a feasible solution $\{ q_{rs}^{n}\}$, $\{x_{a}^{n}\}$. Set $n:=1$

**Step 1: Travel time update :** Set $t_a^n = t_a(x_a^n)$

**Step 2: Direction finding :**

- a) Compute $\{u_{rs}^{n}\}$; Set $c_{rs}^n = u_{rs}^n + \frac{1}{\beta} \, \ln q_{rs}^n$ (Sheffi, 1985, p.p.189-197)

- b) Solve **Hitchcock's transportation problem with** costs
This yields with costs $\{c_{rs}^{n}\}$. This yields $\{v_{rs}^{n}\}$.

- c) Assign $\{v_{rs}^n\}$ to the minimum paths identified in **a)**. This yields $\{y_a^n\}$.

**Step 3: Move-size determination :** Find $x^{n}_{a}$ that solves:
$$
\min_{0 \leq \alpha_n \leq 1} \sum_a \int_0^{\textstyle x_{\alpha}^n + \alpha_n (y_{\alpha}^n - x_{\alpha}^n)} t_a (\omega) \, \mathrm{d} \, \omega +
\frac{1}{\beta} \sum_{r \in R} \sum_{s \in S} \big[q_{rs}^n + \alpha_n (v_{rs}^n - q_{rs}^n) \big] \big\{ \ln \left[ q_{rs}^n + \alpha_n (v_{rs}^n - q_{rs}^n) \right] - 1 \big\}
$$

**Step 4: Flow update :** Set
$$
\begin{align*}
x^{n+1}_{a} &= x^n_a + \alpha_a (y^n_a - x^n_a),
\quad \forall \alpha \in R
\\
q^{n+1}_{rs} &= q^n_{rs} + \alpha_a (v^n_{rs} - q^n_{rs}), \quad \forall r \in R, \forall s \in S
\end{align*}
$$

**Step 5: Convergence criterion :** If the stop criterion is fulfilled:
$$
\sum_{a \in A} \frac{\left| x_a^{n+1} - x_a^n\right|}{x_a^n} \leq \varepsilon
$$
then stop, and output the results $x_a^{n+1}$.

Otherwise, set $n:=n+1$ and go to **step 1**.
