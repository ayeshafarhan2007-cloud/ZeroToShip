current_user = None

def login(student_id):
    global current_user
    current_user = student_id
    print(f"Logged in as {student_id}")
    
def logout():
    global current_user
    current_user = None
    print("Logged out successfully.")
    
def is_logged_in():
    return current_user is not None

def can_modify():
    if is_logged_in():
        return True
    return False