# Solving Differential Equations - Task Summary

Overview
- Exercise to use GitHub Copilot to implement a solver for the ODE:
 $\frac{dy}{dt} = -2y + 1$ with the initial condition $y(0) = 0, 0 \leq t \leq 5$
- Goal: produce a working implementation, unit tests, and a short demo.


Task
- Implement a Python function that computes y(t) for given initial value y0 and array (or list) of times t.
- Write a simple numerical solver (explicit Euler) and an exact solver (closed-form) for comparison.
- Add unit tests that verify the numerical solver converges to the analytic solution.

How to use GitHub Copilot (suggested prompts)
- "Create a Python function solve_ode_euler(y0, t, dt) that returns an array of y using explicit Euler for dy/dt = -2*y + 1."
- "Create a Python function solve_ode_exact(y0, t) that returns the analytic solution (y0-1/2)*exp(-2*t)+1/2."
- "Write pytest tests that compare the Euler solver to the exact solver for several dt values and assert error decreases."

Optional: Use Copilot to help write a more generic solver for first order DEs. 