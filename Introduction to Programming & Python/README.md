# Introduction to Programming

## What is Programming?
Programming is the process of giving instructions to a computer so it can perform specific tasks. These instructions are written in a programming language that the computer can interpret and execute.

## Why Python?
Python is a high-level, interpreted programming language that stands out for its simplicity and readability. It’s one of the most beginner-friendly languages, yet powerful enough to be used in advanced applications.

**Python is widely used in many fields, including:**

1. Web Development – Frameworks like Django and Flask make building websites efficient.
2. Data Science and Machine Learning – Libraries such as Pandas, NumPy, and TensorFlow enable powerful data analysis and AI development.
3. Automation and Scripting – Python simplifies repetitive tasks and process automation.
4. Game Development – Tools like Pygame allow developers to create interactive games.

With its large community, extensive library support, and versatility, Python is an excellent starting point for anyone new to programming.


# Installing Python and VS Code

## Installing Python
1. Download Python:

- Visit the official Python website: python.org.
Download the latest version for your operating system (Windows, macOS, or Linux).

2. Install Python:

- Run the installer and ensure you check the box to Add Python to PATH (important for running Python from the command line).

3. Verify Installation:

- Open a terminal or command prompt and type:
``` python
python --version
```
- This should display the installed Python version (e.g., Python 3.13.5).


## Choosing an IDE

**What is an IDE?**

- An Integrated Development Environment (IDE) is a software application that provides tools for writing, testing, and debugging code.

**Popular Python IDEs:**
1. VS Code: Lightweight, customizable, and supports extensions for Python. (We will 2. use this one as our primary IDE)
2. PyCharm: Powerful IDE with advanced features for professional developers.
3. Jupyter Notebook: Great for data science and interactive coding.
4. IDLE: Comes pre-installed with Python; good for beginners.


# Writing Our First Python Program

**The "Hello, World!" Program**
1. Open a folder in your VS code and type the following code in a new file named hello.py:

```python print("Hello, World!") ```

2. Make sure to save the file with a .py extension (e.g., hello.py).
3. Run the program:
  - Use the run button at the top of your IDE or alternatively type this in your VS        Code integrated terminal:
```python python hello.py ```

**Output:**
```python Hello, World! ```

**Key Points:**
  - print() is a built-in function used to display output.
  - Python code is executed line by line.


# Understanding the Python Syntax

## Python Syntax Rules
1. Indentation:

 - Python uses indentation (spaces or tabs) to define blocks of code.
 - Example:
```python
if 5 > 2:
    print("Five is greater than two!") 
    # Spaces before print are called indentation
```

2. Whitespace:

 - Python is sensitive to whitespace. Ensure consistent indentation to avoid errors. Ideally, use 4 spaces for indentation.

3. Statements:

 - Each line of code is a statement. You can write multiple statements on one line using a semicolon (;), but this is not recommended.

4. Comments:

  - Use # for single-line comments.
  - Use ''' or """ for multi-line comments.
  - Example:
```python
# This is a single-line comment
'''
This is a
multi-line comment
'''
```

**Short Notes:**
  - Python is a versatile and beginner-friendly programming language.
  - Setting up Python and choosing the right IDE is the first step to writing code.
  - Python syntax is simple but requires attention to indentation and whitespace.
  - Start with small programs like "Hello, World!" to get comfortable with the basics.
