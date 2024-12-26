import itertools
import string

def brute_force_password(target_password, max_length=4):
    # Define the character set (you can customize this)
    characters = string.ascii_letters + string.digits

    for length in range(1, max_length + 1):
        for attempt in itertools.product(characters, repeat=length):
            attempt = ''.join(attempt)
            print(f"Trying: {attempt}")  # Show the attempt
            if attempt == target_password:
                print(f"Password found: {attempt}")
                return attempt
    print("Password not found.")
    return None

# Example usage
# Uncomment the line below to run
# brute_force_password("abc", max_length=3)