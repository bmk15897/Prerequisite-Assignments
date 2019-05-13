'''
Assignment 1 - Write a Python program to check the validity of a password chosen by a user.
To be considered valid, a password must
a) contain at least 1 letter between [A-Z],
b) contain at least 1 letter between [a-z],
c) contain at least 1 number between [0-9],
d) contain at least 1 special character from [$#@],
e) have a minimum length of 6 characters, and
f) have a maximum length of 12 characters.
Your program will consist of two user-defined functions: validate() and main(). The validate()
function implements the validation procedure described above. The parameter (or input) to the
function is a string s. If s fits the above criteria, print valid Otherwise, print not valid. Also
implement logging.
'''
import re
import logging

#logging configuration
logging.basicConfig(filename='loggingApp.log', filemode='a+', format='%(levelname)s : %(message)s',level=logging.DEBUG)

lengthLowerLimit = 6
lengthUpperLimit = 12

#password validation
def validate(pwd):
    pwdLength = len(pwd)
    if pwdLength>=lengthLowerLimit:
        if pwdLength<=lengthUpperLimit:
            if re.search(".*[a-z].*",pwd):
                if re.search(".*[A-Z].*",pwd):
                    if re.search(".*[0-9].*",pwd):
                        if re.search(".*[$#@].*",pwd):
                            print("Valid Password.")
                            logging.info('Valid Password.')
                        else:
                            print("Invalid Password.")
                            logging.error('Invalid Password. Password should contain special characters.')
                    else:
                        print("Invalid Password.")
                        logging.error('Invalid Password. Password should contain numeric characters.')
                else:
                    print("Invalid Password.")
                    logging.error('Invalid Password. Password should contain uppercase characters.')
            else:
                print("Invalid Password.")
                logging.error('Invalid Password. Password should contain lowercase characters.')
        else:
            print("Invalid Password.")
            logging.error('Invalid Password. Password length should be less than or equal to {0} characters.'.format(lengthUpperLimit))
    else:
        print("Invalid Password.")
        logging.error('Invalid Password. Password length should be equal to or greater than {0} characters.'.format(lengthLowerLimit))

if __name__=='__main__':
    s = input("Enter password: ")
    validate(s)
