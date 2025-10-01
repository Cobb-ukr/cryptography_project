import base64
import os
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC

def encrypt(text_to_encrypt: str, password: str) -> str:
    """
    Encrypts the given text using a password.
    Returns a base64-encoded string containing salt + ciphertext.
    """
    password_bytes = password.encode()
    salt = os.urandom(16)  # Random salt

    # Derive key from password and salt
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password_bytes))

    # Encrypt
    cipher = Fernet(key)
    encrypted_text = cipher.encrypt(text_to_encrypt.encode())

    # Combine salt + ciphertext and return as base64 string
    output = base64.urlsafe_b64encode(salt + encrypted_text)
    return output.decode()


def decrypt(encrypted_input: str, password: str) -> str:
    """
    Decrypts the given base64-encoded string using the password.
    Returns the original plaintext.
    """
    password_bytes = password.encode()
    decoded_data = base64.urlsafe_b64decode(encrypted_input)
    salt = decoded_data[:16]         # Extract salt
    ciphertext = decoded_data[16:]   # Extract encrypted text

    # Derive key using the same password and salt
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100_000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password_bytes))

    # Decrypt
    cipher = Fernet(key)
    decrypted_text = cipher.decrypt(ciphertext).decode()
    return decrypted_text
