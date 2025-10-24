# python_fundamentals

## Purpose

> This repository serves as a collection of notes, code examples, and practice exercises completed to master the **python** programming language. The primary goal is to quickly learn the Python **syntax**, **standard library** features, and **paradigms** (procedural and object-oriented) while transitioning from a **C/C++** background.

## Explanation of Learned Concepts

This project covers fundamental Python concepts essential for scripting, data processing, and object-oriented design.

### Core Data Structures and Types
Python's data types are powerful and flexible, often abstracting complexities found in C/C++ (like manual memory management or fixed-size arrays).

| Concept | Description | C/C++ Analogy |
| :--- | :--- | :--- |
| **Integers (`int`) & Floats (`float`)** | Standard numerical types, supporting arbitrary precision integers. | `int`, `long long`, `float`, `double` |
| **Strings (`str`)** | Immutable sequences of Unicode characters, supporting extensive built-in methods for manipulation. | `char*`, `std::string` |
| **Boolean (`bool`)** | Logical values (`True`/`False`), used extensively in control flow. | `bool` |
| **Lists (`list`)** | Mutable, ordered sequences of heterogeneous elements (dynamic arrays). | `std::vector` (but more flexible) |
| **Tuples (`tuple`)** | Immutable, ordered sequences of heterogeneous elements (fixed-size records). | `struct` or a fixed-size `std::array` |
| **Dictionaries (`dict`)** | Mutable collections of unique key:value pairs, optimized for retrieval. | `std::map`, `std::unordered_map` |

### Control Flow and Functions
Python's approach to conditions and loops emphasizes readability and simplified syntax.

* **Conditional Statements (`if`/`elif`/`else`):** Used for branching logic. Blocks are defined by **indentation**, not braces (`{}`).
* **While Loops:** Execute a block of code repeatedly as long as a condition is `True`.
* **For Loops:** Primarily used for **iterating** over elements in any iterable (like lists, tuples, or strings), rather than index-based counting (though index-based loops can be implemented).
* **Functions (`def`):** Defined using the `def` keyword. They are **first-class objects**, meaning they can be passed as arguments or returned from other functions.

## 💻 Key Paradigms and Features

The tutorial progresses into advanced topics crucial for building larger applications.

### Object-Oriented Programming (OOP)
Python implements OOP using a class-based system, often with simpler syntax than C++.

* **Classes (`class`):** Blueprints for creating objects, supporting inheritance.
* **Methods:** Functions defined within a class. The first parameter is conventionally **`self`**, which references the instance of the object.
* **Constructor (`__init__`)**: A special method called when a new object is created, used for initialization.

### Modules and Standard Library
Python heavily relies on **modules** (files containing Python code) for code organization and reusability.

* **Modules & Imports:** The **`import`** statement is used to bring functionality from external files or the standard library into the current scope.
* **Standard Library:** A vast collection of modules providing ready-to-use tools for file I/O, math, system interaction, and more.

### Error Handling
Python uses a robust mechanism for handling runtime errors.

* **Exceptions (`try`/`except`):** Instead of checking return codes for every function call (common in C), Python uses a `try...except` block to gracefully catch and handle errors (**exceptions**) at the point where they occur, preventing program crashes.

## 📂 Repository Structure

The files are organized by the core concept or module they explore.

```
.
├── python_tutorial/
│ ├── ex00/
│ │ ├── datatypes.py             # Basics: int, float, boolean, and casting
│ │ ├── EUR_BARTH_coverter.py    # Example calculation/variable usage
│ │ └── kino_ticket.py           # Simple conditional logic or calculation
│ ├── ex01/
│ │ ├── dict.py                  # Dictionaries implementation
│ │ ├── lists.py                 # Lists, list methods, and mutability
│ │ └── tuple.py                 # Tuples and their immutability
│ └── ex02/
│ ├── riddle.py                  # A short programming riddle/challenge
│ ├── shopping_list.py           # Practical exercise, using lists/loops
│ └── while.py                   # While loop examples
└── README.md
````

## 🚀 Execution

All files in this repository are standard Python scripts.

To run any script:

```bash
python <filename>.py
````

### Requirements

1.  **Python 3:** Ensure Python 3 is installed.
2.  **IDE:** An IDE like PyCharm is recommended for development but I used VS Code.

-----

## 🔗 Tutorial Reference

This project is based on the comprehensive Python Tutorial by **Daniel Rappert**.

  * [[Link to free Tutorial]](https://www.youtube.com/watch?v=e6vPt_e9sRw&t=9458s)

## License

This repository is for personal learning and educational purposes only.
