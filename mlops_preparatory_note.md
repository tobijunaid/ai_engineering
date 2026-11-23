# Learn2Earn Preparatory Book

## AI-Native Software Engineering → Machine Learning → MLOps

I understand exactly what you're trying to accomplish. You don't want to wait until February to start learning. You want to arrive at the programme with enough understanding of the fundamentals that you can follow the learning process more quickly, solve challenges more confidently, and eventually become one of the strongest people in your cohort.

And I don't want to give you a superficial tutorial full of definitions you memorise and forget.

I want this to function as a **preparatory textbook** — something you can read, study, practise, revisit, and use as a reference while you progress through the programme.

Your eventual specialization will be **MLOps (Machine Learning Operations)**, but the preparation must first establish the broader engineering foundation that makes MLOps possible.

---

## 1. Understanding the Learn2Earn curriculum

I reviewed the curriculum and the programme information on the official Learn2Earn website.

The programme describes a project-based, self-paced, challenge-driven learning environment that covers software engineering, Python, AI and machine learning, frontend and backend development, databases, APIs, Git, command-line tools, collaboration, career preparation, and specialization.

The specialization options include AI & ML, Mobile Development, DevOps & Cybersecurity, Blockchain, Game Development, and UI/UX. The programme's structure also includes practical training, internship experience, and access to paid work opportunities.

## Your learning trajectory

Phase 1 — Become a strong engineer

Python · Computer Science fundamentals · Git · Linux · Problem-solving

---

Phase 2 — Become an AI-native engineer

Data · APIs · Backend · Databases · AI tools · Machine learning

---

Phase 3 — Specialize in MLOps

Docker · CI/CD · Cloud · ML pipelines · Deployment · Monitoring · Reliability

---

Phase 4 — Build commercially valuable systems

Production AI products · SaaS · Open-source portfolio · Revenue-generating projects

### What this book will cover

I am going to structure the preparation around the actual engineering progression rather than teaching random technologies.

| Part | Subject                               | Why it matters                                |
| ---- | ------------------------------------- | --------------------------------------------- |
| 1    | Engineering mindset & problem-solving | Learn how engineers think                     |
| 2    | Computer fundamentals                 | Understand what happens beneath software      |
| 3    | Terminal & Linux                      | Control your development environment          |
| 4    | Git & GitHub                          | Collaborate and manage code                   |
| 5    | Python programming                    | Build your primary engineering language       |
| 6    | Data structures & algorithms          | Write efficient, reliable programs            |
| 7    | Software engineering                  | Build maintainable systems                    |
| 8    | Databases & SQL                       | Store and retrieve information                |
| 9    | APIs & backend development            | Connect software and services                 |
| 10   | Frontend fundamentals                 | Understand complete applications              |
| 11   | Mathematics for AI                    | Understand ML rather than blindly use it      |
| 12   | Data engineering fundamentals         | Prepare data for intelligent systems          |
| 13   | Machine learning                      | Build predictive models                       |
| 14   | Deep learning & generative AI         | Understand modern AI                          |
| 15   | AI-assisted engineering               | Use AI effectively without becoming dependent |
| 16   | Cloud & infrastructure                | Run software beyond your laptop               |
| 17   | MLOps specialization                  | Deploy, monitor, maintain, and scale ML       |
| 18   | Security & responsible AI             | Protect systems and users                     |
| 19   | Product development & business        | Build products people pay for                 |
| 20   | Portfolio & career preparation        | Demonstrate professional competence           |

This will be extensive. I will organize it in chapters, with explanations, examples, code, exercises, practical projects, and engineering notes.

---

# PART I — THE ENGINEERING MINDSET

## Chapter 1: What does it mean to be a software engineer?

Before learning Python, AI, Docker, or cloud platforms, you need to understand what software engineering actually is.

A programmer writes code.

A software engineer solves problems by designing, building, testing, maintaining, and improving software systems.

These are not necessarily mutually exclusive, but the distinction is important.

Suppose a business owner tells you:

> "I need a way to track my customers, sales, expenses, and inventory."

A beginner may immediately start writing code.

An engineer first asks:

- What problem is the business experiencing?
- Who will use the application?
- What information must be stored?
- What happens when an item is sold?
- What happens when stock runs out?
- What happens when two employees make changes simultaneously?
- How is information protected?
- How will the application be deployed?
- How will errors be detected?
- What happens if the application crashes?
- How will it be maintained after delivery?

The actual code is only one part of the solution.

### 1.1 The software engineering lifecycle

Most software projects follow some version of this process:

Problem → Requirements → Design → Implementation → Testing → Deployment → Monitoring → Improvement

#### Step 1: Identify the problem

You need to understand what needs to be solved.

Example:

A pharmacy manually tracks its inventory using notebooks. It frequently loses track of medicine expiry dates and runs out of important products.

The problem is not simply:

> Build an application.

The problem is:

> Reduce inventory errors, prevent avoidable stockouts, identify medicines approaching expiry, and improve business visibility.

That is a much better engineering starting point.

#### Step 2: Gather requirements

Requirements describe what a system must do.

Functional requirements:

- A user can add products.
- A user can record purchases.
- A user can record sales.
- The application updates stock levels.
- The system alerts users when stock is low.
- The system identifies products approaching expiry.

Non-functional requirements:

- The system should respond quickly.
- Users should not lose information.
- Data should be protected.
- The application should support multiple users.
- The application should work reliably.
- It should be easy to maintain.

#### Step 3: Design the solution

Before coding, decide:

- What components will the system contain?
- What database will it use?
- What information belongs in each table?
- How will the frontend communicate with the backend?
- What services need to interact?
- How will the system be deployed?

#### Step 4: Implement

Now write the code.

Implementation means translating your design into a working system.

#### Step 5: Test

You verify that the software behaves as expected.

You test normal behaviour, unusual situations, invalid input, failures, security boundaries, and edge cases.

#### Step 6: Deploy

You make the software available to its intended users.

#### Step 7: Monitor

You observe whether it is actually working.

For example:

- Is the application crashing?
- Is the API slow?
- Is the database running out of storage?
- Are users experiencing errors?
- Is an AI model producing poor predictions?

#### Step 8: Improve

Software is rarely finished permanently.

New requirements, bugs, performance problems, and user feedback create opportunities for improvement.

---

## Chapter 2: The problem-solving process

This is one of the most important skills you will develop during an intensive technical programme.

The ability to solve a problem independently is often more valuable than knowing a particular programming language.

### 2.1 Breaking large problems into smaller problems

This process is called decomposition.

Suppose you want to build a system that automatically analyses financial transactions and identifies suspicious activity.

The complete problem is intimidating.

Instead, divide it into smaller problems:

1. Collect transaction data.
2. Validate the data.
3. Store transactions.
4. Calculate transaction statistics.
5. Identify unusual patterns.
6. Generate risk scores.
7. Display results.
8. Send alerts.
9. Monitor the system.
10. Improve the model.

Each of these can be solved separately.

This is how complex software becomes manageable.

### 2.2 Example: build a simple expense analyser

Suppose you have this data:

```
expenses = [1500, 2500, 1000, 5000, 2000]
```

You want to calculate the total expense.

```
total = 0

for expense in expenses:
    total += expense

print(total)
```

Output:

```
12000
```

Now calculate the average.

```
average = total / len(expenses)print(average)
```

Output:

```
2400.0
```

You have just decomposed a problem into:

- A collection of values.
- A variable for accumulating a total.
- A loop.
- A calculation.

That is algorithmic thinking.

### 2.3 The four fundamental problem-solving techniques

#### A. Decomposition

Break one large problem into manageable pieces.

#### B. Pattern recognition

Look for similarities between problems you have already solved.

For example, if you know how to calculate the total price of items in a shopping cart, you can adapt the same logic to:

- Total monthly expenses.
- Total revenue.
- Total employee salaries.
- Total electricity consumption.

#### C. Abstraction

Focus on relevant details and ignore unnecessary ones.

Suppose you are developing a payment system.

You do not necessarily need to know the internal design of the bank's entire infrastructure. You need to understand the interface the bank exposes to your application.

Abstraction lets you work with a simplified representation of complex systems.

#### D. Algorithm design

Create a sequence of steps that solves the problem.

Example:

**Problem:** Determine whether a customer qualifies for a discount.

Algorithm:

1. Receive the customer's total purchase amount.
2. Check whether it is greater than or equal to ₦50,000.
3. If true, apply a 10% discount.
4. Otherwise, apply no discount.
5. Return the final price.

Python:

```
purchase_amount = 60000if purchase_amount >= 50000:    discount = purchase_amount * 0.10else:    discount = 0final_price = purchase_amount - discountprint(final_price)
```

Output:

```
54000.0
```

---

## Chapter 3: Debugging — the engineer's superpower

Debugging is the process of identifying, understanding, and correcting errors in software.

A common beginner mistake is to treat errors as proof that they are bad at programming.

This is incorrect.

Errors are normal. Experienced engineers encounter errors every day.

The difference is that experienced engineers have developed a systematic way of investigating them.

### 3.1 The debugging process

Whenever something breaks:

1. Read the error message.
2. Identify the line where the failure occurred.
3. Understand what the program expected.
4. Understand what it actually received.
5. Reproduce the error.
6. Isolate the problem.
7. Test a solution.
8. Verify that the solution does not create another problem.

### Example

```
numbers = [10, 20, 30]

print(numbers[3])
```

Error:

```
IndexError: list index out of range
```

Why?

Python lists begin indexing at zero.

| Value | Index |
| ----- | ----- |
| 10    | 0     |
| 20    | 1     |
| 30    | 2     |

There is no index `3`.

Correct:

```
print(numbers[2])
```

### 3.2 Error types you should recognise

| Error                 | Meaning                                                   |
| --------------------- | --------------------------------------------------------- |
| `SyntaxError`         | Python cannot understand the structure of the code        |
| `NameError`           | A variable or function name does not exist                |
| `TypeError`           | An operation is being used with an incompatible type      |
| `ValueError`          | The type is acceptable, but the value is invalid          |
| `IndexError`          | A list or sequence index is outside the available range   |
| `KeyError`            | A dictionary key does not exist                           |
| `AttributeError`      | An object does not have the requested attribute or method |
| `ImportError`         | An import cannot be completed                             |
| `ModuleNotFoundError` | A module cannot be located                                |
| `FileNotFoundError`   | The requested file does not exist                         |
| `ZeroDivisionError`   | A number was divided by zero                              |

### 3.3 Example: debugging a type error

Incorrect:

```
age = 24

print("I am " + age + " years old")
```

Python cannot directly concatenate a string and an integer.

One solution:

```
print(f"I am {age} years old")
```

Another:

```
print("I am " + str(age) + " years old")
```

The first approach uses an f-string and is generally cleaner.

### 3.4 AI-assisted debugging

When using an AI coding assistant, do not simply paste an error and ask it to fix everything.

Instead:

1. Paste the error.
2. Provide the relevant code.
3. Explain what you expected.
4. Explain what happened.
5. Ask for the root cause.
6. Ask for the smallest correction.
7. Ask it to explain why the correction works.

A useful prompt:

```
I am learning Python.

Here is my code:
[paste code]

Here is the error:
[paste error]

I expected:
[expected behaviour]

Please:
1. Identify the root cause.
2. Explain it in beginner-friendly language.
3. Show the smallest possible correction.
4. Explain why the correction works.
5. Give me a similar exercise to test whether I understand.
Do not rewrite my entire program.
```

This allows AI to accelerate your learning instead of replacing it.

---

# PART II — COMPUTER FUNDAMENTALS

## Chapter 4: How computers work

You cannot become a strong engineer by understanding only Python syntax.

You need a basic understanding of the computer executing your code.

### 4.1 The major components

A computer consists of several important components.

### CPU — Central Processing Unit

The CPU executes instructions.

When you run:

```
x = 10
y = 20
result = x + y
```

The processor performs operations that ultimately involve instructions represented in machine-level form.

The CPU is responsible for tasks such as:

- Arithmetic.
- Logical operations.
- Executing instructions.
- Coordinating computational activities.

### RAM — Random Access Memory

RAM provides temporary working storage.

When your program is running, its variables, objects, and other working information may occupy memory.

Example:

```
users = ["Tobi", "David", "Sarah"]
```

Python creates and manages objects in memory.

RAM is generally much faster to access than persistent storage, but its contents are normally lost when power is removed.

### Storage

Storage devices retain information even when the computer is turned off.

Examples include:

- SSDs.
- HDDs.
- USB drives.

Your Python file:

```
main.py
```

exists on storage.

When you run it, the operating system loads the necessary program information into memory, and the CPU executes instructions.

### GPU — Graphics Processing Unit

A GPU performs many computations in parallel.

Although originally designed for graphics, GPUs are especially useful for machine learning because neural networks involve enormous numbers of mathematical operations.

For example, training a neural network may involve multiplying large matrices.

GPUs can perform many of these operations simultaneously.

---

## Chapter 5: Bits, bytes, and binary

Computers fundamentally represent information using binary.

Binary uses only two digits:

```
0
1
```

These correspond conceptually to two states.

A bit is one binary digit.

A byte contains eight bits.

```
1 byte = 8 bits
```

### 5.1 Binary representation

Decimal number:

```
13
```

Binary representation:

```
1101
```

Why?

Binary positions represent powers of two.

| Position | Value |
| -------- | ----- |
| 2³       | 8     |
| 2²       | 4     |
| 2¹       | 2     |
| 2⁰       | 1     |

Therefore:

\\[ 13 = 8 + 4 + 1 \\]\\[ 13 = 1101_2 \\]

Python can convert decimal numbers to binary:

```
number = 13

print(bin(number))
```

Output:

```
0b1101
```

### 5.2 Why this matters

Binary is important when working with:

- Memory.
- Networking.
- Data encoding.
- Digital electronics.
- File formats.
- Computer security.
- Hardware.
- Machine learning infrastructure.

You do not need to become an expert in digital logic before the programme, but you should understand what binary represents.

---

## Chapter 6: Operating systems

An operating system manages the computer's resources.

Examples:

- Windows.
- Linux.
- macOS.

The operating system provides interfaces between applications and hardware.

When you execute a Python application, the operating system is involved in:

- Starting the process.
- Allocating resources.
- Managing memory.
- Reading files.
- Writing files.
- Communicating with devices.
- Managing networking.

### 6.1 Processes

A process is a running instance of a program.

Suppose you execute:

```
python main.py
```

The operating system creates a process to execute the Python interpreter and your program.

Each process has resources and execution state.

### 6.2 Threads

Threads allow multiple execution paths within a process.

A web server may use threads or other concurrency mechanisms to handle multiple requests.

### 6.3 Why engineers care

Understanding operating systems becomes particularly important when:

- An application crashes.
- A process consumes too much memory.
- A server becomes slow.
- Multiple programs compete for resources.
- You deploy applications.
- You work with containers.
- You troubleshoot networking.

---

# PART III — THE TERMINAL AND LINUX

## Chapter 7: The command line

The command line allows you to interact with your operating system by typing commands.

This is essential for professional software development.

You will eventually use it for:

- Running programs.
- Installing packages.
- Creating environments.
- Managing files.
- Git.
- Docker.
- Cloud services.
- Servers.
- Deployments.
- Testing.

On Windows, you can use PowerShell, Windows Terminal, or Git Bash.

You will also encounter Linux terminals in servers and cloud environments.

### 7.1 Navigation

Linux/macOS/Git Bash:

```
pwd
```

Prints the current working directory.

```
ls
```

Lists files.

```
ls -la
```

Lists files, including hidden files.

```
cd projects
```

Moves into a directory.

```
cd ..
```

Moves one directory upward.

```
mkdir my_project
```

Creates a directory.

```
touch main.py
```

Creates an empty file in environments supporting `touch`.

Windows PowerShell alternative:

```
New-Item main.py -ItemType File
```

### 7.2 File operations

Linux:

```
cp main.py backup.py
```

Copy.

```
mv main.py app.py
```

Rename or move.

```
rm backup.py
```

Delete.

Be very careful with deletion commands.

### 7.3 Viewing files

```
cat main.py
```

Print file contents.

```
head main.py
```

Show the beginning of a file.

```
tail main.py
```

Show the end.

### 7.4 Searching

```
grep "def" main.py
```

