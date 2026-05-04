# Phase 1 — Weeks 1–2: Finish Python, Think Like a Programmer

**Theme:** Close the CS50P chapter. Write real Python. Stop thinking in syntax, start thinking in logic.

> ← [Back to README](../README.md) | Next → [Phase 2](./phase2-weeks3-5.md)

---


## 📅 WEEK 1

### Days 1–2: Finish CS50P

- [ ] All remaining CS50P problem sets completed (do NOT skip any)
- [ ] CS50P final project built and working
  - Suggested: CLI expense tracker (input expenses, categorize, show totals)
- [ ] CS50P final project pushed to GitHub
  - [ ] Repo named `cs50p-final-project`
  - [ ] README.md written (what it does, how to run it, what you learned — 3–5 sentences minimum)

### Day 3: Git — Deep Enough to Use It

- [ ] Completed learngitbranching.js.org — Main track, first 8 levels
- [ ] Understand: commits, branches, merges conceptually
- [ ] First real push to GitHub completed

### Days 4–5: Python Beyond CS50P

Work through each concept. For each one: read → understand → write 5+ practice examples.

**List Comprehensions**
- [ ] Can write list comprehensions with filtering
- [ ] Can write list comprehensions with nested loops
- [ ] Can write list comprehensions with string operations
- [ ] Wrote 10 list comprehensions from scratch (no copy-paste)

**Dictionaries Deeply**
- [ ] Know `defaultdict` and when to use it
- [ ] Know `Counter` and when to use it
- [ ] Can write dict comprehensions
- [ ] Implemented word frequency counter two ways: manual loop AND Counter

**Functions as First-Class Objects**
- [ ] Understand that functions can be passed as arguments
- [ ] Can use `map()`, `filter()`, `sorted()` with `key=`
- [ ] Can write lambda functions
- [ ] Implemented own `my_map()` and `my_filter()` from scratch

**Exception Handling**
- [ ] Know `try` / `except` / `finally` pattern
- [ ] Can raise custom exceptions
- [ ] Every file I/O operation in your projects uses proper error handling

**File I/O Properly**
- [ ] Know `with open() as f:` pattern and why it's used
- [ ] Can read/write CSV files using the `csv` module
- [ ] Can read/write JSON files using the `json` module

### Day 6: Build and Ship Project #1

**CLI Contact Book**
- [ ] Add a contact (name, phone, email)
- [ ] List all contacts
- [ ] Search by name
- [ ] Delete a contact
- [ ] Data saves to JSON file (persists between runs)
- [ ] Handles all edge cases (file doesn't exist, empty input, duplicate names)
- [ ] Pushed to GitHub
- [ ] README written explaining what it does and how to run it

### Day 7: Review

- [ ] Week 1 reviewed in Notion notes
- [ ] Every shaky concept written down and flagged for Week 2

---

## 📅 WEEK 2

### Days 1–2: Object-Oriented Python

Read: Chapter 9 of Automate the Boring Stuff (automatetheboringstuff.com) — OOP section.

**Concepts to nail:**
- [ ] Understand `class` and instances
- [ ] Understand `__init__` and `self`
- [ ] Can write instance methods vs class methods
- [ ] Understand inheritance (parent/child classes)
- [ ] Know `__str__` and `__repr__` and when to use each
- [ ] Understand `@property` decorator

**Practice:**
- [ ] Rewrote the CLI Contact Book using a `Contact` class and `ContactBook` class (no raw dicts)
- [ ] Every previous dict operation now handled by a class method

### Day 3: CS50x Week 0 + Week 1

Go to cs50.harvard.edu/x

- [ ] Watched CS50x Week 0 (Scratch) — for mental model of computation
- [ ] Watched CS50x Week 1 (C) — do not skip even though SST doesn't use C
- [ ] Completed CS50x Problem Set 1 — Mario pyramid ✓ AND Cash change ✓
- [ ] Understand conceptually: stack vs heap, what a pointer is, why Python hides this

### Days 4–5: Algorithmic Thinking — Big O + Sorting

Watch: CS50x Week 3 (Algorithms) lecture — clearest Big O explanation for beginners.

**Implement from scratch in Python (no library functions):**
- [ ] Linear search implemented and tested
- [ ] Binary search — iterative version
- [ ] Binary search — recursive version
- [ ] Bubble sort implemented and tested
- [ ] Merge sort implemented (this one is hard — take extra time)
- [ ] Selection sort implemented and tested

**For each sorting algorithm, tested on:**
- [ ] Empty list
- [ ] Single element
- [ ] Already sorted list
- [ ] Reverse-sorted list
- [ ] List with duplicates

### Day 6: Leetcode — First 10 Problems

**Rules (follow these every single time):**
1. Timer set for 20 minutes — attempt alone first
2. If stuck at 20 min — look at hint only, not solution
3. If still stuck at 30 min — read solution, close it, rewrite from memory
4. After every solve — write in Notion: "what was the key insight? what made me stuck?"

- [ ] #1 — Two Sum
- [ ] #121 — Best Time to Buy and Sell Stock
- [ ] #217 — Contains Duplicate
- [ ] #53 — Maximum Subarray
- [ ] #283 — Move Zeroes
- [ ] #1480 — Running Sum of 1D Array
- [ ] #1672 — Richest Customer Wealth
- [ ] #1342 — Number of Steps to Reduce to Zero
- [ ] #412 — FizzBuzz
- [ ] #344 — Reverse String
- [ ] Notion reflection written for every problem ✓

### Day 7: Build Project #2 + Week Review

**Number Guessing Game with Statistics**
- [ ] Computer picks random number (1–100 default)
- [ ] User gets "too high / too low" feedback
- [ ] Tracks: number of guesses, average per game, best game, worst game
- [ ] Stats saved to JSON file (persists between runs)
- [ ] Difficulty levels: Easy (1–50), Hard (1–200)
- [ ] Pushed to GitHub with README

**Week Review**
- [ ] Week 2 notes added to Notion
- [ ] All shaky concepts flagged

---

## 📦 Phase 1 Exit Criteria

*Do not move to Phase 2 until all of these are true:*

- [ ] CS50P 100% complete including final project
- [ ] OOP in Python solid — can explain classes, inheritance, `__init__` without notes
- [ ] All 6 sorting/searching algorithms implemented from scratch and working
- [ ] 10 Leetcode Easy problems solved with Notion reflections
- [ ] 2 GitHub repos live with READMEs (Contact Book + Number Game)
- [ ] Git workflow habit: every project is committed and pushed same day it's built
- [ ] CS50x Weeks 0–1 watched, Problem Set 1 complete
