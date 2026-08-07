from services.cli_display import show_menu, display_components
from services.registry_core import borrow_component, return_component
from services.storage import load_components, save_components


def main():
    while True:
        show_menu()

        components = load_components()
        display_components(components)

        choice = input("\nEnter your choice (1-4): ")

        if choice == "1":
            input("\nPress Enter to continue...")

        elif choice == "2":
            try:
                component_id = int(input("Enter Component ID to borrow: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                input("Press Enter to continue...")
                continue

            found = False
            for component in components:
                if component.id == component_id:
                    borrow_component(component)
                    found = True
                    break

            if not found:
                print("Component not found.")

            save_components(components)
            input("\nPress Enter to continue...")

        elif choice == "3":
            try:
                component_id = int(input("Enter Component ID to return: "))
            except ValueError:
                print("Invalid input. Please enter a number.")
                input("Press Enter to continue...")
                continue

            found = False
            for component in components:
                if component.id == component_id:
                    return_component(component)
                    found = True
                    break

            if not found:
                print("Component not found.")

            save_components(components)
            input("\nPress Enter to continue...")

        elif choice == "4":
            print("\nThank you for using Lab Share!")
            break

        else:
            print("\nInvalid choice.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()