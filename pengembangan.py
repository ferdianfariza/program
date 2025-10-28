def kolom_permutasi_cipher(plaintext, key):
    plaintext = plaintext.replace(" ", "").upper()
    key = key.upper()
    
    if not key:
        raise ValueError("Kunci tidak boleh kosong")
    
    key_len = len(key)
    
    pad_len = (-len(plaintext)) % key_len
    plaintext += "X" * pad_len
    
    n_rows = len(plaintext) // key_len
    
    matrix = []
    for i in range(n_rows):
        start = i * key_len
        row = list(plaintext[start:start + key_len])
        matrix.append(row)

    sorted_key = sorted(enumerate(key), key=lambda x: x[1])
    base_order = [index for index, _ in sorted_key]
    
    ciphertext = ""
    
    for col_pos, col_idx in enumerate(base_order):
        column = [matrix[row][col_idx] for row in range(n_rows)]
        
        if col_pos % 2 == 1:
            column.reverse()
            
        ciphertext += "".join(column)
    
    return ciphertext
 
def kolom_permutasi_decipher(ciphertext, key):
    ciphertext = ciphertext.upper()
    key = key.upper()
    
    if not key:
        raise ValueError("Kunci tidak boleh kosong")
    
    key_len = len(key)
    total_chars = len(ciphertext)
    
    if total_chars % key_len != 0:
        raise ValueError("Ciphertext panjangnya harus kelipatan panjang kunci")
    
    n_rows = total_chars // key_len
    
    sorted_key = sorted(enumerate(key), key=lambda x: x[1])
    base_order = [index for index, _ in sorted_key]

    matrix = [['' for _ in range(key_len)] for _ in range(n_rows)]
    
    idx = 0
    
    for col_pos, col_idx in enumerate(base_order):
        if col_pos % 2 == 1:

            temp_col = []
            for _ in range(n_rows):
                temp_col.append(ciphertext[idx])
                idx += 1
            temp_col.reverse()
            for row in range(n_rows):
                matrix[row][col_idx] = temp_col[row]
        else:
            for row in range(n_rows):
                matrix[row][col_idx] = ciphertext[idx]
                idx += 1
    
    plaintext = ''.join(''.join(row) for row in matrix)
    return plaintext


# Enkripsi
plaintext = "ATTACKATDAWN"
key = "KEY"
cipher = kolom_permutasi_cipher(plaintext, key)
print("Plaintext :", plaintext)
print("Ciphertext:", cipher)

# Dekripsi
decrypted = kolom_permutasi_decipher(cipher, key)
print("Decrypted :", decrypted)