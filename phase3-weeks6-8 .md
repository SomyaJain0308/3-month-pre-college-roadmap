# Phase 3 — Weeks 6–8: ML From Scratch + Web Basics + Portfolio

**Theme:** Implement 5 core ML algorithms in NumPy before SST touches ML. Build your portfolio website. Go from "I know Python" to "I understand how machines learn."

> ← [Phase 2](./phase2-weeks3-5.md) | [Back to README](../README.md) | Next → [Phase 4](./phase4-weeks9-10.md)

---

## 📅 WEEK 6 — Linear Regression + Logistic Regression from Scratch

*When SST covers ML in Term 2–3, most students use scikit-learn's `model.fit()`. You will have implemented these yourself. The gap in understanding is enormous.*

### Days 1–2: Linear Regression from Scratch

**Before coding — understand the math:**
- [ ] Can explain: what a cost function is (Mean Squared Error)
- [ ] Can explain: what gradient descent does (iteratively minimize cost by moving in direction of steepest descent)
- [ ] Can write the update rule from memory: `θ = θ - α * (1/m) * X^T * (Xθ - y)`

**Implement `LinearRegression` class:**
- [ ] `__init__` with `learning_rate` and `n_iterations`
- [ ] `fit(X, y)` — gradient descent loop with weight and bias updates
- [ ] `predict(X)` — inference
- [ ] `mse(y_true, y_pred)` — mean squared error metric
- [ ] `r_squared(y_true, y_pred)` — R² metric
- [ ] `cost_history` list tracked during training

**Testing and understanding:**
- [ ] Tested on California Housing dataset (from sklearn — data only, no model)
- [ ] Plotted cost curve over iterations — watched it decrease
- [ ] Experimented: learning rate too high → diverges ✓ (observed this)
- [ ] Experimented: learning rate too low → slow convergence ✓ (observed this)
- [ ] Understand why: can explain learning rate effect in plain English

### Day 3: Logistic Regression from Scratch

**Before coding — understand the math:**
- [ ] Can explain why MSE doesn't work for classification (non-convex loss → local minima)
- [ ] Can derive the sigmoid function `σ(z) = 1/(1+e^(-z))` and why it maps to (0,1)
- [ ] Know Binary Cross-Entropy formula
- [ ] Understand (and can explain) why logistic regression gradient has the same form as linear regression

**Implement `LogisticRegression` class:**
- [ ] `_sigmoid(z)` — sigmoid activation
- [ ] `fit(X, y)` — gradient descent with BCE loss
- [ ] `predict_proba(X)` — returns probability
- [ ] `predict(X)` — returns class (threshold at 0.5)
- [ ] `accuracy(y_true, y_pred)` — accuracy metric

**Testing:**
- [ ] Tested on Iris dataset (binary: setosa vs not-setosa)
- [ ] Achieved > 90% accuracy on test set

### Days 4–5: Mathematics for Machine Learning — Key Chapters

Download free PDF: mml-book.github.io

- [ ] MfML Chapter 2 (Linear Algebra) — sections on norms, inner products, projections, orthogonality
- [ ] MfML Chapter 6 (Probability) — sections 6.1–6.3: probability spaces, discrete/continuous distributions, sum and product rule
- [ ] Notes added to Notion with connections to ML applications
- [ ] Can explain: what orthogonality means and why it matters in ML

### Day 6: Leetcode — Two Pointers Pattern

- [ ] Implemented fixed two-pointer template from memory (opposite ends)
- [ ] Implemented slow/fast pointer template from memory

**Leetcode:**
- [ ] #167 — Two Sum II (Sorted Input)
- [ ] #15 — 3Sum (Medium — very common interview question, spend time)
- [ ] #11 — Container With Most Water (Medium — classic)
- [ ] #42 — Trapping Rain Water (Medium-Hard — attempt it, don't worry if you don't solve it)

### Day 7: Third Codeforces Contest (Div. 3)

