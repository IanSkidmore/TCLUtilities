# -*- coding: utf-8 -*-
"""
Created on Fri Feb 26 15:54:30 2016

@author: IAN

Provides encryption / decryption helper functions
"""
import simplecrypt

def encrypt(m,s):
    return simplecrypt.encrypt(s,m)
    
def decrypt(m,s):
    return simplecrypt.decrypt(s,m)
    
class Crypter():
    def __init__(self,secret='Shbu4@c0h'):
        self.secret = secret

    def encrypt(self,m):
        return simplecrypt.encrypt(self.secret,m)
        
    def decrypt(self,m):
        return simplecrypt.decrypt(self.secret,m)