from pwdlib import PasswordHash

password_hash = PasswordHash.recommended()

#hash_password() converts a plain-text password into a secure hash before storage.
def hash_password(password: str) -> str:
    return password_hash.hash(password)

#verify_password() checks a submitted password against its stored hash.
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return password_hash.verify(plain_password, hashed_password)