import unittest
from parameterized import *
from src.sample.Affine import *


class Affine_test_parameterized(unittest.TestCase):
    def setUp(self):
        self.temp = Affine()

    @parameterized.expand([
        ('veni', 3, 12, 'xyzk'),
        ('VINI', 3, 32, 'RETE'),
        ('dici', 2, 16, 'wgug'),
        ('IL', 5, 15, 'DS'),
        ('DUCE', 25, 25, 'WFXV'),
        ('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 3, 12, 'MPSVYBEHKNQTWZCFILORUXADGJ'),
    ])
    def test_affine_words(self, text, a, b, cipher):
        self.assertEqual(self.temp.affine_encrpyt(text, a, b), cipher)

    @parameterized.expand([
        ('a', 3, 12, 'm'),
        ('B', 3, 12, 'P'),
        ('c', 3, 12, 's'),
        ('X', 3, 12, 'D'),
        ('y', 3, 12, 'g'),
        ('Z', 3, 12, 'J')
    ])
    def test_affine_single_letters(self, text, a, b, cipher):
        self.assertEqual(self.temp.affine_encrpyt(text, a, b), cipher)

    @parameterized.expand([
        ('hello world', 3, 12, 'hyttc acltv'),
        ('witaj swiecie', 3, 12, 'akrmn oakysky'),
        ('WESOLYCH SWIAT', 3, 12, 'AYOCTGSH OAKMR'),
        ('ala ma kota kot ma ALE', 3, 12, 'mtm wm qcrm qcr wm MTY'),
    ])
    def test_affine_sentences(self, text, a, b, cipher):
        self.assertEqual(self.temp.affine_encrpyt(text, a, b), cipher)

    @parameterized.expand([
        ('123', 3, 12),
        (',&!2@;.xxxz', 3, 12),
        (1, 3, 12),
        (str, 3, 12),
        ([], 3, 12),
        ({}, 3, 12),
        (None, 3, 12 ),
        (True, 3, 12 ),
    ])
    def test_affine_wrong_text_provided(self, text, a, b):
        self.assertRaises(Exception, self.temp.affine_encrpyt, text, a, b)
    @parameterized.expand([
        ('hello world', 'x', 12),
        ('witaj swiecie', 'd', 12),
        ('witaj swiecie', -3, 12),
        ('witaj swiecie', [], 12),
        ('witaj swiecie', 3, 'x'),
        ('witaj swiecie', 3, 'd'),
        ('witaj swiecie', 3, -3),
        ('witaj swiecie', 3, []),
        ('witaj swiecie', -3, -3),
        ('witaj swiecie', -1, -2),
    ])
    def test_affine_wrong_a_or_b(self, text, a, b):
        self.assertRaises(Exception, self.temp.affine_encrpyt, text, a, b)
    # ------
    # DECRYPT
    # -----
    @parameterized.expand([
        ('xyzk', 3, 12, 'veni'),
        ('RETE', 3, 32, 'VINI'),
        ('DS', 5, 15, 'IL'),
        ('WFXV', 25, 25, 'DUCE'),
        ('MPSVYBEHKNQTWZCFILORUXADGJ', 3, 12, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'),
    ])
    def test_affine_decrypt_words(self, text, a, b, decrypted_message):
        self.assertEqual(self.temp.affine_decrpyt(text, a, b), decrypted_message)

    @parameterized.expand([
        ('hyttc acltv', 3, 12, 'hello world'),
        ('akrmn oakysky', 3, 12, 'witaj swiecie'),
        ('AYOCTGSH OAKMR', 3, 12, 'WESOLYCH SWIAT'),

    ])
    def test_affine_decrypt_sentences(self, text, a, b, cipher):
        self.assertEqual(self.temp.affine_decrpyt(text, a, b), cipher)

    @parameterized.expand([
        ('123', 3, 12),
        (',&!2@;.xxxz', 3, 12),
        (1, 3, 12),
        (str, 3, 12),
        ([], 3, 12),
        ({}, 3, 12),
        (None, 3, 12 ),
        (True, 3, 12 ),
        ("ĄĄĆGF", 3, 12)
    ])
    def test_affine_decrypt_wrong_cipher_provided(self, text, a, b):
        self.assertRaises(Exception, self.temp.affine_decrpyt, text, a, b)
    @parameterized.expand([
        ('hello world', 'x', 12),
        ('witaj swiecie', 'd', 12),
        ('witaj swiecie', -3, 12),
        ('witaj swiecie', [], 12),
        ('witaj swiecie', 3, 'x'),
        ('witaj swiecie', 3, 'd'),
        ('witaj swiecie', 3, -3),
        ('witaj swiecie', 3, []),
        ('witaj swiecie', -3, -3),
        ('witaj swiecie', -1, -2),
        ('witaj swiecie', 2, 16),
    ])
    def test_affine_decypher_wrong_a_or_b(self, text, a, b):
        self.assertRaises(Exception, self.temp.affine_decrpyt, text, a, b)


