
# Shorting (Sorting)

Learning Day 16: **Bubble Sort**
Learning Day 17: **Selection Sort**
Learning Day 18: **Insertion Sort**
Learning Day 19: **Merge Sort**

## What I Have learned

- Bubble Sort is a simple comparison-based sorting algorithm.
- It repeatedly swaps adjacent elements if they are in the wrong order.
- After each pass, the largest remaining element “bubbles up” to the end.

### Bubble Sort — Algorithm Process

- Start from the beginning of the array.
- Compare adjacent elements `arr[j]` and `arr[j+1]`.
- If `arr[j] > arr[j+1]`, swap them.
- Continue until the end of the array (one pass).
- Repeat passes; after each pass, the largest remaining element is placed at the end.

### Selection Sort

- Selection Sort repeatedly selects the minimum element from the unsorted part.
- It swaps that minimum into the current position (growing a sorted prefix).
- Works in-place, but usually makes more swaps than needed compared to some other sorts.

### Selection Sort — Algorithm Process

- Divide the array into two parts: sorted prefix (left) and unsorted suffix (right).
- For each position `i` from left to right:
- Find the index of the minimum element in the unsorted part (`i..n-1`).
- Swap that minimum element with the element at position `i`.
- Move `i` forward; the sorted prefix grows.

### Insertion Sort

- Insertion Sort builds a sorted portion one element at a time.
- It takes the next element (key) and inserts it into the correct position in the already-sorted left part.
- Good for small arrays and nearly-sorted data.

### Insertion Sort — Algorithm Process

- Assume the first element is already sorted.
- Pick the next element as `key`.
- Shift all elements in the sorted part that are greater than `key` one position to the right.
- Insert `key` into the correct position.
- Repeat until the whole array is sorted.

### Merge Sort

- Merge Sort follows the **divide and conquer** approach.
- It splits the array into halves until single-element arrays remain.
- Then it merges those halves back together in sorted order.

### Merge Sort — Algorithm Process

- Divide the array into two halves.
- Recursively sort the left half.
- Recursively sort the right half.
- Merge the two sorted halves:
- Compare the first unmerged elements of both halves.
- Move the smaller element into the result and advance that half.
- After one half is exhausted, append the remaining elements of the other half.

## Complexity

- Time: $O(n^2)$ (average/worst), $O(n^2)$ in this implementation
- Space: $O(1)$ extra space (in-place)
- Stable: Yes (if only adjacent swaps are used, as in [BubbleSort.py](BubbleSort.py))

### Selection Sort

- Time: $O(n^2)$ (best/average/worst)
- Space: $O(1)$ extra space (in-place)
- Stable: No (typical selection sort swaps can change the order of equal elements)

### Insertion Sort

- Time: $O(n^2)$ (average/worst), $O(n)$ best-case (already sorted)
- Space: $O(1)$ extra space (in-place)
- Stable: Yes (when shifting elements, as in [InsertionSort.py](InsertionSort.py))

### Merge Sort

- Time: $O(n\log n)$ (best/average/worst)
- Space: $O(n)$ extra space (typical merge step uses temporary arrays, as in [MergeSort.py](MergeSort.py))
- Stable: Yes (when merging keeps equal elements in original order, as in `<=` comparison)

## Code

- [BubbleSort.py](BubbleSort.py) — bubble sort function + example
- [SelectionSort.py](SelectionSort.py) — selection sort function + example
- [InsertionSort.py](InsertionSort.py) — insertion sort function + example
- [MergeSort.py](MergeSort.py) — merge sort (divide + merge) + example

## Run

```bash
python "Shorting/BubbleSort.py"
```

```bash
python "Shorting/SelectionSort.py"
```

```bash
python "Shorting/InsertionSort.py"
```

```bash
python "Shorting/MergeSort.py"
```

