import re

def is_valid(username):
    # 1-30 chars, only letters, numbers, underscores, periods
    # Cannot start/end with period, no consecutive periods
    if not re.match(r'^[A-Za-z0-9._]{1,30}$', username):
        return False
    if username.startswith('.') or username.endswith('.'):
        return False
    if '..' in username:
        return False
    return True

def is_strong(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r"[0-9]", password):
        return False, "Password must contain at least one digit."
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        return False, "Password must contain at least one special character."
    return True, ""