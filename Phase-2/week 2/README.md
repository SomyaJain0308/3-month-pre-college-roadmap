# Phase 2 · Week 2 — C++ OOP + STL

**Status: ⬜ NOT STARTED**   
**Resource: [LearnCpp.com](https://learncpp.com) + [The Cherno C++](https://youtube.com/@TheCherno)**

> C++ is the interview language. Every top company SDE role expects it. You already know C — C++ is just C with classes and a massive standard library.

---

## Week Goal
Master OOP in C++ and the STL. Walk out able to write any class hierarchy, use any STL container, and implement linked lists and recursion in C++.

---

## Day 1 — Classes + Constructors + Encapsulation

- [ ] Understand: class vs struct in C++
- [ ] Write a `BankAccount` class with:
  - [ ] Private: balance, accountNumber
  - [ ] Public: deposit(), withdraw(), getBalance()
  - [ ] Default constructor
  - [ ] Parameterized constructor
  - [ ] Copy constructor
  - [ ] Destructor (print message when destroyed)
- [ ] Operator overloading:
  - [ ] Overload `+` for a `Complex` number class
  - [ ] Overload `<<` for printing an object
  - [ ] Overload `==` for comparing two objects
- [ ] Static members and methods demo
- [ ] Friend function demo
- [ ] Commit and push to GitHub

---

## Day 2 — Inheritance

- [ ] Single inheritance: `Animal` → `Dog`
  - [ ] Override `speak()` method
- [ ] Multilevel inheritance: `Vehicle` → `Car` → `ElectricCar`
- [ ] Multiple inheritance: `Flyable` + `Swimmable` → `Duck`
- [ ] Access specifiers in inheritance: public, protected, private
- [ ] Constructor calling order — understand and demo
- [ ] Method overriding vs overloading — know the difference
- [ ] Commit and push to GitHub

---

## Day 3 — Polymorphism + Abstract Classes

- [ ] Virtual functions — why they exist, how vtable works (concept)
- [ ] Runtime polymorphism demo:
  - [ ] `Shape` base class with virtual `area()`
  - [ ] `Circle`, `Rectangle`, `Triangle` — each overrides `area()`
  - [ ] Call via base class pointer — watch polymorphism happen
- [ ] Pure virtual functions — make `Shape` abstract
- [ ] Abstract class — cannot instantiate, can pointer
- [ ] Exception handling:
  - [ ] try, catch, throw
  - [ ] Multiple catch blocks
  - [ ] Custom exception class
  - [ ] Rethrowing exceptions
- [ ] Commit and push to GitHub

---

## Day 4 — Templates + STL Containers

- [ ] Function templates: write `swap<T>`, `max<T>`, `min<T>`
- [ ] Class template: write `Stack<T>` from scratch
- [ ] STL containers — implement one demo program for each:
  - [ ] `vector` — dynamic array operations
  - [ ] `list` — doubly linked list
  - [ ] `deque` — double-ended queue
  - [ ] `stack` — LIFO operations
  - [ ] `queue` — FIFO operations
  - [ ] `priority_queue` — max heap by default
- [ ] Commit and push to GitHub

---

## Day 5 — STL Maps, Sets + Algorithms

- [ ] `map` vs `unordered_map` — know when to use each
  - [ ] Word frequency counter using `unordered_map`
  - [ ] Student grade lookup using `map`
- [ ] `set` vs `unordered_set`
  - [ ] Remove duplicates from array using `set`
- [ ] `pair` and `tuple`
- [ ] STL algorithms:
  - [ ] `sort` with default and custom comparator
  - [ ] `find`, `count`, `accumulate`
  - [ ] `lower_bound`, `upper_bound` on sorted vector
  - [ ] `max_element`, `min_element`
  - [ ] `reverse`, `rotate`
- [ ] Iterators: begin, end, rbegin, rend
- [ ] Commit and push to GitHub

---

## Day 6 — Data Structures in C++

- [ ] Linked List as a class in C++:
  - [ ] `Node` struct + `LinkedList` class
  - [ ] Insert at head, tail, position
  - [ ] Delete by value
  - [ ] Display list
  - [ ] Reverse list
- [ ] Stack from scratch using a class
- [ ] Queue from scratch using a class
- [ ] Recursion problems in C++:
  - [ ] Tower of Hanoi
  - [ ] N-Queens (print solutions)
  - [ ] Rat in a maze
- [ ] Commit and push to GitHub

---

## Day 7 — Mini Project + Review

- [ ] Build: **Library Management System in C++**
  - [ ] `Book` class: title, author, ISBN, available
  - [ ] `Library` class with vector of books
  - [ ] Add book
  - [ ] Search by title or author
  - [ ] Issue a book (mark unavailable)
  - [ ] Return a book
  - [ ] Display all books
  - [ ] Save/load from file
- [ ] Write clean README for mini project
- [ ] Self test: implement a class hierarchy (Shape → Circle/Rectangle) from scratch without help
- [ ] Push everything to GitHub
- [ ] Mark week as complete

---

## Programs Written This Week

| # | Program | File | Done |
|---|---------|------|------|
| 1 | BankAccount class | oop/bank_account.cpp | ⬜ |
| 2 | Operator overloading | oop/operator_overload.cpp | ⬜ |
| 3 | Inheritance demo | inheritance/ | ⬜ |
| 4 | Virtual functions | polymorphism/shapes.cpp | ⬜ |
| 5 | Abstract classes | polymorphism/abstract.cpp | ⬜ |
| 6 | Exception handling | exceptions/ | ⬜ |
| 7 | Templates | templates/ | ⬜ |
| 8 | STL containers | stl/containers.cpp | ⬜ |
| 9 | STL maps + sets | stl/maps_sets.cpp | ⬜ |
| 10 | STL algorithms | stl/algorithms.cpp | ⬜ |
| 11 | Linked list class | ds/linked_list.cpp | ⬜ |
| 12 | Recursion pack | recursion/ | ⬜ |
| 13 | Library Management System | mini-project/ | ⬜ |

---

## Week 2 Done When:
- [ ] All daily tasks above are ticked
- [ ] 13+ programs pushed to GitHub
- [ ] Mini project working and pushed
- [ ] Can implement a class with inheritance + virtual functions in 10 minutes
- [ ] Know which STL container to use for any problem without thinking

---

[← Week 1](../week-1/README.md) | [Phase 2](../README.md) | [Week 3 →](../week-3/README.md)
