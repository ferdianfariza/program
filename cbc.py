"""
Program Kriptografi - Tugas 6: CBC (Cipher Block Chaining)
Implementasi mode operasi CBC.
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

class CBC:
    """Cipher Block Chaining Mode"""
    
    def __init__(self, key: bytes, iv: bytes, block_size: int = 8):
        self.key = key
        self.iv = iv
        self.block_size = block_size
    
    def _pad(self, data: bytes) -> bytes:
        """PKCS7 padding"""
        padding_len = self.block_size - (len(data) % self.block_size)
        return data + bytes([padding_len] * padding_len)
    
    def _unpad(self, data: bytes) -> bytes:
        """Remove PKCS7 padding"""
        padding_len = data[-1]
        return data[:-padding_len]
    
    def encrypt(self, plaintext: bytes) -> bytes:
        """Enkripsi dengan CBC mode"""
        plaintext = self._pad(plaintext)
        ciphertext = b''
        previous = self.iv
        
        for i in range(0, len(plaintext), self.block_size):
            block = plaintext[i:i+self.block_size]
            xored = xor_bytes(block, previous)
            encrypted = simple_block_cipher(xored, self.key)
            ciphertext += encrypted
            previous = encrypted
        
        return ciphertext
    
    def decrypt(self, ciphertext: bytes) -> bytes:
        """Dekripsi dengan CBC mode"""
        plaintext = b''
        previous = self.iv
        
        for i in range(0, len(ciphertext), self.block_size):
            block = ciphertext[i:i+self.block_size]
            decrypted = simple_block_decipher(block, self.key)
            plaintext += xor_bytes(decrypted, previous)
            previous = block
        
        return self._unpad(plaintext)

def main():
    print("=" * 60)
    print("PROGRAM KRIPTOGRAFI - TUGAS 6: CBC Mode")
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
    
    # CBC Mode
    print("\n" + "-"*30)
    print("Mengeksekusi CBC Mode...")
    cbc = CBC(key, iv)
    cbc_encrypted = cbc.encrypt(plaintext)
    print(f"CBC Encrypted (hex): {cbc_encrypted.hex()}")
    
    cbc_decrypted = cbc.decrypt(cbc_encrypted)
    print(f"CBC Decrypted: {cbc_decrypted.decode()}")
    print("=" * 60)

if __name__ == "__main__":
    main()
