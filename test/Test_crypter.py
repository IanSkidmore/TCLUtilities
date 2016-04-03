# -*- coding: utf-8 -*-
"""
Created on Sun Apr 03 14:55:59 2016

@author: IAN
"""

import unittest

from crypter import Crypter

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