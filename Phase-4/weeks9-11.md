# Phase 4 — Weeks 9–10: CS50x + DP + Graphs + SQL + OS Preview

**Theme:** Solidify CS fundamentals that SST covers in Year 1 (OS, memory, databases) so you're not learning them for the first time in class. Push Leetcode to 50+ total.

> ← [Phase 3](./phase3-weeks6-8.md) | [Back to README](../README.md) | Next → [Phase 5](./phase5-weeks11-12.md)

---

## 📅 WEEK 9 — CS50x Memory + DP Introduction + Graph Traversal

### Days 1–2: CS50x Week 2 (Arrays) + Week 4 (Memory)

*Week 4 is the most important one. Pointers and memory will make SST's OS course click.*

**CS50x Week 2:**
- [ ] Watched Week 2 lecture (Arrays in C)
- [ ] Understand: how arrays are stored contiguously in memory
- [ ] Understand: why array index out of bounds is dangerous in C but handled in Python

**CS50x Week 4 (Memory) — the critical one:**
- [ ] Watched Week 4 lecture fully
- [ ] Completed Problem Set 4 — Recover (recover JPEG files from a memory card image)
- [ ] Can explain: stack vs heap in plain English
- [ ] Can explain: what a pointer is and what it stores (a memory address)
- [ ] Can explain: what a memory leak is
- [ ] Can explain: why Python's garbage collector exists and what problem it solves
- [ ] Can explain: why `=` in Python copies a reference, not an object (and what to do about it)

### Day 3: CS50x Week 6 — Python (CS50's Version)

- [ ] Watched Week 6 lecture
- [ ] Noticed: how much shorter the Python implementations are vs C versions
- [ ] Understood *why* Python is shorter (garbage collection, dynamic typing, built-in data structures)
- [ ] This is review — use it to cement, not to learn new things

### Days 4–5: Dynamic Programming — Planting the Seed

*DP is the hardest major pattern. You won't master it in 2 days. You're building the mental model.*

**Key insight to internalize:**
- [ ] Can state from memory: "DP = recursion + memoization. If I can write a recursive solution, I can usually make it DP."

