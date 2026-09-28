def require_login(func):
    def wrapper(user_logged_in, *args, **kwargs):
        if not user_logged_in:
            print("Access Denied! Please log in.")
            return
        return func(*args, **kwargs)
    return wrapper

@require_login
def view_dashboard():
    print("Welcome to your dashboard!")

# Test cases
view_dashboard(True)   # Logged in
view_dashboard(False)  # Not logged in
