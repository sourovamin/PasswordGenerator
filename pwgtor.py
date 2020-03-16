import string
from random import *

class PwGtor:

    """
    Method to generate password.

    @type limit: int or list
    @param x: range of the password characters

    @type lowerCase: boolean
    @param lowerCase: lower case characters in password or not

    @type upperCase: boolean
    @param upperCase: upper case characters in password or not

    @type lowerCase: digits
    @param lowerCase: digits in password or not

    @type lowerCase: punctuation
    @param lowerCase: punctuation characters in password or not
    """
    def generator(self, limit, lowerCase, upperCase, digits, punctuation):
        available = ""
        if(lowerCase):
            available += string.ascii_lowercase
        if(upperCase):
            available += string.ascii_uppercase
        if(digits):
            available += string.digits + string.digits
        if(punctuation):
            available += string.digits + string.punctuation

        if(isinstance(limit,int)):
            password = "".join(choice(available) for x in range(limit))
        else:
            if(len(limit) == 2):
                password = "".join(choice(available) for x in range(randint(limit[0], limit[1])))
            else:
                password = "Wrong limit parameter!"

        return password