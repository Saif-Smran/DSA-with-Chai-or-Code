
# Day 2: Singly Linked List

This folder contains the Day 2 implementation of a **Singly Linked List** in Python.

## What I Learned / Implemented (SimplyLL.py)

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
