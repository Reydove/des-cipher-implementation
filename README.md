<<<<<<< HEAD
# des-cipher-implementation
=======
 DES Cipher Implementation

This repository contains an implementation of the Data Encryption Standard (DES) cipher in Python. The DES cipher is a symmetric-key algorithm for the encryption of digital data. This implementation allows for both encryption and decryption of 64-bit blocks of text using a simplified DES process.

 Table of Contents
- [Introduction]
- [Features]
- [Requirements]
- [Usage]
- [How It Works]
- [Contributing]
- [License]

Introduction
The Data Encryption Standard (DES) is a widely used method of data encryption that utilizes a symmetric key for encrypting and decrypting data. This Python implementation demonstrates the fundamental concepts of DES, including initial and final permutations, expansion, substitution using S-boxes, and the Feistel structure.

Features
- Encrypt a 64-bit block of text.
- Decrypt a 64-bit block of text.
- Simple and easy-to-understand Python code.

 Requirements

- Python 3.12.5

Usage

Clone the Repository
```bash
git clone https://github.com/mobolaji-habib/des-cipher-implementation.git
cd des_cipher_env

Running the Script
To run the script, use the following command in your terminal:

For Encryption:
python des_cipher.py encrypt "Your 64-bit plain text here"


For Decryption:
python des_cipher.py decrypt "Your 64-bit cipher text here"



How It Works

-Initial Permutation (IP): The input 64-bit block is permuted according to the IP table.
-Feistel Rounds: The block is divided into two halves, and the right half is expanded, XORed with a subkey, substituted using S-boxes, permuted, and then XORed with the left half.
-Final Permutation (IP^-1): After 16 rounds, the halves are swapped and combined, followed by the inverse permutation to get the final cipher text.
Contributing
Contributions are welcome! Feel free to fork this repository, make changes, and submit a pull request.