Search for the text `def`.

Search recursively:

```
grep -r "TODO" .
```

This becomes useful when working with large projects.

### 7.5 Understanding paths

Absolute path:

```
C:\Users\Tobi\Projects\app
```

Relative path:

```
projects/app
```

A relative path depends on your current working directory.

This is important in Python when loading files.

```
from pathlib import Pathcurrent_directory = Path(__file__).parentfile_path = current_directory / "data.txt"print(file_path)
```

This means:

> Locate the directory containing this Python file and then locate `data.txt` inside that directory.

Using `pathlib` is generally preferable to manually concatenating path strings.

---

# PART IV — GIT AND GITHUB

## Chapter 8: Version control

Version control is a system for recording changes to files over time.

Imagine you build an application.

Version 1 works.

You add a feature.

Version 2 breaks.

You attempt to fix it.

Version 3 breaks something else.

Without version control, it may be difficult to return to a working version.

Git solves this problem.

### 8.1 What is Git?

Git is a distributed version control system.

It tracks changes to your project.

You can:

- Save snapshots.
- Compare changes.
- Restore previous versions.
- Create branches.
- Collaborate.
- Merge work.

### 8.2 Git versus GitHub

**Git** is the version control software.

**GitHub** is a platform for hosting Git repositories and collaborating.

Other hosting platforms include GitLab and Bitbucket.

### 8.3 Initialising a repository

```
git init
```

This creates a Git repository in your project.

Check status:

```
git status
```

### 8.4 Staging

```
git add main.py
```

Stages a specific file.

```
git add .
```

Stages changes in the current directory and descendants, subject to Git ignore rules.

### 8.5 Committing

```
git commit -m "Create expense calculator"
```

A commit is a recorded snapshot of your changes.

Good commit messages explain the change.

Good:

```
Add user authentication endpoint
```

Bad:

```
stuff
```

### 8.6 The basic workflow

Modify files

↓

git add

↓

git commit

↓

git push

↓

GitHub repository

### 8.7 Example workflow

```
git init

git add .

git commit -m "Initial project setup"
```

Connect to GitHub:

```
git remote add origin https://github.com/yourusername/project-name.git
```

Push:

```
git branch -M main

git push -u origin main
```

### 8.8 Branches

A branch allows you to work on a separate line of development.

```
git branch
```

Create a branch:

```
git branch feature-authentication
```

Switch to it:

```
git switch feature-authentication
```

Create and switch simultaneously:

```
git switch -c feature-authentication
```

This is useful because you can develop a feature without immediately changing the main working version.

### 8.9 Merge

Once the feature is complete:

```
git switch main

git merge feature-authentication
```

You may encounter merge conflicts.

A merge conflict occurs when Git cannot automatically determine how to combine competing changes.

You must manually resolve the conflicting content.

### 8.10 Your GitHub profile is your engineering portfolio

Don't merely upload random files.

A strong repository should contain:

```
project/
│
├── README.md
├── .gitignore
├── requirements.txt
├── src/
│   └── app.py
├── tests/
│   └── test_app.py
└── docs/
```

The README should explain:

- The problem.
- The solution.
- Features.
- Technology used.
- Architecture.
- Installation.
- Usage.
- Testing.
- Screenshots.
- Future improvements.

---

# PART V — PYTHON PROGRAMMING

## Chapter 9: Introduction to Python

Python is one of the most widely used programming languages in software engineering, automation, data science, artificial intelligence, and machine learning.

It is especially useful for your intended MLOps career because many machine learning frameworks, data-processing tools, orchestration tools, and automation systems use Python.

Examples include:

- FastAPI — backend API development.
- Django — web development.
- Pandas — data manipulation.
- NumPy — numerical computing.
- Scikit-learn — machine learning.
- PyTorch — deep learning.
- TensorFlow — machine learning.
- MLflow — ML experiment tracking and model management.
- Airflow — workflow orchestration.
- Prefect — workflow orchestration.
- Pydantic — data validation.
- pytest — testing.

### 9.1 What is a programming language?

A programming language allows humans to express instructions that a computer can execute.

Python:

```
print("Hello, World!")
```

The instruction tells Python to display a message.

### 9.2 Your first program

Create a file:

```
main.py
```

Write:

```
print("Hello, World!")
```

Execute it:

```
python main.py
```

Expected output:

```
Hello, World!
```

If the command does not work, try:

```
python3 main.py
```

On Windows, `py` may also work:

```
py main.py
```

---

## Chapter 10: Variables and data types

A variable is a name that allows you to refer to a value.

```
name = "Tobi"age = 24height = 1.75is_learning = True
```

Think of a variable as a label associated with a value.

Variable example

Variable name

age

Value

24

Python:

```
age = 24

print(age)
```

Output:

```
24
```

### 10.1 Naming variables

Good:

```
student_name = "Tobi"total_amount = 5000number_of_users = 100
```

Bad:

```
x = "Tobi"a = 5000n = 100
```

Short names can be acceptable in small mathematical expressions, but meaningful names improve readability.

Python convention uses `snake_case`.

```
first_name = "Tobi"monthly_income = 250000
```

### 10.2 Integers

Integers are whole numbers.

```
age = 24quantity = 10negative_number = -5
```

### 10.3 Floats

Floats represent numbers containing decimal components.

```
price = 2500.50

temperature = 28.4

percentage = 0.75
```

### 10.4 Strings

Strings represent text.

```
name = "Tobi"

message = "Welcome to Python"
```

Strings can be created using single or double quotes.

```
name = 'Tobi'

message = "Hello"
```

### 10.5 Booleans

Boolean values represent truth.

```
is_active = True

is_completed = False
```

Boolean values are useful for decisions.

```
is_authenticated = True

if is_authenticated:
    print("Access granted")
```

### 10.6 Lists

Lists store multiple values.

```
students = ["Tobi", "David", "Sarah"]
```

Access elements:

```
print(students[0])
```

Output:

```
Tobi
```

Change elements:

```
students[1] = "John"
```

Add elements:

```
students.append("Mary")
```

Remove elements:

```
students.remove("David")
```

Check length:

```
print(len(students))
```

### 10.7 Tuples

Tuples store collections of values but are immutable.

```
coordinates = (6.5244, 3.3792)
```

Unlike lists, tuples cannot be modified in place.

```
coordinates[0] = 7
```

This will produce an error.

Tuples are useful when the collection is intended to remain unchanged.

### 10.8 Dictionaries

Dictionaries store key-value pairs.

```
student = {
    "name": "Tobi",
    "age": 24,
    "department": "Computer Engineering",
    "score": 90
}
```

Access values:

```
print(student["name"])
```

Output:

```
Tobi
```

Update values:

```
student["score"] = 95
```

Add a value:

```
student["skills"] = ["Python", "Git"]
```

A dictionary is particularly important in backend development because JSON objects and API responses are often represented using dictionaries in Python.

Example API response:

```
{
    "name": "Tobi",
    "role": "engineer",
    "active": true
}
```

Python equivalent:

```
user = {
    "name": "Tobi",
    "role": "engineer",
    "active": True
}
```

Notice the difference: JSON uses `true`, while Python uses `True`.

### 10.9 Sets

Sets store unique values.

```
numbers = {1, 2, 3, 3, 4, 4}
```

Output when displayed:

```
{1, 2, 3, 4}
```

Sets are useful when you need to remove duplicates or perform mathematical set operations.

```
users_a = {"Tobi", "David", "Sarah"}

users_b = {"David", "John", "Sarah"}

print(users_a.intersection(users_b))
```

Output:

```
{'David', 'Sarah'}
```

---

## Chapter 11: Operators

Operators perform operations on values.

### 11.1 Arithmetic operators

| Operator | Meaning        | Example  |
| -------- | -------------- | -------- |
| `+`      | Addition       | `5 + 2`  |
| `-`      | Subtraction    | `5 - 2`  |
| `*`      | Multiplication | `5 * 2`  |
| `/`      | Division       | `5 / 2`  |
| `//`     | Floor division | `5 // 2` |
| `%`      | Modulus        | `5 % 2`  |
| `**`     | Exponentiation | `5 ** 2` |

Examples:

```
print(10 + 5)
print(10 - 5)
print(10 * 5)
print(10 / 5)
print(10 // 3)
print(10 % 3)
print(2 ** 3)
```

### 11.2 Comparison operators

These return Boolean values.

```
age = 24

print(age == 24)
print(age != 20)
print(age > 18)
print(age < 30)
print(age >= 24)
print(age <= 25)
```

### 11.3 Logical operators

`and`, `or`, `not`.

```
age = 24

has_id = True

if age >= 18 and has_id:
    print("Access allowed")
```

Both conditions must be true.

Using `or`:

```
if age >= 18 or has_id:
    print("Access allowed")
```

At least one condition must be true.

Using `not`:

```
is_blocked = False

if not is_blocked:
    print("User can proceed")
```

---

## Chapter 12: Conditional statements

Conditional statements allow programs to make decisions.

### 12.1 `if`

```
temperature = 35

if temperature > 30:
    print("It is hot")
```

### 12.2 `if` and `else`

```
age = 17

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

### 12.3 `elif`

```
score = 72

if score >= 70:
    print("A")
elif score >= 60:
    print("B")
elif score >= 50:
    print("C")
else:
    print("F")
```

Python checks the conditions in order.

Once one condition is true, the remaining conditions are skipped.

### 12.4 Practical example: fraud detection rules

```
transaction_amount = 500000

if transaction_amount > 1000000:
    risk_level = "High"
elif transaction_amount > 300000:
    risk_level = "Medium"
else:
    risk_level = "Low"

print(risk_level)
```

This is a rule-based system.

Later, machine learning can be used to estimate risk based on many features rather than only fixed thresholds.

---

## Chapter 13: Loops

Loops allow you to repeat instructions.

### 13.1 `for` loops

```
students = ["Tobi", "David", "Sarah"]

for student in students:
    print(student)
```

The loop executes once for every element.

### 13.2 `range()`

```
for number in range(5):    print(number)
```

Output:

```
0
1
2
3
4
```

`range(5)` begins at zero and stops before five.

### 13.3 Looping through dictionaries

```
student = {    "name": "Tobi",    "score": 90,    "department": "Computer Engineering"}for key, value in student.items():    print(key, value)
```

### 13.4 `while` loops

A `while` loop continues while a condition is true.

```
count = 1while count <= 5:    print(count)    count += 1
```

### 13.5 Infinite loops

Incorrect:

```
count = 1while count <= 5:    print(count)
```

The value of `count` never changes.

The condition remains true forever.

### 13.6 `break`

Stops a loop.

```
for number in range(10):    if number == 5:        break    print(number)
```

### 13.7 `continue`

Skips the current iteration.

```
for number in range(10):    if number == 5:        continue    print(number)
```

The number five is skipped.

---

## Chapter 14: Functions

Functions allow you to organise reusable logic.

Without functions:

```
price1 = 1000tax1 = price1 * 0.075price2 = 2000tax2 = price2 * 0.075
```

With functions:

```
def calculate_tax(price):    return price * 0.075print(calculate_tax(1000))print(calculate_tax(2000))
```

### 14.1 Function anatomy

```
def greet(name):    return f"Hello, {name}!"
```

| Component | Meaning            |
| --------- | ------------------ |
| `def`     | Defines a function |
| `greet`   | Function name      |
| `name`    | Parameter          |
| `return`  | Returns a result   |
| `f"..."`  | Formatted string   |

### 14.2 Parameters versus arguments

Parameter:

```
def greet(name):
```

Argument:

```
greet("Tobi")
```

The parameter is the variable in the function definition.

The argument is the value passed when the function is called.

### 14.3 Multiple parameters

```
def calculate_total(price, quantity):
    return price * quantity

total = calculate_total(2500, 4)

print(total)
```

Output:

```
10000
```

### 14.4 Default parameters

```
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}"

print(greet("Tobi"))

print(greet("Tobi", "Good morning"))
```

### 14.5 Scope

Variables created inside a function normally belong to that function's local scope.

```
def calculate():
    total = 100

    print(total)

calculate()
```

The variable `total` cannot ordinarily be accessed outside the function.

### 14.6 Functions should have clear responsibilities

Poorly structured:

```
def process_everything():
    # Read input
    # Validate input
    # Calculate results
    # Save files
    # Display output
    # Send emails
    # Perform other tasks
    pass
```

Better:

```
def validate_input():
    pass

def calculate_result():
    pass

def save_result():
    pass

def display_result():
    pass
```

This principle becomes important as your applications grow.

---

## Chapter 15: Error handling

Software must handle unexpected situations.

### 15.1 `try` and `except`

```
try:
    number = int(input("Enter a number: "))
    print(number * 2)

except ValueError:
    print("Please enter a valid integer.")
```

If the user enters:

```
hello
```

Python cannot convert it to an integer.

The exception is caught, preventing the program from crashing.

### 15.2 Handling multiple exceptions

```
try:
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")
```

### 15.3 `finally`

```
try:
    file = open("data.txt")

except FileNotFoundError:
    print("File not found")

finally:
    print("Program finished")
```

The `finally` block executes whether an exception occurs or not.

### 15.4 Why exception handling matters in production

Imagine an API receives thousands of requests.

Some requests may contain:

- Missing fields.
- Invalid formats.
- Incorrect types.
- Unexpected values.
- Malicious input.

The system must respond safely instead of crashing.

---

## Chapter 16: File handling

Applications frequently need to store information.

### 16.1 Reading a file

```
with open("data.txt", "r") as file:
    content = file.read()

print(content)
```

### 16.2 Writing a file

```
with open("data.txt", "w") as file:
    file.write("Hello, world!")
```

The `"w"` mode overwrites existing contents.

### 16.3 Appending

```
with open("data.txt", "a") as file:
    file.write("\nNew information")
```

### 16.4 JSON

JSON is a common format for storing and transmitting structured data.

Example:

```
{
    "name": "Tobi",
    "age": 24,
    "skills": ["Python", "Git", "Machine Learning"]
}
```

Python:

```
import json

student = {
    "name": "Tobi",
    "age": 24,
    "skills": ["Python", "Git", "Machine Learning"]
}

with open("student.json", "w") as file:
    json.dump(student, file, indent=4)
```

Read it:

```
with open("student.json", "r") as file:
    student = json.load(file)

print(student["name"])
```

### 16.5 CSV

CSV files contain tabular information.

Example:

```
name,age,score
Tobi,24,90
David,25,85
Sarah,22,78
```

Python:

```
import csv

with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)
```

CSV and JSON are extremely common in data engineering and machine learning.

---

## Chapter 17: Object-oriented programming

Object-oriented programming (OOP) organises code around objects.

An object can contain:

- Data.
- Behaviour.

### 17.1 Classes

A class is a blueprint for creating objects.

```
class Student:
    pass
```

### 17.2 Objects

```
class Student:
    pass

student1 = Student()

student2 = Student()
```

`student1` and `student2` are separate instances of the class.

### 17.3 Attributes

```
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Tobi", 24)

print(student1.name)
print(student1.age)
```

### 17.4 The constructor

```
def __init__(self, name, age):
```

The `__init__` method initializes the object when it is created.

### 17.5 `self`

`self` refers to the current object.

```
self.name = name
```

The left side represents the object's attribute.

The right side represents the parameter received.

### 17.6 Methods

Methods are functions associated with a class.

```
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def passed(self):
        return self.score >= 70

student1 = Student("Tobi", 90)

print(student1.passed())
```

### 17.7 Practical class

```
class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")

        if amount > self.balance:
            raise ValueError("Insufficient funds")

        self.balance -= amount

    def get_balance(self):
        return self.balance

account = BankAccount("Tobi", 10000)

account.deposit(5000)

account.withdraw(2000)

print(account.get_balance())
```

Output:

```
13000
```

This is more than syntax.

You are modelling an actual entity with rules.

### 17.8 Four important OOP principles

**Encapsulation:** organise data and behaviour together while controlling how internal state is accessed.

**Abstraction:** expose the essential interface while hiding unnecessary implementation details.

**Inheritance:** create a class that inherits behaviour or attributes from another class.

**Polymorphism:** allow different objects to respond to a common interface in their own ways.

These concepts will become more important when building large applications and working with frameworks.

---

# PART VI — DATA STRUCTURES, ALGORITHMS AND SOFTWARE ENGINEERING

## Chapter 18: Data structures

A data structure is a way of organising data so that it can be stored, accessed, and manipulated efficiently.

Choosing the right data structure can significantly improve an application's performance.

### 18.1 Lists

Lists are ordered, mutable collections.

```
numbers = [10, 20, 30, 40]
```

Useful operations:

```
numbers.append(50)

