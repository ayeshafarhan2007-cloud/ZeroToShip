from services.auth import login, logout, is_logged_in, can_modify

print("=== Authentication Test ===")

print("\nChecking login status...")
print(is_logged_in())

print("\nLogging in...")
login("Ayesha")

print("\nChecking login status...")
print(is_logged_in())

print("\nChecking modification access...")
if can_modify():
    print("Component update allowed.")
else:
    print("Access denied.")

print("\nLogging out...")
logout()

print("\nChecking login status...")
print(is_logged_in())

print("\nChecking modification access...")
if can_modify():
    print("Component update allowed.")
else:
    print("Access denied.")