# Phase 2 — Weeks 3–5: DSA Core + Math Bridge

**Theme:** Build the data structures knowledge that makes SST's DSA 101 feel like review. Start the math-to-ML bridge. Establish Codeforces weekly habit.

> ← [Phase 1](./phase1-weeks1-2.md) | [Back to README](../README.md) | Next → [Phase 3](./phase3-weeks6-8.md)

---

## 📅 WEEK 3 — Arrays, Strings, Hash Maps, Recursion

**Leetcode target this week: 15 problems (5 familiar warmup + 10 new)**

### Days 1–2: Arrays and Strings Deeply

**Implement from scratch:**
- [ ] Dynamic array class (understand amortized O(1) append — how Python lists actually work)
- [ ] String reversal function
- [ ] Palindrome check (handles spaces and capitalization)
- [ ] Anagram check
- [ ] Substring search (naive O(n²) first, then understand why KMP exists)

**Leetcode:**
- [ ] #242 — Valid Anagram
- [ ] #125 — Valid Palindrome
- [ ] #345 — Reverse Vowels of a String
- [ ] #14 — Longest Common Prefix
- [ ] #8 — String to Integer atoi (Medium — spend time on this one)

### Day 3: Hash Maps — Most Important DS for Interviews

**Build from scratch:**
- [ ] Basic hash map using list of lists for collision handling (chaining)
- [ ] Can explain: what hashing does, why lookup is O(1) average, what a collision is

**Leetcode:**
- [ ] #49 — Group Anagrams
- [ ] #347 — Top K Frequent Elements
- [ ] #1 — Two Sum (redo it — now solve in O(n) using hash map, explain why it works)

### Days 4–5: Recursion — The Mental Model Shift

*Spend full 2 days here. Everything after (trees, graphs, DP) depends on recursive thinking.*

**Implement recursively:**
- [ ] `factorial(n)`
- [ ] `fibonacci(n)` — naive version first, then understand why it's exponential time
- [ ] `power(base, exponent)` — then implement fast exponentiation (log n)
- [ ] Binary search — recursive version
- [ ] Flatten a nested list: `[[1, [2, 3]], [4]]` → `[1, 2, 3, 4]`
- [ ] Reverse a string recursively
- [ ] Can explain: base case, recursive case, call stack

**Leetcode:**
- [ ] #70 — Climbing Stairs (recursion → DP bridge — important)
- [ ] #231 — Power of Two
- [ ] #206 — Reverse Linked List (recursive version specifically)

### Day 6: First Codeforces Contest

