
# Linked Lists (Day 2–3)

This folder contains implementations and notes for linked list variants in Python.

## Day 2: Singly Linked List (SimplyLL.py)

### 1) Node structure

- Created a `Node` class with:
	- `data`: stores the value
	- `next`: pointer/reference to the next node (defaults to `None`)

### 2) Singly Linked List (SLL) basics

- Created a `SinglyLinkedList` class with:
	- `head`: points to the first node (defaults to `None` for an empty list)

### 3) Insertion operations

- Insert at end: `insertAtEnd(value)`
	- If list is empty: new node becomes `head`
	- Otherwise: traverse to last node and attach the new node

- Insert at beginning: `insertAtBeg(value)`
	- New node’s `next` points to current `head`
	- Update `head` to the new node

- Insert in middle (after a specific value): `insertAtMid(value, x)`
	- Traverses the list to find node with `data == x`
	- Inserts the new node right after it
	- Stops after the first match

### 4) Deletion operation

- Delete a node by value: `deleteLL(val)`
	- Handles deletion at head
	- Otherwise keeps track of `prev` and relinks pointers to remove the node
	- Deletes the first occurrence of the value

### 5) Traversal / Printing

- Print the list: `printLL()`
	- Traverses from `head` and prints each node’s `data`

## Demo Flow Used in the File

The script builds and modifies the list in this order:

- Insert at end: `10 -> 20 -> 30`
- Insert at beginning: `5 -> 10 -> 20 -> 30`
- Insert after `20`: `5 -> 10 -> 20 -> 40 -> 30`
- Delete `20`: `5 -> 10 -> 40 -> 30`
- Print final list

## Run

From the repo root:

```bash
python "Linkedlist/SimplyLL.py"
```

---

## Day 3: Doubly Linked List (DoublyLL.py)

### What I Learned / Implemented

### 1) Node structure (DLL)

- Created a `Node` class with:
	- `data`: stores the value
	- `prev`: pointer to previous node
	- `next`: pointer to next node

### 2) Doubly Linked List (DLL) basics

- Created a `DoublyLinkedList` class with:
	- `head`: points to the first node

### 3) Insertion operations

- Insert at end: `insertAtEnd(value)`
	- Traverses to the last node
	- Links both `next` and `prev` pointers

- Insert at beginning: `insertAtbeg(value)`
	- Prepends the node
	- Updates both `head` and the old head’s `prev`

- Insert in middle (after a specific value): `insertAtMid(value, x)`
	- Finds the node with `data == x`
	- Inserts the new node right after it
	- Updates the surrounding `next/prev` pointers

### 4) Deletion operation

- Delete a node by value: `deleteDLL(val)`
	- Handles deletion at head
	- Handles deletion in the middle
	- Handles deletion at tail

### 5) Traversal / Printing

- Print the list: `printDLL()`
	- Prints values in order with a `<--->` separator

## Run

From the repo root:

```bash
python "Linkedlist/DoublyLL.py"
```

---

## Day 3: Circular Linked List (CircularLL.py)

This file contains two circular linked list implementations:

- Circular Singly Linked List: `CircularSLL` (uses `SLLNode`)
- Circular Doubly Linked List: `CircularDLL` (uses `DLLNode`)

### Circular Singly Linked List (CircularSLL)

- Maintains:
	- `head`: first node
	- `last`: last node (whose `next` points back to `head`)

- Insertion operations:
	- `insertAtEnd(value)`
	- `insertAtBeg(value)`
	- `insertAtMid(value, x)` (inserts after value `x`)

- Deletion:
	- `deleteCLL(val)` (handles head, tail, and middle)

- Traversal / Printing:
	- `printCLL()` (stops once it loops back to `head`)

### Circular Doubly Linked List (CircularDLL)

- Maintains a circular DLL where:
	- `head.prev` is the last node
	- last node’s `next` points to `head`

- Insertion operations:
	- `insertAtEnd(value)`
	- `insertAtBeg(value)`
	- `insertAtMid(value, x)` (inserts after value `x`)

- Deletion:
	- `deleteCDLL(val)` (handles single-node list and head deletion)

- Traversal / Printing:
	- `printCDLL()` (stops once it loops back to `head`)

## Run

From the repo root:

```bash
python "Linkedlist/CircularLL.py"
```
