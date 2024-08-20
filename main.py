import numpy as np 
import pandas as pd
import pdb

# 187 = 17 * 11
# phi(187) = 160
# e = less than phi(N) and coprime with N = 137--> public_key = (137, 187) ((e, N))
# chose d s.t. d*e mod (phi(N)) = 1: d * 137 mod (160): found: 153 therefore private_key = (153, 187)

#key = (power, modulo) 
def rsa_encrypt(c, public_key):
    t = ord(c)
    return chr((t ** public_key[0]) % public_key[1])
    #return (t ** public_key[0]) % public_key[1]

def rsa_encrypt_message(message, public_key):
    out = ''
    for e in message:
        out += (rsa_encrypt((e), public_key=public_key))

    return out


#t = rsa_encrypt('a', (137, 187))
#print(t)

def rsa_decrypt(c, private_key):
    t =  ord(c)
    #print(t ** private_key[0])
    return chr((t**private_key[0]) % private_key[1])

#rsa_decrypt(t, private_key=(153, 187))

def rsa_decrypt_message(message, private_key):
    out = ''
    for e in message:
        out += (rsa_decrypt((e), private_key=private_key))

    return out

t = rsa_encrypt_message("hello there", (137, 187) )
print(t, rsa_decrypt_message(t, private_key=(153,187)))

def generate_key_pair(f1, f2):
    if np.gcd(f1, f2) != 1:
        raise ValueError("inputs must be relatively prime since the modulo must be a semi-prime")

    N = f1 * f2
    def phi(a, b):
        return (a-1)*(b-1)

    p = phi(f1, f2)
    e = []
    for i in range(p):
        if np.gcd(i, N) == 1:
            e.append(i)
    
    public = e[-1]
    d = []
    for i in range(N ):
        if (public * i) % N == 1:
            d.append(i)

    private = d[-1]
    print(e,d)
    return (public, N), (private, N)


generate_key_pair(17, 11)






