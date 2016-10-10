#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Week 07 synthesizing task 02"""

import getpass
import authentication

def login(username, maxattempts = 3):
    """This function checks username and password for correctness.

    Args:
        username (str): A string representing the username of the user
        attempting to log in.
        maxattempts (int, optional): An integer represent the maximum number of
        prompted attempts before the function returns False.

    Returns:
        Returns a True or False in the process of authentication of attampts

    Examples:
        >>> import task_02
        >>> task_02.login('mike', 4)
        Please enter your password:
        Incorrect username or password. You have 3 attempts left.
        Please enter your password:
        Incorrect username or password. You have 2 attempts left.
        Please enter your password:
        Incorrect username or password. You have 1 attempts left.
        Please enter your password:
        Incorrect username or password. You have 0 attempts left.
        False
    """
    authenticated = False
    counter = 1
    
    inputmsg = 'Please enter your password: '
    errormsg = 'Incorrect username or password. You have {0} attempts'
    
    while counter <= maxattempts:
        password = getpass.getpass(inputmsg)
        message = authentication.authenticate(username, password)
        if message:
            authenticated = True
            break
        else:
            print errormsg.format(maxattempts - counter)
            counter += 1
        return authenticated
