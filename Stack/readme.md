## Day 4: Stack

A **Stack** is a linear data structure that follows **LIFO** (Last In, First Out).

This folder contains a simple stack implementation in [Stack/Stack.py](Stack.py) using a Python `list`.

## Implementation notes

The class is named `stack` and stores items in `self.s`.

It demonstrates two ways to simulate stack behavior:

### 1) Using the front of the list (index `0`)

- `pushf(value)`: inserts at index `0`
- `peekf()`: returns `self.s[0]`
- `popf()`: removes and returns `self.s.pop(0)`

Complexity:

- `insert(0, x)` and `pop(0)` are **O(n)** because elements shift.

### 2) Using the end of the list (recommended)

- `pushl(value)`: uses `append(value)`
- `peekl()`: returns `self.s[-1]`
- `popl()`: uses `pop()`

Complexity:

- `append(x)` and `pop()` are typically **O(1)** amortized.

## Helpers

- `length()`: number of elements in the stack
- `isEmpty()`: returns `True` if stack is empty

Empty-stack behavior:

- `peekf/peekl/popf/popl` raise `Exception("Stack is empty")` when the stack has no elements.

## Example usage

```py
from Stack import stack

stk = stack()

stk.pushl(10)
stk.pushl(20)
stk.pushl(30)

print(stk.peekl())  # 30
print(stk.popl())   # 30
print(stk.popl())   # 20
print(stk.length()) # 1
```

## Run

```bash
python "Stack/Stack.py"
```
