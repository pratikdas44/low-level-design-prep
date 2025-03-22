from datetime import datetime

def format_date(date_str: str) -> str:
    """
    Format a date string to a standard format (e.g., "YYYY-MM-DD").
    :param date_str: Input date string.
    :return: Formatted date string.
    """
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%d")
        return date_obj.strftime("%Y-%m-%d")
    except ValueError:
        raise ValueError("Invalid date format. Use 'YYYY-MM-DD'.")

def validate_email(email: str) -> bool:
    """
    Validate an email address.
    :param email: Email address to validate.
    :return: True if valid, False otherwise.
    """
    import re
    regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(regex, email) is not None

def validate_phone(phone: str) -> bool:
    """
    Validate a phone number.
    :param phone: Phone number to validate.
    :return: True if valid, False otherwise.
    """
    import re
    regex = r"^\+?[0-9]{10,15}$"
    return re.match(regex, phone) is not None