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

    @return: string
    """
    def generate(self, limit, lowerCase, upperCase, digits, punctuation):
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


    """
    Method to generate bulk passwords.
    
    @type number: int
    @param number: number of passwords, default: 1
    
    @type limit: int or list
    @param x: range of the password characters, default: [8, 16]

    @type lowerCase: boolean
    @param lowerCase: lower case characters in password or not, default: True

    @type upperCase: boolean
    @param upperCase: upper case characters in password or not, default: True

    @type lowerCase: digits
    @param lowerCase: digits in password or not, default: True

    @type lowerCase: punctuation
    @param lowerCase: punctuation characters in password or not, default: True
    
    @return: list
    """
    def bulk(self, number = 5, limit = [8, 16], lowerCase = True, upperCase = True, digits = True, punctuation = True):
        passwords = []
        for x in range(number):
            password = self.generate(limit, lowerCase, upperCase, digits, punctuation)
            passwords.append(password)

        return passwords

    """
    Method to generate single password.

    @type number: int
    @param number: number of passwords, default: 1

    @type limit: int or list
    @param x: range of the password characters, default: [8, 16]

    @type lowerCase: boolean
    @param lowerCase: lower case characters in password or not, default: True

    @type upperCase: boolean
    @param upperCase: upper case characters in password or not, default: True

    @type lowerCase: digits
    @param lowerCase: digits in password or not, default: True

    @type lowerCase: punctuation
    @param lowerCase: punctuation characters in password or not, default: True

    @return: string
    """
    def single(self, limit = [8, 16], lowerCase = True, upperCase = True, digits = True, punctuation = True):

        return self.generate(limit, lowerCase, upperCase, digits, punctuation)

    """
        Method to generate a file with bulk passwords.

        @type number: int
        @param number: number of passwords, default: 1

        @type limit: int or list
        @param x: range of the password characters, default: [8, 16]

        @type lowerCase: boolean
        @param lowerCase: lower case characters in password or not, default: True

        @type upperCase: boolean
        @param upperCase: upper case characters in password or not, default: True

        @type lowerCase: digits
        @param lowerCase: digits in password or not, default: True

        @type lowerCase: punctuation
        @param lowerCase: punctuation characters in password or not, default: True

        @create: file 
        """

    def file(self, number=5, filePath = "passwords.txt", seperator = "\n", limit=[8, 16], lowerCase=True, upperCase=True, digits=True, punctuation=True):
        pf = open(filePath, "w+")
        for x in range(number):
            password = self.generate(limit, lowerCase, upperCase, digits, punctuation)
            pf.write(password + seperator)

        pf.close()
        return


