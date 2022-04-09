# question1-2-3
##### For any business to succeed in its day to day activities,there is always alot of data being shared in between organisational Departments or even outside the organisaition.
##### - This sets an alarm and bring about the issuee of encrypting data
##### -Encryption of data is always  applied in some important scenarios, such as login, payment and OAuth.Different scenarios require different signature encryption algorithms to achieve business goals.
##### Have worked with several encryption/hashing algorithms and probably the most common.Kindly allow me to take you through
# Types of Encryption/Hashing method and their Implementation
1. Hash algorithm:
###### This algorithm is use to check or to validate intergrity/collectness of a message.**Hash** function in python is used to achieve the goal and helps in implemeting the solution.It generates fixed length output for different length input messages. The common algorithms are **MD5, Sha, HMAC ** and so on.
2. Symmetric encryption:
###### Symmetric encryption achieves the encyprtion by encrypt and decrypting with the same key.The key is the instruction that controls the encryption and decryption process. An algorithm is a set of rules that specify how to encrypt and decrypt. The common symmetry algorithms are AES, DES, 3DES
3. Asymmetric encryption:
###### This oa abit different to  symmetric encryption algorithm, asymmetric encryption algorithm needs two keys: public key and private key. The public key and the private key are a pair. If the public key is used to encrypt the data, only the corresponding private key can be used to decrypt it; If the private key is used to encrypt the data, only the corresponding public key can be used to decrypt. Because encryption and decryption use two different keys, this algorithm is called asymmetric encryption algorithm. The common asymmetric algorithms are **RSA**, **DSA**, **ECC**.

# Implementation of Python
1. #### hash algorithm HMAC, MD5
###### HMAC takes hmacsha1 as the column and needs HMAC_ The encrypted data is usually encoded in Base64 format.
##### Python Code screenshot: 
![alt text](https://github.com/Danchiwaz/question1-2-3/blob/main/screenshots/hash_code.png "HMAC algorithm")
##### Output of encrypted data:
![alt text](https://github.com/Danchiwaz/question1-2-3/blob/main/screenshots/hash_output.png "HMAC output")

2. #### Symmetric encryption AES
```python
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
  

```