numbers.pop()

numbers.sort()

numbers.reverse()
```

Lists are suitable for:

- Collections of records.
- Ordered tasks.
- Shopping cart items.
- Data points.
- Training examples.

### 18.2 Dictionaries

Dictionaries store information using keys.

```
users = {
    1: "Tobi",
    2: "David",
    3: "Sarah"
}
```

Lookup:

```
print(users[2])
```

Output:

```
David
```

Dictionaries are particularly useful when fast lookups by key are required.

### 18.3 Stacks

A stack follows LIFO:

> Last In, First Out.

Imagine a stack of plates.

The last plate placed on top is the first one removed.

Python:

```
stack = []

stack.append("First")
stack.append("Second")
stack.append("Third")

print(stack.pop())
```

Output:

```
Third
```

Applications:

- Undo functionality.
- Browser history.
- Function calls.
- Expression evaluation.

### 18.4 Queues

A queue follows FIFO:

> First In, First Out.

Imagine people waiting for a bank teller.

```
from collections import deque

queue = deque()

queue.append("Customer 1")
queue.append("Customer 2")
queue.append("Customer 3")

print(queue.popleft())
```

Output:

```
Customer 1
```

Queues are important in:

- Background jobs.
- Task processing.
- Messaging systems.
- Web servers.
- Data pipelines.

### 18.5 Sets

Sets store unique values.

```
users = {"Tobi", "David", "Sarah", "Tobi"}

print(users)
```

Duplicates are removed.

Sets can be useful when determining whether an item already exists.

```
registered_users = {"tobi@example.com", "david@example.com"}

email = "tobi@example.com"

if email in registered_users:
    print("Already registered")
```

### 18.6 Which data structure should you use?

| Problem                  | Appropriate structure |
| ------------------------ | --------------------- |
| Ordered collection       | List                  |
| Lookup by identifier     | Dictionary            |
| Unique values            | Set                   |
| Undo operations          | Stack                 |
| Tasks processed in order | Queue                 |
| Immutable grouped values | Tuple                 |

---

## Chapter 19: Algorithms

An algorithm is a defined sequence of steps for solving a problem.

### 19.1 Searching

Suppose:

```
numbers = [4, 8, 15, 16, 23, 42]
```

You want to find whether 23 exists.

#### Linear search

```
def linear_search(numbers, target):
    for index, number in enumerate(numbers):
        if number == target:
            return index

    return -1

print(linear_search(numbers, 23))
```

Output:

```
4
```

Linear search checks items one at a time.

Its worst-case complexity is:

\\[ O(n) \\]

If the list contains 100,000 items, it may need to examine all 100,000.

### 19.2 Binary search

Binary search works on sorted data.

It repeatedly divides the search area in half.

```
def binary_search(numbers, target):
    left = 0
    right = len(numbers) - 1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            return middle

        elif numbers[middle] < target:
            left = middle + 1

        else:
            right = middle - 1

    return -1
```

Test:

```
numbers = [4, 8, 15, 16, 23, 42]

print(binary_search(numbers, 23))
```

Binary search has logarithmic complexity:

\\[ O(\log n) \\]

This is significantly more efficient for large sorted datasets.

### 19.3 Sorting

Sorting arranges data into an order.

```
numbers = [8, 2, 5, 1, 9]

numbers.sort()

print(numbers)
```

Output:

```
[1, 2, 5, 8, 9]
```

Sorting can be used for:

- Ranking students.
- Sorting products by price.
- Ordering transactions.
- Preparing data for algorithms.

### 19.4 Big O notation

Big O describes how the resource requirements of an algorithm grow as the input size increases.

| Complexity       | Interpretation |
| ---------------- | -------------- |
| \\(O(1)\\)       | Constant       |
| \\(O(\log n)\\)  | Logarithmic    |
| \\(O(n)\\)       | Linear         |
| \\(O(n\log n)\\) | Linearithmic   |
| \\(O(n^2)\\)     | Quadratic      |
| \\(O(2^n)\\)     | Exponential    |

Example:

```
print(numbers[0])
```

This is approximately constant time, \\(O(1)\\).

Example:

```
for number in numbers:
    print(number)
```

This is \\(O(n)\\).

Nested loops:

```
for first in numbers:
    for second in numbers:
        print(first, second)
```

This is approximately \\(O(n^2)\\).

Understanding complexity is useful when applications begin handling millions of records.

---

## Chapter 20: Writing maintainable code

Working code is not necessarily good code.

Professional code should be:

- Readable.
- Maintainable.
- Testable.
- Reusable.
- Understandable.
- Consistent.

### 20.1 Naming

Poor:

```
def calc(a, b):
    return a * b
```

Better:

```
def calculate_total_price(price, quantity):
    return price * quantity
```

### 20.2 Avoid duplication

Poor:

```
tax1 = 1000 * 0.075

tax2 = 2000 * 0.075

tax3 = 3000 * 0.075
```

Better:

```
def calculate_tax(amount):
    return amount * 0.075

tax1 = calculate_tax(1000)
tax2 = calculate_tax(2000)
tax3 = calculate_tax(3000)
```

### 20.3 Separation of concerns

A program should separate responsibilities.

For example:

```
Application
│
├── Input handling
├── Business logic
├── Data storage
├── Validation
└── Output
```

Later, in backend applications:

```
Backend
│
├── Routes
├── Services
├── Database models
├── Schemas
├── Authentication
└── Configuration
```

### 20.4 Configuration

Avoid embedding configuration values everywhere.

Poor:

```
database_url = "postgresql://user:password@localhost/database"
```

Better:

```
import os

database_url = os.getenv("DATABASE_URL")
```

Environment variables allow configuration to vary between development, testing, and production.

This is particularly important for MLOps.

---

# PART VII — TESTING

## Chapter 21: Why software testing matters

Testing is the process of verifying whether software behaves as expected.

Without testing, you may not know whether your program works beyond the particular example you tried manually.

Testing is especially important in machine learning systems because a program can execute successfully while producing incorrect predictions.

### 21.1 Manual testing

```
def add_numbers(a, b):
    return a + b

print(add_numbers(2, 3))
```

You manually observe the output.

Expected:

```
5
```

This is useful but insufficient for large systems.

### 21.2 Unit tests

A unit test checks a small piece of functionality.

Using `pytest`:

Install:

```
pip install pytest
```

Project structure:

```
calculator/
│
├── calculator.py
└── test_calculator.py
```

`calculator.py`:

```
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

`test_calculator.py`:

```
from calculator import add, subtract

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 2) == 3
```

Run:

```
pytest
```

The `assert` statement checks whether a condition is true.

If the condition is false, the test fails.

### 21.3 Edge cases

A function may work for ordinary inputs but fail on unusual inputs.

Consider:

```
def calculate_average(numbers):
    return sum(numbers) / len(numbers)
```

What happens if the list is empty?

```
calculate_average([])
```

This causes a division-by-zero error.

Better:

```
def calculate_average(numbers):
    if not numbers:
        raise ValueError("Numbers cannot be empty")

    return sum(numbers) / len(numbers)
```

Now test:

```
import pytest

from calculator import calculate_average

def test_average():
    assert calculate_average([10, 20, 30]) == 20

def test_empty_list():
    with pytest.raises(ValueError):
        calculate_average([])
```

### 21.4 Types of testing

| Testing type | Purpose                                 |
| ------------ | --------------------------------------- |
| Unit         | Test individual components              |
| Integration  | Test components working together        |
| Functional   | Verify features behave correctly        |
| End-to-end   | Test the complete application workflow  |
| Regression   | Ensure old functionality still works    |
| Performance  | Evaluate speed and resource consumption |
| Security     | Identify vulnerabilities                |
| Acceptance   | Verify user requirements are satisfied  |

### 21.5 Testing becomes critical in MLOps

Imagine deploying a machine learning model that predicts whether a customer is likely to default.

You need to test:

- Whether the API accepts valid input.
- Whether invalid input is rejected.
- Whether the model returns predictions.
- Whether predictions are within valid ranges.
- Whether the model loads correctly.
- Whether inference is sufficiently fast.
- Whether a new model performs better than the existing model.
- Whether the deployed version matches the approved model.

A successful API response does not mean the model is good.

This is a distinction you must understand deeply.

---

# PART VIII — SOFTWARE DEVELOPMENT WORKFLOW

## Chapter 22: Virtual environments and package management

Python applications frequently depend on external libraries.

Suppose Project A requires:

```
pandas==2.2
```

Project B requires:

```
pandas==3.0
```

Installing everything globally can cause conflicts.

A virtual environment isolates dependencies.

### 22.1 Create a virtual environment

Windows:

```
python -m venv .venv
```

Activate:

```
.venv\Scripts\Activate.ps1
```

Linux/macOS/Git Bash:

```
python3 -m venv .venv
```

Activate:

```
source .venv/bin/activate
```

### 22.2 Install packages

```
python -m pip install requests
```

### 22.3 Freeze dependencies

```
pip freeze > requirements.txt
```

Example:

```
requests==2.32.3
pytest==8.3.4
```

### 22.4 Install dependencies from a file

```
pip install -r requirements.txt
```

### 22.5 Why MLOps engineers care

Machine learning projects often have complex dependencies.

For example:

```
Python
├── PyTorch
├── NumPy
├── Pandas
├── CUDA-related libraries
├── Scikit-learn
└── FastAPI
```

Different versions can produce incompatibilities.

Reproducible environments help ensure the same application works across machines.

---

## Chapter 23: Software architecture

Architecture describes the structure and relationships of the components of a software system.

### 23.1 Monolithic architecture

A monolithic application contains most functionality within one application.

Example:

```
Application
├── Authentication
├── Payments
├── Inventory
├── Users
└── Reports
```

Advantages:

- Simple to begin.
- Easier deployment initially.
- Less infrastructure complexity.

Disadvantages:

- Can become difficult to maintain.
- Changes may affect unrelated components.
- Scaling individual components can be difficult.

### 23.2 Microservices

A microservices architecture separates the system into independently deployable services.

```
Application
│
├── User Service
├── Payment Service
├── Inventory Service
├── Notification Service
└── Analytics Service
```

Advantages:

- Independent deployment.
- Independent scaling.
- Service isolation.
- Different technologies can be used.

Disadvantages:

- More complex networking.
- More deployment complexity.
- Monitoring becomes harder.
- Distributed failures.
- Data consistency challenges.

Do not assume microservices are always better.

A well-designed monolith is often a better choice for a small product.

### 23.3 Three-tier architecture

A common application structure:

Presentation Layer

Frontend · User interface

↓

Application Layer

Backend · Business logic · APIs

↓

Data Layer

Database · Files · Data storage

This is a useful model for understanding full-stack applications.

---

# PART IX — DATABASES AND DATA ENGINEERING

## Chapter 24: Databases

A database is a system for storing, managing, retrieving, and manipulating data.

Almost every real-world application needs a database.

Examples:

- Social media applications store users, posts, comments, and messages.
- Banking applications store accounts and transactions.
- E-commerce applications store products, orders, and customers.
- AI systems store datasets, predictions, models, experiments, and logs.

### 24.1 Why not just use text files?

Text files are useful for simple applications.

But imagine storing ten million customer records in one text file.

You would need to handle:

- Searching.
- Updating.
- Relationships.
- Concurrent users.
- Data integrity.
- Access control.
- Transactions.
- Indexing.
- Backup and recovery.

Databases are designed to manage these problems.

### 24.2 Relational databases

Relational databases organise information into tables.

Example: `customers`

| customer_id | name  | email              |
| ----------- | ----- | ------------------ |
| 1           | Tobi  | tobi\@example.com  |
| 2           | David | david\@example.com |

Example: `orders`

| order_id | customer_id | amount |
| -------- | ----------- | ------ |
| 101      | 1           | 25000  |
| 102      | 2           | 40000  |
| 103      | 1           | 15000  |

Notice that `customer_id` links an order to a customer.

This is a relationship.

### 24.3 Primary keys

A primary key uniquely identifies a record.

```
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(255)
);
```

Each customer must have a unique identifier.

### 24.4 Foreign keys

A foreign key connects tables.

```
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    amount DECIMAL(10, 2),

    FOREIGN KEY (customer_id)
    REFERENCES customers(customer_id)
);
```

This helps maintain referential integrity.

---

## Chapter 25: SQL

SQL stands for Structured Query Language.

It is used to interact with relational databases.

### 25.1 Creating tables

```
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name VARCHAR(100),
    age INTEGER,
    score FLOAT
);
```

### 25.2 Inserting records

```
INSERT INTO students
(name, age, score)
VALUES
('Tobi', 24, 90);
```

### 25.3 Selecting records

```
SELECT * FROM students;
```

Select particular columns:

```
SELECT name, score
FROM students;
```

### 25.4 Filtering

```
SELECT *
FROM students
WHERE score >= 70;
```

### 25.5 Sorting

```
SELECT *
FROM students
ORDER BY score DESC;
```

### 25.6 Aggregation

```
SELECT AVG(score)
FROM students;
```

Other functions:

```
COUNT()
SUM()
MIN()
MAX()
AVG()
```

### 25.7 Grouping

Suppose a database contains customers from different cities.

```
SELECT city, COUNT(*)
FROM customers
GROUP BY city;
```

This counts customers per city.

### 25.8 Joins

A join combines related information from multiple tables.

```
SELECT
    customers.name,
    orders.amount
FROM customers
JOIN orders
ON customers.customer_id = orders.customer_id;
```

This is a fundamental database operation.

### 25.9 Why SQL matters in machine learning

You will frequently need to extract datasets for model training.

Example:

```
SELECT
    customer_age,
    monthly_income,
    transaction_count,
    loan_amount,
    defaulted
FROM loan_customers;
```

The result becomes a dataset for analysis or model training.

Machine learning engineers who understand SQL are significantly more effective because real-world ML frequently begins with extracting and understanding data.

---

## Chapter 26: Database transactions

A transaction is a group of operations treated as a single logical unit.

Imagine transferring ₦50,000 from Account A to Account B.

Two operations occur:

1. Subtract ₦50,000 from A.
2. Add ₦50,000 to B.

What happens if the first operation succeeds but the second fails?

You could lose money.

Transactions help prevent inconsistent states.

### ACID properties

**Atomicity:** Either all transaction operations succeed or the transaction is rolled back.

**Consistency:** The database remains valid according to its rules.

**Isolation:** Concurrent transactions do not improperly interfere.

**Durability:** Once committed, data remains persisted.

These concepts are extremely important in financial systems.

They also matter in ML systems when managing:

- Training records.
- Model deployment metadata.
- Experiment results.
- Job status.
- Prediction logs.

---

# PART X — APIs AND BACKEND DEVELOPMENT

## Chapter 27: What is an API?

API stands for Application Programming Interface.

An API defines how different software components communicate.

Imagine a mobile application.

The user opens an application and requests account information.

The mobile application sends a request to the backend.

The backend retrieves information from the database.

It returns the result.

The mobile application displays it.

### 27.1 API communication

Mobile / Web App

↓ HTTP request

Backend API

↓ Query

Database

↑ Results

Backend response → Frontend

### 27.2 HTTP

HTTP is a protocol used for communication between clients and servers.

Common methods:

| Method | Purpose                      |
| ------ | ---------------------------- |
| GET    | Retrieve information         |
| POST   | Create or submit information |
| PUT    | Replace a resource           |
| PATCH  | Partially update a resource  |
| DELETE | Delete a resource            |

### 27.3 Status codes

| Code | Meaning                      |
| ---- | ---------------------------- |
| 200  | Successful                   |
| 201  | Resource created             |
| 204  | Successful, no response body |
| 400  | Bad request                  |
| 401  | Unauthenticated              |
| 403  | Forbidden                    |
| 404  | Not found                    |
| 409  | Conflict                     |
| 422  | Validation error             |
| 429  | Too many requests            |
| 500  | Internal server error        |
| 503  | Service unavailable          |

