
# Recursion

Recursion is a technique where a function solves a problem by calling itself on a smaller input, until it reaches a **base case**.

## Key ideas

- **Base case**: the stopping condition that prevents infinite calls.
- **Recursive case**: the part that reduces the problem size (moves toward the base case).
- **Call stack**: each recursive call adds a new stack frame; deep recursion can hit Python’s recursion limit.

## Files in this folder

- `factorial.py`: factorial using recursion
- `fibonacci.py`: Fibonacci using recursion

## Factorial (recursion)

Definition:

$$n! = n \times (n-1)!$$

Base cases:

$$0! = 1, \; 1! = 1$$

Implementation summary (from `fact(n)`):

- If `n` is `0` or `1` → return `1`
- Otherwise → return `n * fact(n - 1)`

Complexity:

- Time: $O(n)$
- Space (call stack): $O(n)$

## Fibonacci (recursion)

Common sequence:

$$F(0)=0,\; F(1)=1,\; F(2)=1,\; F(n)=F(n-1)+F(n-2)$$

Implementation summary (from `fib(n)`):

- If `n <= 0` → return `0`
- If `n` is `1` or `2` → return `1`
- Otherwise → return `fib(n - 1) + fib(n - 2)`

Complexity (naive recursion):

- Time: $O(2^n)$ (recomputes the same subproblems many times)
- Space (call stack): $O(n)$

Note: for practical Fibonacci, add **memoization** (top-down DP) or use an iterative approach.

## How to run

From the repo root:

```bash
python "Recursion/factorial.py"
python "Recursion/fibonacci.py"
```

## Quick examples (in Python)

```py
from Recursion.factorial import fact
from Recursion.fibonacci import fib

print(fact(5))  # 120
print(fib(7))   # 13
```

