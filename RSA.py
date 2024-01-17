import math
import random



def gen_sieve(sieve_size):
    sieve = [True] * sieve_size
    sieve[0] = False
    sieve[1] = False

    for i in range(2, int(math.sqrt(sieve_size)) + 1):
        pointer = i * 2
        while pointer < sieve_size:
            sieve[pointer] = False
            pointer += i

    # Compile the list of primes:
    primes = []
    for i in range(sieve_size):
        if sieve[i]:
            primes.append(i)

    return primes


LOW_PRIMES = gen_sieve(120)


def is_prime(num):
    if num < 2:
        return False
    for prime in LOW_PRIMES:
        if num == prime:
            return True
        if num % prime == 0:
            return False


def gen_large_prime(key_size=1024):
    while True:
        num = random.randrange(2 ** (key_size - 1), 2 ** key_size)
        if is_prime(num):
            return num


def inverse(num: int, mod: int) -> int:
    return pow(num, -1, mod)


def generate_keypair():
    p = gen_large_prime(7)
    q = gen_large_prime(3)

    n = p * q
    phi = (p - 1) * (q - 1)

    # Выбираем открытый ключ open_key, такой что 1 < open_key < phi и open_key взаимно прост с phi
    open_key = random.randrange(2, phi)

    while math.gcd(open_key, phi) != 1:
        open_key = random.randrange(2, phi)

    # Вычисляем закрытый ключ secret_key, такой что secret_key * open_key ≡ 1 (mod phi)
    secret_key = inverse(open_key, phi)

    return (open_key, n), (secret_key, n)


def encrypt(public_key, plaintext):
    e, n = public_key
    ciphertext = [pow(ord(char), e, n) for char in plaintext]
    return ciphertext


def decrypt(private_key, ciphertext):
    d, n = private_key
    plaintext = [chr(pow(char, d, n)) for char in ciphertext]
    return ''.join(plaintext)
