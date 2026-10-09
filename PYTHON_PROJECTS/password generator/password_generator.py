import secrets
import string


def generate_password(length=12):
  # Combine letters, digits, and punctuation symbols
  alphabet = string.ascii_letters + string.digits + string.punctuation

  # Generate a secure random password of the specified length
  password = "".join(secrets.choice(alphabet) for _ in range(length))

  return password


# Example usage: Generate a 16-character password
if __name__ == "__main__":
  new_password = generate_password(16)
  print(f"Generated Password: {new_password}")
