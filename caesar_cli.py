#!/usr/bin/env python3
"""
Caesar Cipher CLI
Algorithm used: Caesar Cipher (a substitution cipher that shifts each letter
by a fixed number of positions in the alphabet).
"""

import sys

ALGORITHM = "Caesar Cipher"


def shift_text(text: str, shift: int) -> str:
    """Shift letters by `shift` positions. Non-letters are left unchanged."""
    result = []
    for ch in text:
        if ch.isascii() and ch.isalpha():
            base = ord("A") if ch.isupper() else ord("a")
            result.append(chr((ord(ch) - base + shift) % 26 + base))
        else:
            result.append(ch)
    return "".join(result)


def encrypt(plain_text: str, key: int) -> str:
    return shift_text(plain_text, key)


def decrypt(cipher_text: str, key: int) -> str:
    return shift_text(cipher_text, -key)


def ask_key() -> int:
    while True:
        raw = input("Enter the key (shift, a whole number, e.g. 3): ").strip()
        try:
            return int(raw)
        except ValueError:
            print("Invalid key. Please enter a whole number.")


def banner() -> None:
    print("=" * 46)
    print(f"  Text Encryption / Decryption Tool")
    print(f"  Algorithm: {ALGORITHM}")
    print("=" * 46)


def menu() -> None:
    print("\n1. Encrypt text")
    print("2. Decrypt text")
    print("3. Exit")


def main() -> None:
    banner()
    while True:
        menu()
        choice = input("Choose an option (1-3): ").strip()

        if choice == "1":
            text = input("Enter plain text: ")
            key = ask_key()
            print(f"\nEncrypted text ({ALGORITHM}, key={key}):")
            print(encrypt(text, key))
        elif choice == "2":
            text = input("Enter cipher text: ")
            key = ask_key()
            print(f"\nDecrypted text ({ALGORITHM}, key={key}):")
            print(decrypt(text, key))
        elif choice == "3":
            print("Goodbye!")
            sys.exit(0)
        else:
            print("Invalid option. Please choose 1, 2 or 3.")


if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nGoodbye!")