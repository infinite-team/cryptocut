from tools import *
from setup import first_run_tui
import fire

class CryptoCut(object):

    def initial(self):
        first_run_tui()

    def encrypt(self,message):
        '''symmetric encryption'''
        encrypted_message = symmetric_encrypt(message,key=read_symmetric_key())
        if(not encrypted_message):
            return "Wrong Password !"
        print(cf.yellow('copied to your clipboard!'))
        return(encrypted_message.decode('utf-8'))

    def decrypt(self,message):
        '''symmetric decryption'''
        decrypted_message = symmetric_decrypt(message,key=read_symmetric_key())
        if(not decrypted_message):
            return "Wrong Password !"
        print(cf.yellow('copied to your clipboard!'))
        return(decrypted_message)

if __name__ == '__main__':
    fire.Fire(CryptoCut)