### 27.4 JSON

An API frequently sends data in JSON.

Request:

```
{
    "name": "Tobi",
    "age": 24
}
```

Response:

```
{
    "message": "User created successfully",
    "user_id": 1
}
```

### 27.5 REST APIs

REST is an architectural style commonly used for APIs.

Example endpoints:

```
GET    /users
GET    /users/1
POST   /users
PATCH  /users/1
DELETE /users/1
```

The endpoint represents a resource.

The HTTP method determines the action.

---

## Chapter 28: Build your first backend API with FastAPI

FastAPI is a Python framework for building APIs.

Install:

```
pip install fastapi uvicorn
```

Create:

```
main.py
```

Code:

```
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to my API"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
```

Run:

```
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000
```

Documentation:

```
http://127.0.0.1:8000/docs
```

FastAPI automatically provides interactive API documentation.

### 28.1 Path parameters

```
@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {
        "user_id": user_id,
        "name": "Tobi"
    }
```

Request:

```
/users/10
```

The endpoint receives `10`.

### 28.2 Query parameters

```
@app.get("/products")
def get_products(limit: int = 10):
    return {
        "limit": limit
    }
```

Request:

```
/products?limit=20
```

### 28.3 Request bodies

```
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class UserCreate(BaseModel):
    name: str
    email: str
    age: int

@app.post("/users")
def create_user(user: UserCreate):
    return {
        "message": "User created",
        "user": user
    }
```

Pydantic validates incoming information.

For example, if `age` should be an integer but the request contains an invalid value, validation can reject the request.

### 28.4 Why backend development matters for MLOps

A trained machine learning model is not usually useful by itself.

You need a way for applications to interact with it.

For example:

```
Customer
    ↓
Web application
    ↓
API
    ↓
ML model
    ↓
Prediction
    ↓
API response
    ↓
Customer
```

This is why your MLOps path must include backend engineering.

---

# PART XI — FRONTEND FUNDAMENTALS

## Chapter 29: Understanding the frontend

The frontend is the part of an application users interact with.

Examples:

- Buttons.
- Forms.
- Dashboards.
- Charts.
- Tables.
- Navigation.
- Mobile screens.

### 29.1 HTML

HTML structures the content.

```
<h1>Welcome</h1>

<p>This is my application.</p>

<button>Submit</button>
```

### 29.2 CSS

CSS controls presentation.

```
h1 {
    color: blue;
}

button {
    padding: 12px;
    border-radius: 8px;
}
```

### 29.3 JavaScript

JavaScript adds behaviour.

```
const button = document.querySelector("button");

button.addEventListener("click", function () {
    alert("Button clicked!");
});
```

### 29.4 Why you need frontend knowledge

Even if you become an MLOps engineer, understanding frontend applications helps you:

- Build complete products.
- Debug API interactions.
- Understand user experience.
- Collaborate with frontend engineers.
- Create demonstrations for your models.
- Build portfolio projects.

You do not need to become an expert frontend designer, but you should be able to understand how a web application communicates with your backend.

---

# PART XII — MATHEMATICS FOR MACHINE LEARNING

## Chapter 30: Why mathematics matters

You do not need to become a mathematician before learning machine learning.

However, mathematics helps you understand why models work, what they are calculating, how they learn, and when their results can be trusted.

The most important areas for your path are:

1. Arithmetic and algebra.
2. Functions.
3. Statistics.
4. Probability.
5. Linear algebra.
6. Calculus.
7. Optimization.

We will approach them practically.

---

## Chapter 31: Algebra

Algebra allows you to represent relationships using symbols.

Example:

\\[ y = 2x + 3 \\]

If \\(x=4\\):

\\[ y = 2(4)+3 \\]\\[ y=11 \\]

This is a function.

### 31.1 Variables in machine learning

Suppose you want to predict the price of a house.

The price might depend on:

- Size.
- Number of bedrooms.
- Location.
- Age of the building.

You might represent the relationship as:

\\[ Price = w_1(Size) + w_2(Bedrooms) + w_3(Location) + b \\]

The \\(w\\) values represent weights.

The \\(b\\) represents a bias term.

Machine learning will eventually learn these weights from data.

---

## Chapter 32: Functions

A mathematical function maps an input to an output.

\\[ f(x) = x^2 \\]

If:

\\[ x=3 \\]

Then:

\\[ f(3)=9 \\]

Python:

```
def square(x):    return x ** 2print(square(3))
```

Machine learning models are often functions.

They receive inputs and produce outputs.

Example:

\\[ f(X) = \hat{y} \\]

Where:

- \\(X\\) = input features.
- \\(\hat{y}\\) = predicted output.

A model is essentially a learned function.

---

## Chapter 33: Statistics

Statistics allows us to understand data.

### 33.1 Mean

The mean is the arithmetic average.

\\[ Mean = \frac{\sum x_i}{n} \\]

Example:

```
scores = [70, 80, 90, 100]mean = sum(scores) / len(scores)print(mean)
```

Output:

```
85.0
```

### 33.2 Median

The median is the middle value after sorting.

```
numbers = [10, 20, 30, 40, 50]median = 30
```

For an even number of values:

```
numbers = [10, 20, 30, 40]median = (20 + 30) / 2
```

Result:

```
25
```

### 33.3 Mode

The mode is the most frequently occurring value.

```
numbers = [1, 2, 2, 3, 4, 4, 4]

mode = 4
```

### 33.4 Variance

Variance measures how spread out values are around the mean.

A low variance means observations are relatively close to the mean.

A high variance means observations are more spread out.

Population variance:

\\[ \sigma^2 = \frac{\sum(x_i-\mu)^2}{n} \\]

Where:

- \\(x_i\\) = each observation.
- \\(\mu\\) = population mean.
- \\(n\\) = number of observations.

### 33.5 Standard deviation

Standard deviation is the square root of variance.

\\[ \sigma = \sqrt{\sigma^2} \\]

It provides a measure of spread in the same units as the original data.

Example:

If average transaction value is ₦10,000 and standard deviation is ₦2,000, transaction values tend to vary around the mean by a scale of approximately ₦2,000.

This does not mean every transaction falls within that range.

---

## Chapter 34: Probability

Probability measures how likely an event is to occur.

Values range from zero to one.

\\[ 0 \leq P(A) \leq 1 \\]

- Zero: impossible.
- One: certain.

Example:

A fair coin.

\\[ P(Heads)=\frac{1}{2} \\]

### 34.1 Conditional probability

Conditional probability measures the probability of an event given another event.

\\[ P(A|B)=\frac{P(A\cap B)}{P(B)} \\]

This is important in machine learning.

Example:

What is the probability a customer defaults given that their credit score is low?

\\[ P(Default|LowScore) \\]

The model attempts to estimate relationships like this using data.

### 34.2 Probability versus certainty

A model predicting:

```
Probability of fraud: 0.95
```

does not mean fraud is guaranteed.

It means the model estimates a 95% probability according to its learned behaviour and assumptions.

Probability outputs must be evaluated and calibrated.

---

## Chapter 35: Linear algebra

Linear algebra is one of the most important mathematical foundations of machine learning.

### 35.1 Scalars

A scalar is a single number.

```
x = 5
```

### 35.2 Vectors

A vector is an ordered collection of values.

\\[ \mathbf{x} = \begin{bmatrix} 2\\\ 4\\\ 6 \end{bmatrix} \\]

Python:

```
x = [2, 4, 6]
```

In machine learning, a vector might represent one customer:

```
[age, income, credit_score]
```

Example:

```
customer = [24, 250000, 720]
```

### 35.3 Matrices

A matrix contains rows and columns.

\\[ X = \begin{bmatrix} 1 & 2 & 3\\\ 4 & 5 & 6 \end{bmatrix} \\]

Python:

```
X = [    [1, 2, 3],    [4, 5, 6]]
```

A dataset is often represented as a matrix.

Rows represent observations.

Columns represent features.

### 35.4 Matrix multiplication

Matrix multiplication is central to neural networks.

A simplified operation:

\\[ y = XW \\]

Where:

- \\(X\\) contains inputs.
- \\(W\\) contains learned weights.
- \\(y\\) contains outputs.

Modern machine learning frameworks perform these operations efficiently using CPUs and GPUs.

---

## Chapter 36: Calculus

Calculus studies change.

One of its most important concepts is the derivative.

The derivative tells us how a function changes when its input changes.

Example:

\\[ f(x)=x^2 \\]

Derivative:

