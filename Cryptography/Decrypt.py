ytd = raw_input("Welcome to the C1 Decrypter! Enter a phrase or word from the C1 Encrypter. I will reveal the true meaning.")

encrypt_key = {'A':'F', 'B':'Z', 'C':'B', 'D':'V', 'E':'K', 'F':'I', 'G':'X', 'H':'A', 'I':'Y', 'J':'M', 'K':'E', 'L':'P', 'M':'L', 'N':'S', 'O':'D', 'P':'H', 'Q':'J', 'R':'O', 'S':'R', 'T':'G', 'U':'N', 'V':'Q', 'W':'C', 'X':'U', 'Y':'T', 'Z':'W', ' ':' ', '.':'.' }

decrypt_key= dict (zip(encrypt_key.values(),encrypt_key.keys()))

def decrypt(c):
    return decrypt_key[c]

print "Here is the true meaning:\n"
print map(decrypt, list(ytd))