# 🔧 Multi-Utility Toolkit

A beginner-friendly **Python Multi-Utility Toolkit** that combines multiple built-in Python modules into one menu-driven application.

This project demonstrates how Python modules can be used to perform **date and time operations, mathematical calculations, random data generation, UUID generation, file handling, and module exploration**.

---

## 📌 Project Information

**Project:** PR. 7 - Moduler & Packager
**Project Name:** Multi-Utility Toolkit
**Language:** Python
**Level:** Beginner / Intermediate
**Interface:** Console / Menu Driven
**Python Version:** Python 3.x

---

## 🎯 Objective

The main objective of this project is to understand how Python's **built-in modules** can be imported and used in a practical application.

The project demonstrates the use of:

* `datetime`
* `time`
* `math`
* `random`
* `string`
* `uuid`
* `os`

It also demonstrates the use of Python functions, loops, conditions, file handling, `dir()`, and `if __name__ == "__main__"`.

---

## ✨ Features

### 1. 📅 Date and Time Operations

The application provides several date and time utilities:

* Display current date and time
* Find difference between two dates
* Format the current date
* Run a countdown timer

**Module Used:**

```python
datetime
time
```

---

### 2. 🧮 Mathematical Operations

The mathematical section provides:

* Factorial calculation
* Compound interest calculation
* Circle area calculation
* Rectangle area calculation
* Trigonometric calculations
* Square root calculation

**Module Used:**

```python
math
```

---

### 3. 🎲 Random Data Generation

The random data section can generate:

* Random number
* Random list
* Random password
* 6-digit OTP
* Random sample
* Simple dice game

**Modules Used:**

```python
random
string
```

---

### 4. 🆔 UUID Generator

The UUID section generates a unique identifier using:

```python
uuid.uuid4()
```

Example:

```text
Generated UUID:
550e8400-e29b-41d4-a716-446655440000
```

**Module Used:**

```python
uuid
```

---

### 5. 📁 File Operations

The file management section allows users to:

* Create a file
* Write data to a file
* Read a file
* Append data to a file
* Check whether a file exists

**Module Used:**

```python
os
```

Python's built-in `open()` function is used for reading and writing files.

---

### 6. 🔍 Module Explorer

The project also includes a simple module explorer using Python's:

```python
dir()
```

The user can explore available attributes and functions of:

* `math`
* `random`
* `datetime`
* `uuid`
* `time`

Example:

```python
print(dir(math))
```

---

## 🖥️ Main Menu

When the program starts, the following menu is displayed:

```text
==========================================
       WELCOME TO MULTI-UTILITY TOOLKIT
==========================================

1. Date and Time Operations
2. Mathematical Operations
3. Random Data Generation
4. Generate Unique ID (UUID)
5. File Operations
6. Explore Module using dir()
7. Exit
```

The user selects an option and can perform the required operation.

---

## 🛠️ Technologies Used

| Technology | Purpose                   |
| ---------- | ------------------------- |
| Python     | Main programming language |
| datetime   | Date and time operations  |
| time       | Countdown timer           |
| math       | Mathematical calculations |
| random     | Random data generation    |
| string     | Password characters       |
| uuid       | Unique ID generation      |
| os         | File existence checking   |
| `dir()`    | Module exploration        |

---

## 📂 Project Structure

A simple version of the project can be organized as:

```text
Multi-Utility-Toolkit/
│
├── multi_utility_toolkit.py
│
└── README.md
```

If the project is later divided into multiple modules/packages, it can be organized like:

```text
Multi-Utility-Toolkit/
│
├── main.py
├── modules/
│   ├── date_time.py
│   ├── mathematics.py
│   ├── random_data.py
│   ├── uuid_generator.py
│   └── file_operations.py
│
├── README.md
└── requirements.txt
```

The current version works as a **single Python file**.

---

## ⚙️ Requirements

You only need:

* Python 3.x
* Any Python IDE or code editor

Recommended:

* VS Code
* PyCharm
* IDLE
* Jupyter Notebook (for learning/testing)

No external libraries are required because the project uses Python's built-in modules.

---

## 🚀 How to Run

### Step 1: Install Python

Install Python 3.x on your computer.

Check the installation:

```bash
python --version
```

or:

```bash
py --version
```

---

### Step 2: Download or Clone the Repository

Clone the project:

```bash
git clone <your-github-repository-url>
```

Move into the project folder:

```bash
cd Multi-Utility-Toolkit
```

---

### Step 3: Run the Program

Run:

```bash
python multi_utility_toolkit.py
```

or on Windows:

```bash
py multi_utility_toolkit.py
```

---

## 💡 Example Usage

### Current Date and Time