- [ ] Checked codeforces.com/contests for upcoming Div. 4
- [ ] Either participated live OR did a virtual contest on a recent Div. 4 round
- [ ] Solved problem **A** ✓
- [ ] Solved problem **B** ✓
- [ ] Read editorial for every problem not solved ✓ (mandatory — do not skip)
- [ ] Contest added to [Codeforces Contest Log](../README.md#-codeforces-contest-log)

### Day 7: Math Bridge — Session 1

Watch 3Blue1Brown "Essence of Linear Algebra" — Chapters 1–3 (youtube.com/3blue1brown)

- [ ] Chapter 1 (Vectors) watched with notes
- [ ] Chapter 2 (Linear combinations, span) watched with notes
- [ ] Chapter 3 (Matrix as transformation) watched with notes

**Implement in Jupyter notebook after each chapter:**
- [ ] After Ch. 1: Vector addition and scalar multiplication visualized with matplotlib
- [ ] After Ch. 2: Check if a 2D vector is in the span of two other vectors
- [ ] After Ch. 3: Matrix-vector multiplication, visualized the transformation

---

## 📅 WEEK 4 — Linked Lists, Stacks, Queues + Math Bridge Continues

### Days 1–2: Linked Lists from Scratch

**Implement a full singly linked list:**
- [ ] `append(val)` — add to end
- [ ] `prepend(val)` — add to front
- [ ] `delete(val)` — remove first occurrence
- [ ] `search(val)` — return True/False
- [ ] `reverse()` — iterative version
- [ ] `reverse()` — recursive version (both must work)
- [ ] `has_cycle()` — Floyd's algorithm (two pointers)
- [ ] `find_middle()` — slow/fast pointer technique
- [ ] `__str__()` — print list nicely as `1 → 2 → 3 → None`

**Leetcode:**
- [ ] #206 — Reverse Linked List (confirm it's solid now)
- [ ] #876 — Middle of the Linked List
- [ ] #141 — Linked List Cycle
- [ ] #21 — Merge Two Sorted Lists
- [ ] #19 — Remove Nth Node From End of List (Medium — two pointer)

### Day 3: Stacks and Queues

**Implement using Python lists:**
- [ ] Stack class: `push`, `pop`, `peek`, `is_empty`, `size`
- [ ] Queue class: `enqueue`, `dequeue`, `front`, `is_empty`, `size`
- [ ] Queue using two Stacks — understand *why* this works (amortized O(1))

**Leetcode:**
- [ ] #20 — Valid Parentheses
- [ ] #155 — Min Stack
- [ ] #232 — Implement Queue using Stacks
- [ ] #682 — Baseball Game

### Day 4: CS50x Week 5 — Data Structures

- [ ] Watched CS50x Week 5 lecture (linked lists, trees, hash tables in C with memory visuals)
- [ ] Key insight: understand what's happening in memory, not just the Python abstraction

### Day 5: Codeforces Practice

- [ ] Did Div. 4 or Div. 3 virtual contest (or upsolving session)
- [ ] Solved A ✓
- [ ] Solved B ✓
- [ ] Attempted C ✓
- [ ] Read editorial for C (whether you solved it or not)
- [ ] Practiced: reading problem statement precisely, identifying edge cases before coding

### Days 6–7: Math Bridge — Sessions 2 & 3

Watch 3Blue1Brown LA Chapters 4–7:

- [ ] Chapter 4 (Matrix multiplication as composition) watched + implemented
  - [ ] Showed AB ≠ BA in NumPy with a concrete example
- [ ] Chapter 5 (The determinant) watched + implemented
  - [ ] Created a matrix with det = 0, understood why it's not invertible
- [ ] Chapter 6 (Inverse matrices, column space, null space) watched + implemented
  - [ ] Verified A @ inv(A) = identity matrix in NumPy
- [ ] Chapter 7 (Dot products and duality) watched + implemented
  - [ ] Implemented `dot_product(v1, v2)` manually (without np.dot)

---

## 📅 WEEK 5 — Binary Trees, Binary Search Pattern, Sliding Window

### Days 1–2: Binary Trees + BST from Scratch

**Implement Binary Tree:**
- [ ] Inorder traversal (left, root, right) — recursive
- [ ] Preorder traversal (root, left, right) — recursive
- [ ] Postorder traversal (left, right, root) — recursive
- [ ] Level-order traversal — BFS using a queue (important — used in interviews constantly)
- [ ] `height()` — height of the tree
- [ ] `count_nodes()` — total nodes
- [ ] `search(val)` — find a value

**Implement BST (on top of Binary Tree):**
- [ ] `insert(val)` — maintaining BST property
- [ ] `find_min()` and `find_max()`
- [ ] `delete(val)` — this is hard, spend extra time (3 cases: leaf, one child, two children)
- [ ] `is_valid_bst()` — verify a tree is a valid BST (classic interview problem)

**Leetcode:**
- [ ] #104 — Maximum Depth of Binary Tree
- [ ] #226 — Invert Binary Tree
- [ ] #101 — Symmetric Tree
- [ ] #112 — Path Sum
- [ ] #98 — Validate Binary Search Tree (Medium)

### Day 3: Binary Search as a Pattern (not just an algorithm)

*Binary search is a template for eliminating half the search space. It appears in 50+ problems.*

- [ ] Implemented the canonical binary search template from memory (with `left + (right-left)//2`)
- [ ] Can explain why `left + (right-left)//2` and not `(left+right)//2`

**Leetcode:**
- [ ] #704 — Binary Search (warmup)
- [ ] #278 — First Bad Version
- [ ] #35 — Search Insert Position
- [ ] #153 — Find Minimum in Rotated Sorted Array (Medium)
- [ ] #33 — Search in Rotated Sorted Array (Medium)

### Day 4: Sliding Window Pattern

*Turns O(n²) array problems into O(n). Once you see it, you can't unsee it.*

- [ ] Implemented fixed-window max sum example from scratch
- [ ] Understand variable-window pattern (expand right, shrink left when condition violated)

**Leetcode:**
- [ ] #643 — Maximum Average Subarray I
- [ ] #3 — Longest Substring Without Repeating Characters (Medium — classic)
- [ ] #209 — Minimum Size Subarray Sum (Medium)
- [ ] #904 — Fruit Into Baskets (Medium)

### Day 5: Math Bridge — Eigenvalues

Watch 3Blue1Brown Chapters 13–14 (Eigenvectors + Eigenvalues, Abstract vector spaces)

- [ ] Chapters 13–14 watched with notes
- [ ] Implemented eigenvalue/eigenvector computation in NumPy
- [ ] Verified: A @ v = λ * v for each eigenvector (should return True with `np.allclose`)
- [ ] Read setosa.io/ev/principal-component-analysis — visual PCA intuition (no equations)
- [ ] Can explain in plain English: "An eigenvector of a matrix is a vector that only gets scaled, not rotated, when the matrix transforms it."

### Day 6: Second Codeforces Contest

- [ ] Contest 2 completed (Div. 4 or Div. 3)
- [ ] Solved A ✓, B ✓, attempted C ✓
- [ ] Rating improving? (note current rating): _______
- [ ] Editorial read for unsolved problems ✓
- [ ] Added to [Contest Log](../README.md#-codeforces-contest-log)

### Day 7: Build Project #3 — BST Visualizer

**BST command-line visualizer:**
- [ ] Insert nodes
- [ ] Display tree visually in terminal (horizontal layout showing left/right children)
- [ ] Show inorder, preorder, postorder traversals on command
- [ ] Search for a value
- [ ] Delete a value
- [ ] Display tree height and node count
- [ ] Pushed to GitHub
- [ ] README explains BSTs, their time complexities (insert/search/delete: O(log n) avg, O(n) worst), and when you'd use one

---

## 📦 Phase 2 Exit Criteria

*Do not move to Phase 3 until all of these are true:*

- [ ] All 5 data structures implemented from scratch: Arrays, Linked Lists, Stacks, Queues, Trees/BST
- [ ] 30+ Leetcode problems total (cumulative from Phase 1 + 2)
- [ ] 2 Codeforces contests participated in
- [ ] 3B1B Linear Algebra Chapters 1–7 + 13–14 complete with NumPy implementations
- [ ] Can explain Big O of every data structure operation without notes
- [ ] BST Visualizer project live on GitHub
- [ ] Week 3–5 notes in Notion
