yte = raw_input("Hi. I am the C1 Encrypter. Enter a phrase or word. I will encrypt it.")

encrypt_key = {'A':'F', 'B':'Z', 'C':'B', 'D':'V', 'E':'K', 'F':'I', 'G':'X', 'H':'A', 'I':'Y', 'J':'M', 'K':'E', 'L':'P', 'M':'L', 'N':'S', 'O':'D', 'P':'H', 'Q':'J', 'R':'O', 'S':'R', 'T':'G', 'U':'N', 'V':'Q', 'W':'C', 'X':'U', 'Y':'T', 'Z':'W', ' ': ' ', '.':'.' }

def encrypt(c):
    return encrypt_key[c]

print "Here is the encrypted message:\n"
print map(encrypt, list(yte.upper()))
print "\nUse it carefully. Use the C1 Decrypter to decrypt the message."

