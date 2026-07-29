# Phase 3 – Component Status Management & JSON Storage

## Project Overview

This phase focuses on managing component status safely and storing component data permanently using JSON files. The project ensures that components can only change status according to defined rules and that all data can be saved and loaded from a local file.

## Objective

- Build secure component status transition functions.
- Save component data to a JSON file.
- Load component data from a JSON file.
- Test the functionality through a Python script.

## Features

- Borrow component functionality
- Return component functionality
- Save components using `json.dump()`
- Load components using `json.load()`
- Error handling for missing or invalid JSON files

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON
- Git & GitHub

## Folder Structure

```
Phase-3/
│
├── gear.json
├── models/
│   └── component.py
├── services/
│   ├── registry_core.py
│   └── storage.py
├── Output/
│   └── storage_test_output.png
├── test_storage.py
└── README.md
```

## How to Run

1. Open the terminal.
2. Navigate to the `Phase-3` folder.
3. Run:

```bash
python test_storage.py
```

## Expected Output

The program:

- Saves component data to `gear.json`
- Loads the saved data
- Displays the loaded component information

## Status

✅ Phase 3 implementation completed successfully.