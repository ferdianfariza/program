"""
Program Kriptografi - Tugas 4: Caesar & Monoalphabetic Cipher
Enkripsi data mahasiswa menggunakan kombinasi dua algoritma.
Ferdian Nur Fariza - A11.2023.15074
"""

import random

class CaesarCipher:
    """Implementasi Caesar Cipher"""
    
    @staticmethod
    def encrypt(plaintext: str, shift: int) -> str:
        """Enkripsi menggunakan Caesar Cipher"""
        result = ""
        for char in plaintext:
            if char.isalpha():
                start = ord('A') if char.isupper() else ord('a')
                shifted = (ord(char) - start + shift) % 26
                result += chr(start + shifted)
            else:
                result += char
        return result
    
    @staticmethod
    def decrypt(ciphertext: str, shift: int) -> str:
        """Dekripsi Caesar Cipher"""
        return CaesarCipher.encrypt(ciphertext, -shift)

class MonoalphabeticCipher:
    """Implementasi Monoalphabetic Substitution Cipher"""
    
    def __init__(self, key: str = None):
        """
        key: 26 karakter substitusi untuk A-Z
        Jika None, akan generate random key
        """
        if key is None:
            alphabet = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
            random.shuffle(alphabet)
            self.key = ''.join(alphabet)
        else:
            self.key = key.upper()
        
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.decrypt_key = str.maketrans(self.key, self.alphabet)
        self.encrypt_key = str.maketrans(self.alphabet, self.key)
    
    def encrypt(self, plaintext: str) -> str:
        """Enkripsi menggunakan Monoalphabetic Cipher"""
        result = []
        for char in plaintext:
            if char.upper() in self.alphabet:
                is_lower = char.islower()
                encrypted = char.upper().translate(self.encrypt_key)
                result.append(encrypted.lower() if is_lower else encrypted)
            else:
                result.append(char)
        return ''.join(result)
    
    def decrypt(self, ciphertext: str) -> str:
        """Dekripsi Monoalphabetic Cipher"""
        result = []
        for char in ciphertext:
            if char.upper() in self.alphabet:
                is_lower = char.islower()
                decrypted = char.upper().translate(self.decrypt_key)
                result.append(decrypted.lower() if is_lower else decrypted)
            else:
                result.append(char)
        return ''.join(result)

class MahasiswaEncryption:
    """Sistem enkripsi data mahasiswa menggunakan kombinasi Caesar dan Monoalphabetic"""
    
    def __init__(self, caesar_shift: int = 3, mono_key: str = None):
        self.caesar = CaesarCipher()
        self.mono = MonoalphabeticCipher(mono_key)
        self.caesar_shift = caesar_shift
    
    def encrypt_data(self, nama: str, nim: str, jurusan: str) -> dict:
        """Enkripsi data mahasiswa dengan double encryption"""
        # Pertama enkripsi dengan Caesar kemudian Monoalphabetic
        return {
            'nama': self.mono.encrypt(self.caesar.encrypt(nama, self.caesar_shift)),
            'nim': self.mono.encrypt(self.caesar.encrypt(nim, self.caesar_shift)),
            'jurusan': self.mono.encrypt(self.caesar.encrypt(jurusan, self.caesar_shift))
        }
    
    def decrypt_data(self, encrypted_data: dict) -> dict:
        """Dekripsi data mahasiswa"""
        # Pertama dekripsi dengan Monoalphabetic kemudian Caesar
        return {
            'nama': self.caesar.decrypt(self.mono.decrypt(encrypted_data['nama']), self.caesar_shift),
            'nim': self.caesar.decrypt(self.mono.decrypt(encrypted_data['nim']), self.caesar_shift),
            'jurusan': self.caesar.decrypt(self.mono.decrypt(encrypted_data['jurusan']), self.caesar_shift)
        }

def main():
    print("=" * 60)
    print("PROGRAM KRIPTOGRAFI - TUGAS 4: DATA MAHASISWA")
    print("=" * 60)
    
    nama = input("Masukkan Nama: ")
    nim = input("Masukkan NIM: ")
    jurusan = input("Masukkan Jurusan: ")
    shift = int(input("Masukkan Caesar Shift (angka, misal 3): "))
    
    encryptor = MahasiswaEncryption(caesar_shift=shift)
    
    print("\n" + "-"*30)
    print("Data Original:")
    print(f"Nama: {nama}")
    print(f"NIM: {nim}")
    print(f"Jurusan: {jurusan}")
    
    # Enkripsi
    encrypted = encryptor.encrypt_data(nama, nim, jurusan)
    
    print("\nData Terenkripsi:")
    for key, value in encrypted.items():
        print(f"{key.capitalize()}: {value}")
    
    print(f"\nKunci Monoalphabetic (Gunakan ini untuk dekripsi): {encryptor.mono.key}")
    
    # Dekripsi
    decrypted = encryptor.decrypt_data(encrypted)
    
    print("\nData Terdekripsi:")
    for key, value in decrypted.items():
        print(f"{key.capitalize()}: {value}")
    print("=" * 60)

if __name__ == "__main__":
    main()
