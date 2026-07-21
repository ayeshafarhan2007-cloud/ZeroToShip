from models.component import Component

# Create a Component object
component = Component(1, "Arduino Uno", "Ayesha")

# Convert object to dictionary
component_dict = component.to_dict()

print("Dictionary:")
print(component_dict)

# Convert dictionary back to object
new_component = Component.from_dict(component_dict)

print("\nNew Component Object:")
print(f"ID: {new_component.id}")
print(f"Name: {new_component.name}")
print(f"Owner: {new_component.owner}")
print(f"Status: {new_component.status}")