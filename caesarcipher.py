import csv
import xlsxwriter

string = [
"Andi Pratama Wijaya",
"Siti Nur Aisyah",
"Budi Santoso Putra",
"Rina Maharani Dewi",
"Ahmad Fauzan Hakim",
"Dian Kartika Sari",
"Joko Tri Haryanto",
"Maya Lestari Utami",
"Rizky Aditya Pratama",
"Putri Ayu Maharani",
"Hendra Gunawan Saputra",
"Laila Nur Rahma",
"Bayu Setiawan Pratomo",
"Intan Cahya Permata",
"Arif Hidayatullah Ramadhan",
"Nanda Febri Kusuma",
"Farhan Yusuf Alamsyah",
"Mega Puspita Sari",
"Dimas Arya Nugraha",
"Nurul Fitria Zahra",
"Kevin Jonathan Prasetyo",
"Clara Melati Anggraini",
"Samuel Adrian Hartono",
"Olivia Citra Maharani",
"Rangga Pradipta Wibowo",
"Ayu Kartini Prameswari",
"Fajar Rizki Saputra",
"Melisa Anindya Putri",
"Surya Dharmawan Pratama",
"Hana Safira Khairunnisa"
]

# Function
def caesarcipher(data, nilai):
    array = []
    for char in data:
        if char == " ":
            array.append(" ")
            continue
        if 65 <= ord(char) <= 90:
            result = (ord(char) - 65 + nilai) % 26 + 65
            
        elif 97 <= ord(char) <= 122:
            result = (ord(char) - 97 + nilai) % 26 + 97
        else:
            result = ord(char)
        array.append(chr(result))
    return "".join(array)


def caesarcipheradd(data, nilai):
    array = []
    for i, char in enumerate(data):
        if char == " ":
            array.append(" ")
            continue
        if 65 <= ord(char) <= 90:
            result = (ord(char) - 65 + (i + 1) + nilai) % 26 + 65
            
        elif 97 <= ord(char) <= 122:
            result = (ord(char) - 97 + (i + 1) + nilai) % 26 + 97
        else:
            result = ord(char)
        array.append(chr(result))
    return "".join(array)


def caesarcipheradd_decrypt(data, nilai):
    array = []
    for i, char in enumerate(data):
        if char == " ":
            array.append(" ")
            continue
        if 65 <= ord(char) <= 90:
            result = (ord(char) - 65 - (i + 1) - nilai) % 26 + 65
            
        elif 97 <= ord(char) <= 122:
            result = (ord(char) - 97 - (i + 1) - nilai) % 26 + 97
            
        else:
            result = ord(char)
        array.append(chr(result))
    return "".join(array)

def caesarcipher_decrypt(data, nilai):
    array = []
    for char in data:
        if char == " ":
            array.append(" ")
            continue
        if 65 <= ord(char) <= 90:
            result = (ord(char) - 65 - nilai) % 26 + 65
            
        elif 97 <= ord(char) <= 122:
            result = (ord(char) - 97 - nilai) % 26 + 97
        else:
            result = ord(char)
        array.append(chr(result))
    return "".join(array)

# Program Input
inputkey = int(input("Key: "))
    
# CSV
# with open('caesarciphermodif.csv', mode='w',newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     reader = csv.DictReader(csvfile)
#     writer.writerow(["NO","Plaintext","Key (Int)","Caesar Cipher Modified","Decrypt"])
#     for i, text in enumerate(string, start=1):
#         encrypted = caesarcipheradd(text,inputkey)
#         writer.writerow([i, text, inputkey ,encrypted])
#     for i, text in enumerate(string, start=1):
#         encrypted2 = caesarcipheradd(text.upper(),inputkey)
#         writer.writerow([i, text.upper(), inputkey ,encrypted2])

# with open('caesarcipherbasic.csv', mode='w',newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     reader = csv.DictReader(csvfile)
#     writer.writerow(["NO","Plaintext","Key (Int)","Caesar Cipher Basic","Decrypt"])
#     for i, text in enumerate(string, start=1):
#         encrypted = caesarcipher(text,inputkey)
#         writer.writerow([i, text, inputkey ,encrypted])
#     for i, text in enumerate(string, start=1):
#         encrypted2 = caesarcipher(text.upper(),inputkey)
#         writer.writerow([i, text.upper(), inputkey ,encrypted2])

# XLSX
workbook_mod = xlsxwriter.Workbook('caesarciphermodif.xlsx')
worksheet_mod = workbook_mod.add_worksheet()

worksheet_mod.write(0,0, "NO")
worksheet_mod.write(0,1, "Plaintext")
worksheet_mod.write(0,2, "Key(int)")
worksheet_mod.write(0,3, "Caesar Cipher Modified")

row = 1
for i, text in enumerate(string, start=1):
    worksheet_mod.write(row, 0, i)
    worksheet_mod.write(row, 1, text.upper())
    worksheet_mod.write(row, 2, inputkey)
    worksheet_mod.write(row, 3, caesarcipheradd(text.upper(), inputkey))
    row += 1

workbook_mod.close()

# Bagian Basic
workbook_basic = xlsxwriter.Workbook('caesarcipherbasic.xlsx')
worksheet_basic = workbook_basic.add_worksheet()

worksheet_basic.write(0,0, "NO")
worksheet_basic.write(0,1, "Plaintext")
worksheet_basic.write(0,2, "Key(int)")
worksheet_basic.write(0,3, "Caesar Cipher Basic")

row = 1
for i, text in enumerate(string, start=1):
    worksheet_basic.write(row, 0, i)
    worksheet_basic.write(row, 1, text.upper())
    worksheet_basic.write(row, 2, inputkey)
    worksheet_basic.write(row, 3, caesarcipher(text.upper(), inputkey))
    row += 1

workbook_basic.close()
