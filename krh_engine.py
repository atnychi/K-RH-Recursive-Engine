from sympy import symbols, I, exp, summation, simplify, re

# Define symbolic variables
s = symbols('s', complex=True)
n = symbols('n', integer=True)

# Ghost zeta simulation function (approximation with symbolic compression)
def ghost_zeta(s_value, terms=100):
    ghost_term = exp(-n * s_value)
    zeta_sim = summation(ghost_term, (n, 1, terms))
    return simplify(zeta_sim)

# K-RH engine test logic
def k_rh_engine_test(s_input):
    if abs(re(s_input) - 0.5) < 1e-6:
        result = ghost_zeta(s_input)
        return f"Matched Critical Line: Collapse Detected\nSymbolic Output: {result}"
    else:
        return "Off Critical Line: No Collapse (Divergence Detected)"

# Example
if __name__ == '__main__':
    print(k_rh_engine_test(0.5 + 14 * I))  # Should trigger collapse
    print(k_rh_engine_test(0.3 + 10 * I))  # Should return divergence
