# ------------------------------------------------------------------------------
# Copyright (c) 2021, Infinite Development Team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file COPYING.txt, distributed with this software.
# ------------------------------------------------------------------------------

import platform
from tools import create_user_key
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
        pass
    if (platform.system() == "Linux"):
        pass
        # os.system("pip install -r req.txt")
    from cryptography.fernet import Fernet

    print("hello from Infinite Team.")
    user_pass = input("enter your password(we use this for our symmetric encryption.its recommanded to choose a strong password) :")
    user_key = (create_user_key(user_pass))
    # generate a random secret for user using crypto lib
    fernet = Fernet(user_key)
    random_key = Fernet.generate_key()
    symmetric_key = fernet.encrypt(random_key)
    # write the random secret as symmetric_key in symmetric.key
    # TODO : we can use a diffrent path for this
    with open("symmetric.key", "wb") as key_file:
        key_file.write(symmetric_key)
    print("done! \nsuccessfully initialized the symmetric key")


if __name__ == '__main__':
    first_run_tui()
