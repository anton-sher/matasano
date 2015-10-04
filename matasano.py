import base64
import math

def hex2byte(hx):
    return bytes([int(hx[i*2:i*2 + 2], base=16) for i in range(0, len(hx) // 2)])

def byte2hex(b):
    return ''.join(format(i, '02x') for i in b)

def hex2base64(hx):
    return bytes.decode(base64.b64encode(hex2byte(hx)), 'ascii')

def xor(a, b):
    return bytes([z[0] ^ z[1] for z in zip(a, b)])

# Challenge 3: cracking single-byte XOR
def single_byte_xor(s, c):
    return bytes.decode(xor(str.encode(s), bytes([c]) * len(s)), 'ascii')

def char_occurrences(s):
    occur = {}
    for c in s:
        if c in occur:
            occur[c] = occur[c] + 1
        else:
            occur[c] = 1
    return occur

def char_frequencies(s):
    occur = char_occurrences(s)
    s = sum(occur.values())
    freq = {}
    for k in occur:
        freq[k] = occur[k] / s
    return freq

ref_frequencies = char_frequencies('''
We can't introduce these any better than Maciej Ceglowski did, so read that blog post first.

We've built a collection of 48 exercises that demonstrate attacks on real-world crypto.

This is a different way to learn about crypto than taking a class or reading a book. We give you problems to solve. They're derived from weaknesses in real-world systems and modern cryptographic constructions. We give you enough info to learn about the underlying crypto concepts yourself. When you're finished, you'll not only have learned a good deal about how cryptosystems are built, but you'll also understand how they're attacked.
''')

def diff_frequencies(f1, f2):
    keys = set(f1) | set(f2)
    s = 0
    for key in keys:
        d = 0
        if key in f1:
            d += f1[key]
        if key in f2:
            d -= f2[key]
        s += d * d
    return math.sqrt(s)

def guess_xor_key(s):
    k_min = 0
    d_min = 0
    for k in range(1, 255):
        try:
            d = diff_frequencies(ref_frequencies, char_frequencies(single_byte_xor(s, k)))
            if k_min == 0 or d < d_min:
                k_min = k
                d_min = d
        except:
            pass
    return k_min

def solve_3():
    cyphertext = bytes.decode(hex2byte('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736'), 'ascii')
    print('cyphertext:', cyphertext)
    k = guess_xor_key(cyphertext)
    print('key:', k)
    print('plaintext:', single_byte_xor(cyphertext, k))

def solve_4():
    with open('data/4.txt') as f:
        lines = f.read().splitlines()
    for line in lines:
        pass
