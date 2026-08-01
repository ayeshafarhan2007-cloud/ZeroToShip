# Phase 4 – Terminal User Interface

## Project Overview

This phase focuses on building the presentation layer of the Lab-Share application using a terminal-based interface. The interface uses hardcoded mock data to display lab equipment and their availability without connecting to the backend.

## Objective

- Create a clean terminal interface.
- Display a menu using ASCII borders.
- Show mock component data.
- Highlight component status using colored labels.

## Features

- Clear terminal screen
- ASCII menu layout
- Component list display
- Green **[Available]** status
- Red **[Borrowed]** status
- Hardcoded mock data

## Technologies Used

- Python 3
- Built-in `os` module
- ANSI color codes

## Folder Structure

```
Phase-4/
│
├── services/
│   └── cli_display.py
├── Output/
│   └── cli_display_output.png
└── README.md
```

## How to Run

```bash
python services/cli_display.py
```

## Status

✅ Phase 4 completed successfully.