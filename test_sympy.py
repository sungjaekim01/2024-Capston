import sympy

# Juypter 노트북에서 수학식의 LaTeX 표현을 위해 필요함
sympy.init_printing(use_latex='mathjax')

x, mu, sigma = sympy.symbols('x mu sigma')
f = sympy.exp((x - mu) ** 2 / sigma ** 2)
print(f)
print(sympy.diff(f, x))
print(sympy.simplify(sympy.diff(f, x)))
print(sympy.diff(f, x, x))