- [ ] Graduated to Div. 3 (harder than Div. 4)
- [ ] Solved A ✓
- [ ] Solved B ✓
- [ ] Attempted C ✓
- [ ] Practiced: identifying edge cases before writing any code
- [ ] Added to [Contest Log](../README.md#-codeforces-contest-log)

---

## 📅 WEEK 7 — K-Means, Decision Trees, PCA + Web Fundamentals

### Day 1: K-Means Clustering from Scratch

**Implement `KMeans` class:**
- [ ] `__init__` with `k` and `max_iterations`
- [ ] `fit(X)` — full EM loop: init centroids → assign clusters → recompute centroids → check convergence
- [ ] `_assign_clusters(X)` — assign each point to nearest centroid using Euclidean distance
- [ ] Convergence check using `np.allclose`

**Visualization:**
- [ ] Plotted 2D clustered data with different colors per cluster
- [ ] Showed centroid movement across iterations (animation or step-by-step plot)
- [ ] **Blog post written:** "K-Means from scratch — with visualization" (publish this week or next)

### Day 2: Decision Tree (Simplified Version)

*A full decision tree is complex. Build a simplified binary classifier.*

**Implement:**
- [ ] `gini_impurity(y)` function
- [ ] `information_gain(y, y_left, y_right)` function
- [ ] A `DecisionNode` class with threshold and feature index
- [ ] Recursive tree building up to a max depth
- [ ] `predict(X)` — traverse the tree for each sample
- [ ] Tested on a simple dataset (Iris binary classification)

### Day 3: PCA from Scratch — Math Advantage Pays Off Here

*Most students follow a tutorial. You're going to derive it using what you know about eigendecomposition.*

**Implement `PCA` class:**
- [ ] `fit(X)` — center data, compute covariance matrix, eigendecomposition, sort by descending eigenvalue, store top n components
- [ ] `transform(X)` — project data onto principal components
- [ ] `fit_transform(X)` — convenience method
- [ ] `explained_variance_ratio` stored and accessible

**Applied to MNIST:**
- [ ] Used MNIST handwritten digits dataset
- [ ] Reduced from 784 dimensions → 2 dimensions
- [ ] Plotted the 2D result (digits should visually cluster by class)
- [ ] Can explain: "PCA finds the directions of maximum variance using eigendecomposition of the covariance matrix"

**Blog post written (this is the important one):**
- [ ] Title: "I implemented PCA from scratch using only NumPy — here's the math"
- [ ] Covers: covariance matrix, eigendecomposition, why eigenvectors are principal components
- [ ] Includes the MNIST visualization
- [ ] Published (Hashnode or dev.to or GitHub Pages)
- [ ] **5 ML algorithms total now implemented:** Linear Regression ✓ Logistic Regression ✓ K-Means ✓ Decision Tree ✓ PCA ✓

### Days 4–5: Web Fundamentals

Use The Odin Project — Foundations Path (theodinproject.com). 2 days, not more.

**HTML:**
- [ ] Understand elements, attributes, semantic HTML (header, main, section, article, footer)
- [ ] Can build a form (input, label, button)
- [ ] Know when to use div vs semantic elements

**CSS:**
- [ ] Understand the box model (margin, border, padding, content)
- [ ] Can use Flexbox to center things and create layouts
- [ ] Know CSS selectors (class, id, element, pseudo-class)
- [ ] One media query working (mobile breakpoint)

**JavaScript:**
- [ ] Variables (`let`, `const` — understand the difference)
- [ ] Functions (declaration and arrow functions)
- [ ] DOM manipulation: `document.querySelector`, `addEventListener`, `innerHTML`
- [ ] Built one small interactive element (button that does something on click)

### Day 6: Codeforces — Graphs Intro Reading

- [ ] Read Competitive Programmer's Handbook Chapter 11 (Basics of Graphs)
- [ ] Read CPH Chapter 12 (Graph traversal — BFS and DFS explained)
- [ ] Solved Codeforces 580A (Kefa and First Steps)
- [ ] Solved Codeforces 339A (Helpful Maths)

### Day 7: Week Review + Notion Audit

- [ ] Phase 2 and 3 concepts reviewed in Notion
- [ ] All 5 algorithm implementations tested and working
- [ ] Shakiest concepts identified and flagged for extra practice

---

## 📅 WEEK 8 — Portfolio Website + Consolidation

### Days 1–3: Build and Deploy Portfolio Website

**Build requirements (plain HTML/CSS + minimal JS — no React, no template):**
- [ ] Your name and 2-line bio ("CS + AI student at SST. Interested in ML systems and software engineering.")
- [ ] Links: GitHub, LinkedIn, blog — all working
- [ ] Projects section with 3–4 projects, short descriptions, GitHub links
- [ ] Skills section (only honest skills — Python, NumPy, Git, SQL, Algorithms, Data Structures, Basic ML)
- [ ] "Currently learning" section
- [ ] Mobile-responsive (at least one CSS media query)
- [ ] Clean design: simple layout, black/white + one accent color, readable font

**Deployment:**
- [ ] Hosted on GitHub Pages at `yourusername.github.io`
- [ ] Custom repo named exactly `yourusername.github.io` on GitHub
- [ ] All links verified working on mobile and desktop
- [ ] Site loads in under 3 seconds

**Design check:**
- [ ] Looked at brittanychiang.com for inspiration (principles: readable, fast, focused)
- [ ] Did NOT copy — absorbed the principles only

### Days 4–5: Weak Area Remediation

Check your tracking sheet. Days 4–5 are for whatever you're shakiest on.

Priority order:
- [ ] If recursion still shaky: redo Week 3 recursive exercises without looking at previous solutions
- [ ] If linked list shaky: redo reverse, cycle detection, find middle from memory
- [ ] If binary search shaky: redo all 5 binary search problems without notes
- [ ] If PCA derivation shaky: write it out on paper from memory (center → covariance → eigen → sort → project)

### Day 6: Fourth Codeforces Contest — Live

- [ ] Participated in a LIVE Div. 3 or Div. 4 contest (not virtual — live)
- [ ] Solved A ✓, B ✓, attempted C ✓
- [ ] Current Codeforces rating: _______
- [ ] Added to [Contest Log](../README.md#-codeforces-contest-log)

### Day 7: Major Blog Post + GitHub Cleanup

**Write and publish: "5 ML algorithms I implemented from scratch in NumPy"**
- [ ] Post written covering all 5 algorithms
- [ ] Each section has: 3–5 sentence explanation, key code snippet, one visual
- [ ] Covers: why gradient descent works (linear regression), why sigmoid + cross-entropy (logistic), EM-like structure (k-means), information gain (decision tree), eigendecomposition = directions of max variance (PCA)
- [ ] Published on blog
- [ ] Shared on LinkedIn (tag SST if they have a page)

**GitHub audit:**
- [ ] Every repo has a README ✓
- [ ] Every README includes: what the project is, how to run it, what you learned ✓
- [ ] Best 4 repos pinned on GitHub profile ✓
- [ ] GitHub profile README created (yourusername/yourusername repo with README.md) ✓
- [ ] Profile README includes: who you are, what you're building, links to blog and portfolio ✓

---

## 📦 Phase 3 Exit Criteria

*Do not move to Phase 4 until all of these are true:*

- [ ] All 5 ML algorithms implemented from scratch in NumPy and tested ✓
- [ ] PCA applied to MNIST with 2D visualization ✓
- [ ] Portfolio website live at `yourusername.github.io` ✓
- [ ] "5 ML algorithms from scratch" blog post published ✓
- [ ] 40+ Leetcode problems total (cumulative) ✓
- [ ] 4 Codeforces contests participated in ✓
- [ ] GitHub profile README live ✓
- [ ] 5+ repos on GitHub with proper READMEs ✓
