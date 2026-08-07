# Phase 1 – Component Data Model

## Project Overview

This phase focuses on building the core data model for the Lab-Share application. The goal is to represent lab equipment as Python objects and implement serialization methods to convert objects to and from dictionaries.

## Objective

- Create a `Component` class.
- Store equipment information using object-oriented programming.
- Implement serialization and deserialization methods.
- Verify functionality through manual testing.

## Features

- Component class with:
  - ID
  - Name
  - Owner
  - Status (default: Available)
- `to_dict()` method
- `from_dict()` class method
- Manual testing script

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Git & GitHub

## Folder Structure

```
Phase-1/
│
├── models/
│   └── component.py
│
├── Output/
│
├── manual_test.py
│
└── README.md
```

## How to Run

1. Open the terminal.
2. Navigate to the `Phase-1` folder.
3. Run:

```bash
python manual_test.py
```

## Expected Output

```
Dictionary:
{'id': 1, 'name': 'Arduino Uno', 'owner': 'Ayesha', 'status': 'Available'}

New Component Object:
ID: 1
Name: Arduino Uno
Owner: Ayesha
Status: Available
```

## Status

✅ Phase 1 implementation completed successfully.git status