ytd = raw_input("Welcome to the C1 Decrypter! Enter a phrase or word from the C1 Encrypter. I will reveal the true meaning.")

encrypt_key = {'A':'H', 'B':'Y', 'C':'P', 'D':'L', 'E':'I', 'F':'J', 'G':'Z', 'H':'Q', 'I':'M', 'J':'V', 'K':'R', 'L':'E', 'M':'N', 'N':'S', 'O':'A', 'P':'G', 'Q':'F', 'R':'U', 'S':'T', 'T':'C', 'U':'O', 'V':'W', 'W':'D', 'X':'K', 'Y':'Z', 'Z':'B', ' ':' ', '.':'.' }

decrypt_key= dict (zip(encrypt_key.values(),encrypt_key.keys()))

def decrypt(c):
    return decrypt_key[c]

print "Here is the true meaning:\n"
print map(decrypt, list(ytd))
