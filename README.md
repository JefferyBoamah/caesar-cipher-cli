# Text Encryption & Decryption CLI

**Index Number:** 10374466  
**Name:** Boamah Jeffrey

## Encryption Algorithm Used

**Caesar Cipher**: a substitution cipher where each letter in the text is
shifted by a fixed number of positions (the *key*) in the alphabet.

- Encryption: `E(x) = (x + key) mod 26`
- Decryption: `D(x) = (x - key) mod 26`
- Upper/lower case is preserved; digits, spaces and punctuation are unchanged.

Example (key = 3): `Hello, World!` -> `Khoor, Zruog!`

## Requirements

- Python 3.7+
- No external libraries

## How to Run

```bash
python3 caesar_cli.py
```

## Usage

1. Run the program and choose **1** to encrypt or **2** to decrypt.
2. Enter your text.
3. Enter the key (a whole number, e.g. 3).
4. The program prints the result.
5. Choose **3** to exit.

To decrypt, use option 2 with the same key that was used to encrypt.

## Project Structure

```
.
├── caesar_cli.py   # the program
└── README.md
```