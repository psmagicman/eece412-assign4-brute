"""
Author: Julien Law
Date: Oct. 23, 2013
Description: This script is intended to break a 4 digit pin using a brute force method. The pin is salted and encrypted using SHA-1
"""

import hashlib

salted_pass = 'pK904B3CB05F59B00431FCDBDB0D4EBDEE14D36D39'
salt = 'pK'
no_salt = '904B3CB05F59B00431FCDBDB0D4EBDEE14D36D39'

def hashCheck(value):
    input_val = value.lower()
    #print value
    #print input_val
    for i in range(0, 10000):
        pin = "%04d" % i
        if generateSha1(salt + pin) == input_val:
            return salt+pin
        elif generateSha1(pin + salt) == input_val:
            return pin+salt
        
def generateSha1(number):
    m = hashlib.sha1()
    m.update(number)
    return m.hexdigest()
     
#print generateSha1('1234')
#print generateSha1('1234').__len__()

my_pin = hashCheck(no_salt)
print salted_pass
print no_salt
print my_pin
print generateSha1(my_pin).upper()
