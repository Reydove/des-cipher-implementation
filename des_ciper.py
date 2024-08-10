import sys

# Define necessary tables (IP, IP_inverse, E, P, S_BOX)
IP = [58, 50, 42, 34, 26, 18, 10, 2,
      60, 52, 44, 36, 28, 20, 12, 4,
      62, 54, 46, 38, 30, 22, 14, 6,
      64, 56, 48, 40, 32, 24, 16, 8,
      57, 49, 41, 33, 25, 17, 9, 1,
      59, 51, 43, 35, 27, 19, 11, 3,
      61, 53, 45, 37, 29, 21, 13, 5,
      63, 55, 47, 39, 31, 23, 15, 7]

IP_inverse = [40, 8, 48, 16, 56, 24, 64, 32,
              39, 7, 47, 15, 55, 23, 63, 31,
              38, 6, 46, 14, 54, 22, 62, 30,
              37, 5, 45, 13, 53, 21, 61, 29,
              36, 4, 44, 12, 52, 20, 60, 28,
              35, 3, 43, 11, 51, 19, 59, 27,
              34, 2, 42, 10, 50, 18, 58, 26,
              33, 1, 41, 9, 49, 17, 57, 25]

E = [32, 1, 2, 3, 4, 5, 4, 5,
     6, 7, 8, 9, 8, 9, 10, 11,
     12, 13, 12, 13, 14, 15, 16, 17,
     16, 17, 18, 19, 20, 21, 20, 21,
     22, 23, 24, 25, 24, 25, 26, 27,
     28, 29, 28, 29, 30, 31, 32, 1]

P = [16, 7, 20, 21,
     29, 12, 28, 17,
     1, 15, 23, 26,
     5, 18, 31, 10,
     2, 8, 24, 14,
     32, 27, 3, 9,
     19, 13, 30, 6,
     22, 11, 4, 25]

S_BOX = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
     [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
     [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]]
    # Add other S-boxes (S2, S3, ..., S8)
]

def permute(block, table):
    return [block[i - 1] for i in table]

def xor(a, b):
    return [i ^ j for i, j in zip(a, b)]

def sbox_substitution(block):
    row = (block[0] << 1) + block[5]
    col = (block[1] << 3) + (block[2] << 2) + (block[3] << 1) + block[4]
    return [int(x) for x in format(S_BOX[0][row][col], '04b')]

def text_to_bin(text):
    binary = ''.join(format(ord(c), '08b') for c in text)
    return [int(b) for b in binary]

def bin_to_text(binary):
    binary_str = ''.join(str(b) for b in binary)
    text = ''.join(chr(int(binary_str[i:i+8], 2)) for i in range(0, len(binary_str), 8))
    return text

def des_encrypt(plain_text, key):
    plain_text = permute(plain_text, IP)
    left, right = plain_text[:32], plain_text[32:]

    for _ in range(16):
        right_expanded = permute(right, E)
        sub_key = key
        right_expanded = xor(right_expanded, sub_key)
        
        right_sbox = []
        for i in range(0, 48, 6):
            right_sbox += sbox_substitution(right_expanded[i:i+6])
        
        right_permuted = permute(right_sbox, P)
        right, left = xor(right_permuted, left), right
    
    combined = right + left
    cipher_text = permute(combined, IP_inverse)
    
    return cipher_text

def des_decrypt(cipher_text, key):
    cipher_text = permute(cipher_text, IP)
    left, right = cipher_text[:32], cipher_text[32:]

    for _ in range(16):
        right_expanded = permute(right, E)
        sub_key = key
        right_expanded = xor(right_expanded, sub_key)
        
        right_sbox = []
        for i in range(0, 48, 6):
            right_sbox += sbox_substitution(right_expanded[i:i+6])
        
        right_permuted = permute(right_sbox, P)
        right, left = xor(right_permuted, left), right
    
    combined = right + left
    decrypted_text = permute(combined, IP_inverse)
    
    return decrypted_text

def main():
    if len(sys.argv) != 3:
        print("Usage: python des_cipher.py <encrypt/decrypt> <text>")
        return

    mode = sys.argv[1].lower()
    input_text = sys.argv[2]

    # Convert text to binary
    if mode == "encrypt":
        binary_text = text_to_bin(input_text)
        if len(binary_text) < 64:
            binary_text += [0] * (64 - len(binary_text))
        elif len(binary_text) > 64:
            binary_text = binary_text[:64]

        key = [0] * 48
        cipher_text = des_encrypt(binary_text, key)
        cipher_text_str = ''.join(str(b) for b in cipher_text)
        print("Cipher Text:", cipher_text_str)

    elif mode == "decrypt":
        # Convert binary string to list of integers
        binary_text = [int(b) for b in input_text]
        if len(binary_text) != 64:
            print("Input binary text must be exactly 64 bits")
            return
        
        key = [0] * 48
        decrypted_text_binary = des_decrypt(binary_text, key)
        decrypted_text = bin_to_text(decrypted_text_binary)
        print("Decrypted Text:", decrypted_text)

    else:
        print("Invalid mode. Use 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()
