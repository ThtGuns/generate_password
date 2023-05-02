import secrets
import string

def generate_password(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(letters) for i in range(length))

def protect_password(password):
    password = password[::-1]
    password = ''.join([chr(ord(c)+1) for c in password])
    return password

def verify_password(password, protected_password):
    password = ''.join([chr(ord(c)-1) for c in password])
    password = password[::-1]
    return password == protected_password

secure_password = generate_password(7)
protected_password = protect_password(secure_password)
print(f"Mot de passe sécurisé : {protected_password}")