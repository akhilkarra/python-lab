yte = raw_input("Hi. I am the C1 Encrypter. Enter a phrase or word. I will encrypt it.")

encrypt_key = {'A':'H', 'B':'Y', 'C':'P', 'D':'L', 'E':'I', 'F':'J', 'G':'Z', 'H':'Q', 'I':'M', 'J':'V', 'K':'R', 'L':'E', 'M':'N', 'N':'S', 'O':'A', 'P':'G', 'Q':'F', 'R':'U', 'S':'T', 'T':'C', 'U':'O', 'V':'W', 'W':'D', 'X':'K', 'Y':'Z', 'Z':'B', ' ': ' ', '.':'.' }

def encrypt(c):
    return encrypt_key[c]

print "Here is the encrypted message:\n"
print map(encrypt, list(yte.upper()))
print "\nUse it carefully. Use the C1 Decrypter to decrypt the message."

