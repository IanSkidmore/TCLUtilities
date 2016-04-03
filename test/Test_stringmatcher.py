# -*- coding: utf-8 -*-
"""
Created on Sun Apr 03 12:12:11 2016

@author: IAN

print "Skiddmoore", sm.Match("Skiddmoore")

print "Danniel", nm.Match("Danniel")
print "Daneil", nm.Match("Daneil")

nm.addValue("Peter")
nm.addSynonym("David", "Dave")
nm.addValue("Adam")
"""
import unittest

from stringmatcher import StringHelper, StringMatcher, SynonymMatcher

class Test_StringHelper(unittest.TestCase):
    def setUp(self):
        self.sh = StringHelper()
        
    def tearDown(self):
        self.sh = None

class Test_StringMatcher(unittest.TestCase):
    def setUp(self):
        self.sm = StringMatcher("Skidmore")
    
    def tearDown(self):
        self.sm = None
        
    def test_no_match(self):
        self.assertEqual(self.sm.Match('Garbage'), 'NoMatch')
    
    def test_full_match(self):
        self.assertEqual(self.sm.Match('Skidmore'), 'FullMatch')
    
    def test_soundex_match(self):
        self.assertEqual(self.sm.Match('Skydnorre'), 'SoundexMatch')
    
    def test_consonant_match(self):
        self.assertEqual(self.sm.Match('Skydmoore'), 'ConsonantMatch')      
            
    def test_transpose_match(self):
        self.assertEqual(self.sm.Match('Skimdore'), 'TransposeMatch')             
            
    def test_no_transpose_match(self):
        self.assertEqual(self.sm.Match('Skimdoer'), 'NoMatch') 
            
    def test_duplicate_character_match(self):
        self.assertEqual(self.sm.Match('Skiddmore'), 'DuplicateCharacterMatch') 
            
    def test_no_duplicate_character_match(self):
        self.assertEqual(self.sm.Match('Skiddmoore'), 'SoundexMatch') 
        
class Test_SynonymMatcher(unittest.TestCase):
    def setUp(self):
        self.nm = SynonymMatcher("Daniel", r"C:\Users\IAN\Documents\Python Scripts\synonyms.csv")
    
    def tearDown(self):
        self.nm = None
        
    def test_full_match(self):
        self.assertEqual(self.nm.Match('Daniel'), 'FullMatch')    
        
    def test_synonym_match(self):
        self.assertEqual(self.nm.Match('Dan'), 'SynonymMatch')    
        
    def test_another_synonym_match(self):
        self.assertEqual(self.nm.Match('Danny'), 'SynonymMatch')          
        
    def test_no_match(self):
        self.assertEqual(self.nm.Match('Dani'), 'NoMatch')      
        
    def test_consonant_match(self):
        self.assertEqual(self.nm.Match('Danel'), 'ConsonantMatch')         
        
    def test_duplicate_character_match(self):
        self.assertEqual(self.nm.Match('Danniel'), 'DuplicateCharacterMatch')          
                
    def test_transpose_match(self):
        self.assertEqual(self.nm.Match('Daneil'), 'TransposeMatch')  