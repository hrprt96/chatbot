import onetimepad

def encrypted_text(username,password):
    cipher = onetimepad.encrypt(password, username)
    return cipher

def decrypted_text(username,cipher_txt):
    text = onetimepad.decrypt(cipher_txt, username)
    return text
