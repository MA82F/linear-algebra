import numpy as np

def create_key_matrix(n):
    while True:
        key_matrix = np.random.randint(0, 26, size=(n, n))
        det = int(np.round(np.linalg.det(key_matrix)))
        if det % 26 != 0 and np.gcd(det, 26) == 1:
            return key_matrix

def mod_inverse(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    return 1

def hill_cipher_encrypt(plain_text, key_matrix):
    n = key_matrix.shape[0]
    plain_text = plain_text.upper()
    padding_length = (n - len(plain_text) % n) % n
    plain_text += 'X' * padding_length
    encrypted_text = ""
    for i in range(0, len(plain_text), n):
        vector = [ord(char) - ord('A') for char in plain_text[i:i + n]]
        encrypted_vector = np.dot(key_matrix, vector) % 26
        encrypted_text += ''.join(chr(num + ord('A')) for num in encrypted_vector)
    return encrypted_text

def hill_cipher_decrypt(encrypted_text, key_matrix):
    n = key_matrix.shape[0]
    det = int(np.round(np.linalg.det(key_matrix)))
    det_inv = mod_inverse(det, 26)
    key_matrix_inv = det_inv * np.round(det * np.linalg.inv(key_matrix)).astype(int) % 26
    decrypted_text = ""
    for i in range(0, len(encrypted_text), n):
        vector = [ord(char) - ord('A') for char in encrypted_text[i:i + n]]
        decrypted_vector = np.dot(key_matrix_inv, vector) % 26
        decrypted_text += ''.join(chr(int(num) + ord('A')) for num in decrypted_vector)
    return decrypted_text

# مثال:
n = 3
key_matrix = create_key_matrix(n)
print("ماتریس کلید:\n", key_matrix)

plain_text = "HELLO"
encrypted_text = hill_cipher_encrypt(plain_text, key_matrix)
print("متن رمز شده:", encrypted_text)

decrypted_text = hill_cipher_decrypt(encrypted_text, key_matrix)
print("متن رمزگشایی شده:", decrypted_text)
