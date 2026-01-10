## Day 5: Queue and Deque

This folder contains simple Python implementations of:

- **Queue** (FIFO)
- **Deque** (double-ended queue)

## Day 6: Circular Queue

Implementation:

- **Circular Queue** (fixed-size queue with wrap-around)

### Queue (FIFO)

File: `Queue.py`

**Class:** `Queue`

**Methods**

- `isEmpty()` → returns `True` if the queue has no items.
- `enqueue(value)` → adds `value` to the rear of the queue.
- `dequeue()` → removes and returns the front item.
	- If the queue is empty, it prints `Queue is empty` and returns `None`.

**Note on performance:** This implementation uses a Python list and `pop(0)`, so `dequeue()` is $O(n)$ due to shifting.

Run:

```bash
python "Queue/Queue.py"
```

### Deque (Double-Ended Queue)

File: `DeQueue.py`

**Class:** `Deque`

**Methods**

- `isEmpty()` → returns `True` if the deque is empty.
- `size()` → returns the number of items.
- `insertAtFront(value)` → inserts `value` at the front.
- `insertAtEnd(value)` → inserts `value` at the end.
- `deleteAtFront()` → removes and returns the front item.
	- If empty, prints `Queue is empty` and returns `None`.
- `deleteAtEnd()` → removes and returns the last item.
	- If empty, prints `Queue is empty` and returns `None`.

Run:

```bash
python "Queue/DeQueue.py"
```

### Circular Queue (Fixed-size, wrap-around)

File: `CircularQueue.py`

**Class:** `CircularQueue`

A circular queue uses a fixed-size array and treats the ends as connected (wrap-around). Instead of shifting elements (like `pop(0)`), it moves two pointers:

- `front` → index of the current front element
- `rear` → index where the last element was inserted

When `rear` reaches the end, it wraps using modulo:

$$
rear = (rear + 1) \bmod size
$$

**Empty condition**

- `front == -1`

**Full condition**

- `(rear + 1) % size == front`

**Methods**

- `isEmpty()` → returns `True` if the queue has no items.
- `isFull()` → returns `True` if the queue is at capacity.
- `enqueue(value)` → inserts `value` at the rear.
	- Raises `Exception("Queue is full")` if full.
- `dequeue()` → removes and returns the front value.
	- Raises `Exception("Queue is empty")` if empty.

**Time complexity**

- `enqueue` / `dequeue` are $O(1)$ because indices move without shifting elements.

Run:

```bash
python "Queue/CircularQueue.py"
```

Note: The current demo intentionally calls `enqueue(60)` on a size-5 queue, which raises `Queue is full` and exits with an error. Comment that line out (or wrap it in `try/except`) to see `dequeue()` run.

