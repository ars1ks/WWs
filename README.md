# 🔐 HexCrypt: 16x16 Grid Encryption Tool

*A simple yet powerful hex-based cryptographic system for educational purposes.*

---

## 🌟 Features
- **Hex Grid Mapping** — 16x16 grid with shuffled characters.
- **Custom Key Support** — Deterministic shuffling using a secret key 🔑.
- **Shift Offset** — Flexible starting position (0-255).
- **Linear Complexity** — Fast encryption/decryption (O(n)).

---

## 🛠️ Algorithm Overview

### 🔄 Workflow Diagram
Plaintext → [Shuffle Alphabet] → [Hex Grid] → [Encrypt] → Ciphertext (e.g., "0A1B2C")
Ciphertext → [Hex Grid] → [Decrypt] → Plaintext

### 📊 Technical Details
| Component           | Complexity | Description                          |
|---------------------|------------|--------------------------------------|
| Grid Generation     | O(1)       | Fixed 16x16 grid                     |
| Alphabet Shuffling  | O(n)       | n = alphabet length (~100 chars)     |
| Encryption/Decryption | O(m)     | m = message length                   |

---

📊 Performance
Message Length	Encryption Time	Decryption Time
100 chars	         1.2 ms	       0.8 ms
10,000 chars	      110 ms	       95 ms

# 🚀 Quick Start

### Generate a key
- Run key.py
```bash
python key.py
```

- Copy key hash

### Encrypt
- Run encoder.py
```bash
python encoder.py
```

- Enter shift, key, and message

```
Сообщение: test 
 11524B11
```

- Copy encoded message

### Decrypt
- Run decryptor.py
```bash
python decryptor.py
```

```
Введите зашифрованное сообщение: 12382F3019
Расшифрованное сообщение: @LОK7
```

- Enter shift, key, and encrypted message

⚠️ Weaknesses
~~Brute-Force Vulnerable~~ — Only 256 possible shifts.

~~Predictable Seed~~ — Seed = sum(key ASCII values).

📜 License
MIT License | Made with ❤️ by Arsiks

🛠️ How to Contribute
Fork the repository 🍴

Create a branch: git checkout -b feature/amazing-feature

Commit changes: git commit -m "Add amazing feature"

Push: git push origin feature/amazing-feature

Open a Pull Request 🌟
