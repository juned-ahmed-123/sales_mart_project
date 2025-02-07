import base64
from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import PBKDF2
import sys

from resources.dev import config

# Manually define key, iv, and salt
# key = 'mysecretkey12345'  # 16, 24, or 32 bytes depending on AES key size (e.g., AES-128 uses 16 bytes)
# iv = 'myinitialvector12'  # Should be 16 bytes for AES CBC mode
# salt = 'somesaltvalue123'  # Salt should be at least 8 bytes, but can be longer
key = config.key
iv = config.iv
salt = config.salt
BS = 16

# Padding and unpadding functions
pad = lambda s: bytes(s + (BS - len(s) % BS) * chr(BS - len(s) % BS), 'utf-8')
unpad = lambda s: s[0:-ord(s[-1:])]

def get_private_key():
    """Generate a 32-byte key using PBKDF2 from the provided key and salt."""
    Salt = salt.encode('utf-8')
    kdf = PBKDF2(key, Salt, 64, 1000)
    key32 = kdf[:32]  # Use the first 32 bytes of the derived key
    return key32

def get_valid_iv(iv):
    """Ensure the IV is 16 bytes long for AES CBC mode."""
    iv = iv.encode('utf-8')
    if len(iv) != 16:
        iv = iv.ljust(16, b'\0')  # Pad to 16 bytes if it's shorter
    elif len(iv) > 16:
        iv = iv[:16]  # Truncate to 16 bytes if it's longer
    return iv

def encrypt1(raw):
    """Encrypt the raw data using AES CBC."""
    print(raw)
    raw = pad(raw)
    iv_valid = get_valid_iv(iv)  # Ensure IV is 16 bytes long
    cipher = AES.new(get_private_key(), AES.MODE_CBC, iv_valid)
    return base64.b64encode(cipher.encrypt(raw))

def decrypt(enc):
    """Decrypt the encoded data using AES CBC."""
    iv_valid = get_valid_iv(iv)  # Ensure IV is 16 bytes long
    # cipher = AES.new(get_private_key(), AES.MODE_CBC, iv_valid)
    cipher = AES.new(get_private_key(), AES.MODE_CBC, iv.encode('utf-8'))
    return unpad(cipher.decrypt(base64.b64decode(enc))).decode('utf8')


# Example usage:
raw_data = "This is a secret message."
encrypted_data = encrypt1(raw_data)
print(f"Encrypted: {encrypted_data}")

decrypted_data = decrypt(encrypted_data)
print(f"Decrypted: {decrypted_data}")

# import base64
# from Cryptodome.Cipher import AES
# from Cryptodome.Protocol.KDF import PBKDF2
# import os, sys
# from resources.dev import config
# # from logging_config import logger
#
# try:
#     key = config.key
#     iv = config.iv
#     salt = config.salt
#
#     if not (key and iv and salt):
#         raise Exception(F"Error while fetching details for key/iv/salt")
# except Exception as e:
#     print(f"Error occured. Details : {e}")
#     # logger.error("Error occurred. Details: %s", e)
#     sys.exit(0)
#
# BS = 16
# pad = lambda s: bytes(s + (BS - len(s) % BS) * chr(BS - len(s) % BS), 'utf-8')
# unpad = lambda s: s[0:-ord(s[-1:])]
#
# def get_private_key():
#     Salt = salt.encode('utf-8')
#     kdf = PBKDF2(key, Salt, 64, 1000)
#     key32 = kdf[:32]
#     return key32
#
#
# def encrypt1(raw):
#     print(raw)
#     raw = pad(raw)
#     cipher = AES.new(get_private_key(), AES.MODE_CBC, iv.encode('utf-8'))
#     return base64.b64encode(cipher.encrypt(raw))
#
#
# def decrypt(enc):
#     cipher = AES.new(get_private_key(), AES.MODE_CBC, iv.encode('utf-8'))
#     return unpad(cipher.decrypt(base64.b64decode(enc))).decode('utf8')

# import os
# import base64
# from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
# from cryptography.hazmat.primitives import hashes
# from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
# from cryptography.hazmat.backends import default_backend
# from cryptography.hazmat.primitives.padding import PKCS7
# from resources.dev.config import Access0_key, Secret_access_key
#
# # Generate random salt and IV (Initialization Vector)
# salt = os.urandom(16)
# iv = os.urandom(16)
#
# print(f"Salt: {salt.hex()} (Save securely)")
# print(f"IV: {iv.hex()} (Save securely)")
#
#
# def derive_key(password: str, salt: bytes) -> bytes:
#     """Derive a cryptographic key from a password and salt using PBKDF2."""
#     kdf = PBKDF2HMAC(
#         algorithm=hashes.SHA256(),
#         length=32,  # AES-256 key size
#         salt=salt,
#         iterations=100000,
#         backend=default_backend()
#     )
#     return kdf.derive(password.encode())
#
#
# def encrypt_data(data: str, key: bytes, iv: bytes) -> bytes:
#     """Encrypt data using AES-CBC with PKCS7 padding."""
#     padder = PKCS7(128).padder()
#     padded_data = padder.update(data.encode()) + padder.finalize()
#     cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
#     encryptor = cipher.encryptor()
#     return encryptor.update(padded_data) + encryptor.finalize()
#
#
# def decrypt_data(encrypted_data: bytes, key: bytes, iv: bytes) -> str:
#     """Decrypt AES-CBC encrypted data."""
#     cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
#     decryptor = cipher.decryptor()
#     decrypted_padded = decryptor.update(encrypted_data) + decryptor.finalize()
#
#     unpadder = PKCS7(128).unpadder()
#     decrypted_data = unpadder.update(decrypted_padded) + unpadder.finalize()
#     return decrypted_data.decode()
#
#
# # Password for encryption/decryption
# password = "sufyan"
# encryption_key = derive_key(password, salt)
#
# print(f"Derived Key (Base64): {base64.b64encode(encryption_key).decode()}")
#
# # Encrypt AWS credentials
# encrypted_access_key = encrypt_data(Access0_key, encryption_key, iv)
# encrypted_secret_key = encrypt_data(Secret_access_key, encryption_key, iv)
#
# print("AWS Credentials Encrypted Successfully")
#
# # Save salt, IV, and encrypted credentials
# with open("salt_iv.key", "wb") as f:
#     f.write(salt + iv)
# with open("aws_credentials.enc", "wb") as f:
#     f.write(encrypted_access_key + b"\n" + encrypted_secret_key)
#
# print("Encrypted data saved.")
#
# # Load salt and IV for decryption
# with open("salt_iv.key", "rb") as f:
#     saved_data = f.read()
#     saved_salt, saved_iv = saved_data[:16], saved_data[16:]
#
# decryption_key = derive_key(password, saved_salt)
#
# # Load encrypted credentials
# with open("aws_credentials.enc", "rb") as f:
#     encrypted_lines = f.readlines()
#
# decrypted_access_key = decrypt_data(encrypted_lines[0].strip(), decryption_key, saved_iv)
# decrypted_secret_key = decrypt_data(encrypted_lines[1].strip(), decryption_key, saved_iv)
#
# print("Decrypted AWS Credentials:")
# print(f"Access Key: {decrypted_access_key}")
# print(f"Secret Key: {decrypted_secret_key}")