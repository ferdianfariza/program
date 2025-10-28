# add lib
from operator import*

# tugas 1
def bin_to_ascii(data):
    chars = []
    for i in range(0, len(data), 8):
        byte = data[i:i+8]
        if len(byte) == 8:
            decimal = int(byte, 2)
            chars.append(chr(decimal))
    return ''.join(chars)


def ascii_to_bin(data):
    binary_representation = []
    for char in data:
            ascii_value = ord(char)
            binary_char = bin(ascii_value)[2:].zfill(8)
            binary_representation.append(binary_char)
    return ' '.join(binary_representation)

# tugas 2

def swap_left_new(data):
    to_biner = ascii_to_bin(data).replace(" ", "")
    decimal = int(to_biner, 2)
    swapped = decimal << 1
    return bin(swapped)[2:]

def swap_right_new(data):
    to_biner = ascii_to_bin(data).replace(" ", "")
    decimal = int(to_biner, 2)
    swapped = decimal >> 1
    return bin(swapped)


# running

# input
y = input("Masukan Biner: ")
print("Hasil Karakter:",bin_to_ascii(y))

x = input("Masukan Karakter: ")
print(ascii_to_bin(x), "-->", x, "(Hasil Biner)")



# swap left
biner_kekiri = swap_left_new(x)
array_biner_kiri = [biner_kekiri[i:i+8] for i in range(0, len(biner_kekiri), 8)]
hasil_biner_kiri = " ".join(array_biner_kiri)

# to ascii swap left
kekiri_to_ascii = bin_to_ascii(hasil_biner_kiri.replace(" ",""))

print(hasil_biner_kiri, kekiri_to_ascii)

# swap right
biner_kekanan = "00" + swap_right_new(x)[2:]
array_biner_kanan = [biner_kekanan[i:i+8] for i in range(0, len(biner_kekanan), 8)]
hasil_biner_kanan = " ".join(array_biner_kanan)

# to ascii swap right
kekanan_to_ascii = bin_to_ascii(hasil_biner_kanan.replace(" ",""))
print(hasil_biner_kanan, kekanan_to_ascii)

print(bin(ord("Ø"))[2:].zfill(10))