\\[ f'(x)=2x \\]

At \\(x=3\\):

\\[ f'(3)=6 \\]

The derivative measures the slope at that point.

### 36.1 Why derivatives matter in machine learning

A machine learning model makes predictions.

We calculate how wrong the predictions are using a loss function.

The training process attempts to reduce the loss.

The derivative tells us how changing a model parameter affects the loss.

This allows us to update model parameters.

---

# PART XIII — MACHINE LEARNING

## Chapter 37: What is machine learning?

Machine learning is a field of artificial intelligence in which systems learn patterns from data to perform tasks.

Traditional programming:

```
Rules + Input → Output
```

Machine learning:

```
Data + Desired outcomes → Learned model
```

Then:

```
Learned model + New input → Prediction
```

### 37.1 Traditional programming example

Suppose you want to determine whether a transaction is suspicious.

You manually write:

```
def is_suspicious(amount):
    return amount > 500000
```

This is rule-based programming.

### 37.2 Machine learning example

You have historical transactions.

Each transaction contains:

- Amount.
- Time.
- Location.
- Customer behaviour.
- Device.
- Previous transaction frequency.
- Fraud label.

You train a model to learn patterns associated with fraudulent transactions.

The model may discover patterns that are difficult to express manually.

---

## Chapter 38: Types of machine learning

### 38.1 Supervised learning

The model learns from labelled data.

Example:

| Transaction | Amount  | Fraud |
| ----------- | ------- | ----- |
| 1           | 5,000   | No    |
| 2           | 200,000 | Yes   |
| 3           | 2,000   | No    |

The target is known.

The model learns a relationship between input features and the target.

Two major supervised learning tasks:

**Classification:** Predict a category.

Examples:

- Fraud or legitimate.
- Spam or not spam.
- Disease or no disease.
- Customer churn or no churn.

**Regression:** Predict a numerical value.

Examples:

- House price.
- Electricity consumption.
- Revenue.
- Temperature.

### 38.2 Unsupervised learning

The model receives data without target labels.

It attempts to discover patterns.

Examples:

- Customer segmentation.
- Clustering.
- Anomaly detection.
- Dimensionality reduction.

### 38.3 Reinforcement learning

An agent learns by interacting with an environment.

The agent receives rewards or penalties.

Examples:

- Robotics.
- Game-playing agents.
- Resource optimisation.

---

## Chapter 39: Features and labels

A feature is an input used by a model.

A label is the outcome the model is trying to predict in supervised learning.

Example:

| Age | Income  | Transactions | Default |
| --- | ------- | ------------ | ------- |
| 25  | 200,000 | 10           | 0       |
| 40  | 500,000 | 20           | 0       |
| 22  | 80,000  | 5            | 1       |

Features:

```
Age
Income
Transactions
```

Label:

```
Default
```

Python:

```
X = [
    [25, 200000, 10],
    [40, 500000, 20],
    [22, 80000, 5]
]

y = [0, 0, 1]
```

In this example:

- `X` contains features.
- `y` contains labels.

---

## Chapter 40: Your first machine learning model

We will use Scikit-learn.

Install:

```
pip install scikit-learn
```

### 40.1 Regression example

Suppose you have this dataset:

```
hours_studied = [1, 2, 3, 4, 5]

scores = [20, 35, 50, 65, 80]
```

You want to predict a student's score based on study hours.

```
from sklearn.linear_model import LinearRegression

X = [[1], [2], [3], [4], [5]]

y = [20, 35, 50, 65, 80]

model = LinearRegression()

model.fit(X, y)

prediction = model.predict([[6]])

print(prediction)
```

The model learns a relationship between hours studied and score.

### 40.2 Understanding `.fit()`

```
model.fit(X, y)
```

This trains the model.

The model examines:

- Inputs.
- Corresponding outputs.
- Relationships between them.

It attempts to learn parameters that reduce prediction error.

### 40.3 Understanding `.predict()`

```
model.predict([[6]])
```

The model uses the learned relationship to estimate the score for six hours of study.

---

## Chapter 41: Training and testing data

One of the biggest mistakes in machine learning is evaluating a model using the same data used for training.

A model may memorise the training dataset.

But memorisation does not guarantee it can perform well on new data.

### 41.1 Train-test split

We divide our dataset into:

- Training data.
- Testing data.

The training data is used to learn.

The test data is used to evaluate performance on unseen examples.

```
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

`test_size=0.2` means 20% of the data is reserved for testing.

`random_state=42` makes the split reproducible.

### 41.2 Why reproducibility matters

If you run the same experiment repeatedly, you want to understand whether differences came from:

- A change in data.
- A change in code.
- A change in model.
- A different random split.

Reproducibility is a core MLOps principle.

---

## Chapter 42: Model evaluation

A model should be evaluated using appropriate metrics.

### 42.1 Classification accuracy

\\[ Accuracy = \frac{CorrectPredictions}{TotalPredictions} \\]

Example:

A model correctly predicts 90 out of 100 transactions.

\\[ Accuracy = 0.90 \\]

### 42.2 Precision

Precision answers:

> Of the predictions classified as positive, how many were actually positive?

\\[ Precision = \frac{TP}{TP+FP} \\]

Where:

- TP = true positives.
- FP = false positives.

For fraud detection, high precision reduces the number of legitimate transactions incorrectly blocked.

### 42.3 Recall

Recall answers:

> Of all actual positive cases, how many did the model identify?

\\[ Recall = \frac{TP}{TP+FN} \\]

Where:

\- FN = false negatives.

For fraud detection, recall matters because missing fraudulent transactions can be costly.

### 42.4 F1 score

F1 combines precision and recall.

\\[ F1 = 2 \times \frac{Precision \times Recall}{Precision + Recall} \\]

### 42.5 Why accuracy can be misleading

Imagine:

100,000 transactions.

Only 100 are fraudulent.

A model predicts every transaction as legitimate.

Accuracy:

\\[ \frac{99,900}{100,000}=99.9\\% \\]

The model appears excellent.

But it detects zero fraud.

This is why evaluation must be aligned with the actual problem.

---

## Chapter 43: Overfitting and underfitting

### Overfitting

A model learns the training data too closely.

It performs well on training data but poorly on new data.

This is similar to memorising examination answers without understanding the subject.

### Underfitting

A model is too simple to capture the underlying pattern.

It performs poorly on both training and testing data.

### The goal

We want a model that learns useful patterns and generalises to unseen examples.

### 43.1 Regularization

Regularization discourages overly complex models.

For example, L1 and L2 regularization penalise certain model parameter configurations.

This can reduce overfitting.

### 43.2 Data leakage

Data leakage occurs when information that would not legitimately be available during prediction influences training or evaluation.

Example:

You are predicting whether a customer will default.

Your dataset accidentally includes:

```
loan_recovery_status
```

This field may only become known after the customer defaults.

The model can appear excellent because it is using information from the future.

But it will fail in real deployment.

Data leakage is one of the most dangerous problems in machine learning.

---

# PART XIV — DEEP LEARNING AND GENERATIVE AI

## Chapter 44: Neural networks

A neural network is a computational model composed of interconnected mathematical units commonly called neurons.

Neural networks are inspired loosely by biological nervous systems, but modern artificial neural networks are mathematical and computational systems rather than literal replicas of the human brain.

### 44.1 A simple neuron

A neuron receives inputs, multiplies them by weights, adds a bias, and applies an activation function.

\\[ z = w_1x_1+w_2x_2+\cdots+w_nx_n+b \\]

Then:

\\[ a=f(z) \\]

Where:

- \\(x\\) = input.
- \\(w\\) = weights.
- \\(b\\) = bias.
- \\(f\\) = activation function.
- \\(a\\) = output.

### 44.2 Activation functions

Activation functions introduce non-linearity.

Without suitable non-linear activation functions, stacking many linear transformations would still produce an overall linear transformation.

Common activation functions:

- ReLU.
- Sigmoid.
- Tanh.
- Softmax.

ReLU:

\\[ f(x)=\max(0,x) \\]

Python:

```
def relu(x):
    return max(0, x)
```

### 44.3 Neural network layers

A neural network may contain:

```
Input Layer
    ↓
Hidden Layer
    ↓
Hidden Layer
    ↓
Output Layer
```

Each layer transforms information.

### 44.4 Training

Training involves:

1. Feeding inputs into the model.
2. Calculating predictions.
3. Calculating loss.
4. Computing gradients.
5. Updating parameters.
6. Repeating.

---

## Chapter 45: Gradient descent

Gradient descent is an optimization method used to reduce a model's loss.

Suppose the model has a parameter \\(w\\).

We calculate the derivative of the loss with respect to \\(w\\).

Then update:

\\[ w\_{new}=w\_{old}-\eta\frac{\partial L}{\partial w} \\]

Where:

- \\(w\\) = model parameter.
- \\(L\\) = loss.
- \\(\eta\\) = learning rate.

### 45.1 Learning rate

The learning rate determines the size of parameter updates.

Too large:

- Training may become unstable.
- The model may overshoot useful values.
- Loss may increase or oscillate.

Too small:

- Training may be extremely slow.
- Learning may take too long.

### 45.2 Why this matters for MLOps

A training job can fail because:

- Learning rate is inappropriate.
- GPU memory is insufficient.
- Data is malformed.
- Model parameters become unstable.
- Training takes too long.

MLOps engineers need to monitor training jobs, logs, resource consumption, metrics, and failures.

---

## Chapter 46: Transformers and modern AI

Transformers are a neural network architecture that has become central to modern language models and many other AI systems.

They use attention mechanisms to process relationships between elements of input sequences.

Examples of transformer-based systems include many modern:

- Large language models.
- Text generation systems.
- Translation systems.
- Multimodal systems.
- Vision models.

### 46.1 Tokens

Language models generally process tokenized input.

A token may represent:

- A word.
- Part of a word.
- A punctuation mark.
- A character group.

Text:

```
Machine learning is fascinating.
```

May be divided into tokens.

Tokenization is important because model input and output are measured in tokens rather than simply words.

### 46.2 Embeddings

Embeddings represent information as numerical vectors.

For example:

```
"bank"
```

may have different meanings depending on context:

- Financial institution.
- Riverbank.

Embeddings help represent semantic relationships.

### 46.3 Large language models

LLMs learn patterns from large datasets and generate text by predicting tokens based on context.

They can perform:

- Text generation.
- Summarization.
- Translation.
- Classification.
- Coding assistance.
- Reasoning-like tasks.
- Information extraction.

However, LLM outputs can be incorrect.

A production AI system should not assume generated output is automatically trustworthy.

### 46.4 Retrieval-augmented generation

RAG combines retrieval with generation.

Instead of relying entirely on the model's internal knowledge, a system retrieves relevant information from external sources.

Architecture:

```
User question
      ↓
Embedding / retrieval
      ↓
Relevant documents
      ↓
Prompt construction
      ↓
LLM
      ↓
Generated response
```

Example:

A company has 10,000 internal documents.

An employee asks:

> What is our reimbursement policy for international travel?

The system retrieves the relevant policy and provides it to the language model.

The model answers using the retrieved information.

RAG is especially useful for:

- Enterprise knowledge assistants.
- Customer support.
- Document search.
- Research tools.
- Internal policy systems.

---

# PART XV — AI-NATIVE ENGINEERING

## Chapter 47: Working with AI coding assistants

AI tools can accelerate software development.

However, there is an important distinction:

**Using AI to produce code is not the same as understanding the code.**

You should be able to explain:

- What the code does.
- Why it exists.
- How it works.
- Its dependencies.
- Its failure cases.
- Its security implications.
- How to test it.

### 47.1 The correct workflow

```
Problem
   ↓
Your understanding
   ↓
Plan
   ↓
AI assistance
   ↓
Code review
   ↓
Testing
   ↓
Debugging
   ↓
Commit
```

### 47.2 Ask AI to help you think

Instead of:

> Build my entire application.

Try:

> I want to implement user authentication. Help me identify the components and responsibilities. Do not write the code yet.

Then:

> Explain how password hashing works and why storing plaintext passwords is unsafe.

Then:

> Help me implement a registration endpoint using FastAPI. Explain each section.

Then:

> Generate unit tests for the endpoint, including invalid inputs.

This process builds capability.

### 47.3 AI-generated code must be reviewed

Check:

- Is the code correct?
- Does it use secure practices?
- Are secrets exposed?
- Are errors handled?
- Are dependencies necessary?
- Are tests present?
- Is the architecture appropriate?
- Does it introduce unnecessary complexity?

### 47.4 Hallucinations

AI systems can generate incorrect information confidently.

They may:

- Invent APIs.
- Use outdated packages.
- Create nonexistent functions.
- Misinterpret requirements.
- Introduce subtle bugs.

You should verify outputs using documentation, tests, and direct execution.

---

# PART XVI — CLOUD AND INFRASTRUCTURE

## Chapter 48: What is cloud computing?

Cloud computing provides computing resources through remote infrastructure.

Instead of owning and maintaining every server, you can rent computing resources from cloud providers.

Examples include:

- AWS.
- Microsoft Azure.
- Google Cloud Platform.

Cloud services include:

- Virtual machines.
- Storage.
- Databases.
- Networking.
- GPUs.
- Containers.
- Monitoring.
- Serverless computing.

### 48.1 Virtual machines

A virtual machine behaves like a computer running within another computer.

You can create a VM with:

- Operating system.
- CPU.
- RAM.
- Storage.
- Network configuration.

You can deploy your application to it.

### 48.2 Object storage

Object storage is useful for storing files.

Machine learning applications frequently store:

- Datasets.
- Model files.
- Images.
- Videos.
- Logs.
- Training artifacts.

### 48.3 Cloud databases

Instead of maintaining a database server yourself, you can use managed database services.

Benefits may include:

- Backups.
- Monitoring.
- Managed upgrades.
- Availability.
- Security controls.

### 48.4 Why cloud matters for MLOps

Machine learning workloads may require significant computational resources.

For example:

- Training a model.
- Running inference.
- Processing large datasets.
- Serving many users.
- Running scheduled pipelines.

Cloud infrastructure makes it possible to provision and scale resources as needed.

---

## Chapter 49: Containers and Docker

Docker is one of the most important technologies you should learn for MLOps.

A container packages an application and its required dependencies into a portable environment.

Imagine your Python application works on your laptop.

You deploy it to a server.

It fails because:

- Python versions differ.
- Dependencies differ.
- System libraries differ.
- Configuration differs.

Containers help reduce these differences.

### 49.1 Docker image

An image is a packaged template used to create containers.

### 49.2 Container

A container is a running instance of an image.

### 49.3 Dockerfile

A Dockerfile defines how to build an image.

Example:

```
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "main.py"]
```

Explanation:

| Instruction | Meaning                               |
| ----------- | ------------------------------------- |
| `FROM`      | Select a base image                   |
| `WORKDIR`   | Set working directory                 |
| `COPY`      | Copy files                            |
| `RUN`       | Execute commands during build         |
| `CMD`       | Default command when container starts |

### 49.4 Build an image

```
docker build -t my-python-app .
```

### 49.5 Run a container

```
docker run my-python-app
```

### 49.6 Expose a web application

For a FastAPI application:

```
FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Run:

```
docker run -p 8000:8000 my-api
```

Now the application can be accessed through the mapped port.

### 49.7 Why Docker is essential for ML

Imagine a model was trained using:

```
Python 3.12
PyTorch 2.x
NumPy 2.x
Scikit-learn
```

Your production environment needs compatible versions.

Docker helps package the environment alongside your application.

---

# PART XVII — YOUR SPECIALIZATION: MLOPS

This is the most important section for your eventual specialization.

I want you to understand MLOps beyond the definition. You should understand the actual problems MLOps engineers solve, the architecture of the systems they build, the technologies they use, and how to create a portfolio that demonstrates those skills.

## Chapter 50: What is MLOps?

MLOps stands for Machine Learning Operations.

It combines machine learning, software engineering, DevOps, infrastructure, automation, data management, and monitoring to reliably build, deploy, and maintain machine learning systems in production.

Traditional software engineering focuses on delivering software that works.

MLOps extends that challenge to systems whose behaviour depends on data and trained models.

A conventional application might have:

```
Code → Build → Test → Deploy → Monitor
```

A machine learning application involves:

```
Data
 ↓
Data validation
 ↓
Feature preparation
 ↓
Model training
 ↓
Model evaluation
 ↓
Model approval
 ↓
Deployment
 ↓
Monitoring
 ↓
Retraining / Improvement
```

### 50.1 Why MLOps exists

Imagine a company builds a machine learning model that predicts fraudulent transactions.

During development:

- The model performs well.
- The training dataset is available.
- The engineer runs experiments locally.
- Predictions look accurate.

Now the company wants to use it in production.

New problems emerge.

- How do you deploy the model?
- How do you serve predictions to millions of requests?
- How do you ensure the correct model is running?
- What happens if the model crashes?
- What happens if the data changes?
- How do you know the model is becoming less accurate?
- How do you roll back a bad deployment?
- How do you retrain it?
- How do you track experiments?
- How do you secure the model?
- How do you prevent users from manipulating predictions?

MLOps provides the engineering processes and infrastructure to manage these problems.

---

## Chapter 51: The difference between DevOps and MLOps

DevOps focuses on improving the development and operational lifecycle of software.

MLOps applies many DevOps principles to machine learning systems, while addressing additional challenges.

| DevOps                 | MLOps                                      |
| ---------------------- | ------------------------------------------ |
| Software code          | Code, data and models                      |
| Software testing       | Software testing plus model evaluation     |
| Build pipelines        | Training and deployment pipelines          |
| Application monitoring | Application, data and model monitoring     |
| Software releases      | Model releases                             |
| Version control        | Code, data, model and experiment tracking  |
| Deployment rollback    | Model and application rollback             |
| CI/CD                  | CI/CD plus potentially continuous training |

### The key difference

A conventional software application may behave differently because its code changed.

A machine learning application may behave differently because:

- Code changed.
- Data changed.
- Model parameters changed.
- The model was retrained.
- The environment changed.
- The real-world distribution changed.

This is why ML systems require additional monitoring and governance.

---

## Chapter 52: The complete MLOps lifecycle

Let's examine each stage.

### Stage 1: Data collection

Data comes from:

- Databases.
- APIs.
- Files.
- Sensors.
- Application logs.
- User interactions.
- External datasets.

Example:

A financial transaction prediction system receives:

```
{
    "transaction_id": "TX001",
    "amount": 250000,
    "location": "Lagos",
    "hour": 23,
    "device": "mobile",
    "customer_age": 24
}
```

### Stage 2: Data validation

You must ensure that data is usable.

Questions:

- Are required fields present?
- Are amounts valid?
- Are dates formatted correctly?
- Are values within acceptable ranges?
- Are duplicate records present?
- Are labels correct?
- Are there missing values?

Example:

```
def validate_transaction(transaction):
    required_fields = [
        "amount",
        "location",
        "hour",
        "device"
    ]

    for field in required_fields:
        if field not in transaction:
            raise ValueError(
                f"Missing field: {field}"
            )

    if transaction["amount"] <= 0:
        raise ValueError(
            "Transaction amount must be positive"
        )

    if not 0 <= transaction["hour"] <= 23:
        raise ValueError(
            "Hour must be between 0 and 23"
        )

    return True
```

### Stage 3: Data preprocessing

Raw data may not be directly suitable for machine learning.

You might need to:

- Remove duplicates.
- Handle missing values.
- Convert categories into numerical representations.
- Scale numerical values.
- Correct inconsistent formats.
- Remove irrelevant features.

Example:

```
import pandas as pd

df = pd.read_csv("transactions.csv")

df = df.drop_duplicates()

df["amount"] = df["amount"].fillna(0)

df["hour"] = df["hour"].fillna(
    df["hour"].median()
)
```

### Stage 4: Feature engineering

Feature engineering involves creating or transforming useful inputs for a model.

Raw features:

```
Transaction amount
Transaction time
Customer age
```

Engineered features:

```
Amount relative to customer's average transaction
Number of transactions in the previous hour
Time since last transaction
Distance from usual location
Transaction amount percentile
```

For example:

```
transaction_amount = 50000

average_customer_amount = 10000

relative_amount = (
    transaction_amount /
    average_customer_amount
)

print(relative_amount)
```

Output:

```
5.0
```

The transaction is five times the customer's typical amount.

This may be more informative than the transaction amount alone.

### Stage 5: Training

You select a model and train it using prepared data.

Example:

```
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)
```

### Stage 6: Evaluation

You measure model performance.

```
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

predictions = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, predictions))

print("Precision:", precision_score(y_test, predictions))

print("Recall:", recall_score(y_test, predictions))

print("F1:", f1_score(y_test, predictions))
```

You may also evaluate:

- Latency.
- Memory usage.
- Model size.
- Fairness.
- Robustness.
- Cost.

### Stage 7: Model registration

A model registry stores and manages model versions.

Example:

```
Fraud Detection Model

Version 1
Version 2
Version 3
Version 4
```

You should know:

- Which model was trained?
- Which dataset was used?
- Which parameters were used?
- What was its performance?
- Who approved it?
- Is it currently deployed?
- Can it be rolled back?

### Stage 8: Deployment

A model can be deployed in several ways.

**Online inference:** predictions are returned immediately.

Example:

```
User submits transaction
        ↓
API
        ↓
Model prediction
        ↓
Risk score
        ↓
Immediate response
```

**Batch inference:** predictions are generated for many records at once.

Example:

```
10,000 customer records
        ↓
Batch prediction job
        ↓
Predictions stored in database
```

**Streaming inference:** predictions are generated as events arrive.

Example:

```
Transaction event
        ↓
Streaming pipeline
        ↓
Fraud prediction
        ↓
Alert
```

### Stage 9: Monitoring

You monitor:

- Application health.
- Model performance.
- Prediction latency.
- Error rate.
- Data quality.
- Data drift.
- Model drift.
- Infrastructure resources.

### Stage 10: Retraining

When performance deteriorates or new data becomes available, the model may need retraining.

The retraining process should not automatically mean deploying the new model.

The new model must be evaluated.

A good system may require:

```
New model
    ↓
Evaluation
    ↓
Compare with production model
    ↓
Approval
    ↓
Deployment
```

---

## Chapter 53: Machine learning pipelines

A machine learning pipeline automates the stages of ML development.

Example:

```
Extract Data
     ↓
Validate Data
     ↓
Preprocess Data
     ↓
Train Model
     ↓
Evaluate Model
     ↓
Register Model
     ↓
Deploy Model
```

### 53.1 Why pipelines matter

Without automation:

An engineer manually:

1. Downloads data.
2. Runs a script.
3. Cleans data.
4. Trains a model.
5. Evaluates it.
6. Saves the model.
7. Deploys it.

This is error-prone.

A pipeline makes the process repeatable.

### 53.2 Pipeline characteristics

Good ML pipelines should be:

- Repeatable.
- Observable.
- Versioned.
- Reliable.
- Testable.
- Recoverable.
- Automated.

### 53.3 Pipeline example

Imagine:

```
train.py
```

```
def load_data():
    pass

def validate_data():
    pass

def preprocess_data():
    pass

def train_model():
    pass

def evaluate_model():
    pass

def save_model():
    pass

def main():
    load_data()
    validate_data()
    preprocess_data()
    train_model()
    evaluate_model()
    save_model()

if __name__ == "__main__":
    main()
```

This is a simple sequential pipeline.

Later, you will use dedicated orchestration tools.

---

## Chapter 54: Experiment tracking

Machine learning often involves experimentation.

You may change:

- Model type.
- Parameters.
- Dataset.
- Features.
- Training strategy.
- Random seed.

Without tracking experiments, it becomes difficult to identify which experiment produced the best result.

Imagine:

| Experiment | Model               | Accuracy | F1   |
| ---------- | ------------------- | -------- | ---- |
| 001        | Logistic Regression | 0.81     | 0.74 |
| 002        | Random Forest       | 0.89     | 0.82 |
| 003        | XGBoost             | 0.91     | 0.85 |
| 004        | Neural Network      | 0.87     | 0.79 |

You want to know:

- What parameters were used?
- What data was used?
- What code version was used?
- How long did training take?
- What model artifact was generated?

Experiment tracking helps record these details.

### MLflow

MLflow is a tool used for managing ML experiments, tracking parameters and metrics, managing model artifacts, and supporting model lifecycle workflows.

You will eventually learn to:

- Log parameters.
- Log metrics.
- Save artifacts.
- Compare experiments.
- Register models.

Example:

```
import mlflow

with mlflow.start_run():

    mlflow.log_param(
        "model_type",
        "RandomForest"
    )

    mlflow.log_param(
        "n_estimators",
        100
    )

    mlflow.log_metric(
        "accuracy",
        0.91
    )
```

This creates a record of the experiment.

---

## Chapter 55: Model registry

A model registry provides a structured way to manage model versions.

A production system should not rely on:

```
model_final.pkl
model_final2.pkl
model_really_final.pkl
```

Instead, use structured versions.

Example:

```
Fraud Detection

Version 1
Version 2
Version 3
```

Each version should have associated information.

```
Model version: 3

Training dataset: transactions_2026_10

Algorithm: Random Forest

Accuracy: 0.92

Precision: 0.87

Recall: 0.91

Status: Approved

Environment: Python 3.12
```

Model registries help with:

- Reproducibility.
- Deployment.
- Governance.
- Rollbacks.
- Auditing.

---

## Chapter 56: Continuous integration and continuous delivery

CI/CD stands for Continuous Integration and Continuous Delivery/Deployment.

### Continuous Integration

Developers frequently integrate code changes into a shared repository.

Automated checks run.

Examples:

- Unit tests.
- Linting.
- Type checking.
- Security scanning.
- Build checks.

### Continuous Delivery

The software is prepared for release.

Deployment may require approval.

### Continuous Deployment

Changes that pass required checks can automatically be deployed.

### 56.1 A simple pipeline

```
Developer pushes code
        ↓
GitHub
        ↓
Automated tests
        ↓
Build
        ↓
Security checks
        ↓
Deployment
```

### 56.2 GitHub Actions example

Create:

```
.github/workflows/tests.yml
```

```
name: Python Tests

on:
  push:
  pull_request:

jobs:
  test:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Install dependencies
        run: |
          pip install -r requirements.txt

      - name: Run tests
        run: |
          pytest
```

This workflow automatically runs tests when code is pushed or a pull request is created.

This is a very important portfolio skill.

---

## Chapter 57: Continuous training

Continuous training is the process of automating model retraining when certain conditions are met.

Examples:

- New data becomes available.
- A schedule is reached.
- Model performance deteriorates.
- Data drift is detected.
- An engineer triggers retraining.

### 57.1 Continuous training does not mean blind retraining

Suppose the existing model has:

```
F1 = 0.89
```

A newly trained model has:

```
F1 = 0.76
```

The new model should not automatically replace the existing model.

A deployment gate may require:

```
if new_model_f1 > production_model_f1:    approve_candidate()else:    reject_candidate()
```

In a real system, this comparison should account for statistical uncertainty, business metrics, dataset representativeness, fairness, and other requirements.

---

## Chapter 58: Model deployment strategies

### 58.1 Recreate deployment

The old version is replaced with the new version.

Simple but can create downtime.

### 58.2 Rolling deployment

Gradually replace old instances with new instances.

### 58.3 Blue-green deployment

Two environments exist:

```
Blue = Existing production
Green = New version
```

You deploy and test the new version in Green.

When ready, traffic switches to Green.

If something goes wrong, traffic can switch back.

### 58.4 Canary deployment

Deploy the new version to a small percentage of users.

For example:

```
95% → Model V1

5% → Model V2
```

Monitor the results.

If the new model performs well, increase traffic.

If it performs poorly, roll back.

Canary deployment is especially useful for high-risk ML systems.

---

## Chapter 59: Model monitoring

Monitoring is one of the most important responsibilities of an MLOps engineer.

You cannot assume a model remains good forever.

A model may perform well during training and become less effective after deployment.

### 59.1 Application monitoring

Monitor:

- API availability.
- CPU usage.
- Memory usage.
- Response latency.
- Error rates.
- Request volume.
- Database performance.

Example:

```
API uptime: 99.9%

Average latency: 120 ms

Error rate: 0.3%

Requests per minute: 500
```

### 59.2 Model monitoring

Monitor:

- Prediction distributions.
- Confidence.
- Model performance.
- Input characteristics.
- Output characteristics.
- Feature distributions.

### 59.3 Data drift

Data drift occurs when the distribution of input data changes.

Example:

Your fraud model was trained on transactions primarily between ₦1,000 and ₦100,000.

Over time, the business begins processing transactions between ₦100,000 and ₦5,000,000.

The model may not behave as expected.

### 59.4 Concept drift

Concept drift occurs when the relationship between inputs and outcomes changes.

Example:

Historically:

```
Large transaction at midnight
    ↓
Higher fraud probability
```

But fraudsters change their behaviour.

Now fraudulent transactions occur during normal working hours.

The relationship the model learned becomes less reliable.

### 59.5 Data drift versus concept drift

| Data drift                     | Concept drift                                         |
| ------------------------------ | ----------------------------------------------------- |
| Input distribution changes     | Relationship between inputs and outcomes changes      |
| May be detected without labels | Often requires outcomes or labels                     |
| Can be an early warning        | Indicates the predictive relationship may be changing |

A system may experience data drift without its performance deteriorating.

A system may also experience performance deterioration without obvious data drift.

Monitoring must therefore be comprehensive.

---

## Chapter 60: Observability

Observability is the ability to understand the internal state of a system from the information it exposes.

The three commonly discussed pillars are:

### Logs

Records of events.

Example:

```
2026-11-19 10:00:00
INFO
Model loaded successfully
```

### Metrics

Numerical measurements.

Examples:

```
Request latency
Memory consumption
CPU usage
Prediction count
Error count
```

### Traces

Traces help follow a request across multiple components.

Example:

```
Frontend
   ↓
API
   ↓
Database
   ↓
Model service
   ↓
Response
```

If a request takes five seconds, tracing can help determine where the delay occurred.

### Why this matters in MLOps

A production model may depend on:

- API.
- Database.
- Feature service.
- Model server.
- Cloud infrastructure.

You need visibility into the entire system.

---

## Chapter 61: Workflow orchestration

A workflow orchestrator coordinates tasks.

Example:

```
1. Download data
2. Validate data
3. Prepare features
4. Train model
5. Evaluate model
6. Save artifact
7. Notify engineer
```

An orchestrator manages:

- Task dependencies.
- Scheduling.
- Retries.
- Execution.
- Failure handling.
- Monitoring.
- Logs.

### Common orchestration tools

- Apache Airflow.
- Prefect.
- Dagster.

Example workflow:

```
        Data Ingestion
              ↓
        Data Validation
              ↓
       Feature Processing
              ↓
         Model Training
              ↓
        Model Evaluation
              ↓
     ┌────────┴────────┐
     ↓                 ↓
  Approved          Rejected
     ↓                 ↓
  Deployment       Notification
```

### What should you learn first?

I recommend the following progression:

1. Write Python scripts that perform each pipeline stage.
2. Connect the scripts.
3. Understand dependencies.
4. Learn scheduling.
5. Learn retries and failure handling.
6. Learn Prefect or Airflow.
7. Learn how to deploy orchestrated pipelines.

Do not start with a complicated orchestration framework before understanding the tasks it is orchestrating.

---

## Chapter 62: Kubernetes

Kubernetes is a container orchestration platform.

It helps manage containerised applications at scale.

It can support:

- Deployment.
- Scaling.
- Service discovery.
- Load balancing.
- Self-healing.
- Configuration management.
- Rolling updates.

### 62.1 Why Docker alone is insufficient at scale

Docker can run containers.

But imagine you have:

```
100 containers
20 servers
```

You need to manage:

- Which server runs each container?
- What happens if a server fails?
- How do you scale?
- How do you update?
- How do containers communicate?
- How do you distribute traffic?

Kubernetes helps automate these processes.

### 62.2 Kubernetes concepts

**Pod:** The smallest commonly deployed unit in Kubernetes.

**Deployment:** Manages desired replicas and application updates.

**Service:** Provides stable network access to a group of pods.

**ConfigMap:** Stores non-sensitive configuration.

**Secret:** Stores sensitive configuration, although secure handling still requires appropriate controls.

**Namespace:** Provides logical separation of resources.

### 62.3 Deployment example

A simplified Kubernetes deployment:

```
apiVersion: apps/v1
kind: Deployment

metadata:
  name: prediction-api

spec:
  replicas: 2

  selector:
    matchLabels:
      app: prediction-api

  template:
    metadata:
      labels:
        app: prediction-api

    spec:
      containers:
        - name: prediction-api
          image: prediction-api:latest

          ports:
            - containerPort: 8000
```

This describes a deployment with two replicas.

### 62.4 Should you learn Kubernetes immediately?

No.

Learn in this order:

```
Linux
    ↓
Python
    ↓
Git
    ↓
Backend APIs
    ↓
Docker
    ↓
CI/CD
    ↓
Cloud
    ↓
Kubernetes
```

Kubernetes becomes easier when you already understand containers, networking, deployment, and infrastructure.

---

## Chapter 63: Infrastructure as Code

Infrastructure as Code (IaC) allows you to define infrastructure using configuration or code.

Instead of manually creating resources, you define:

- Servers.
- Networks.
- Storage.
- Databases.
- Permissions.
- Services.

Tools include:

- Terraform.
- OpenTofu.
- Pulumi.

### Why IaC matters

Imagine your ML application requires:

```
API server
Database
Storage bucket
Network
Monitoring
Model serving infrastructure
```

If you manually create everything, reproducing the environment is difficult.

IaC allows infrastructure to be versioned, reviewed, and recreated.

This is especially useful when:

- Building development environments.
- Creating staging environments.
- Creating production environments.
- Recovering from infrastructure failures.
- Managing multiple cloud accounts.

---

## Chapter 64: Security in MLOps

Security is not an optional final step.

It should be incorporated throughout the system.

### 64.1 Secrets

Never commit:

```
API_KEY = "my-secret-key"
```

Instead:

```
import osapi_key = os.getenv("API_KEY")
```

Use appropriate secret-management systems for production.

### 64.2 Authentication

Authentication answers:

> Who are you?

Examples:

- Passwords.
- Multi-factor authentication.
- Tokens.
- Identity providers.

### 64.3 Authorization

Authorization answers:

> What are you allowed to do?

For example:

```
Admin
    → Manage models

Data scientist
    → Train models

Viewer
    → View metrics
```

### 64.4 Model security

ML systems may be exposed to:

- Malicious inputs.
- Data poisoning.
- Model theft.
- Prompt injection.
- Sensitive information leakage.
- Dependency vulnerabilities.

### 64.5 Secure deployment checklist

- Use HTTPS.
- Protect secrets.
- Validate inputs.
- Authenticate users.
- Restrict permissions.
- Scan dependencies.
- Log security events.
- Avoid exposing unnecessary endpoints.
- Protect databases.
- Review model access.

---

# PART XVIII — SPECIALIST TRACKS: WHAT YOU SHOULD KNOW ABOUT THE OTHERS

Although your specialization is MLOps, I want you to understand how other engineering disciplines connect to your career.

## Chapter 65: AI & ML

This is the closest track to your specialization.

You will need to understand:

- Data science.
- Statistics.
- Machine learning.
- Deep learning.
- Model training.
- Model evaluation.
- Generative AI.
- Experimentation.

MLOps is the bridge between building models and operating them reliably.

## Chapter 66: Mobile development

Mobile developers build applications for:

- Android.
- iOS.

Technologies include:

- Flutter.
- Kotlin.
- Swift.

MLOps may support mobile ML by:

- Deploying models to cloud APIs.
- Managing model updates.
- Supporting inference services.
- Monitoring usage.
- Managing model versions.

## Chapter 67: DevOps & cybersecurity

This track is extremely complementary to MLOps.

You will benefit from learning:

- Linux.
- Networking.
- Cloud.
- Docker.
- CI/CD.
- Monitoring.
- Infrastructure.
- Security.

In fact, your MLOps specialization will overlap heavily with DevOps.

## Chapter 68: Blockchain

Blockchain systems involve distributed ledgers and decentralised applications.

Technologies include:

- Smart contracts.
- Solidity.
- Ethereum.
- Web3 infrastructure.

For MLOps, blockchain is not a core requirement.

However, niche applications may involve verifiable data provenance, decentralised coordination, or audit trails. These are not automatically better than conventional systems; they require a clear business reason.

## Chapter 69: Game development

Game development involves:

- Physics.
- Graphics.
- Animation.
- Interactive systems.
- Real-time computation.

MLOps can support:

- Game AI.
- Player analytics.
- Recommendation systems.
- Dynamic game behaviour.
- AI asset pipelines.

## Chapter 70: UI/UX design

UI/UX focuses on designing systems that are usable and understandable.

For your ML products, good UX is essential.

A model might be technically excellent but practically useless if users cannot understand:

- What it predicts.
- Why it made a prediction.
- What actions they should take.
- How reliable its results are.

For AI products, interfaces should communicate uncertainty and limitations appropriately.

---

# PART XIX — BUILDING A PORTFOLIO THAT ACTUALLY STANDS OUT

I don't want your GitHub profile to become a collection of basic tutorials such as:

- Calculator.
- To-do list.
- Simple weather application.
- Basic CRUD application.

These projects are useful when learning, but they will not sufficiently differentiate you once you are targeting AI engineering and MLOps roles.

Your portfolio should demonstrate that you understand real problems, engineering architecture, deployment, data, reliability, and the business implications of your systems.

The projects below are deliberately designed around problems that exist in Nigeria and potentially in other markets.

---

# Chapter 71: Project One — SME Intelligence & Business Copilot

(Recommended flagship product)

## The problem

Many small and medium businesses operate using:

- Paper records.
- WhatsApp messages.
- Excel spreadsheets.
- Manual stock counting.
- Intuition.
- Inconsistent bookkeeping.

A business owner may know how much money came in today but not:

- Which products are profitable.
- Which products are becoming slow-moving.
- Which products are likely to run out.
- How much money is tied up in inventory.
- Whether sales are declining.
- What they should restock.
- How much they should purchase.
- Which customers are becoming inactive.

This creates significant financial inefficiency.

## Your proposed solution

Build an AI-powered business intelligence platform for small businesses.

Working name:

**MarketPilot AI**

The platform helps a business owner understand their business and make better decisions using their existing operational data.

### Core features

**1. Sales tracking**

Track:

- Product.
- Quantity.
- Price.
- Date.
- Customer.
- Payment method.

**2. Inventory management**

Track:

- Stock levels.
- Purchases.
- Sales.
- Restocking.
- Expiry.
- Inventory value.

**3. Sales forecasting**

Predict future sales.

Example:

```
Product: Malt Drink

Expected sales next week:
320 units

Current stock:
180 units

Recommended restocking:
200 units
```

**4. AI business assistant**

A business owner asks:

> Why did my sales drop this week?

The system analyses relevant information and provides a grounded answer.

**5. Financial intelligence**

Identify:

- Revenue trends.
- Expenses.
- Profit estimates.
- Cash-flow concerns.
- High-performing products.

**6. Alerts**

Examples:

```
Stock alert:
Rice may run out within 5 days.
```

```
Sales alert:
Your average daily sales declined by 18%.
```

```
Recommendation:
Restock 25 units of your highest-performing product.
```

---

## Architecture

```
Business Owner
      ↓
Web / Mobile Application
      ↓
Backend API
      ↓
Business Database
      ↓
Data Processing Pipeline
      ↓
Forecasting Models
      ↓
AI Analysis Layer
      ↓
Business Insights
      ↓
Dashboard / Notifications
```

### Suggested technology stack

| Component              | Technology                      |
| ---------------------- | ------------------------------- |
| Frontend               | React                           |
| Backend                | FastAPI                         |
| Database               | PostgreSQL                      |
| Data analysis          | Pandas                          |
| ML                     | Scikit-learn                    |
| Experiment tracking    | MLflow                          |
| API testing            | Pytest                          |
| Containers             | Docker                          |
| CI/CD                  | GitHub Actions                  |
| Cloud                  | AWS, Azure or another cloud     |
| Monitoring             | Prometheus + Grafana            |
| Pipeline orchestration | Prefect                         |
| AI assistant           | LLM API with grounded retrieval |

You do not need to implement all of these technologies immediately.

Build the product progressively.

### Phase 1 — Functional MVP

- User registration.
- Business creation.
- Product creation.
- Sales recording.
- Stock tracking.
- Dashboard.

### Phase 2 — Data analytics

- Revenue calculations.
- Profit estimates.
- Product rankings.
- Sales charts.
- Daily and weekly reports.

### Phase 3 — Machine learning

- Sales forecasting.
- Stockout prediction.
- Demand prediction.
- Customer segmentation.

### Phase 4 — MLOps

- Training pipeline.
- Experiment tracking.
- Model registry.
- API inference.
- Docker.
- CI/CD.
- Monitoring.
- Drift detection.

### Phase 5 — AI assistant

Allow users to ask questions about their own business data.

The assistant must use actual business data and should not invent financial facts.

---

## Revenue model

Potential models:

### Freemium

Free:

- Basic inventory.
- Limited products.
- Basic sales tracking.

Paid:

- Advanced analytics.
- AI insights.
- Forecasting.
- Multiple branches.
- Staff management.
- Automated reports.

### Subscription

Potential illustrative pricing:

| Plan       | Illustrative monthly price |
| ---------- | -------------------------- |
| Starter    | ₦3,000                     |
| Business   | ₦8,000                     |
| Growth     | ₦15,000                    |
| Enterprise | Custom                     |

These are hypothetical starting prices for testing willingness to pay, not validated market prices.

### Global market

The same platform could be adapted for businesses outside Nigeria.

However, international expansion would require appropriate:

- Currency support.
- Tax considerations.
- Regional integrations.
- Data protection.
- Localisation.
- Payments.

### Your MLOps portfolio value

This project demonstrates:

- Full-stack engineering.
- Data engineering.
- ML.
- API development.
- CI/CD.
- Containerisation.
- Model deployment.
- Monitoring.
- Product thinking.

It could become your strongest portfolio project if executed well.

---

# Chapter 72: Project Two — PowerGuard AI

## The problem

Energy systems are expensive and difficult to manage.

Businesses using:

- Solar.
- Inverters.
- Batteries.
- Generators.
- Grid electricity.

Need to understand:

- Consumption.
- Battery health.
- Energy efficiency.
- Abnormal usage.
- Equipment faults.
- Energy costs.

## The solution

Build a system that monitors energy data and predicts abnormal behaviour.

### Features

- Energy monitoring dashboard.
- Voltage monitoring.
- Current monitoring.
- Power consumption.
- Battery status.
- Equipment anomaly detection.
- Energy usage forecasting.
- Maintenance alerts.

### Machine learning component

Predict abnormal patterns.

Example:

```
Equipment:
Inverter A

Current operating pattern:
Normal

Anomaly score:
0.94

Possible issue:
Unusual temperature rise combined
with increased load.
```

The system should clearly communicate that this is a risk signal, not a confirmed diagnosis of equipment failure.

### MLOps components

- IoT data ingestion.
- Data validation.
- Time-series storage.
- Model training.
- Deployment.
- Monitoring.
- Retraining.

This project connects particularly well with your Computer Engineering background and your solar/wind project.

It can potentially become a specialised monitoring product for:

- Solar installations.
- Small factories.
- Hotels.
- Offices.
- Farms.

---

# Chapter 73: Project Three — AgricPredict

## Problem

Farmers face uncertainty around:

- Weather.
- Crop yields.
- Disease.
- Market prices.
- Soil conditions.
- Planting decisions.

## Proposed solution

A data-driven agricultural decision platform.

Features:

- Weather information.
- Crop monitoring.
- Yield forecasting.
- Market information.
- Disease risk alerts.
- Recommendation engine.

### ML models

Potential models:

- Yield prediction.
- Weather-related risk classification.
- Crop disease classification.
- Market demand prediction.

### Business model

- Subscription.
- Cooperative partnerships.
- Agricultural businesses.
- Farm-management services.
- Enterprise analytics.

This project could have meaningful impact but requires credible data and domain partnerships to become commercially useful.

---

# Chapter 74: Project Four — FinRisk AI

## Problem

Financial institutions need to identify:

- Fraud.
- Suspicious transactions.
- Unusual customer behaviour.
- Credit risk.
- Money laundering indicators.

## Solution

A transaction-risk intelligence platform.

Features:

- Transaction ingestion.
- Risk scoring.
- Anomaly detection.
- Explainable alerts.
- Risk dashboard.
- Analyst review.

### Example

```
Transaction ID:
TX-19384

Amount:
₦850,000

Risk score:
0.89

Risk factors:
- Amount significantly above usual spending
- Unusual transaction time
- New device
- Location differs from typical activity
```

### Important limitation

A machine learning risk score should not automatically be treated as proof of fraud.

The system should support investigation and appropriate human oversight, especially when decisions affect access to money or financial services.

### Portfolio skills

- Classification.
- Anomaly detection.
- Feature engineering.
- Model evaluation.
- Data pipelines.
- Model monitoring.
- API deployment.

---

# Chapter 75: Project Five — DocuMind AI

## Problem

Companies process enormous amounts of documents:

- Invoices.
- Contracts.
- Receipts.
- Reports.
- Statements.
- Policies.

Manually processing documents is slow.

## Solution

An AI document-processing platform.

Users upload documents.

The system:

1. Extracts text.
2. Classifies the document.
3. Extracts important fields.
4. Validates the fields.
5. Stores structured information.
6. Allows searching.
7. Generates summaries.

### Example

Invoice:

```
Vendor: ABC Supplies

Invoice Number: INV-2026-102

Amount: ₦450,000

Date: 15 November 2026
```

AI extracts:

```
{
    "vendor": "ABC Supplies",
    "invoice_number": "INV-2026-102",
    "amount": 450000,
    "date": "2026-11-15"
}
```

### MLOps components

- Document ingestion.
- OCR.
- Model inference.
- Validation.
- Batch processing.
- Queue management.
- Model versioning.
- Monitoring.

This could potentially be sold to:

- SMEs.
- Accounting firms.
- Logistics companies.
- Law firms.
- Financial institutions.

---

# Chapter 76: Which project should you prioritise?

## My recommendation: MarketPilot AI

Use it as your primary long-term flagship project.

It provides the opportunity to demonstrate a broad engineering skill set while solving a problem that can be understood by potential users and tested with real businesses.

You should not attempt all five projects simultaneously.

My suggested strategy:

| Priority | Project                      | Purpose                          |
| -------- | ---------------------------- | -------------------------------- |
| 1        | File/Data automation project | Establish Python fundamentals    |
| 2        | MarketPilot AI               | Flagship full-stack + MLOps      |
| 3        | FinRisk AI                   | Focused ML engineering           |
| 4        | PowerGuard AI                | Technical domain differentiation |
| 5        | DocuMind AI                  | Applied AI / LLM systems         |

Build fewer projects, but make them genuinely excellent.

---

# PART XX — THE MLOPS ENGINEERING ROADMAP

## Chapter 77: The technologies you should eventually master

Do not try to learn every tool at once.

MLOps is a broad field. The value comes from understanding how the technologies fit together, not from collecting tool names.

### Level 1 — Core foundation

Python

Programming & automation

Git

Version control

Linux

Operating systems

SQL

Database operations

Testing

Software quality

Networking

Communication

### Level 2 — Software engineering

- FastAPI.
- PostgreSQL.
- Data structures.
- Algorithms.
- Software architecture.
- Authentication.
- REST APIs.
- Testing.
- Dependency management.

### Level 3 — Data and ML

- NumPy.
- Pandas.
- Scikit-learn.
- Statistics.
- Data preprocessing.
- Feature engineering.
- Model evaluation.
- PyTorch.

### Level 4 — MLOps foundations

- Docker.
- MLflow.
- GitHub Actions.
- Model serving.
- Model registries.
- Data validation.
- Pipeline orchestration.

### Level 5 — Infrastructure

- Cloud computing.
- AWS / Azure / GCP.
- Linux servers.
- Terraform.
- Kubernetes.
- Networking.
- Security.

### Level 6 — Production MLOps

- Monitoring.
- Data drift.
- Model drift.
- Continuous training.
- Feature stores.
- Model governance.
- Deployment strategies.
- Distributed systems.
- Scalability.
- Cost optimisation.

---

## Chapter 78: What is a feature store?

A feature store manages machine learning features.

Features may be used in:

- Training.
- Inference.
- Multiple models.
- Different applications.

Imagine you have:

```
Customer ID: 1001

Average transaction amount:
₦15,000

Transactions in last 24 hours:
12

Transactions in last 7 days:
45

Average transaction interval:
3 hours
```

These features may be useful for a fraud detection model.

A feature store helps organise and serve features consistently.

### Why feature consistency matters

Imagine during training you calculate:

```
Average transaction amount
```

using historical data.

But in production, you calculate it differently.

Your model receives different feature values than it did during training.

This can create training-serving skew.

A feature store can help standardise feature definitions and delivery.

You don't need to begin with a feature store. Learn the underlying problem first.

---

## Chapter 79: Batch processing versus real-time processing

### Batch

Process many records together.

Example:

```
Every night at 1 AM:

10,000 customers
       ↓
Prediction pipeline
       ↓
Customer risk scores
       ↓
Database
```

### Real-time

Process events as they arrive.

Example:

```
Customer makes payment
       ↓
Transaction event
       ↓
Risk model
       ↓
Prediction in milliseconds
       ↓
Payment decision system
```

### When should you use each?

| Batch                                 | Real-time                      |
| ------------------------------------- | ------------------------------ |
| Historical analysis                   | Immediate decisions            |
| Scheduled processing                  | Event-driven                   |
| Often lower infrastructure complexity | More infrastructure complexity |
| Can tolerate delay                    | Requires low latency           |

A common mistake is using real-time architecture when batch processing would solve the problem more cheaply.

---

## Chapter 80: Model serving

Model serving makes a trained model available for predictions.

There are several approaches.

### Direct Python inference

```
import joblib

model = joblib.load("model.pkl")

prediction = model.predict([[50000, 24, 10]])

print(prediction)
```

### API serving

```
from fastapi import FastAPI
import joblib

app = FastAPI()

model = joblib.load("model.pkl")

@app.post("/predict")
def predict(data: dict):

    features = [
        data["amount"],
        data["age"],
        data["transaction_count"]
    ]

    prediction = model.predict([features])

    return {
        "prediction": int(prediction[0])
    }
```

In a production application, you should use structured validation, proper error handling, authentication, logging, model version management, and monitoring.

---

## Chapter 81: Latency and throughput

These are two important performance concepts.

### Latency

How long it takes for an operation to complete.

Example:

```
Prediction latency: 80 milliseconds
```

### Throughput

How much work a system performs over a period.

Example:

```
1000 predictions per second
```

An application can have low latency but low throughput.

It can also have high throughput but unacceptable latency for individual users.

MLOps engineers must understand both.

---

## Chapter 82: Reliability

Reliability refers to the ability of a system to operate correctly over time.

Production systems must account for failure.

### Common failures

- Server crash.
- Database unavailable.
- Network failure.
- Model loading failure.
- Memory exhaustion.
- Corrupted input.
- Cloud outage.

### Reliability strategies

- Health checks.
- Retries.
- Timeouts.
- Backups.
- Redundancy.
- Monitoring.
- Rollbacks.
- Graceful degradation.

Example:

If an AI service becomes unavailable, a business application may still allow users to complete non-AI operations.

This is called graceful degradation.

---

# PART XXI — PRACTICAL PROJECTS AND EXERCISES

## Chapter 83: Your project ladder

I recommend building projects in the following sequence.

### Project 0 — Python command-line utilities

Examples:

- Expense tracker.
- File organiser.
- CSV analyser.
- Student grading system.

Skills:

- Variables.
- Loops.
- Functions.
- Dictionaries.
- Files.
- Exceptions.
- Git.

### Project 1 — API service

Build:

```
Student Management API
```

Features:

- Create students.
- Retrieve students.
- Update students.
- Delete students.
- Validation.
- Database.

Skills:

- FastAPI.
- REST.
- SQL.
- PostgreSQL.
- Testing.

### Project 2 — Data pipeline

Build:

```
Sales Data Pipeline
```

Pipeline:

```
CSV
 ↓
Validation
 ↓
Cleaning
 ↓
Transformation
 ↓
Database
 ↓
Dashboard
```

Skills:

- Pandas.
- Data quality.
- SQL.
- Automation.

### Project 3 — Machine learning application

Build:

```
Customer Churn Prediction
```

Features:

- Data analysis.
- Model training.
- Evaluation.
- API predictions.

Skills:

- Scikit-learn.
- ML.
- Metrics.
- Model serving.

### Project 4 — Containerised ML application

Package the model API using Docker.

Skills:

- Docker.
- Environments.
- Deployment.

### Project 5 — MLOps pipeline

Build:

```
Data
 ↓
Validation
 ↓
Training
 ↓
Evaluation
 ↓
Experiment Tracking
 ↓
Model Registry
 ↓
Deployment
 ↓
Monitoring
```

Skills:

- MLflow.
- CI/CD.
- Orchestration.
- Monitoring.

### Project 6 — Flagship commercial product

Build MarketPilot AI.

This combines the previous projects into a production-oriented system.

---

## Chapter 84: A detailed flagship implementation roadmap

### Phase 1 — Requirements

Write a proper product specification.

Document:

- Problem.
- Target users.
- User stories.
- Functional requirements.
- Non-functional requirements.
- Risks.
- Success metrics.

### Phase 2 — Database design

Potential tables:

```
users
businesses
products
sales
sale_items
inventory
expenses
customers
```

Establish relationships.

For example:

```
Business
  ├── Products
  ├── Sales
  ├── Expenses
  └── Users
```

### Phase 3 — Backend

Implement:

- Authentication.
- Business registration.
- Product management.
- Sales.
- Inventory.
- Expenses.
- Reports.

### Phase 4 — Testing

Test:

- Authentication.
- Business isolation.
- Invalid data.
- Stock updates.
- Sales calculations.
- Permissions.

### Phase 5 — Data engineering

Build:

- Data extraction.
- Cleaning.
- Validation.
- Feature generation.
- Storage.

### Phase 6 — Machine learning

Develop:

- Sales forecasting.
- Demand forecasting.
- Customer segmentation.

### Phase 7 — MLOps

Implement:

- Experiment tracking.
- Model versioning.
- Training pipelines.
- CI/CD.
- Docker.
- Deployment.
- Monitoring.

### Phase 8 — Product intelligence

Build:

- AI assistant.
- Automated insights.
- Alerts.
- Recommendations.

### Phase 9 — Commercial testing

Interview real businesses.

Do not assume they will pay because the product sounds interesting.

Investigate:

- Their current workflow.
- Their biggest financial problem.
- How they currently solve it.
- What they would pay to solve it.
- Whether your solution saves money or increases revenue.
- What information they would trust you to process.

### Phase 10 — Launch

Start with a small group of businesses.

Measure:

- Weekly active users.
- Transactions recorded.
- Accuracy of forecasts.
- Stockout reduction.
- Revenue retention.
- Customer satisfaction.
- Conversion to paid plans.

---

# PART XXII — YOUR PREPARATION SCHEDULE BEFORE FEBRUARY

## Chapter 85: The 12-week head-start plan

Assuming your programme begins in February 2027, this schedule is designed to use the time between now and then productively.

It is not designed to replace your official programme.

The goal is to make the programme easier to absorb by giving you familiarity with the concepts, terminology, tools, and problem-solving techniques.

Because you have already been working on Python and backend projects, you do not necessarily need to repeat every beginner exercise from scratch. Use the exercises to assess your understanding and spend more time on weak areas.

## Preparation targets

# 12

Weeks of preparation

# 6–10

Study hours per week, adjustable

# 1

Small project every few weeks

# 1

Flagship project foundation

### Weeks 1–2: Python mastery

Topics:

- Variables.
- Data types.
- Operators.
- Conditionals.
- Loops.
- Functions.
- Lists.
- Dictionaries.
- Sets.
- Tuples.
- Exceptions.

Practice:

- Student grading system.
- Expense calculator.
- Number analyser.
- Simple inventory tracker.

Goal:

You should be able to write small programs without constantly looking up every syntax element.

### Weeks 3–4: Python engineering

Topics:

- OOP.
- File handling.
- JSON.
- CSV.
- Modules.
- Packages.
- Virtual environments.
- Type hints.
- Testing.

Project:

```
Personal Expense Tracker

Features:
- Add expense
- Categorise expense
- Save expenses
- Load expenses
- Calculate totals
- Generate reports
- Handle invalid inputs
- Test functions
```

### Week 5: Git, Linux and development workflow

Topics:

- Git.
- GitHub.
- Branches.
- Commits.
- Pull requests.
- Terminal.
- Linux commands.
- Virtual environments.

Goal:

You should be comfortable creating a repository, making changes, committing them, and pushing to GitHub.

### Week 6: SQL and databases

Topics:

- Tables.
- Primary keys.
- Foreign keys.
- CRUD.
- Filtering.
- Joins.
- Aggregation.
- Relationships.

Project:

Build a small sales database.

### Week 7: Backend and APIs

Topics:

- HTTP.
- REST.
- JSON.
- FastAPI.
- Request validation.
- Responses.
- Status codes.
- API documentation.

Project:

Build an inventory API.

### Week 8: Software engineering and testing

Topics:

- Architecture.
- Separation of concerns.
- Unit testing.
- Integration testing.
- Error handling.
- Logging.
- Code quality.

Improve your inventory API.

### Week 9: Data analysis

Topics:

- NumPy.
- Pandas.
- CSV.
- Data cleaning.
- Missing values.
- Statistics.
- Visualisation.

Project:

Analyse a Nigerian business sales dataset.

### Week 10: Machine learning fundamentals

Topics:

- Features.
- Labels.
- Regression.
- Classification.
- Training.
- Testing.
- Overfitting.
- Metrics.

Project:

Build a basic sales or customer prediction model.

### Week 11: Docker and deployment

Topics:

- Containers.
- Images.
- Dockerfiles.
- Environment variables.
- Ports.
- Container deployment.

Containerise your API.

### Week 12: MLOps introduction

Topics:

- ML pipelines.
- Model tracking.
- Deployment.
- CI/CD.
- Monitoring.
- Data drift.

Project:

Build a miniature ML pipeline with automated testing.

---

## Chapter 86: Your daily study method

I recommend a structure like this:

## A 2-hour learning session

20 min

**Learn**

Read concepts, watch a tutorial, study documentation.

---

50 min

**Code**

Implement the concepts independently.

---

30 min

**Problem-solving**

Exercises and debugging challenges.

---

20 min

**Review**

Document what you learned and commit your work.

You don't have to follow these exact durations every day.

The principle is to avoid spending all your time consuming tutorials without writing code.

---

# PART XXIII — PREPARATION EXERCISES

## Chapter 87: Python exercises

### Beginner

1. Print your name and occupation.
2. Calculate the area of a rectangle.
3. Convert Celsius to Fahrenheit.
4. Determine whether a number is even or odd.
5. Determine whether a number is positive, negative, or zero.
6. Calculate the average of five numbers.
7. Find the largest number in a list.
8. Count the number of vowels in a string.
9. Reverse a string.
10. Determine whether a word is a palindrome.

### Intermediate

11. Build a calculator.
12. Build a student grading system.
13. Build a contact book.
14. Build a bank account class.
15. Build an inventory manager.
16. Build an expense tracker.
17. Read a CSV file and calculate statistics.
18. Save data to JSON and reload it.
19. Build a file organiser.
20. Write tests for your functions.

### Advanced beginner

21. Build an API.
22. Connect it to a database.
23. Implement authentication.
24. Add validation.
25. Write integration tests.
26. Containerise it.
27. Create automated CI.
28. Deploy it.

---

## Chapter 88: Machine learning exercises

1. Calculate mean, median, and mode.
2. Calculate variance and standard deviation.
3. Explain the difference between classification and regression.
4. Train a linear regression model.
5. Train a classification model.
6. Split a dataset into training and testing sets.
7. Calculate accuracy, precision, recall, and F1.
8. Explain overfitting.
9. Explain underfitting.
10. Identify data leakage in a hypothetical dataset.
11. Compare two models.
12. Create a model inference API.

---

## Chapter 89: MLOps exercises

1. Package a model with Docker.
2. Write unit tests for preprocessing.
3. Create a GitHub Actions workflow.
4. Track model experiments.
5. Save model artifacts.
6. Build a pipeline.
7. Add logging.
8. Add a health endpoint.
9. Monitor prediction latency.
10. Implement a model rollback strategy.
11. Compare a candidate model with a production model.
12. Create a simple data drift detector.

---

# PART XXIV — A PROFESSIONAL MLOPS PROJECT STRUCTURE

## Chapter 90: How to organise a real project

Eventually, a project like MarketPilot AI might have a structure resembling:

```
marketpilot-ai/
│
├── README.md
├── pyproject.toml
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── .gitignore
├── .env.example
│
├── .github/
│   └── workflows/
│       ├── tests.yml
│       └── deployment.yml
│
├── app/
│   ├── api/
│   │   ├── routes/
│   │   └── dependencies.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   └── security.py
│   │
│   ├── database/
│   │   ├── connection.py
│   │   └── models.py
│   │
│   ├── services/
│   │   ├── sales.py
│   │   ├── inventory.py
│   │   └── forecasting.py
│   │
│   └── main.py
│
├── ml/
│   ├── data/
│   ├── features/
│   ├── training/
│   ├── evaluation/
│   ├── inference/
│   └── models/
│
├── pipelines/
│   ├── training_pipeline.py
│   └── prediction_pipeline.py
│
├── tests/
│   ├── unit/
│   ├── integration/
│   └── ml/
│
├── monitoring/
│   ├── metrics.py
│   └── drift.py
│
├── scripts/
│   ├── train.py
│   └── evaluate.py
│
└── docs/
    ├── architecture.md
    ├── api.md
    └── deployment.md
```

This is an example architecture, not a mandatory template.

You should avoid creating unnecessary folders and abstractions for a tiny project.

Architecture should evolve as the project grows.

---

# PART XXV — RESOURCES YOU SHOULD USE

Do not attempt to learn everything from one source.

The most effective approach is to combine explanations, documentation, exercises, and actual projects.

## 1. Python

**Python**

Official Python Tutorial

Language fundamentals, functions, classes, modules, files and exceptions.

## 2. Git

**Git**

Pro Git Book

Version control, branches, commits, remotes and collaboration.

## 3. Linux

**Linux**

Linux Command Line

Terminal usage, filesystem, processes and commands.

## 4. SQL

**PostgreSQL**

Official Documentation

Database fundamentals, SQL, queries, indexes and database administration.

## 5. FastAPI

**FastAPI**

Official Documentation

Backend APIs, request validation, dependencies and deployment.

## 6. Machine learning

**Scikit-learn**

User Guide

Supervised learning, preprocessing, evaluation and model selection.

## 7. Deep learning

**PyTorch**

Tutorials

Neural networks, tensors, training loops and GPU computing.

## 8. Docker

**Docker**

Docker Getting Started

Images, containers, Dockerfiles and deployment.

## 9. MLflow

**MLflow**

Official Documentation

Experiment tracking, model evaluation, model registry and lifecycle management.

## 10. GitHub Actions

**GitHub Actions**

Official Documentation

Automated testing, builds, workflows and deployments.

## 11. Kubernetes

**Kubernetes**

Official Tutorials

Container orchestration, deployment, scaling and infrastructure.

---

# PART XXVI — THE GLOSSARY YOU SHOULD KNOW

| Term                | Meaning                                              |
| ------------------- | ---------------------------------------------------- |
| Algorithm           | A sequence of steps for solving a problem            |
| API                 | An interface through which software communicates     |
| Backend             | Server-side application logic                        |
| CLI                 | Command-line interface                               |
| CI                  | Continuous integration                               |
| CD                  | Continuous delivery or deployment                    |
| Container           | An isolated application environment                  |
| CPU                 | Central processing unit                              |
| Database            | Organised system for storing data                    |
| Data pipeline       | Process for moving and transforming data             |
| Dataset             | Collection of data                                   |
| Deployment          | Making software available for use                    |
| Docker              | Containerisation platform                            |
| Feature             | Input used by an ML model                            |
| Git                 | Version control system                               |
| GitHub              | Git repository hosting and collaboration platform    |
| GPU                 | Graphics processing unit                             |
| HTTP                | Web communication protocol                           |
| Inference           | Using a trained model to make predictions            |
| JSON                | Structured data format                               |
| Kubernetes          | Container orchestration platform                     |
| Latency             | Time taken to complete an operation                  |
| Label               | Target output in supervised learning                 |
| Logging             | Recording application events                         |
| ML                  | Machine learning                                     |
| MLOps               | Engineering and operational practices for ML systems |
| Model               | Learned mathematical representation                  |
| Monitoring          | Observing system behaviour                           |
| Overfitting         | Learning training data too closely                   |
| Pipeline            | Automated sequence of processing stages              |
| Precision           | Correctness among predicted positive cases           |
| Recall              | Coverage of actual positive cases                    |
| Regression          | Predicting numerical values                          |
| Repository          | Project storage managed by version control           |
| REST                | Common architectural style for APIs                  |
| SQL                 | Language for relational database operations          |
| Test                | Verification of software behaviour                   |
| Throughput          | Amount of work processed per unit of time            |
| Training            | Process of learning model parameters                 |
| Vector              | Ordered numerical collection                         |
| Virtual environment | Isolated Python dependency environment               |

---

# PART XXVII — HOW TO APPROACH THE PROGRAMME

## Chapter 91: Don't become a tutorial collector

One of the biggest traps in learning technology is spending months watching videos and reading documentation without building anything.

You can watch a 10-hour Python course and still struggle to solve a problem independently.

The goal is not:

> I completed a course.

The goal is:

> I can use the knowledge to solve a problem without needing the tutorial to tell me every step.

### The learning cycle

```
Understand
    ↓
Attempt
    ↓
Get stuck
    ↓
Investigate
    ↓
Experiment
    ↓
Solve
    ↓
Explain
    ↓
Apply somewhere else
```

This is the cycle I want you to use.

### The Feynman technique

After learning a concept, explain it in simple language as if teaching someone who has never encountered it.

For example:

**What is a database?**

A weak answer:

> A database is a database management system used to store information.

A better answer:

> A database is a structured system for storing information so that applications can reliably retrieve, update, organise, and manage it. Instead of storing business information in scattered files, a database allows us to manage relationships, search information efficiently, and protect the consistency of our records.

If you can explain a concept without hiding behind technical jargon, you probably understand it more deeply.

---

## Chapter 92: What to do when you get stuck

During the programme, you will encounter challenges that may take hours or even days.

Use this procedure.

### Step 1 — Understand the problem

Write down:

- What am I trying to achieve?
- What is the expected behaviour?
- What is currently happening?

### Step 2 — Break it down

Divide the problem into smaller components.

### Step 3 — Attempt it yourself

Do not immediately ask AI for a complete solution.

Spend time thinking.

### Step 4 — Research

Use:

- Documentation.
- Search engines.
- Error messages.
- Examples.
- Discussions.

### Step 5 — Ask targeted questions

Instead of:

> My code isn't working.

Ask:

> My FastAPI endpoint receives a request, but the database record isn't being created. I verified that the endpoint executes and the validation passes. I suspect the database session is not committing. Can you explain how I should investigate this?

### Step 6 — Test hypotheses

Do not randomly change code.

Test one assumption at a time.

### Step 7 — Document the solution

Create a record of:

- Problem.
- Root cause.
- Solution.
- What you learned.

Your personal debugging journal can become an invaluable learning resource.

---

## Chapter 93: What makes an engineer employable?

Certificates alone are not enough.

Employability comes from a combination of:

- Technical knowledge.
- Problem-solving.
- Communication.
- Collaboration.
- Reliability.
- Portfolio quality.
- Practical experience.
- Learning adaptability.

A recruiter or engineer reviewing your GitHub should be able to see evidence that you can build systems.

Your portfolio should gradually demonstrate:

### Software engineering

- Structured code.
- APIs.
- Databases.
- Testing.
- Documentation.

### Machine learning

- Data analysis.
- Model training.
- Evaluation.
- Appropriate metrics.

### MLOps

- Pipelines.
- Model tracking.
- Deployment.
- Containers.
- Automation.
- Monitoring.

### Product thinking

- Clear problem.
- Target users.
- Value proposition.
- Business model.
- Real feedback.

---

# PART XXVIII — YOUR PERSONAL MLOPS CAREER DIRECTION

## Chapter 94: Possible career progression

Your path could evolve approximately like this:

Software Engineering Foundation

Python · Git · Linux · SQL · APIs

↓

AI / ML Engineering

Data · Models · Training · Evaluation

↓

Cloud / DevOps Foundation

Docker · CI/CD · Cloud · Infrastructure

↓

MLOps Engineer

ML pipelines · Model serving · Monitoring · Reliability

↓

Senior / Platform / ML Infrastructure Engineer

Scale · Architecture · Reliability · Leadership

Possible job titles you could eventually target:

- Machine Learning Engineer.
- MLOps Engineer.
- ML Platform Engineer.
- AI Infrastructure Engineer.
- Data Engineer.
- Cloud Engineer.
- Software Engineer, AI.
- Platform Engineer.

You do not need to lock yourself into one title immediately.

The goal is to build transferable skills that allow you to move across related roles.

---

# PART XXIX — IMPORTANT NOTES ABOUT THE OFFICIAL CURRICULUM

I noticed that the official Learn2Earn webpages describe some programme timelines and stages differently.

The curriculum page describes a two-year training/internship structure, with one year of focused learning and one year of internships, and also lists a six-month specialization period. The current programme homepage describes a one-year training phase followed by a year of AI specialization and internships/access to work. These descriptions may reflect different programme versions or how the stages are presented.

I would therefore use the official programme's actual learning platform and instructions as the final authority once your cohort begins, particularly for:

- Exact module order.
- Specific languages and frameworks.
- Project requirements.
- Specialization timing.
- Assessment requirements.
- Internship structure.

This preparation is intentionally designed around the fundamental skills that remain valuable regardless of those changes.

---

# Your ultimate objective

By the time you finish this preparation, I want you to be able to do the following without feeling intimidated:

- Open a terminal and navigate a project.
- Create and manage a Python environment.
- Write Python functions, classes, and modules.
- Read unfamiliar code.
- Debug errors systematically.
- Work with Git and GitHub.
- Build an API.
- Connect an application to a database.
- Write SQL queries.
- Test software.
- Analyse a dataset.
- Train a basic machine learning model.
- Understand model evaluation.
- Explain Docker.
- Containerise a Python application.
- Understand what CI/CD does.
- Explain the ML lifecycle.
- Understand why production models require monitoring.
- Describe how an MLOps pipeline works.
- Start developing your own substantial project.

And most importantly:

**You should be able to learn unfamiliar technologies independently.**

That is the skill that will continue to compound throughout your career.

---

## The three things I would prioritise most before February

If you have limited time, do not attempt to master everything in this book.

Focus on these three areas:

**1. Python fluency**

Be comfortable writing programs, using functions, manipulating data, handling errors, and solving problems.

---

**2. Software engineering fundamentals**

Git, testing, terminal usage, APIs, databases, debugging, and code organisation.

---

**3. Early exposure to AI and MLOps**

Understand what machine learning is, how models are trained, why deployment is difficult, and what MLOps solves.

You don't need to arrive in February already knowing Kubernetes, advanced neural networks, cloud architecture, and every ML framework.

You need to arrive with a strong foundation, confidence in problem-solving, and the discipline to learn rapidly.

**Your advantage will not be how much information you memorise before the programme. It will be how effectively you turn information into practical competence.**

I would recommend treating this as your master preparatory textbook and working through it progressively, with exercises, implementation challenges, and project checkpoints rather than attempting to read it all in one sitting. The next step would be to turn this into a properly formatted, expanded study book with deeper chapter-by-chapter explanations, practical assignments, solutions, diagrams, and a structured 12-week companion workbook.