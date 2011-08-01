'''
Created on Dec 18, 2010

@author: ppa
'''
import sys
from datetime import datetime

import logging
LOG = logging.getLogger(__name__)

googCSVDateformat = "%d-%b-%y"

def import_class(path, fileName, className=None):
    ''' dynamically import class '''
    if not className:
        className = capitalize(fileName)
    sys.path.append(path)

    mod = __import__(fileName)
    return getattr(mod, className)

def capitalize(inputString):
    ''' capitalize first letter '''
    return inputString[0].upper() + inputString[1:] if len(inputString) > 1 else inputString[0].upper()

def deCapitalize(inputString):
    ''' de-capitalize first letter '''
    return inputString[0].lower() + inputString[1:] if len(inputString) > 1 else inputString[0].lower()

def splitByComma(inputString):
    ''' split string by comma '''
    return [name.strip() for name in inputString.split(',')]

def convertGoogCSVDate(googCSVDate):
    ''' convert date 25-Jul-2010 to 2010-07-25'''
    return datetime.strptime(googCSVDate, googCSVDateformat).date()
