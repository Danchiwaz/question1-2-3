import hmac
import hashlib
from hashlib import sha1
import base64

def hash_hmac(data, hmac_key):
    data = base64.b64encode(data.encode('utf-8')).decode("utf-8")
    hmac_code = hmac.new(hmac_key.encode(), data.encode(), sha1).hexdigest()

    sign = hashlib.md5(hmac_code.encode()).hexdigest()

    return sign

if __name__ == "__main__":
    encoded_text = hash_hmac("Maina","potential")
    print(encoded_text)