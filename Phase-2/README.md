# Phase 2 – Authentication & Session Management

## Project Overview

This phase focuses on implementing a simple authentication system for the Lab-Share application. It manages user login sessions and ensures that only authenticated users can modify component information.

## Objective

- Build a lightweight user session manager.
- Track the currently logged-in user.
- Restrict component modifications without an active session.
- Verify functionality through manual testing.

## Features

- User login functionality
- User logout functionality
- Session status checking
- Access control using a gatekeeper function
- Authentication test script

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- Git & GitHub

## Folder Structure

Phase-2/
│
├── services/
│   └── auth.py
│
├── Output/
│   └── auth_test_output.png
│
├── test_auth.py
│
└── README.md

## How to Run

1. Open the terminal.
2. Navigate to the `Phase-2` folder.
3. Run:

```bash
python test_auth.py