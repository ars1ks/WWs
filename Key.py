import random
import hashlib

def generate_key():
    key_length = 20 
    key = "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!№@;%:?*") for _ in range(key_length))
    return key

def hash_key(key, algorithm="sha256"):
    hasher = hashlib.new(algorithm)
    hasher.update(key.encode("utf-8"))
    return hasher.hexdigest()

def main():
    key = generate_key()
    print(f"Сгенерированный ключ: {key}")

    hashed_key = hash_key(key)
    print(f"Хешированный ключ (SHA-256): {hashed_key}")

if __name__ == "__main__":
    main()
