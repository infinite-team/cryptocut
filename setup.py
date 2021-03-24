# ------------------------------------------------------------------------------
# Copyright (c) 2021, Infinite Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ------------------------------------------------------------------------------

import platform
from tools import create_user_key
from art import *
import colorful as cf

# detect OS
# install tools for specific OS/distro
# copy files


def first_run_tui():
    '''
    first setups and creating key's and personal passwords
    '''
    import os
    if (platform.system() == "Darwin"):
        pass
    if (platform.system() == "Windows"):
        os.system("pip install -r requirements.txt")
        # pass
    if (platform.system() == "Linux"):
        pass
    from cryptography.fernet import Fernet

    cryptocut_art = text2art("cRYPTOcUT","confused3")
    setup_art=text2art("setup")
    print('\n',cf.green(cryptocut_art))
    print(cf.cyan(setup_art))
    user_pass = input(cf.yellow("enter your password for symmetric encryption : "))
    user_key = (create_user_key(user_pass))
    # generate a random secret for user using crypto lib
    fernet = Fernet(user_key)
    random_key = Fernet.generate_key()
    symmetric_key = fernet.encrypt(random_key)
    # write the random secret as symmetric_key in symmetric.key
    # TODO : we can use a diffrent path for this
    with open("symmetric.key", "wb") as key_file:
        key_file.write(symmetric_key)
    print(cf.green("done! \nsuccessfully initialized the symmetric key"))


if __name__ == '__main__':
    first_run_tui()
