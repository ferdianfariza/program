"""
Program Kriptografi - Tugas 2: LFSR (Linear Feedback Shift Register)
Implementasi Keystream Cipher menggunakan LFSR.
Ferdian Nur Fariza - A11.2023.15074
"""

from typing import List

class LFSR:
    """Implementasi LFSR untuk keystream cipher"""
    
    def __init__(self, seed: str, taps: List[int]):
        """
        seed: initial state (binary string, e.g., '1011')
        taps: posisi tap untuk XOR (e.g., [3, 2] untuk x^4 + x^3 + x^2 + 1)
        """
        self.state = [int(bit) for bit in seed]
        self.taps = taps
        self.length = len(seed)
    
    def shift(self) -> int:
        """Lakukan satu shift dan return bit output"""
        feedback = 0
        for tap in self.taps:
            feedback ^= self.state[tap]
        
        output = self.state[-1]
        self.state = [feedback] + self.state[:-1]
        return output
    
    def generate_keystream(self, length: int) -> str:
        """Generate keystream sepanjang length bit"""
        return ''.join(str(self.shift()) for _ in range(length))

def lfsr_encrypt(plaintext: str, seed: str, taps: List[int]) -> tuple:
    """Enkripsi teks menggunakan LFSR keystream"""
    # Convert plaintext ke binary
    binary_plain = ''.join(format(ord(char), '08b') for char in plaintext)
    
    # Generate keystream
    lfsr = LFSR(seed, taps)
    keystream = lfsr.generate_keystream(len(binary_plain))
    
    # XOR plaintext dengan keystream
    binary_cipher = ''.join(str(int(p) ^ int(k)) for p, k in zip(binary_plain, keystream))
    
    # Convert binary ke hex untuk display
    cipher_hex = hex(int(binary_cipher, 2))[2:].upper()
    
    return cipher_hex, keystream

def lfsr_decrypt(cipher_hex: str, seed: str, taps: List[int], original_length: int) -> str:
    """Dekripsi cipher menggunakan LFSR keystream"""
    # Convert hex ke binary
    binary_cipher = bin(int(cipher_hex, 16))[2:].zfill(original_length * 8)
    
    # Generate keystream yang sama
    lfsr = LFSR(seed, taps)
    keystream = lfsr.generate_keystream(len(binary_cipher))
    
    # XOR cipher dengan keystream
    binary_plain = ''.join(str(int(c) ^ int(k)) for c, k in zip(binary_cipher, keystream))
    
    # Convert binary ke teks
    plaintext = ''.join(chr(int(binary_plain[i:i+8], 2)) for i in range(0, len(binary_plain), 8))
    
    return plaintext

def main():
    print("=" * 60)
    print("PROGRAM KRIPTOGRAFI - TUGAS 2: LFSR")
    print("=" * 60)
    
    plaintext = input("Masukkan plaintext: ")
    seed = input("Masukkan LFSR Seed (binary, misal '1011'): ")
    taps_str = input("Masukkan LFSR Taps (pisahkan dengan koma, misal '3,2'): ")
    taps = [int(t.strip()) for t in taps_str.split(',')]
    
    print(f"\nPlaintext: {plaintext}")
    print(f"LFSR Seed: {seed}")
    print(f"LFSR Taps: {taps}")
    
    cipher_hex, keystream = lfsr_encrypt(plaintext, seed, taps)
    print(f"\nCiphertext (Hex): {cipher_hex}")
    print(f"Keystream (sebagian): {keystream[:40]}...")
    
    decrypted = lfsr_decrypt(cipher_hex, seed, taps, len(plaintext))
    print(f"Decrypted: {decrypted}")
    print("=" * 60)

if __name__ == "__main__":
    main()