**Implement Fibonacci 3 ways:**
- [ ] Naive recursive (understand why it's O(2^n))
- [ ] Top-down with `@lru_cache` memoization (understand why this is now O(n))
- [ ] Bottom-up iterative DP (understand: same answer, no recursion overhead)
- [ ] Can draw the recursion tree for fib(6) from memory and explain where the overlap is

**Leetcode DP problems — in this exact order:**
- [ ] #70 — Climbing Stairs (redo as proper DP — write recursive → memoized → iterative)
- [ ] #198 — House Robber
- [ ] #322 — Coin Change (Medium — very important, spend time)
- [ ] #300 — Longest Increasing Subsequence (Medium)
- [ ] #139 — Word Break (Medium)

**For every DP problem — follow this 3-step process:**
1. Write the recursive solution first
2. Add memoization (top-down DP)
3. Convert to iterative (bottom-up DP)
- [ ] Did all 3 steps for every DP problem above ✓

### Days 6–7: Graphs — BFS and DFS

*Will appear in SST curriculum and every systems/algorithms interview.*

**Implement from scratch:**
- [ ] BFS using `collections.deque` — level-by-level traversal
- [ ] DFS — recursive version
- [ ] DFS — iterative version (using a stack)
- [ ] Can explain: when to use BFS (shortest path, level-order) vs DFS (cycle detection, topological sort)
- [ ] Can explain: why BFS uses a queue and DFS uses a stack

**Leetcode graph problems:**
- [ ] #200 — Number of Islands (Medium — classic BFS/DFS, very common in interviews)
- [ ] #133 — Clone Graph (Medium)
- [ ] #207 — Course Schedule (Medium — cycle detection in directed graph, important)
- [ ] #417 — Pacific Atlantic Water Flow (Medium — multi-source BFS)

---

## 📅 WEEK 10 — SQL + OS Concepts + Leetcode Sprint to 50+

### Days 1–2: CS50x Week 7 — SQL

*SST covers databases in Term 4. Walk in already knowing this.*

Watch CS50x Week 7 lecture, then practice on SQLiteOnline.com (no install needed).

**Master these SQL operations:**

- [ ] `CREATE TABLE` with proper data types and constraints
- [ ] `INSERT INTO` — single and multiple rows
- [ ] `SELECT` with `WHERE`, `ORDER BY`, `LIMIT`
- [ ] `UPDATE` and `DELETE` with `WHERE` clauses
- [ ] `JOIN` (INNER JOIN — the most important one)
- [ ] `LEFT JOIN` — understand how it differs from INNER JOIN
- [ ] `GROUP BY` with aggregate functions: `COUNT`, `AVG`, `SUM`, `MAX`, `MIN`
- [ ] `HAVING` — filter on aggregated results (understand why you can't use WHERE here)
- [ ] Subqueries — a SELECT inside a SELECT

**Practice exercises (write all of these yourself on SQLiteOnline.com):**
- [ ] Create a `students` table and an `enrollments` table and a `courses` table
- [ ] Write a query: "list all students enrolled in more than 2 courses"
- [ ] Write a query: "find the course with the highest average grade"
- [ ] Write a query: "find students NOT enrolled in any course" (LEFT JOIN + NULL check)
- [ ] Write a query: "rank students by GPA descending, show top 5"

**Concept checks:**
- [ ] Can explain: what a PRIMARY KEY is and why it matters
- [ ] Can explain: what a FOREIGN KEY is and what referential integrity means
- [ ] Can explain: what an index does and why it speeds up queries
- [ ] Can explain: why `SELECT *` in production code is usually bad

### Day 3: OS Concepts Preview

Read: OSTEP (ostep.org) — free, outstanding book. Read, don't code.

- [ ] Chapter 1 — Introduction (what an OS actually does)
- [ ] Chapter 2 — Introduction to Processes
- [ ] Chapter 4 — The Abstraction: The Process

**Concept checks after reading:**
- [ ] Can explain: what a process is (a running program + its state)
- [ ] Can explain: what a thread is and how it differs from a process
- [ ] Can explain: what a system call is (the interface between user programs and the OS)
- [ ] Can explain: why concurrency is hard (one sentence: "shared state + non-deterministic scheduling")
- [ ] Can explain: what context switching is
- [ ] Notes added to Notion

### Days 4–7: Leetcode Sprint — Reach 50+ Total

*Check the [Leetcode Tracker](../README.md#-leetcode-tracker) and identify remaining problems.*

**Patterns to fill gaps in:**

**Prefix Sums:**
- [ ] Can explain: what a prefix sum array is and why it makes range sum queries O(1)
- [ ] Implemented prefix sum array from scratch
- [ ] #303 — Range Sum Query - Immutable
- [ ] #238 — Product of Array Except Self (Medium — elegant, no division)

**Monotonic Stack:**
- [ ] Can explain: what a monotonic stack is (stack that maintains increasing or decreasing order)
- [ ] #496 — Next Greater Element I
- [ ] #739 — Daily Temperatures (Medium)

**Heap / Priority Queue:**
- [ ] Know Python's `heapq` module (min-heap by default — know the trick for max-heap)
- [ ] Can explain: what a heap is and why insertion/extraction is O(log n)
- [ ] #215 — Kth Largest Element in an Array (Medium)
- [ ] #703 — Kth Largest Element in a Stream (Medium)

**General sprint — any pattern you're weakest on:**
- [ ] Problem 41 — solved ✓
- [ ] Problem 42 — solved ✓
- [ ] Problem 43 — solved ✓
- [ ] Problem 44 — solved ✓
- [ ] Problem 45 — solved ✓
- [ ] Problem 46 — solved ✓
- [ ] Problem 47 — solved ✓
- [ ] Problem 48 — solved ✓
- [ ] Problem 49 — solved ✓
- [ ] Problem 50 — solved ✓
- [ ] Problem 51 — solved ✓
- [ ] Problem 52 — solved ✓
- [ ] Problem 53 — solved ✓
- [ ] Problem 54 — solved ✓

**Leetcode total count: _______ / 54+**

---

## 📦 Phase 4 Exit Criteria

*Do not move to Phase 5 until all of these are true:*

- [ ] CS50x Weeks 2, 4, 6, 7 complete ✓
- [ ] Can explain stack vs heap, pointers, memory leaks, garbage collection without notes ✓
- [ ] All 5 DP problems done using all 3 steps (recursive → memoized → iterative) ✓
- [ ] BFS and DFS implemented from scratch, all 4 graph Leetcode problems solved ✓
- [ ] SQL: can write JOINs, GROUP BY + HAVING, subqueries confidently ✓
- [ ] OSTEP Chapters 1, 2, 4 read with notes ✓
- [ ] **50+ Leetcode problems solved total** ✓
- [ ] Codeforces rating: _______ (target: 700+) ✓
