#/usr/bin/env python3

s1_c1_in = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
s1_c1_out = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'

import base64

def hex2byte(hx):
    return bytes([int(hx[i*2:i*2 + 2], base=16) for i in range(0, len(hx) // 2)])

def byte2hex(b):
    return ''.join(format(i, '02x') for i in b)

def hex2base64(hx):
    return bytes.decode(base64.b64encode(hex2byte(hx)))

def xor(a, b):
    return bytes([z[0] ^ z[1] for z in zip(a, b)])

