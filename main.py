"""
File: main.py
-------------------
A message encryption/description script which use a master password to hide any message
"""

import encryption
import decryption

def main():
  print("+----------------------------------------------+")
  print("|         Let's encrypt some messages!         |")
  print("+----------------------------------------------+")

  prompt = "0"
  while (prompt != "3"):
    prompt = input("Type 1 to encrypt, 2 to decrypt and 3 to exit: ")
    match prompt:
      case "1":
        encrypt()
      case "2":
        decrypt()
      case "3":
        print("Goodbye!")
        print("------------------------------------------------")
      case _:
        print("Wrong command, try again!")

def encrypt():
  encryption.main()

def decrypt():
  decryption.main()

__name__ == "__main__" and main()