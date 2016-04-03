# -*- coding: utf-8 -*-
"""
Created on Sun Apr 03 14:55:59 2016

@author: IAN
"""

import unittest

from crypter import Crypter, encrypt, decrypt

class Test_Crypter(unittest.TestCase):
    def setUp(self):
        self.c = Crypter()
        
    def tearDown(self):
        self.c = None
        
    def test_encryption_decryption(self):
        msg = 'The quick brown fox jumps over the lazy dog'
        m = self.c.encrypt(msg)
        newMsg = self.c.decrypt(m)
        self.assertEqual(newMsg, msg)
        
    def test_set_crypter_secret_encryption_decryption(self):
        self.c.secret = 'Ftmws2dtw01'
        msg = 'The quick brown fox jumps over the lazy dog'
        m = self.c.encrypt(msg)
        newMsg = self.c.decrypt(m)
        self.assertEqual(newMsg, msg)        

class Test_crypt_fuctions(unittest.TestCase):
    def test_encryption_decryption(self):
        secret = 'Ftmws2dtw01'
        msg = 'The quick brown fox jumps over the lazy dog'
        m = encrypt(msg,secret)
        newMsg = decrypt(m,secret)
        self.assertEqual(newMsg, msg)
        