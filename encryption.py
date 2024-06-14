"""
File: encryption.py
-------------------
Encrypt a password using a master password
"""

def main():
  print(encrypt("abcdef", "ghijkl"))
  # input_pwd = input("Input your normal password to be encrypt: ")
  # master_pwd = input("What's your master password? ")
  # encrypted_pwd = "password"
  # print(f"Your encrypted password is {encrypted_pwd}. Keep your master password safe for future decryption")

def encrypt(input_pwd, master_pwd):
  characters = ['a', 'o', '3', 'b', 'p', 'L', 'e', 'u', 'k', 'G', 'q', 'f', 'N', 'j', 'W', 'X', '8', '6', '9', 'F', 'J', 'S', 's', '7', 'm', 'P', 'D', '2', 'I', 'E', 'C', 'K', '5', '0', 'R', 'd', 'h', 'H', 'n', 'r', 'B', 'V', 'T', 'c', 'v', 'Y', 'i', 'g', 'y', 'Q', 'M', 'A', 'U', '1', 't', 'z', 'w', 'Z', 'x', 'O', '4', 'l']
  master_pwd_values =  list(map(lambda i: characters.index(i), master_pwd))
  return master_pwd_values

__name__ == "__main__" and main()