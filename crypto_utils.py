# crypto_utils.py

import re
import os
from cryptography.fernet import Fernet

# Load or generate key
FERNET_KEY = os.getenv("FERNET_KEY")
if not FERNET_KEY:
    FERNET_KEY = Fernet.generate_key().decode()
    print(f"Generated Fernet Key (store this safely!): {FERNET_KEY}")

fernet = Fernet(FERNET_KEY.encode())

# Pattern to match 4-digit numbers
FOUR_DIGIT_PATTERN = re.compile(r"\b\d{4}\b")

def encrypt_4digit_numbers(text: str) -> str:
    def _encrypt(match):
        plaintext = match.group(0)
        encrypted = fernet.encrypt(plaintext.encode()).decode()
        return f"[ENCRYPTED:{encrypted}]"

    return FOUR_DIGIT_PATTERN.sub(_encrypt, text)
