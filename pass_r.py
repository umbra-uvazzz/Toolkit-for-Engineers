import re

def check_password_strength(password):

    score = 0
    suggestions = []

    # Length check
    if len(password) >= 12:
        score += 2

    elif len(password) >= 8:
        score += 1

    else:
        suggestions.append("Use at least 8 characters.")

    # Uppercase
    if re.search(r'[A-Z]', password):
        score += 1

    else:
        suggestions.append("Add uppercase letters.")

    # Lowercase
    if re.search(r'[a-z]', password):
        score += 1

    else:
        suggestions.append("Add lowercase letters.")

    # Digits
    if re.search(r'\d', password):
        score += 1

    else:
        suggestions.append("Add numbers.")

    # Special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        score += 1

    else:
        suggestions.append("Add special characters.")

    # Final result
    if score >= 6:
        strength = "💪 Very Strong"

    elif score >= 4:
        strength = "✅ Strong"

    elif score >= 3:
        strength = "⚠️ Moderate"

    else:
        strength = "❌ Weak"

    print(f"\nPassword Strength: {strength}")

    if suggestions:
        print("Suggestions:")
        
        for s in suggestions:
            print(f"- {s}")