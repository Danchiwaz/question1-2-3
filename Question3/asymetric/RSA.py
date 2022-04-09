from Crypto.Cipher import PKCS1_v1_5
from Crypto.PublicKey import RSA
import base64

def cipher(data, rsa_key):
    """
    Public key encryption
    : param MSG: to encrypt content
    : Return: encrypted ciphertext
    """
    #Get public key
    key = rsa_key
    publickey = RSA.importKey(key)
    #Segmented encryption
    pk = PKCS1_v1_5.new(publickey)
    encrypt_text = []
    #Segment encryption of data
    for i in range(0, len(data), 100):
        cont = data[i:i + 100]
        encrypt_text.append(pk.encrypt(cont.encode("utf-8")))
    #Segmented encryption完进行拼接
    cipher_text = b''.join(encrypt_text)
    #Base64
    result = base64.b64encode(cipher_text)
    return result.decode()

if __name__ == '__main__':
    Data = "Walkman AI focuses on the game field, has accumulated AI technology for many years, and provides one-stop audit of text, picture, audio / video content, game AI and data platform services."
    #Read the file where the public key is stored to get the public key
    rsa_key = open('publickey.pem').read()
    cipher(Data, rsa_key)
