import os


def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")


def show_menu():
    clear_screen()

    print("+------------------------------------------------+")
    print("|                LAB SHARE SYSTEM                |")
    print("+------------------------------------------------+")
    print("| 1. View Components                             |")
    print("| 2. Borrow Component                            |")
    print("| 3. Return Component                            |")
    print("| 4. Exit                                        |")
    print("+------------------------------------------------+")
    print()


def display_components():
    # Hardcoded mock data (required for Phase 4)
    components = [
        {"name": "Arduino Uno", "status": "Available"},
        {"name": "Raspberry Pi", "status": "Borrowed"},
        {"name": "ESP32", "status": "Available"},
    ]

    print("+------------------------------------------------+")
    print("|               COMPONENT LIST                   |")
    print("+----------------------+-------------------------+")
    print("| Name                 | Status                  |")
    print("+----------------------+-------------------------+")

    for component in components:
        if component["status"] == "Available":
            status = "\033[92m[Available]\033[0m"
        else:
            status = "\033[91m[Borrowed]\033[0m"

        print(f"| {component['name']:<20} | {status:<23}|")

    print("+----------------------+-------------------------+")


def main():
    show_menu()
    display_components()


if __name__ == "__main__":
    main()