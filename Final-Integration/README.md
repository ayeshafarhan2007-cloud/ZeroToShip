# Lab-Share

A simple command-line application that helps manage lab equipment. Users can view available components, borrow them, return them, and save changes using JSON storage.

## Features

- View all lab components
- Borrow a component
- Return a component
- Persistent JSON storage
- Simple command-line interface
- Input validation for invalid menu choices and component IDs

## Technologies Used

- Python 3
- Object-Oriented Programming (OOP)
- JSON
- Command Line Interface (CLI)

## Project Structure

```
Final-Integration/
│
├── app.py
├── gear.json
├── README.md
├── models/
│   └── component.py
├── services/
│   ├── auth.py
│   ├── cli_display.py
│   ├── registry_core.py
│   └── storage.py
└── Output/
```

## How to Run

1. Open the project in VS Code.
2. Navigate to the Final-Integration folder.
3. Run:

```bash
python app.py
```

## How to Test

1. View the list of components.
2. Borrow a component by entering its ID.
3. Exit the application.
4. Run the application again to verify the component status was saved.
5. Return the component and verify the status updates correctly.

## Author

Ayesha Khan