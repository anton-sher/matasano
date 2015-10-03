import unittest
import matasano1

class TestMatasano1(unittest.TestCase):
    
    def test_hex2base64(self):
        hx = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
        b64 = 'SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t'
        self.assertEqual(matasano1.hex2base64(hx), b64)

    def test_xor(self):
        a = matasano1.hex2byte('1c0111001f010100061a024b53535009181c')
        b = matasano1.hex2byte('686974207468652062756c6c277320657965')
        expected_result = matasano1.hex2byte('746865206b696420646f6e277420706c6179')
        self.assertEqual(matasano1.xor(a, b), expected_result)

if __name__ == '__main__':
    unittest.main()
