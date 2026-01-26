
# Shorting (Sorting)

Learning Day 16: **Bubble Sort**
Learning Day 17: **Selection Sort**

## What I Have learned

- Bubble Sort is a simple comparison-based sorting algorithm.
- It repeatedly swaps adjacent elements if they are in the wrong order.
- After each pass, the largest remaining element “bubbles up” to the end.

### Selection Sort

- Selection Sort repeatedly selects the minimum element from the unsorted part.
- It swaps that minimum into the current position (growing a sorted prefix).
- Works in-place, but usually makes more swaps than needed compared to some other sorts.

## Complexity

- Time: $O(n^2)$ (average/worst), $O(n^2)$ in this implementation
- Space: $O(1)$ extra space (in-place)
- Stable: Yes (if only adjacent swaps are used, as in [BubbleSort.py](BubbleSort.py))

### Selection Sort

- Time: $O(n^2)$ (best/average/worst)
- Space: $O(1)$ extra space (in-place)
- Stable: No (typical selection sort swaps can change the order of equal elements)

## Code

- [BubbleSort.py](BubbleSort.py) — bubble sort function + example
- [SelectionSort.py](SelectionSort.py) — selection sort function + example

## Run

```bash
python "Shorting/BubbleSort.py"
```

```bash
python "Shorting/SelectionSort.py"
```

