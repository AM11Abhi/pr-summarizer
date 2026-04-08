def validate_password(password):
    """
    Validate password strength.
    """
    if len(password) < 8:
        return False
    if not any(char.isdigit() for char in password):
        return False
    if not any(char.isupper() for char in password):
        return False
    return True


def hash_password(password):
    """
    Simple hashing (for demo purposes only).
    """
    return hash(password)


def register_user(username, password):
    """
    Register a new user with validation.
    """
    if not validate_password(password):
        raise ValueError("Password is too weak")

    hashed = hash_password(password)

    return {
        "username": username,
        "password": hashed
    }


def login_user(stored_user, username, password):
    """
    Authenticate user login.
    """
    if stored_user["username"] != username:
        return False

    if stored_user["password"] != hash_password(password):
        return False

    return True


if __name__ == "__main__":
    user = register_user("admin", "StrongPass123")

    success = login_user(user, "admin", "StrongPass123")

    if success:
        print("Login successful")
    else:
        print("Login failed")