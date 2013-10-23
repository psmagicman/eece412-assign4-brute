"""
Author: Julien Law
Date: Oct. 23, 2013
Description: Brute force password cracker for question 2
"""

import hashlib
import random
import string

password = 'Aw30898863401E5C09AED7311AF30DB00FF451209A'
salt = 'Aw'
no_salt = '30898863401E5C09AED7311AF30DB00FF451209A'
input_set = 'abcdefghijklmnopqarstuvqxyzABCDEFGHIJKLMNOPQRSTUVWXWZ1234567890!@#$%^&*()_+-='
max_chars = 6

#print no_salt.__len__()

def generateSha1(password):
    """
    This function will take a string and hash it with SHA-1
    Returns the hex representation of the hash
    """
    m = hashlib.sha1()
    m.update(password)
    return m.hexdigest()
    
#print generateSha1('lol')

def generateRandomString(input_set, max_chars):
    """
    This function will generate and return a string of random chars
    """
    return ''.join(random.choice(input_set) for x in range(max_chars))
    
#print generateRandomString(input_set, max_chars)

def hashCheck(input_string):
    """
       This function takes an input string and compares it with the hash of a randomly generated string.
       If the hash is found, the randomly generated string is returned
    """
    value = input_string.lower()
    password = generateRandomString(input_set, max_chars)
    while(True):
        if generateSha1(salt + password) == value:
            break
        elif generateSha1(password + salt) == value:
            break
        password = generateRandomString(input_set, max_chars)
    return password
    
print 'Hashed password: ' + password
print 'Salt: ' + salt
    
print hashCheck(no_salt)
        
    
