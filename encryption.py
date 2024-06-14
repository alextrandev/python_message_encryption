"""
File: encryption.py
-------------------
Encrypt a password using a master password
"""

CHARACTERS = ['a', 'o', '3', 'b', 'p', 'L', 'e', 'u', 'k', 'G', 'q', 'f', 'N', 'j', 'W', 'X', '8', '6', '9', 'F', 'J', 'S', 's', '7', 'm', 'P', 'D', '2', 'I', 'E', 'C', 'K', '5', '0', 'R', 'd', 'h', 'H', 'n', 'r', 'B', 'V', 'T', 'c', 'v', 'Y', 'i', 'g', 'y', 'Q', 'M', 'A', 'U', '1', 't', 'z', 'w', 'Z', 'x', 'O', '4', 'l']

def main():
  input_pwd = input("Input your normal password to be encrypt: ")
  master_pwd = input("What's your master password? ")
  encrypted_pwd = encrypt(input_pwd, master_pwd)
  print(f"Your encrypted password is {encrypted_pwd}. Keep your master password safe for future decryption")

def encrypt(input_pwd, master_pwd):
  master_pwd_values =  map_to_value(master_pwd)
  input_pwd_values = map_to_value(input_pwd)
  encrypted_pwd_values = combine_values(input_pwd_values, master_pwd_values)
  encrypted_pwd = map_to_char(encrypted_pwd_values)
  return encrypted_pwd

def map_to_value(string):
  return list(map(lambda i: CHARACTERS.index(i), string)) 

def map_to_char(array):
  return ''.join(map(lambda i: CHARACTERS[i], array))

def combine_values(values, master_values):
  return list(map(
    lambda i: (values[i] + master_values[i % len(master_values)]) % len(CHARACTERS),
    range(len(values))
  ))

__name__ == "__main__" and main()