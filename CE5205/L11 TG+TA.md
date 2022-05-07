# Combined Trip Distribution and Traffic Assignment Model

**Assumption: ** Motorists try to accomplish two goals:

- travel to the destination with the **highest attraction measure**
- while spending the **least possible time** in travel.

Under this assumption the choice of destination is the result of a **trade-off** between attraction and travel time.

## 1. Fixed-Demand Equivalent UE Program

**Assumption :**

- $M_s$ is an attraction measure on destination $s$. It reflects the activity opportunities available.

  $M_s$ has to be specified in travel time units in order to be compatible with the network travel times.

- The total flow originating at each source node, $r$, is fixed to be $O_r$.

- $u_{rs}$ is the travel time on the minimum path from $r$ to $s$

- Travelers are assumed to choose destinations that are attractive (high $M_s$ value), on the one hand, and close by (low $u_{rs}$ value), on the other.

  Thus, destinations are chosen so that the difference, ($M_s - u_{rs}$), is maximized.

  That is a minimization of the **net travel impedance** $u_{rs} - M_s$

### 1.1 Formualation
$$
\begin{align*}
& \min z(\boldsymbol{x}, \boldsymbol{q}) = \sum_{a \in A} \int_0^{x_a} t_a (\omega) \, \mathrm{d} \omega - \sum_{r \in R} \sum_{s \in S} M_{s} q_{rs}
\\
& \qquad \quad \begin{array}{lll}
  \text{s.t.} \quad & \sum \limits_{s \in S} q_{rs} = O_r, & \forall r \in R \\
  & \sum \limits_{k \in K_{rs}} f_{k}^{rs} = q_{rs}, & \forall r \in R, \ \forall s \in S \\
  & f_{k}^{rs} \geq 0, & \forall k \in K_{rs}, \ \forall r \in R, \ \forall s \in S \\
  & q_{rs} \geq 0, & \forall r \in R, \ \forall s \in S
\end{array}
\end{align*}
$$

### 1.2 KKT conditions

According to KKT condition:
$$
\begin{array}{rl}
f_k^{rs} (c_k^{rs} - u_{rs}) = 0, & \forall k \in K_{rs}, \ \forall r \in R, \ \forall s \in S
\\
c_k^{rs} - u_{rs} \geq 0, & \forall k \in K_{rs}, \ \forall r \in R, \ \forall s \in S
\\
q_{rs} \left[(u_{rs} - M_s) - \mu_r \right] = 0, & \forall r \in R, \ \forall s \in S
\\
(u_{rs} - M_s) - \mu_r \geq 0, & \forall r \in R, \ \forall s \in S
\\
\sum \limits_{s \in S} q_{rs} = O_r, & r \in R
\\
\sum \limits_{k \in K_{rs}} f_{k}^{rs} = q_{rs}, & \forall r \in R, \ \forall s \in S
\\
f_{k}^{rs} \geq 0, & \forall k \in K_{rs}, \ \forall r \in R, \ \forall s \in S
\\
q_{rs} \geq 0, & \forall r \in R, \ \forall s \in S
\end{array}
$$

This model:

- Fulfill DUE conditions

### 1.3 Solutions



## 2. Distribution / Assignment with Destination Demand functions

### 2.1


## 3. Combining the entropy concept

### 3.1 Formulation

$$
\begin{align*}
& \min z(\boldsymbol{x}, \boldsymbol{q})
  = \sum_{a \in A} \int_0^{x_a} t_a (\omega) \, \mathrm{d} \omega
  - \frac{1}{\beta} \sum_{r \in R} \sum_{s \in S} \big[ q_{rs} \times (\ln q_{rs} - 1) \big]
\\
& \qquad \quad \begin{array}{lll}
  \text{s.t.} \quad & \sum \limits_{s \in S} q_{rs} = D_r, & r \in R \\
  & \sum \limits_{r \in R} q_{rs} = D_s, & s \in S \\
  & \sum \limits_{k \in K_{rs}}f_{k}^{rs} = q_{rs}, \ & \forall r \in R, \ \forall s \in S \\
  & x_a = \sum \limits_{r \in R} \sum \limits_{s \in S} \sum \limits_{k \in K_{rs}} \delta_{ak}^{rs} \cdot f_{k}^{rs}, & \forall a \in A \\
  & f_{k}^{rs} \geq 0, \ & \forall k \in K_{rs}, \ \forall r \in R, \ \forall s \in S \\
  & q_{rs} \geq 0, & \forall r \in R, \ \forall s \in S
