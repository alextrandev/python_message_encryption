"""
File: decryption.py
-------------------
Decrypt an encrypted message with a master password
"""

CHARACTERS = ['a', 'o', '3', 'b', 'p', 'L', 'e', ' ', 'u', 'k', 'G', 'q', 'f', 'N', 'j', 'W', 'X', '8', '6', '9', 'F', 'J', 'S', 's', '7', 'm', 'P', 'D', '2', 'I', 'E', 'C', 'K', '5', '0', 'R', 'd', 'h', 'H', 'n', 'r', 'B', 'V', 'T', 'c', 'v', 'Y', 'i', 'g', 'y', 'Q', 'M', 'A', 'U', '1', 't', 'z', 'w', 'Z', 'x', 'O', '4', 'l']

def main():
  input_msg = input("Input your encrypted message: ")
  master_pwd = input("What's your master password? ")
  decrypted_msg = decrypt(input_msg, master_pwd)
  print(f"Your original message is {decrypted_msg}")

def decrypt(input_msg, master_pwd):
  master_pwd_values =  map_to_value(master_pwd)
  input_msg_values = map_to_value(input_msg)
  decrypted_msg_values = subtract_values(input_msg_values, master_pwd_values)
  decrypted_msg = map_to_char(decrypted_msg_values)
  return decrypted_msg

def map_to_value(string):
  return list(map(lambda i: CHARACTERS.index(i), string)) 

def map_to_char(array):
  return ''.join(map(lambda i: CHARACTERS[i], array))

def subtract_values(values, master_values):
  return list(map(
    lambda i: (values[i] - master_values[i % len(master_values)]) % len(CHARACTERS),
    range(len(values))
  ))

__name__ == "__main__" and main()