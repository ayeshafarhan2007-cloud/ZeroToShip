print("Program started")

from models.component import Component
from services.storage import save_components, load_components

print("Imports successful")

component1 = Component(1, "Arduino Uno", "Ayesha", "Available")
component2 = Component(2, "Raspberry Pi", "Ali", "Borrowed")

components = [component1, component2]

print("Saving components...")
save_components(components)

print("Loading components...")
loaded_components = load_components()

print("Loaded Components:")
for component in loaded_components:
    print(component.to_dict())

print("Program finished")