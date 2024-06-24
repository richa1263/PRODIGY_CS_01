def cipher(text, shift, mode):
  alphabets = {
      "uppercase": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
      "lowercase": "abcdefghijklmnopqrstuvwxyz"
  }
  result = ""
  for char in text:

    if char in alphabets["uppercase"] or char in alphabets["lowercase"]:

      index = alphabets["uppercase"].index(char) if char in alphabets["uppercase"] else alphabets["lowercase"].index(char)

      if mode == "encrypt":
        index = (index + shift) % 26
      elif mode == "decrypt":
        index = (index - shift) % 26

      result += alphabets["uppercase"][index] if char in alphabets["uppercase"] else alphabets["lowercase"][index]
    else:

      result += char

  return result

original=input("Enter word: ")
print("Original: ",original)

encrypted_text = cipher(original, 3, "encrypt")
print("Encrypted Text: ",encrypted_text)  

decrypted_text = cipher(encrypted_text, 3, "decrypt")
print("Decrypted Text: ",decrypted_text)  