\end{array}
\end{align*}
$$

where $\beta$ is a parameter (calibrated from data).

This model:

- It is a strictly convex programming model

- The optimal solution of the above model is unique.

The optimal link flow and trip distribution solution:
$$
\begin{align*}
&x_a^{\text{DUE}}, \qquad \forall a \in A \\
&q_{rs}^{\text{DUE}}, \qquad \forall r \in R, s \in S
\end{align*}
$$
where $q_{rs}^{\text{DUE}} = \alpha_r \gamma_s \exp(-\beta \, c_{rs}^{\text{DUE}})$

### 3.2 Proof using the KKT conditions

#### (1) Lagrangian function

The Lagrangian function of the formulation with respect to **path flow** $\boldsymbol{f}$ and **travel demand** $\boldsymbol{q}$
$$
L\left(\boldsymbol{x}, \boldsymbol{q}, \right)
$$

#### (2) KKT Equation

The derivatives of the Lagrangian function with respect to the O-D flow variable $q_{rs}$ are given by:
$$
\frac{L}{\partial q_{rs}} = \frac{1}{\beta} \, \ln q_{rs} + \mu_{rs} - \mu_r - \lambda_s =0, \quad \forall r \in R, \forall s \in S
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

#### (3)

When these expressions are substituted into the flow conservation constraints, the result is:
$$
\begin{align*}
\exp(\beta \, \mu_r) &= \frac{O_r}{\sum \limits_{s \in S} \exp \big[ -\beta \, (\mu_{rs} - \lambda_s) \big]}, \quad \forall r \in R
\\
\exp(\beta \, \lambda_s) &= \frac{D_s}{\sum \limits_{r\in R} \exp \big[ -\beta \, (\mu_{rs} - \mu_r) \big]}, \quad \forall s \in S
\end{align*}
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
\begin{align*}
A_r &= \frac{1}{\displaystyle \sum_{s \in S} B_s D_s \exp \left(-\beta \, c_{rs}^{\text{DUE}} \right)}, \quad \forall r \in R
\\
B_s &= \frac{1}{\displaystyle \sum_{r \in R} A_r O_r \exp \left(-\beta \, c_{rs}^{\text{DUE}} \right)}, \quad \forall s \in S
\end{align*}
$$

### 3.3 Frank-Wolfe Method

**Step 0: Initialization :** Find a feasible solution $\{ q_{rs}^{n}\}$, $\{x_{a}^{n}\}$. Set $n:=1$

**Step 1: Travel time update :** Set $t_a^n = t_a(x_a^n)$

**Step 2: Direction finding :**

- a) Compute $\{u_{rs}^{n}\}$; Set $c_{rs}^n = u_{rs}^n + \frac{1}{\beta} \, \ln q_{rs}^n$ (Sheffi, 1985, p.p.189-197)

- b) Solve **Hitchcock's transportation problem with** costs
This yields with costs $\{c_{rs}^{n}\}$. This yields $\{v_{rs}^{n}\}$.

- c) Assign $\{v_{rs}^n\}$ to the minimum paths identified in **a)**. This yields $\{y_a^n\}$.

**Step 3: Move-size determination :** Find $x^{n}_{a}$ that solves:
$$
\begin{align*}
\min_{0 \leq \alpha_n \leq 1} & \sum_a \int_0^{\textstyle x_{\alpha}^n + \alpha_n (y_{\alpha}^n - x_{\alpha}^n)} t_a (\omega) \, \mathrm{d} \, \omega \\
&+ \frac{1}{\beta} \sum_{r \in R} \sum_{s \in S} \big[q_{rs}^n + \alpha_n (v_{rs}^n - q_{rs}^n) \big] \big\{ \ln \left[ q_{rs}^n + \alpha_n (v_{rs}^n - q_{rs}^n) \right] - 1 \big\}
\end{align*}
$$

**Step 4: Flow update :** Set
$$
\begin{align*}
x^{n+1}_{a} &= x^n_a + \alpha_a (y^n_a - x^n_a),
\quad \forall a \in A
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
