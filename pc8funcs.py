#Functions that might come in handy
#Functions written by PythonCoder8

def urlConnect(url:str) -> bool:
    '''Checks connectivity to URL'''
    if isinstance(url, str) == False:
        return 'URL must be string data type'
    import requests
    requests.packages.urllib3.disable_warnings()
    try:
        r = requests.get(url, verify=False)
        return True
    except:
        return False


def factorial(num:int) -> int:
    '''Returns the factorial of a number'''
    if isinstance(num, int) == False:
        return 'Number must be integer data type'
    factorial = 1
    for i in range(1,num+1):
        factorial *= i
    return factorial


def isPalindrome(phrase:str) -> bool:
    '''Tells you if a string is a palindrome'''
    if isinstance(phrase, str) == False:
        return 'Phrase must be string data type'
    import re
    modified_string = re.sub(r'[^A-Za-z]', '',phrase).lower()
    if modified_string[::-1] == modified_string:
        return True
    else:
        return False

def datetimenow() -> str:
    '''Tells you the current date and time'''
    import datetime
    import time
    import sys
    now = datetime.datetime.now()
    return now.strftime('%m-%d-%Y %H:%M:%S')