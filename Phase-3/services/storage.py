import json
from models.component import Component


def save_components(components):
    data = []

    for component in components:
        data.append(component.to_dict())

    with open("gear.json", "w") as file:
        json.dump(data, file, indent=4)


def load_components():
    try:
        with open("gear.json", "r") as file:
            data = json.load(file)

        components = []

        for item in data:
            components.append(Component.from_dict(item))

        return components

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []