def borrow_component(component):
    if component.status == "Available":
        component.status = "Borrowed"
        print("Component borrowed successfully.")
    else:
        print("Component is already borrowed.")


def return_component(component):
    if component.status == "Borrowed":
        component.status = "Available"
        print("Component returned successfully.")
    else:
        print("Component is already available.")