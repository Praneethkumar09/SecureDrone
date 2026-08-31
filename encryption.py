from cryptography.fernet import Fernet
import os


KEY_FILE = "data/secret.key"


def generate_key():

    if not os.path.exists(KEY_FILE):

        key = Fernet.generate_key()

        with open(KEY_FILE, "wb") as file:
            file.write(key)

        print("Encryption key created.")


def load_key():

    generate_key()

    with open(KEY_FILE, "rb") as file:
        return file.read()


def encrypt_data(data):

    key = load_key()

    cipher = Fernet(key)

    encrypted = cipher.encrypt(
        data.encode()
    )

    return encrypted.decode()


def decrypt_data(encrypted_data):

    key = load_key()

    cipher = Fernet(key)

    decrypted = cipher.decrypt(
        encrypted_data.encode()
    )

    return decrypted.decode()


if __name__ == "__main__":

    original_data = "14.6819,77.6006,120,35,82"

    print("\nOriginal Drone Data:")
    print(original_data)

    encrypted = encrypt_data(original_data)

    print("\nEncrypted Drone Data:")
    print(encrypted)

    decrypted = decrypt_data(encrypted)

    print("\nDecrypted Drone Data:")
    print(decrypted)