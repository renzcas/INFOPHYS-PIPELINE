import sympy as sp

class SymbolicOrgan:
    def __init__(self):
        self.x = sp.symbols('x')

    def step(self, value):
        expr = value * self.x**2 + 2*self.x + 1
        simplified = sp.simplify(expr)
        derivative = sp.diff(expr, self.x)

        return {
            "expr": str(expr),
            "simplified": str(simplified),
            "derivative": str(derivative)
        }