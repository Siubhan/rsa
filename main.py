from RSA import *

if __name__ == '__main__':
    open_key, secret_key = generate_keypair()
    text = 'ASDqwrzxc'
    print(open_key, secret_key)
    print(text)
    text = encrypt(open_key, text)
    print(text)
    text = decrypt(secret_key, text)
    print(text)


