import secrets

# Generate a secure secret key with 32 bytes (256 bits)
secret_key = secrets.token_hex(32)

print(secret_key)