```text
----- DATE AND TIME OPERATIONS -----

1. Current Date and Time
2. Difference Between Two Dates
3. Format Current Date
4. Countdown Timer
5. Back to Main Menu

Enter your choice: 1

Current Date and Time:
2026-10-03 12:00:00
```

---

### Mathematical Operation

```text
----- MATHEMATICAL OPERATIONS -----

1. Factorial
2. Compound Interest
3. Circle Area
4. Rectangle Area
5. Trigonometry
6. Square Root
7. Back to Main Menu

Enter your choice: 1

Enter a number: 5

Factorial: 120
```

---

### Random Password

```text
Enter your choice: 3

Enter password length: 10

Generated Password: aB7@kP2$xQ
```

---

### UUID Generation

```text
----- UUID GENERATOR -----

Generated UUID:
550e8400-e29b-41d4-a716-446655440000
```

---

## 🧠 Python Concepts Demonstrated

This project helps practice several important Python concepts:

### Functions

Each major feature is separated into a function.

```python
def mathematical_operations():
    ...
```

### Loops

`while` loops are used to keep menus running until the user chooses to go back.

```python
while True:
    ...
```

### Conditional Statements

`if`, `elif`, and `else` are used for menu selection.

```python
if choice == "1":
    ...
elif choice == "2":
    ...
else:
    ...
```

### User Input

The program accepts input using:

```python
input()
```

### File Handling

Files are opened using:

```python
with open(file_name, "r") as file:
    data = file.read()
```

### Exception-Prone Operations

The project works with operations such as:

* Date conversion
* Integer conversion
* Floating-point conversion
* File access
* Mathematical calculations

Input validation can be added as a future improvement.

### `dir()` Function

The project demonstrates how `dir()` can be used to inspect module attributes.

```python
print(dir(math))
```

### `__name__ == "__main__"`

The program uses:

```python
if __name__ == "__main__":
    main()
```

This ensures that the main program starts when the Python file is executed directly.

---

## 📦 Modules Used

### `datetime`

Used for working with dates and times.

```python
datetime.datetime.now()
```

### `time`

Used for the countdown timer.

```python
time.sleep(1)
```

### `math`

Used for mathematical operations.

```python
math.factorial()
math.sqrt()
math.pi
math.sin()
```

### `random`

Used to generate random values.

```python
random.randint()
random.choice()
random.sample()
```

### `string`

Used to provide characters for password generation.

```python
string.ascii_letters
string.digits
```

### `uuid`

Used to generate unique identifiers.

```python
uuid.uuid4()
```

### `os`

Used to check whether a file exists.

```python
os.path.exists(file_name)
```

---

## 🔄 Program Flow

```text
Start
  ↓
Main Menu
  ↓
Select Operation
  ↓
┌──────────────────────────────┐
│ Date & Time                  │
│ Mathematics                  │
│ Random Data                  │
│ UUID                         │
│ File Operations              │
│ Module Explorer              │
└──────────────────────────────┘
  ↓
Perform Operation
  ↓
Return to Main Menu
  ↓
Exit
```

---

## 🔐 Security Note

The generated password and OTP features are intended for **learning and demonstration purposes**.

The project uses Python's `random` module. For security-sensitive password or authentication systems, a cryptographically secure approach such as Python's `secrets` module should be used instead.

---

## 🚧 Limitations

The current version is a learning project and has some limitations:

* Limited input validation
* Invalid date formats can cause errors
* Invalid numeric input can cause errors
* Negative values are not fully validated
* Password generation is for demonstration
* The dice game does not validate that the user's number is between 1 and 6
* File paths are entered directly by the user

---

## 🔮 Future Improvements

Possible improvements include:

* Add `try-except` error handling
* Add stronger input validation
* Add a graphical user interface using Tkinter
* Add more mathematical operations
* Add currency conversion
* Add temperature conversion
* Add stronger password generation using `secrets`
* Add file deletion and rename options
* Divide the project into separate Python modules
* Create a proper Python package
* Add automated tests
* Add logging functionality
* Add configuration files

---

## 📚 Learning Outcomes

After completing this project, you can understand:

* How to import Python modules
* How built-in modules work
* How to organize functionality using functions
* How menu-driven programs work
* How to perform file operations
* How to generate random data
* How to create UUIDs
* How to use `dir()` for module exploration
* How to use `__name__` and `__main__`
* How modules can be organized into larger Python projects

---

## 👨‍💻 Author

**Dharmendra Rajput**

Python Learner | Aspiring Data Analyst

---

## 📄 License

This project is created for **educational and learning purposes**.

You are free to study, modify, and improve the project.

---

## ⭐ If You Like This Project

If this project helped you learn Python modules and packages, consider giving the repository a ⭐ on GitHub.
