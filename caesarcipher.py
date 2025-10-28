from tkinter import *

# Cipher
def caesarcipher(data, nilai):
    array = []
    for char in data:
        result = 0
        if ord(char) == 32:  # space
            result = 32
        else:
            if 65 <= ord(char) <= 90:
                result = (ord(char) - 65 + nilai) % 26 + 65
            elif 97 <= ord(char) <= 122:
                result = (ord(char) - 97 + nilai) % 26 + 97
            else:
                result = ord(char)
        array.append(chr(result))
    return "".join(array)

def caesarcipheradd(data):
    array = []
    for char in data:
        if ord(char) == 32:
            array.append(" ")
            continue
        if 65 <= ord(char) <= 90:
            nilai = (ord(char) - 65) + 1
            result = (ord(char) - 65 + nilai) % 26 + 65
            array.append(chr(result))
        elif 97 <= ord(char) <= 122:
            nilai = (ord(char) - 97) + 1
            result = (ord(char) - 97 + nilai) % 26 + 97
            array.append(chr(result))
        else:
            array.append(char)
    return "".join(array)


def decrypt(data, nilai):
    return caesarcipher(data, -nilai)


def decryptadd_with_ref(encrypted2, encrypted1):
    result = []
    for e, ref in zip(encrypted2, encrypted1):
        if e == " ":
            result.append(" ")
        elif 65 <= ord(e) <= 90:
            shift = ord(ref) - 64
            val = (ord(e) - 65 - shift) % 26 + 65
            result.append(chr(val))
        elif 97 <= ord(e) <= 122:
            shift = ord(ref) - 96
            val = (ord(e) - 97 - shift) % 26 + 97
            result.append(chr(val))
        else:
            result.append(e)
    return "".join(result)


def decryptadd_bruteforce(encrypted2):
    array = []
    for e in encrypted2:
        if e == " ":
            array.append(" ")
            continue
        if 65 <= ord(e) <= 90:
            found = False
            for possible in range(65, 91):  # A..Z
                nilai = possible - 64
                result = (possible - 65 + nilai) % 26 + 65
                if chr(result) == e:
                    array.append(chr(possible))
                    found = True
                    break
            if not found:
                array.append("?")
        elif 97 <= ord(e) <= 122:
            found = False
            for possible in range(97, 123):  # a..z
                nilai = possible - 96
                result = (possible - 97 + nilai) % 26 + 97
                if chr(result) == e:
                    array.append(chr(possible))
                    found = True
                    break
            if not found:
                array.append("?")
        else:
            array.append(e)
    return "".join(array)

# GUI
root = Tk()
root.title("Caesar Cipher Ganda (GUI)")
root.geometry('520x320')
root.resizable(False, False)

# Stored 
last_enkripsi1 = None
last_enkripsi2 = None

# Button
def encryptClick():
    global last_enkripsi1, last_enkripsi2
    string = text1.get()
    try:
        integer = int(txt2.get())
    except ValueError:
        resDisplay.config(text="Key harus angka!", fg="red")
        return

    if not string:
        resDisplay.config(text="Masukkan teks terlebih dahulu!", fg="red")
        return

    enkripsi1 = caesarcipher(string, integer)
    enkripsi2 = caesarcipheradd(enkripsi1)
    last_enkripsi1 = enkripsi1
    last_enkripsi2 = enkripsi2

    result = (
        f"Enkripsi 1 : {enkripsi1}\n"
        f"Enkripsi 2 : {enkripsi2}\n\n"
        f"[Disimpan sebagai referensi untuk dekripsi]"
    )
    resDisplay.config(text=result, fg="black")


def decryptClick():
    global last_enkripsi1, last_enkripsi2
    string = text1.get()
    try:
        integer = int(txt2.get())
    except ValueError:
        resDisplay.config(text="Key harus angka!", fg="red")
        return

    if not string:
        if last_enkripsi2 is None:
            resDisplay.config(text="Tidak ada input untuk didekripsi dan tidak ada data tersimpan.", fg="red")
            return
        encrypted2 = last_enkripsi2
        method = "stored_ref"
    else:
        encrypted2 = string
        if last_enkripsi1 is not None and len(last_enkripsi1) == len(encrypted2):
            method = "stored_ref"
        else:
            method = "bruteforce"

    if method == "stored_ref":
        ref = last_enkripsi1
        dekripsi2 = decryptadd_with_ref(encrypted2, ref)
    else:
        dekripsi2 = decryptadd_bruteforce(encrypted2)

    dekripsi1 = decrypt(dekripsi2, integer)

    result = (
        f"Method       : {method}\n"
        f"Enkripsi 2   : {encrypted2}\n"
        f"Dekripsi 2   : {dekripsi2}\n"
        f"Dekripsi 1   : {dekripsi1}"
    )
    resDisplay.config(text=result, fg="black")


# Layout
Label(root, text="Masukkan teks (plaintext atau Enkripsi tahap 2):").pack(pady=6)
text1 = Entry(root, width=60)
text1.pack()

Label(root, text="Masukkan nilai kunci (integer):").pack(pady=6)
txt2 = Entry(root, width=60)
txt2.pack()

frame = Frame(root)
frame.pack(pady=12)

Button(frame, text="Encrypt", width=18, command=encryptClick).grid(row=0, column=0, padx=6)
Button(frame, text="Decrypt", width=18, command=decryptClick).grid(row=0, column=1, padx=6)

resDisplay = Label(root, text="", justify=LEFT, font=("Consolas", 10), anchor="w")
resDisplay.pack(padx=8, pady=8, fill="both")

root.mainloop()
