## Day 5: Queue and Deque

This folder contains simple Python implementations of:

- **Queue** (FIFO)
- **Deque** (double-ended queue)

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

