# Phase 2 · Week 4 — DSA Part 2: Graphs + DP + Backtracking

**Status: ⬜ NOT STARTED**  
**Resource: Striver's Graph Series + NeetCode DP playlist**

> Graphs and DP are the two topics that decide whether you pass or fail a top company interview. Most candidates are weak here. You won't be.

---

## Week Goal
Master graphs (BFS, DFS, shortest path, MST), Dynamic Programming patterns, and Backtracking. Hit 50+ LeetCode problems total by end of week.

---

## Daily LeetCode Tracker

| Day | Problem 1 | Problem 2 | Bonus | Total |
|-----|-----------|-----------|-------|-------|
| Mon | ⬜ | ⬜ | ⬜ | 0 |
| Tue | ⬜ | ⬜ | ⬜ | 0 |
| Wed | ⬜ | ⬜ | ⬜ | 0 |
| Thu | ⬜ | ⬜ | ⬜ | 0 |
| Fri | ⬜ | ⬜ | ⬜ | 0 |
| Sat | ⬜ | ⬜ | ⬜ | 0 |
| Sun | ⬜ | ⬜ | ⬜ | 0 |

**Week total: 0 / 14 minimum | Running total: 0 / 50 target**

---

## Day 1 — Graphs: Representation + BFS + DFS

- [ ] Graph representation: adjacency matrix
- [ ] Graph representation: adjacency list (use this in interviews)
- [ ] BFS from scratch — using queue, level by level
- [ ] DFS from scratch — recursive + iterative (using stack)
- [ ] Applications:
  - [ ] Find all connected components
  - [ ] Check if path exists between two nodes
  - [ ] Detect cycle in undirected graph
- [ ] LeetCode:
  - [ ] Number of Islands (#200)
  - [ ] Flood Fill (#733)
  - [ ] Bonus: Clone Graph (#133)
- [ ] Commit and push

---

## Day 2 — Graphs: Shortest Path + MST

- [ ] Topological sort: DFS approach + Kahn's BFS approach
- [ ] Cycle detection in directed graph
- [ ] Dijkstra's algorithm — shortest path (non-negative weights)
- [ ] Bellman-Ford algorithm — handles negative weights
- [ ] Floyd-Warshall — all pairs shortest path
- [ ] Prim's algorithm — Minimum Spanning Tree
- [ ] Kruskal's algorithm + Union-Find (DSU) data structure
- [ ] LeetCode:
  - [ ] Course Schedule (#207) — topological sort
  - [ ] Network Delay Time (#743) — Dijkstra
  - [ ] Bonus: Number of Provinces (#547)
- [ ] Commit and push

---

## Day 3 — Dynamic Programming: Foundations

- [ ] The mindset — identify these two things:
  1. Overlapping subproblems
  2. Optimal substructure
- [ ] Memoization (top-down) vs Tabulation (bottom-up) — understand both
- [ ] Classic 1D DP:
  - [ ] Fibonacci: recursive → memo → tabulation → space optimised
  - [ ] Climbing stairs
  - [ ] House robber
  - [ ] Jump game
- [ ] LeetCode:
  - [ ] Climbing Stairs (#70)
  - [ ] House Robber (#198)
  - [ ] Bonus: Jump Game (#55)
- [ ] Commit and push

---

## Day 4 — Dynamic Programming: Classic Problems

- [ ] 2D DP problems:
  - [ ] 0/1 Knapsack — the DP archetype
  - [ ] Longest Common Subsequence
  - [ ] Edit Distance (Levenshtein)
  - [ ] Matrix Chain Multiplication
  - [ ] Unique Paths (grid DP)
  - [ ] Coin Change (min coins)
  - [ ] Coin Change II (number of ways)
  - [ ] Longest Increasing Subsequence
- [ ] For each: write recursive → memo → tabulation
- [ ] LeetCode:
  - [ ] Coin Change (#322)
  - [ ] Longest Common Subsequence (#1143)
  - [ ] Bonus: Unique Paths (#62)
- [ ] Commit and push

---

## Day 5 — Backtracking

- [ ] Backtracking template — learn the pattern:
  ```
  void backtrack(state) {
      if (base case) { add to result; return; }
      for (each choice) {
          make choice
          backtrack(next state)
          undo choice
      }
  }
  ```
- [ ] Implement:
  - [ ] N-Queens problem
  - [ ] Rat in a maze
  - [ ] Sudoku solver
  - [ ] Word search in grid
  - [ ] Generate all permutations
  - [ ] Generate all subsets
  - [ ] Generate all combinations that sum to target
- [ ] LeetCode:
  - [ ] Subsets (#78)
  - [ ] Permutations (#46)
  - [ ] Bonus: Combination Sum (#39)
- [ ] Commit and push

---

## Day 6 — Greedy + Divide and Conquer

- [ ] Greedy algorithm mindset: locally optimal → globally optimal
- [ ] Greedy problems:
  - [ ] Activity selection problem
  - [ ] Fractional knapsack
  - [ ] Huffman encoding (understand the concept)
  - [ ] Job scheduling with deadlines
- [ ] Divide and Conquer:
  - [ ] Binary search (generalised)
  - [ ] Closest pair of points
  - [ ] Strassen's matrix multiplication (concept)
- [ ] LeetCode:
  - [ ] Jump Game II (#45) — greedy
  - [ ] Search in Rotated Sorted Array (#33) — D&C
  - [ ] Bonus: Merge Intervals (#56)
- [ ] Commit and push

---

## Day 7 — Review + Python Automation Project

- [ ] Timed LeetCode: 3 problems, 25 mins each, zero hints
- [ ] Review: any DP pattern still unclear? Spend 2 hours on it
- [ ] Build Python automation project (keep Python alive):
  - [ ] Option A: Web scraper that pulls job listings
  - [ ] Option B: File organiser (sort downloads by extension)
  - [ ] Option C: Price tracker with email alert
  - [ ] Option D: News aggregator from multiple sources
- [ ] Push automation project to GitHub with README
- [ ] Mark week as complete
- [ ] Update total LeetCode count

---

## LeetCode Problems This Week (Target: 14+)

**Graphs:**
- [ ] Number of Islands
- [ ] Flood Fill
- [ ] Course Schedule
- [ ] Network Delay Time

**DP:**
- [ ] Climbing Stairs
- [ ] House Robber
- [ ] Coin Change
- [ ] Longest Common Subsequence
- [ ] Unique Paths
- [ ] Jump Game

**Backtracking:**
- [ ] Subsets
- [ ] Permutations
- [ ] Combination Sum

**Greedy:**
- [ ] Jump Game II
- [ ] Merge Intervals

---

## Week 4 Done When:
- [ ] All daily tasks ticked
- [ ] 50+ LeetCode total (Week 3 + Week 4 combined)
- [ ] Can implement BFS/DFS for graphs without help
- [ ] Can solve a DP problem using both memo and tabulation
- [ ] Python project #1 pushed to GitHub
- [ ] Understand the backtracking template cold

---

## Phase 2 Complete When This Week is Done 🎉

You will have:
- ✅ C — Sem 1 done
- ✅ C++ OOP + STL — Sem 2 done
- ✅ DSA: Arrays, Trees, Graphs, DP, Backtracking — Sem 3 done
- ✅ 50+ LeetCode problems solved
- ✅ 2 mini projects + 1 Python project on GitHub
- ✅ Daily coding habit locked in

---

[← Week 3](../week-3/README.md) | [Phase 2](../README.md) | [Phase 3 →](../../phase-3/README.md)
