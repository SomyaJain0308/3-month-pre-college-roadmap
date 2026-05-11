<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>GSoC Month 1 Tracker — May–Jun 2026</title>
<style>
  *{box-sizing:border-box;margin:0;padding:0}
  :root{
    --bg:#0d0f12;--surface:#161a1f;--surface2:#1e2329;--border:#2a2f38;--border2:#3a404c;
    --text:#e8eaed;--text2:#9aa3b0;--text3:#5c6472;
    --green:#22c55e;--green-bg:#0d2818;--green-dim:#16a34a;
    --amber:#f59e0b;--amber-bg:#2a1f08;
    --blue:#60a5fa;--blue-bg:#0f1e35;
    --mono:'JetBrains Mono','Fira Code','Courier New',monospace;
    --sans:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  }
  body{background:var(--bg);color:var(--text);font-family:var(--sans);min-height:100vh}
  a{color:var(--blue);text-decoration:none}
  a:hover{text-decoration:underline}
  .shell{max-width:780px;margin:0 auto;padding:24px 16px 60px}
  .header{margin-bottom:28px}
  .header-top{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:12px}
  .title{font-family:var(--mono);font-size:20px;font-weight:700;color:var(--text);letter-spacing:-0.5px}
  .subtitle{font-size:12px;color:var(--text3);margin-top:3px;font-family:var(--mono)}
  .total-pct{font-family:var(--mono);font-size:28px;font-weight:700;color:var(--green)}
  .prog-track{height:4px;background:var(--surface2);border-radius:99px;overflow:hidden}
  .prog-fill{height:100%;background:var(--green);border-radius:99px;transition:width 0.4s ease}
  .week-tabs{display:flex;gap:6px;margin-bottom:20px;flex-wrap:wrap}
  .wtab{padding:8px 14px;border-radius:6px;border:1px solid var(--border);background:transparent;
        cursor:pointer;font-family:var(--mono);font-size:12px;color:var(--text2);transition:all 0.15s;text-align:left}
  .wtab:hover{border-color:var(--border2);color:var(--text)}
  .wtab.active{border-color:var(--green-dim);background:var(--green-bg);color:var(--green)}
  .wtab-title{font-weight:700;display:block}
  .wtab-sub{font-size:10px;opacity:0.7;margin-top:1px;display:block}
  .wtab-pct{font-size:10px;margin-top:4px;display:block}
  .week-label{font-family:var(--mono);font-size:10px;color:var(--text3);letter-spacing:0.1em;
              text-transform:uppercase;margin-bottom:10px;font-weight:600}
  .day-card{border:1px solid var(--border);border-radius:8px;overflow:hidden;margin-bottom:8px;transition:border-color 0.15s}
  .day-card:hover{border-color:var(--border2)}
  .day-card.is-today{border-color:var(--blue);box-shadow:0 0 0 1px var(--blue-bg)}
  .day-card.is-done{opacity:0.6}
  .day-card.is-checkpoint{border-color:var(--amber)}
  .day-head{width:100%;padding:11px 14px;background:transparent;border:none;cursor:pointer;
            display:flex;align-items:center;gap:12px;text-align:left;transition:background 0.15s}
  .day-head:hover{background:var(--surface)}
  .day-num{width:32px;height:32px;border-radius:6px;flex-shrink:0;background:var(--surface2);
           display:flex;align-items:center;justify-content:center;
           font-family:var(--mono);font-size:11px;font-weight:700;color:var(--text3)}
  .day-num.done{background:var(--green-bg);color:var(--green)}
  .day-num.today{background:var(--blue-bg);color:var(--blue)}
  .day-num.chk{background:var(--amber-bg);color:var(--amber)}
  .day-info{flex:1;min-width:0}
  .day-topic{font-size:13px;font-weight:600;color:var(--text);display:flex;align-items:center;gap:6px;flex-wrap:wrap}
  .day-meta{font-size:11px;color:var(--text3);margin-top:2px;font-family:var(--mono)}
  .badge{font-size:10px;padding:2px 7px;border-radius:99px;font-weight:600;white-space:nowrap}
  .badge-today{background:var(--blue-bg);color:var(--blue)}
  .badge-chk{background:var(--amber-bg);color:var(--amber)}
  .day-pct{font-family:var(--mono);font-size:12px;color:var(--text3);flex-shrink:0}
  .chevron{font-size:12px;color:var(--text3);flex-shrink:0;transition:transform 0.2s}
  .chevron.open{transform:rotate(180deg)}
  .day-divider{height:2px;background:var(--border)}
  .day-prog{height:100%;transition:width 0.3s}
  .day-body{padding:14px 16px 16px;background:var(--surface)}
  .day-goal{font-size:13px;color:var(--text2);line-height:1.6;margin-bottom:14px;
            border-left:2px solid var(--border2);padding-left:10px}
  .section-label{font-family:var(--mono);font-size:10px;color:var(--text3);letter-spacing:0.1em;
                 text-transform:uppercase;font-weight:700;margin-bottom:8px}
  .resources{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:16px}
  .res-link{display:inline-flex;align-items:center;gap:6px;padding:6px 10px;border-radius:6px;
            border:1px solid var(--border);background:var(--surface2);font-size:12px;color:var(--text2);
            text-decoration:none;transition:all 0.15s;line-height:1.3}
  .res-link:hover{border-color:var(--border2);color:var(--text);background:var(--bg);text-decoration:none}
  .tasks{display:flex;flex-direction:column}
  .task-row{display:flex;align-items:flex-start;gap:10px;padding:9px 0;
            border-bottom:1px solid var(--border);cursor:pointer;user-select:none}
  .task-row:last-child{border-bottom:none}
  .chkbox{width:18px;height:18px;border-radius:4px;flex-shrink:0;margin-top:1px;
          border:1.5px solid var(--border2);background:transparent;
          display:flex;align-items:center;justify-content:center;transition:all 0.15s;font-size:11px}
  .chkbox.checked{border-color:var(--green);background:var(--green);color:#000}
  .task-text{font-size:13px;color:var(--text2);line-height:1.5}
  .task-text.checked{text-decoration:line-through;color:var(--text3)}
</style>
</head>
<body>
<div class="shell">
  <div class="header">
    <div class="header-top">
      <div>
        <div class="title">gsoc_month1.py</div>
        <div class="subtitle">// May 13 – Jun 9, 2026 &nbsp;·&nbsp; Python Mastery &nbsp;·&nbsp; Starts: May 13</div>
      </div>
      <div class="total-pct" id="totalPct">0%</div>
    </div>
    <div class="prog-track"><div class="prog-fill" id="mainProg" style="width:0%"></div></div>
    <div style="font-size:11px;color:var(--text3);font-family:var(--mono);margin-top:5px" id="totalLabel">0 / 140 tasks</div>
  </div>
  <div class="week-tabs" id="weekTabs"></div>
  <div class="week-label" id="weekLabel"></div>
  <div id="dayList"></div>
</div>

<script>
const DAYS=[
  // ── WEEK 1 · May 13–19 ── Functional Python
  {n:1,w:1,date:'May 13',topic:'*args & **kwargs',tag:'functional',today:true,
   goal:'Day 1. Master Python\'s variable-argument syntax — the foundation of every library you will read in open source.',
   res:[
     {icon:'📄',label:'Real Python: *args & **kwargs',url:'https://realpython.com/python-kwargs-and-args/'},
     {icon:'▶',label:'Corey Schafer: Python Tutorial Playlist',url:'https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU'},
   ],
   tasks:['Read the Real Python article fully — no skimming','Write 5 functions using only *args','Write 5 functions using only **kwargs','Write 3 functions combining both *args and **kwargs','Challenge: replicate Python\'s built-in print() signature from scratch']},

  {n:2,w:1,date:'May 14',topic:'List, Dict & Set Comprehensions',tag:'functional',
   goal:'Replace verbose loops with clean expressions. This is how real Python code looks.',
   res:[
     {icon:'📄',label:'Real Python: List Comprehensions',url:'https://realpython.com/list-comprehension-python/'},
     {icon:'📖',label:'Python Docs: Data Structures',url:'https://docs.python.org/3/tutorial/datastructures.html'},
   ],
   tasks:['List comprehensions: 10 exercises (evens, squares, string transforms)','Dict comprehensions: invert a dict, square all values','Set comprehensions: find unique word lengths in a sentence','Nested comprehensions: flatten a 2D matrix into 1D','Challenge: rewrite 5 Day 1 functions using comprehensions']},

  {n:3,w:1,date:'May 15',topic:'Lambda, map, filter, zip',tag:'functional',
   goal:'The functional quartet. NumPy and pandas use these patterns everywhere.',
   res:[
     {icon:'📄',label:'Real Python: Lambda Functions',url:'https://realpython.com/python-lambda/'},
     {icon:'📄',label:'Real Python: map() built-in',url:'https://realpython.com/python-map-function/'},
   ],
   tasks:['Write 5 lambdas: sorting keys, transforms, conditional logic','Use map() to transform a list — no for-loops','Use filter() to select items — no loops allowed','Use zip() to merge two lists into a dict in one line','Challenge: chain map + filter + sorted in a single expression']},

  {n:4,w:1,date:'May 16',topic:'Unpacking & Walrus Operator',tag:'functional',
   goal:'Unpacking appears in every open source codebase. Know every pattern cold.',
   res:[
     {icon:'📄',label:'Real Python: Unpacking in Python',url:'https://realpython.com/python-unpacking-operator/'},
     {icon:'📄',label:'Real Python: Walrus Operator :=',url:'https://realpython.com/walrus-operator/'},
   ],
   tasks:['Swap without temp variable — 5 variations','Extended unpacking: a, *b, c = [1,2,3,4,5]','Unpack tuples directly in a for loop','Unpack into function calls: func(*list, **dict)','Use walrus := in a while loop and a list comprehension']},

  {n:5,w:1,date:'May 17',topic:'itertools — The Secret Weapon',tag:'functional',
   goal:'Every serious Python codebase uses itertools. Reading code without knowing it is painful.',
   res:[
     {icon:'📄',label:'Real Python: itertools Recipes',url:'https://realpython.com/python-itertools/'},
     {icon:'📖',label:'Python Docs: itertools',url:'https://docs.python.org/3/library/itertools.html'},
   ],
   tasks:['chain(): flatten nested iterables without recursion','islice() + cycle(): paginate an infinite sequence','product(): generate all pairs from two lists','groupby(): group a list of dicts by a shared key','combinations(): find all unique pairs in a roster']},

  {n:6,w:1,date:'May 18',topic:'Practice Day — Week 1',tag:'practice',
   goal:'No new theory. Combine everything from Week 1 in pure coding exercises.',
   res:[
     {icon:'🔗',label:'Exercism: Python Track',url:'https://exercism.org/tracks/python'},
     {icon:'🔗',label:'Codewars: Python Katas',url:'https://www.codewars.com/kata/search/python'},
   ],
   tasks:['Solve 5 Exercism Python exercises using only Week 1 concepts','No for-loops: solve 3 problems using map/filter/zip only','Write a function that flattens any-depth nested list using itertools','Review Days 1–5 — refactor anything ugly or repetitive','Push everything to GitHub with a proper README']},

  {n:7,w:1,date:'May 19',topic:'Build: Text Processor CLI',tag:'build',
   goal:'First real project. Uses *args, **kwargs, comprehensions, itertools. Push it.',
   res:[
     {icon:'📄',label:'Real Python: argparse for CLIs',url:'https://realpython.com/command-line-interfaces-python-argparse/'},
   ],
   tasks:['Plan a CLI that reads text files and outputs word stats','Accept multiple files via *args','Accept options via **kwargs: ignore_case, top_n','Use comprehensions + Counter for word frequency','Push to GitHub with usage examples in the README']},

  // ── WEEK 2 · May 20–26 ── Python Essentials
  {n:8,w:2,date:'May 20',topic:'String Methods Mastery',tag:'essentials',
   goal:'Strings are in every program. Know every method without opening the docs.',
   res:[
     {icon:'📄',label:'Real Python: Python Strings',url:'https://realpython.com/python-strings/'},
     {icon:'📖',label:'Python Docs: str methods (read all)',url:'https://docs.python.org/3/library/stdtypes.html#string-methods'},
   ],
   tasks:['Go through every str method — one live example each','Master f-string formatting: padding, alignment, number specs','split, join, strip, replace, find, count — 3 exercises each','Build: Caesar cipher using string methods only','Build: URL slug generator (spaces→hyphens, lowercase, strip special chars)']},

  {n:9,w:2,date:'May 21',topic:'File I/O & pathlib',tag:'essentials',
   goal:'Open source projects read and write files constantly. This must become automatic.',
   res:[
     {icon:'📄',label:'Real Python: Working with Files',url:'https://realpython.com/read-write-files-python/'},
     {icon:'📖',label:'Python Docs: pathlib',url:'https://docs.python.org/3/library/pathlib.html'},
   ],
   tasks:['Read a file line by line using a generator — never load all at once','Write and append to files always inside context managers','Use pathlib.Path — the modern standard (not os.path)','Parse a CSV file manually with file I/O only (no pandas yet)','Build: note-taking CLI that saves timestamped entries to a .txt']},

  {n:10,w:2,date:'May 22',topic:'Exception Handling',tag:'essentials',
   goal:'Real code fails. Handling errors properly separates contributors from beginners.',
   res:[
     {icon:'📄',label:'Real Python: Python Exceptions',url:'https://realpython.com/python-exceptions/'},
     {icon:'📄',label:'Real Python: raise & custom exceptions',url:'https://realpython.com/python-raise-exception/'},
     {icon:'📖',label:'Python Docs: Built-in Exceptions list',url:'https://docs.python.org/3/library/exceptions.html'},
   ],
   tasks:['try / except / else / finally — understand all FOUR blocks','Always catch specific exceptions — never bare except','Create 3 custom exception classes inheriting from Exception','Use raise to re-raise with context: raise NewError() from original_err','Wrap Day 9 file I/O with proper, specific exception handling']},

  {n:11,w:2,date:'May 23',topic:'Modules, Packages & Imports',tag:'essentials',
   goal:'You will import thousands of modules in open source. Know how Python finds them.',
   res:[
     {icon:'📄',label:'Real Python: Modules & Packages',url:'https://realpython.com/python-modules-packages/'},
     {icon:'📖',label:'Python Docs: The import system',url:'https://docs.python.org/3/reference/import.html'},
   ],
   tasks:['Create a multi-file Python project with imports between files','Understand __init__.py — when you need it and when you don\'t','Absolute vs relative imports — know the difference cold','Explain __name__ == "__main__" — what does this guard actually do?','Create a package with 3 submodules that import from each other']},

  {n:12,w:2,date:'May 24',topic:'Virtual Environments & pip',tag:'essentials',
   goal:'Every GSoC contribution starts with this. Make it muscle memory.',
   res:[
     {icon:'📄',label:'Real Python: Virtual Environments',url:'https://realpython.com/python-virtual-environments-a-primer/'},
     {icon:'📖',label:'pip documentation',url:'https://pip.pypa.io/en/stable/'},
   ],
   tasks:['Create venv, activate, deactivate — do it 10 times until instant','pip install, pip freeze, pip install -r requirements.txt','Install a specific version: pip install requests==2.28.0','Read a real open source repo\'s requirements.txt — research each dep','Understand pyproject.toml vs setup.py vs requirements.txt']},

  {n:13,w:2,date:'May 25',topic:'Practice Day — Week 2',tag:'practice',
   goal:'Consolidate Week 2. Focus on making your code robust and production-ready.',
   res:[
     {icon:'🔗',label:'Exercism: Python Track',url:'https://exercism.org/tracks/python'},
   ],
   tasks:['Add proper exception handling to all Week 1 projects','Refactor all file I/O to use pathlib throughout','Create a proper package structure for your best project','Solve 5 Exercism exercises requiring error handling','Push all updates with meaningful commit messages']},

  {n:14,w:2,date:'May 26',topic:'Build: File Organizer',tag:'build',
   goal:'Week 2 project. File I/O + exceptions + modules + packages = real usable tool.',
   res:[
     {icon:'📄',label:'Real Python: Working with Files in Python',url:'https://realpython.com/working-with-files-in-python/'},
   ],
   tasks:['Script that sorts files into folders by extension (.mp4→videos/, .pdf→docs/)','Use pathlib for all file system operations','Handle FileNotFoundError, PermissionError, OSError gracefully','Load extension→folder rules from a config.json','Push to GitHub with a demo screenshot in the README']},

  // ── WEEK 3 · May 27–Jun 2 ── OOP
  {n:15,w:3,date:'May 27',topic:'Classes & __init__',tag:'oop',
   goal:'The foundation of OOP. Everything in Python is a class — understand it at the deepest level.',
   res:[
     {icon:'📄',label:'Real Python: OOP in Python 3',url:'https://realpython.com/python3-object-oriented-programming/'},
     {icon:'▶',label:'Corey Schafer: OOP Part 1 — Classes & Instances',url:'https://www.youtube.com/watch?v=ZDa-Z5JzLYM'},
   ],
   tasks:['Build a BankAccount class: deposit, withdraw, get_balance','Add __init__ with validation (no negative balances on creation)','Understand self — it\'s just the first argument, not magic','Add a transaction history list as an instance variable','Create 10 BankAccount instances and test every method']},

  {n:16,w:3,date:'May 28',topic:'Dunder / Magic Methods',tag:'oop',
   goal:'What separates Python OOP from every other language. Libraries use these everywhere.',
   res:[
     {icon:'▶',label:'Corey Schafer: OOP Part 4 — Special/Magic Methods',url:'https://www.youtube.com/watch?v=3ohzBxoFHAY'},
     {icon:'📄',label:'Real Python: Python Magic Methods',url:'https://realpython.com/python-magic-methods/'},
   ],
   tasks:['Add __str__ (user-friendly) and __repr__ (dev-friendly) to BankAccount','Add __len__ — returns number of transactions','Add __eq__ — two accounts equal if same account number','Add __add__ — merge two accounts into a new one','Challenge: add __iter__ to loop over transactions directly']},

  {n:17,w:3,date:'May 29',topic:'Inheritance & super()',tag:'oop',
   goal:'Every framework uses inheritance. You\'ll see it in every GSoC codebase on day one.',
   res:[
     {icon:'▶',label:'Corey Schafer: OOP Part 3 — Inheritance',url:'https://www.youtube.com/watch?v=RSl87lqOXDE'},
     {icon:'📄',label:'Real Python: Inheritance & Composition',url:'https://realpython.com/inheritance-composition-python/'},
   ],
   tasks:['Create SavingsAccount and CheckingAccount from BankAccount','Use super().__init__() correctly in both subclasses','Override withdraw() differently in each subclass','Understand isinstance() and issubclass() — test both','Research: when is composition better than inheritance? Write a short note']},

  {n:18,w:3,date:'May 30',topic:'Class vs Static vs Instance Methods',tag:'oop',
   goal:'Classic interview question AND daily open source reality. Know it cold.',
   res:[
     {icon:'▶',label:'Corey Schafer: OOP Part 2 — Class & Static Methods',url:'https://www.youtube.com/watch?v=rq8cL2XMM5M'},
   ],
   tasks:['Add @classmethod from_json(cls, data) constructor to BankAccount','Add @staticmethod validate_amount(amount) utility','Articulate out loud: why @classmethod takes cls and not self','Write a class with all 3 types that makes logical sense','Find one example of each type in a real library\'s source code']},

  {n:19,w:3,date:'May 31',topic:'@property Decorator',tag:'oop',
   goal:'Getters/setters the Python way. NumPy uses @property constantly.',
   res:[
     {icon:'▶',label:'Corey Schafer: OOP Part 5 — Property Decorators',url:'https://www.youtube.com/watch?v=jCzT9XFZ5bw'},
     {icon:'📄',label:'Real Python: Python property()',url:'https://realpython.com/python-property/'},
   ],
   tasks:['Add @property balance computed from transaction history','Add @balance.setter with validation','Add @balance.deleter that resets history to zero','Understand why @property beats public attributes in library design','Refactor BankAccount to use @property throughout']},

  {n:20,w:3,date:'Jun 1',topic:'Practice OOP',tag:'practice',
   goal:'Build OOP from scratch without looking anything up. Struggling is the point.',
   res:[
     {icon:'🔗',label:'Exercism: Python OOP exercises',url:'https://exercism.org/tracks/python'},
   ],
   tasks:['Build a Deck of Cards class from scratch — no hints','Add shuffle(), deal(n), remaining as @property','Add __len__, __str__, __iter__ to Deck','Add a Hand class using composition (not inheritance)','Push to GitHub — real portfolio material']},

  {n:21,w:3,date:'Jun 2',topic:'Build: OOP Project',tag:'build',
   goal:'Week 3 project. Use everything: classes, dunder methods, @property, file I/O, exceptions.',
   res:[
     {icon:'📄',label:'Real Python: Python pathlib',url:'https://realpython.com/python-pathlib/'},
   ],
   tasks:['Build a Todo List app: Task class + TodoList class','Use dunder methods, @property, @classmethod throughout','Save/load tasks from a JSON file using Week 2 file I/O skills','Handle all errors: file not found, invalid input, duplicates','Push to GitHub with README and usage examples']},

  // ── WEEK 4 · Jun 3–9 ── Advanced Python + Translator Project
  {n:22,w:4,date:'Jun 3',topic:'Decorators From Scratch',tag:'advanced',
   goal:'The most important advanced concept in Python. Your translator will use @retry and @lru_cache.',
   res:[
     {icon:'📄',label:'Real Python: Primer on Decorators',url:'https://realpython.com/primer-on-python-decorators/'},
     {icon:'📖',label:'Python Docs: functools.wraps',url:'https://docs.python.org/3/library/functools.html#functools.wraps'},
   ],
   tasks:['Build a @timer decorator that measures and prints runtime','Build a @logger that prints function name, args, return value','Build a @retry(n) decorator that accepts arguments','Use functools.wraps — understand exactly why you need it','Read 2 decorators from a real library\'s source (Flask @app.route is great)']},

  {n:23,w:4,date:'Jun 4',topic:'Generators & yield',tag:'advanced',
   goal:'Memory-efficient processing. Your translator uses generators for large file inputs.',
   res:[
     {icon:'📄',label:'Real Python: Introduction to Generators',url:'https://realpython.com/introduction-to-python-generators/'},
     {icon:'📖',label:'Python Docs: yield expressions',url:'https://docs.python.org/3/reference/expressions.html#yield-expressions'},
   ],
   tasks:['Build a fibonacci() generator — infinite, lazy sequence','Build a file_reader(path) generator yielding one line at a time','Use yield from to delegate to a sub-generator','Compare memory: list of 1M ints vs generator — use tracemalloc','Build a pipeline: read file → filter blanks → yield sentences']},

  {n:24,w:4,date:'Jun 5',topic:'Context Managers',tag:'advanced',
   goal:'You\'ve used with open(). Now build your own. Your translator uses these for API sessions.',
   res:[
     {icon:'📄',label:'Real Python: Context Managers & with',url:'https://realpython.com/python-with-statement/'},
     {icon:'📖',label:'Python Docs: contextlib',url:'https://docs.python.org/3/library/contextlib.html'},
   ],
   tasks:['Build a Timer context manager using __enter__ and __exit__','Build a TempDirectory that creates and auto-cleans a temp folder','Use @contextmanager from contextlib (generator approach)','What happens when an exception fires inside with? Find out.','Add a context manager to BankAccount from Week 3 (auto-save on exit)']},

  {n:25,w:4,date:'Jun 6',topic:'functools & Advanced Tools',tag:'advanced',
   goal:'lru_cache will cache translated phrases in your project to avoid redundant API calls.',
   res:[
     {icon:'📄',label:'Real Python: functools module guide',url:'https://realpython.com/python-functools/'},
     {icon:'📖',label:'Python Docs: functools',url:'https://docs.python.org/3/library/functools.html'},
   ],
   tasks:['lru_cache: cache translated phrases — avoid repeat API calls (directly useful!)','partial(): pre-fill arguments of a translate() function','reduce(): implement your own sum() and max() from scratch','wraps: fix all your Week 4 decorators to preserve metadata','Challenge: build memoize() from scratch — replicate lru_cache behavior']},

  {n:26,w:4,date:'Jun 7',topic:'Translator — Plan & Structure',tag:'build',
   goal:'Your checkpoint project starts now. Plan before writing a single line of code.',
   res:[
     {icon:'📦',label:'deep-translator on GitHub',url:'https://github.com/nidhaloff/deep-translator'},
     {icon:'📦',label:'gTTS (Google Text-to-Speech) docs',url:'https://gtts.readthedocs.io/en/latest/'},
     {icon:'📄',label:'Real Python: argparse tutorial',url:'https://realpython.com/command-line-interfaces-python-argparse/'},
   ],
   tasks:['pip install deep-translator gtts — test both work in a fresh venv','Design classes on paper: Translator, VoiceEngine, TranslatorApp','Plan CLI: translate "text", --no-audio, --file input.txt, --save out.mp3','Set up project structure: src/, tests/, README.md, requirements.txt','Create GitHub repo, push skeleton with README describing the project']},

  {n:27,w:4,date:'Jun 8',topic:'Translator — Build Day',tag:'build',
   goal:'8 hours of focused building. Hindi → English text + American accent audio. No distractions.',
   res:[
     {icon:'📄',label:'deep-translator: GoogleTranslator usage',url:'https://deep-translator.readthedocs.io/en/latest/usage.html'},
     {icon:'📄',label:'gTTS: tld="com" for American accent',url:'https://gtts.readthedocs.io/en/latest/module.html#localized-accents'},
     {icon:'📄',label:'Real Python: pytest testing',url:'https://realpython.com/pytest-python-testing/'},
   ],
   tasks:['Implement Translator class using GoogleTranslator from deep-translator','Implement VoiceEngine using gTTS with tld="com" for American accent','Build the full argparse CLI — all flags working end to end','Add @retry on API calls + @lru_cache to avoid retranslating same text','Write 3 pytest tests — translate known phrases, verify output type and content']},

  {n:28,w:4,date:'Jun 9',topic:'⚑ CHECKPOINT: Ship the Translator',tag:'checkpoint',
   goal:'Ship it. A working pushed project beats a perfect unpushed one every single time.',
   res:[
     {icon:'📄',label:'Real Python: Documenting Python Code',url:'https://realpython.com/documenting-python-code/'},
   ],
   tasks:['Test all CLI flags manually: direct text, --file, --no-audio, --save','Handle all error cases: no internet, empty input, bad file path','Write full README: what it does, install steps, usage examples with sample output','Test fresh: new venv → pip install -r requirements.txt → runs clean','⚑ CHECKPOINT: Tag v1.0, push — project is live, documented, and working']},
];

const WEEKS=[
  {n:1,label:'Week 1',sub:'Functional Python',days:'May 13–19'},
  {n:2,label:'Week 2',sub:'Essentials',days:'May 20–26'},
  {n:3,label:'Week 3',sub:'OOP',days:'May 27–Jun 2'},
  {n:4,label:'Week 4',sub:'Advanced + Translator',days:'Jun 3–9'},
];

let done={};
let activeWeek=1;
let openDay=1;

function save(){try{localStorage.setItem('gsoc-m1-v2',JSON.stringify(done));}catch(e){}}
function load(){try{const r=localStorage.getItem('gsoc-m1-v2');if(r)done=JSON.parse(r);}catch(e){}}
function tasks(day){return day.tasks.map((t,i)=>({id:'d'+day.n+'_'+i,text:t}));}
function pct(day){const ts=tasks(day);const c=ts.filter(t=>done[t.id]).length;return ts.length?Math.round(c/ts.length*100):0;}
function toggle(id){done[id]=!done[id];save();render();}

function renderHeader(){
  const all=DAYS.flatMap(tasks);
  const c=all.filter(t=>done[t.id]).length;
  const p=Math.round(c/all.length*100);
  document.getElementById('totalPct').textContent=p+'%';
  document.getElementById('mainProg').style.width=p+'%';
  document.getElementById('totalLabel').textContent=c+' / '+all.length+' tasks completed';
}

function renderTabs(){
  document.getElementById('weekTabs').innerHTML=WEEKS.map(w=>{
    const ts=DAYS.filter(d=>d.w===w.n).flatMap(tasks);
    const c=ts.filter(t=>done[t.id]).length;
    const p=ts.length?Math.round(c/ts.length*100):0;
    return `<button class="wtab${w.n===activeWeek?' active':''}" onclick="activeWeek=${w.n};openDay=-1;render()">
      <span class="wtab-title">${w.label}</span>
      <span class="wtab-sub">${w.sub}</span>
      <span class="wtab-pct" style="color:${p===100?'#22c55e':'#5c6472'}">${p}% done</span>
    </button>`;
  }).join('');
  const w=WEEKS.find(x=>x.n===activeWeek);
  document.getElementById('weekLabel').textContent='// '+w.sub+' · '+w.days;
}

function renderDays(){
  document.getElementById('dayList').innerHTML=DAYS.filter(d=>d.w===activeWeek).map(day=>{
    const ts=tasks(day);
    const p=pct(day);
    const isToday=!!day.today;
    const isDone=p===100;
    const isCp=day.tag==='checkpoint';
    let nc='day-num'+(isDone?' done':isToday?' today':isCp?' chk':'');
    const isOpen=openDay===day.n;
    const pc=isDone?'#22c55e':isToday?'#60a5fa':'#4b5563';
    return `<div class="day-card${isToday?' is-today':''}${isDone?' is-done':''}${isCp?' is-checkpoint':''}">
      <button class="day-head" onclick="openDay=${isOpen?-1:day.n};render()">
        <div class="${nc}">${isDone?'✓':day.n}</div>
        <div class="day-info">
          <div class="day-topic">${day.topic}
            ${isToday?'<span class="badge badge-today">start here</span>':''}
            ${isCp?'<span class="badge badge-chk">checkpoint</span>':''}
          </div>
          <div class="day-meta">${day.date} · ${ts.filter(t=>done[t.id]).length}/${ts.length} tasks</div>
        </div>
        <div class="day-pct">${p}%</div>
        <div class="chevron${isOpen?' open':''}">▼</div>
      </button>
      <div class="day-divider"><div class="day-prog" style="width:${p}%;background:${pc}"></div></div>
      ${isOpen?`<div class="day-body">
        <div class="day-goal">${day.goal}</div>
        <div class="section-label">Resources</div>
        <div class="resources">${day.res.map(r=>`<a class="res-link" href="${r.url}" target="_blank" rel="noopener"><span>${r.icon}</span>${r.label} ↗</a>`).join('')}</div>
        <div class="section-label">Tasks</div>
        <div class="tasks">${ts.map(t=>`<div class="task-row" onclick="toggle('${t.id}')">
          <div class="chkbox${done[t.id]?' checked':''}">${done[t.id]?'✓':''}</div>
          <span class="task-text${done[t.id]?' checked':''}">${t.text}</span>
        </div>`).join('')}</div>
      </div>`:''}
    </div>`;
  }).join('');
}

function render(){renderHeader();renderTabs();renderDays();}
load();render();
</script>
</body>
</html>
