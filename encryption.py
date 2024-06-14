"""
File: encryption.py
-------------------
Encrypt a password using a master password
"""

def main():
  input_pwd = input("Input your normal password to be encrypt: ")
  master_pwd = input("What's your master password? ")
  encrypted_pwd = "password"
  print(f"Your encrypted password is {encrypted_pwd}. Keep your master password safe for future decryption")

def encrypt(input_pwd, master_pwd):
  pass