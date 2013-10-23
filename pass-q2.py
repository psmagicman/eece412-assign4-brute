"""
Author: Julien Law
Date: Oct. 23, 2013
Description: Brute force password cracker for question 2
"""

import hashlib

password = 'Aw30898863401E5C09AED7311AF30DB00FF451209A'
salt = 'Aw'
no_salt = '30898863401E5C09AED7311AF30DB00FF451209A'

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
