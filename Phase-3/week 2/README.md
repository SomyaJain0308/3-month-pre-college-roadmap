# Phase 3 · Week 2 — First Real Web App: Flask + Deployed

**Status: ⬜ NOT STARTED**   
**Resource: Flask docs + Render.com**

> A live deployed app with a real URL is worth 10x a local project. "Check it out here: link" in an interview or Fiverr gig changes everything.

---

## Daily LeetCode Tracker

| Day | P1 | P2 | P3 | Total |
|-----|----|----|-----|-------|
| Mon | ⬜ | ⬜ | ⬜ | 0 |
| Tue | ⬜ | ⬜ | ⬜ | 0 |
| Wed | ⬜ | ⬜ | ⬜ | 0 |
| Thu | ⬜ | ⬜ | ⬜ | 0 |
| Fri | ⬜ | ⬜ | ⬜ | 0 |
| Sat | ⬜ | ⬜ | ⬜ | 0 |
| Sun | ⬜ | ⬜ | ⬜ | 0 |

**Week total: 0 / 21 minimum**

---

## Day 1 — Flask Basics

- [ ] Install Flask in WSL2: `pip install flask`
- [ ] Understand: routes, views, templates, static files
- [ ] Build these small apps to learn the basics:
  - [ ] Hello World Flask app
  - [ ] App with multiple routes (/home, /about, /contact)
  - [ ] Template with Jinja2 — pass variable from Python to HTML
  - [ ] Form that takes user input and displays it back
- [ ] Learn HTML + CSS basics (just enough to make it look decent):
  - [ ] Basic HTML tags: div, p, h1-h6, a, img, form, input, button
  - [ ] CSS: flexbox, basic styling, colors, fonts
- [ ] LeetCode: 3 medium problems
- [ ] Commit and push

---

## Day 2 — Flask + Database

- [ ] SQLite with Flask using SQLAlchemy
- [ ] Create a model (table) for your app
- [ ] CRUD operations: Create, Read, Update, Delete via Flask routes
- [ ] User authentication:
  - [ ] Register (hash password with bcrypt)
  - [ ] Login / logout (Flask-Login)
  - [ ] Protected routes (login required)
- [ ] Flash messages for success/error feedback
- [ ] LeetCode: 3 medium problems
- [ ] Commit and push

---

## Days 3–5 — Build the App

Pick one idea and build it fully. Must have: login, database, at least 3 pages.

**Option A: Expense Tracker**
- [ ] User registration + login
- [ ] Add expense (amount, category, date, note)
- [ ] View all expenses in a table
- [ ] Filter by category or date range
- [ ] Total spent this month (dashboard stat)
- [ ] Delete an expense

**Option B: Task Manager**
- [ ] User registration + login
- [ ] Create task (title, description, due date, priority)
- [ ] Mark task as complete
- [ ] Filter: all / active / completed
- [ ] Delete task

**Option C: URL Shortener**
- [ ] User registration + login
- [ ] Paste long URL, get short code
- [ ] Redirect short URL to original
- [ ] Track click count per link
- [ ] User dashboard showing all their links

**Build checklist (whichever you pick):**
- [ ] Day 3: Models, auth, basic routes working
- [ ] Day 4: Core features working end to end
- [ ] Day 5: UI looks clean, edge cases handled, tested
- [ ] LeetCode: 3 problems each day
- [ ] Commit after every feature

---

## Day 6 — Deploy

- [ ] Create account on [Render.com](https://render.com) (free)
- [ ] Add `requirements.txt`: `pip freeze > requirements.txt`
- [ ] Add `Procfile`: `web: gunicorn app:app`
- [ ] Install gunicorn: `pip install gunicorn`
- [ ] Push to GitHub
- [ ] Connect GitHub repo to Render
- [ ] Deploy — get your live URL
- [ ] Test every feature on the live URL
- [ ] Add the live URL to your GitHub README
- [ ] Add the live URL to your LinkedIn
- [ ] LeetCode: 3 problems
- [ ] Commit and push

---

## Day 7 — Fiverr + LinkedIn + Polish

- [ ] Set up Fiverr seller profile:
  - [ ] Profile photo, description, skills
  - [ ] Gig 1: "I will build you a Python web scraper"
  - [ ] Gig 2: "I will build you a Flask web application"
  - [ ] Price: start at ₹999 — just get the first review
- [ ] LinkedIn post about your project:
  - [ ] What it does (1 line)
  - [ ] What you built it with (1 line)
  - [ ] What you learned (2 lines)
  - [ ] Live link + GitHub link
  - [ ] This post. Do it. Don't overthink it.
- [ ] GitHub profile polish:
  - [ ] Pin your best 2 projects
  - [ ] Update bio: "CS student · Python developer · Building real things"
  - [ ] Profile README (optional but impressive)
- [ ] LeetCode: 3 problems
- [ ] Mark week complete

---

## Week 2 Done When:
- [ ] Web app working end to end
- [ ] App deployed — live URL exists
- [ ] Fiverr profile live with at least 1 gig
- [ ] LinkedIn post published
- [ ] 90+ LeetCode total running count

---

[← Week 1](../week-1/README.md) | [Phase 3](../README.md) | [Week 3 →](../week-3/README.md)
