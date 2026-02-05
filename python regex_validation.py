import re

# -----------------------------
# Regex Patterns
# -----------------------------

# Email validation (industry-standard style, practical)
EMAIL_PATTERN = re.compile(
    r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
)

# Indian mobile number validation
# Supports: 9876543210, +919876543210, 0919876543210
MOBILE_PATTERN = re.compile(
    r"^(?:\+91|91|0)?[6-9]\d{9}$"
)

# Password validation
# Rules:
# - Minimum 8 characters
# - At least 1 digit
# - At least 1 special character
# - At least 1 uppercase and 1 lowercase letter
PASSWORD_PATTERN = re.compile(
    r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"
)


# -----------------------------
# Reusable Validation Functions
# -----------------------------

def validate_email(email: str) -> bool:
    if not email:
        return False
    return bool(EMAIL_PATTERN.fullmatch(email))


def validate_mobile(mobile: str) -> bool:
    if not mobile:
        return False
    return bool(MOBILE_PATTERN.fullmatch(mobile))


def validate_password(password: str) -> bool:
    if not password:
        return False
    return bool(PASSWORD_PATTERN.fullmatch(password))


# -----------------------------
# User Interaction Logic
# -----------------------------

def main():
    print("--- REGEX VALIDATION SYSTEM ---")

    email = input("Enter email address: ").strip()
    if validate_email(email):
        print("✓ Email is valid")
    else:
        print("✗ Invalid email format")

    mobile = input("Enter Indian mobile number: ").strip()
    if validate_mobile(mobile):
        print("✓ Mobile number is valid")
    else:
        print("✗ Invalid Indian mobile number")

    password = input("Enter password: ").strip()
    if validate_password(password):
        print("✓ Password is strong")
    else:
        print("✗ Weak password (min 8 chars, digit, upper, lower, special char required)")


# -----------------------------
# Edge Case Testing (Optional)
# -----------------------------

def edge_case_tests():
    test_emails = ["", "user@", "user@gmail", "user@gmail.com"]
    test_mobiles = ["", "12345", "9876543210", "+919876543210"]
    test_passwords = ["", "abc", "Password1", "Password@1"]

    print("\n--- EDGE CASE TESTS ---")

    for e in test_emails:
        print(f"Email '{e}':", validate_email(e))

    for m in test_mobiles:
        print(f"Mobile '{m}':", validate_mobile(m))

    for p in test_passwords:
        print(f"Password '{p}':", validate_password(p))


if __name__ == "__main__":
    main()
    # Uncomment to test edge cases
    # edge_case_tests()
