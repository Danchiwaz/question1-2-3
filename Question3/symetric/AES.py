import json
import base64
from Crypto.Cipher import AES




def add_to_16(value):
    while len(value) % 16 != 0:
        value += b'\0'
    return value





def encrypt_aes(data, aes_key):
    encrypting_key = aes_key.encode() #ec
    #Text to be encrypted
    data_being_encypted = bytes(json.dumps(data).replace(" ", "").encode('utf-8'))
    #Filling in encrypted data
    data_being_encypted = add_to_16(data_being_encypted)
    #Initialize the encryptor and use ECB mode
    aes = AES.new(encrypting_key, AES.MODE_ECB)
    #AES encryption first
    aes_code = aes.encrypt(data_being_encypted)
    #Convert to string form with Base64, execute encryption and transcoding to return bytes
    encrypted_text = base64.encodebytes(aes_code) 

    return encrypted_text



    
if __name__ == '__main__':
    data_to_be_encrypted = "Hello,the one who is doing the server encription needs to be very careful and ensure all the security, protocals are observed"
    encrypting_key = "danielmainawachi"
    encrypt_the_data = encrypt_aes(data_to_be_encrypted, encrypting_key)
    print(encrypt_the_data)
  
