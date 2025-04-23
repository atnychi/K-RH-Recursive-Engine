# Ghost Zeta Simulation – K-RH Recursive Engine

This document explains how to use `krh_engine.py` to simulate symbolic collapse behavior for the recursive Riemann Hypothesis verifier.

## How It Works

The engine uses a symbolic variant of the zeta function:
\[
\zeta_\varepsilon(s) = \sum_{n=1}^\infty e^{-\Omega_\varepsilon(n)s}
\]

Where `Ω_ε(n)` is symbolically represented by the linear term `n`, preserving recursive structure in the public implementation.

## Inputs

You can test values like:

```python
k_rh_engine_test(0.5 + 14*I)  # Collapse expected
k_rh_engine_test(0.3 + 10*I)  # Divergence expected
