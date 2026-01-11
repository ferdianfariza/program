"""
Program Kriptografi - Tugas 5: CFB (Cipher Feedback)
Implementasi mode operasi CFB.
"""

def xor_bytes(a: bytes, b: bytes) -> bytes:
    """XOR dua bytes"""
    return bytes(x ^ y for x, y in zip(a, b))

def simple_block_cipher(block: bytes, key: bytes) -> bytes:
    """Simple block cipher untuk demonstrasi (XOR dengan key)"""
    return xor_bytes(block, key)

def simple_block_decipher(block: bytes, key: bytes) -> bytes:
    """Simple block decipher"""
    return xor_bytes(block, key)

class CFB:
    """Cipher Feedback Mode"""
    
    def __init__(self, key: bytes, iv: bytes, block_size: int = 8):
        self.key = key
        self.iv = iv
        self.block_size = block_size
    
    def encrypt(self, plaintext: bytes) -> bytes:
        """Enkripsi dengan CFB mode"""
        ciphertext = b''
        shift_register = self.iv
        
        for i in range(0, len(plaintext), self.block_size):
            # Encrypt shift register
            encrypted_sr = simple_block_cipher(shift_register, self.key)
            
            # Get plaintext block
            block = plaintext[i:i+self.block_size]
            
            # XOR dengan encrypted shift register
            cipher_block = xor_bytes(block, encrypted_sr[:len(block)])
            ciphertext += cipher_block
            
            # Update shift register
            shift_register = shift_register[len(cipher_block):] + cipher_block
            if len(shift_register) < self.block_size:
                shift_register += b'\x00' * (self.block_size - len(shift_register))
        
        return ciphertext
    
    def decrypt(self, ciphertext: bytes) -> bytes:
        """Dekripsi dengan CFB mode"""
        plaintext = b''
        shift_register = self.iv
        
        for i in range(0, len(ciphertext), self.block_size):
            # Encrypt shift register
            encrypted_sr = simple_block_cipher(shift_register, self.key)
            
            # Get cipher block
            block = ciphertext[i:i+self.block_size]
            
            # XOR untuk mendapatkan plaintext
            plain_block = xor_bytes(block, encrypted_sr[:len(block)])
            plaintext += plain_block
            
            # Update shift register dengan ciphertext
            shift_register = shift_register[len(block):] + block
            if len(shift_register) < self.block_size:
                shift_register += b'\x00' * (self.block_size - len(shift_register))
        
        return plaintext

def main():
    print("=" * 60)
    print("PROGRAM KRIPTOGRAFI - TUGAS 5: CFB Mode")
    print("=" * 60)
    
    text = input("Masukkan teks yang akan dienkripsi: ")
    plaintext = text.encode()
    
    key_str = input("Masukkan Kunci (8 karakter): ")
    if len(key_str) < 8: key_str = key_str.ljust(8, '0')
    key = key_str[:8].encode()
    
    iv_str = input("Masukkan IV (8 karakter): ")
    if len(iv_str) < 8: iv_str = iv_str.ljust(8, '0')
    iv = iv_str[:8].encode()
    
    print(f"\nPlaintext: {text}")
    print(f"Key: {key_str[:8]}")
    print(f"IV: {iv_str[:8]}")
    
    # CFB Mode
    print("\n" + "-"*30)
    print("Mengeksekusi CFB Mode...")
    cfb = CFB(key, iv)
    cfb_encrypted = cfb.encrypt(plaintext)
    print(f"CFB Encrypted (hex): {cfb_encrypted.hex()}")
    
    cfb_decrypted = cfb.decrypt(cfb_encrypted)
    print(f"CFB Decrypted: {cfb_decrypted.decode()}")
    print("=" * 60)

if __name__ == "__main__":
    main()
