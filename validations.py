#!/usr/bin/env python3


def validate_user(username, milen):
    """Checks if the recieved username matches the required conditions."""
    if type(username) != str:
        raise TypeError("username must be a string")
    if milen < 1:
        raise ValueError("milen must be at least 1")
    if len(username) < minlen:
        return False
    if not username.isalnum():
        return False
    # Usernames can't begin with a number
    if username[0].isnumeric():
        return False
    return True