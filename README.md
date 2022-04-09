# question 1-2-3
# QUESTION 1
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
1. #### hash algorithm HMAC, MD5 [Access the code on Github ](https://github.com/Danchiwaz/question1-2-3/blob/main/Question3/HMSC_MD5.py)
###### HMAC takes hmacsha1 as the column and needs HMAC_ The encrypted data is usually encoded in Base64 format.
##### Python Code screenshot: 
![alt text](https://github.com/Danchiwaz/question1-2-3/blob/main/screenshots/hash_code.png "HMAC algorithm")
##### Output of encrypted data:
![alt text](https://github.com/Danchiwaz/question1-2-3/blob/main/screenshots/hash_output.png "HMAC output")

2. #### Symmetric encryption AES [Access the code on Github ](https://github.com/Danchiwaz/question1-2-3/blob/main/Question3/symetric/AES.py)
###### For symmetric encryption or asymmetric encryption, a third-party library needs to be installed. The password Library in Python is pycrypto, but it has stopped updating in 2012. Now pycryptodome is used to replace pycrypto.
######  AES has five encryption modes, which are ECB, CBC, CTR, CFB and OFB. Take the ECB mode of AES as an example, AES also needs encryption key AES_ Key. It should be noted that if the encrypted data is less than 16 or 32 bits, it needs to be supplemented as a multiple of them. Take the multiple of 16 as an example:
###### Here we need to install `pip install pycryptodome`

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
###### The output should be `b'NvXwEIpr6HIh8RqdcRsfrO+Jh1PftKB6JtsFOnUa7PPlQR6f4k5EHCNlTFzXVPG8T39KVtHMYw7d\nJENzEoFWQDi9LmbQw+dUxIq8BBEr7s5XwDYALNSSHX3N924f6qo2bHxMrMS5jAorFd11f+nDPQ==\n'`

3. #### Asymmetric encryption RSA [Access the code on Github ](https://github.com/Danchiwaz/question1-2-3/blob/main/Question3/asymetric/RSA.py)
###### This algorithm also needs pycryptodome to be installed
###### RSA encryption needs public key to encrypt. It should be noted that sometimes when the amount of data to be encrypted is large, it needs to be encrypted by segments.I will use segmented encryption. This encyption methodology is also much effective for less data.
###### Here we need to install `pip install pycryptodome`
##### The python code for RSA is a follows
```python
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
    #Segmented encryption
    cipher_text = b''.join(encrypt_text)
    #Base64
    result = base64.b64encode(cipher_text)
    return result.decode()

if __name__ == '__main__':
    Data = "Walkman AI focuses on the game field, has accumulated AI technology for many years, and provides one-stop audit of text, picture, audio / video content, game AI and data platform services."
    #Read the file where the public key is stored to get the public key
    rsa_key = open('publickey.pem').read()
    cipher(Data, rsa_key)

```

#QUESTION 2
#### The intergration protocals that I have come across and probably most used is **XML** and **json**
###### This approach of **json** or **XML** has tons of advantages. These protocols are widely supported so that you can find a library, plugin, or extension for pretty much every application framework and platform. Consequently, it is easy to modify and integrate applications that support these protocols.
###### Example ,I  django has a very good framework for developing restful Api's i.e django restframework, the output of this framework is json which is compatible with so many platforms and frameworks.
1. ### Json
###### JSON stands for JavaScript Object Notation
###### JSON is a lightweight format for storing and transporting data
###### JSON is often used when data is sent from a server to a web page
#### JSON Syntax Rule:-
* Data is in name/value pairs
* Data is separated by commas
* Curly braces hold objects
* Square brackets hold arrays
###### Though django restframework does it best and also for production but still its achievable in python 3.
```python
# converting data to json 
# i will use dummy data just for simplicty 

import json

daniel_data ={
    "name":"Daniel Maina Wachira",
    "tel_number":"0712747209",
    "area_of_residence":"Nairobi Kenya",
    "intership_expected":"interIntel",
    "profession":"Software Engineer"

}

convert_to_json = json.dumps(daniel_data)

print(convert_to_json)
```
##### The output of the above code will be


