#!/usr/bin/env python
# coding: utf-8

# In[7]:


# Nama : Clariva Meydieta Widagdo
# NIM : V3922012
# Kelas TI D

# AFFINE CHIPER Menggunakan kunci program 1 dan 2 karena angka terakhir nomor telepong saya 1 dan 2 (0858-7725-7312)
# VIGENERE CHIPER Menggunakan kunci program Clariva karena nama panggilan saya clariva


# SOURCE CODE
# Fungsi untuk menghitung modulus inverse a modulo m.
def mod_inverse(a, m):
    # Fungsi ini mencari nilai invers modulo dari a terhadap m.
    for x in range(1, m):
        if (a * x) % m == 1:
            return x  # Jika ditemukan, kembalikan nilai invers modulo
    return None  # Jika tidak ditemukan, kembalikan None

# Fungsi untuk melakukan enkripsi menggunakan affine cipher.
def affine_encrypt(plain_text, key_a, key_b):
    encrypted_text = ""
    for char in plain_text:
        if char.isalpha():
            char_idx = ord(char) - ord('A')  # Mengubah huruf menjadi indeks (A=0, B=1, ...).
            encrypted_idx = (key_a * char_idx + key_b) % 26  # Rumus enkripsi affine.
            encrypted_char = chr(encrypted_idx + ord('A'))  # Mengubah indeks kembali menjadi huruf.
            encrypted_text += encrypted_char
        else:
            encrypted_text += char  # Menambahkan karakter selain huruf tanpa perubahan.
    return encrypted_text # mengembalikan enkripsi teks

# Fungsi untuk melakukan dekripsi menggunakan affine cipher.
def affine_decrypt(encrypted_text, key_a, key_b):
    decrypted_text = ""
    key_a_inv = mod_inverse(key_a, 26)  # Menghitung modulus inverse untuk kunci a.
    if key_a_inv is None:
        return "Kunci tidak valid."  # Memeriksa apakah kunci a memiliki modulus inverse.

    for char in encrypted_text:
        if char.isalpha():
            char_idx = ord(char) - ord('A')  # Mengubah huruf menjadi indeks (A=0, B=1, ...).
            decrypted_idx = (key_a_inv * (char_idx - key_b)) % 26  # Rumus dekripsi affine.
            decrypted_char = chr(decrypted_idx + ord('A'))  # Mengubah indeks kembali menjadi huruf.
            decrypted_text += decrypted_char 
        else:
            decrypted_text += char  # Menambahkan karakter selain huruf tanpa perubahan.
    return decrypted_text # mengembalikan deskripsi teks

# Membuat fungsi untuk menghasilkan Tabula Recta
def generate_tabula_recta(): #deklarasi n=menggunakan tabula recta dalam program
    tabula_recta = [[chr((i + j) % 26 + 65) for i in range(26)] for j in range(26)] # menginisialisasi Tabula Recta
    return tabula_recta # mengembalikan hasil tabula recta

# Fungsi untuk melakukan enkripsi menggunakan metode Vigenère Cipher
def vigenere_encrypt(plain_text, key, tabula_recta):
    # Mengonversi plain_text dan key menjadi huruf kapital
    plain_text = plain_text.upper() 
    key = key.upper() # Mengubah teks masukan plain_text dan key menjadi huruf kapital
    encrypted_text = "" # Inisialisasi variabel encrypted_text untuk menyimpan teks terenkripsi

    for i in range(len(plain_text)):
        if plain_text[i] == ' ':
            # Jika karakter adalah spasi, tambahkan spasi ke teks terenkripsi
            encrypted_text += ' '
        else:
            # Menghitung indeks x dari key dan y dari plain_text
            x = ord(key[i % len(key)]) - 65
            y = ord(plain_text[i]) - 65
            # Mengambil karakter terenkripsi dari Tabula Recta
            encrypted_char = tabula_recta[x][y]
            # Menambahkan karakter terenkripsi ke teks terenkripsi
            encrypted_text += encrypted_char

    return encrypted_text

# Fungsi untuk melakukan dekripsi menggunakan metode Vigenère Cipher
def vigenere_decrypt(encrypted_text, key, tabula_recta):
    encrypted_text = encrypted_text.upper()
    key = key.upper() # Mengubah teks masukan plain_text dan key menjadi huruf kapital
    decrypted_text = "" # Inisialisasi variabel descrypted_text untuk menyimpan teks terenkripsi

    for i in range(len(encrypted_text)):
    # Melakukan iterasi melalui semua karakter dalam teks terenkripsi
        if encrypted_text[i] == ' ':
            decrypted_text += ' '
        # Jika karakter adalah spasi, tambahkan spasi ke teks terdekripsi
        else:
        # Jika bukan spasi, lanjutkan ke langkah dekripsi
            x = ord(key[i % len(key)]) - 65
        # Menghitung indeks x yang digunakan untuk mencari dalam Tabula Recta
            for y in range(26):
            # Melakukan iterasi melalui semua kemungkinan nilai y (indeks kolom dalam Tabula Recta)
                if tabula_recta[x][y] == encrypted_text[i]:
                    # Memeriksa apakah karakter terenkripsi cocok dengan Tabula Recta
                    decrypted_char = chr(y + 65)
                    # Jika cocok, ambil karakter yang sesuai dari alfabet
                    decrypted_text += decrypted_char
                    # Tambahkan karakter terdekripsi ke teks terdekripsi
                    break
                # Hentikan pencarian setelah karakter terdekripsi ditemukan

    return decrypted_text # mengembalikan nilai deskripsi

# Loop utama untuk mengatur pilihan enkripsi atau dekripsi.
while True:
    print("Selamat datang di Program Enkripsi-Dekripsi!") # cetak judul

    
    # membuat opsi enkripsi dan deskripsi
    choice = input("Pilih operasi:\n1. Affine Enkripsi\n2. Vigenère Enkripsi\n3. Vigenère Dekripsi\n4. Affine Dekripsi\nPilihan (1/2/3/4): ")
    if choice not in ['1', '2', '3', '4']: # selain memilih 1-4
        print("Pilihan tidak valid. Silakan pilih 1, 2, 3, atau 4.") # muncul kalimat tidak valid
        continue

    if choice in ['1', '4']: # untuk opsi 1 dan 4 
        try:
            key_a = int(input("Masukkan nilai kunci a (bilangan bulat): ")) # memasukkan kunci numerik a
            key_b = int(input("Masukkan nilai kunci b (bilangan bulat): ")) # memasukkan kunci numerik b
        except ValueError: # jika tidak
            print("Kunci harus berupa bilangan bulat.") # muncul peringatan
            continue

    if choice in ['2', '3']: # jika memilih opsi 2 dan 3
        key = input("Masukkan kunci: ") # maka masukkan kunci berupa kata, misal nama panggilan

    if choice == '1': # jika kode 1
        plain_text = input("Masukkan teks yang ingin dienkripsi: ").upper() # input teks yang akan dienkripsi
        encrypted_text = affine_encrypt(plain_text, key_a, key_b) # rumus enkripsi
        print("Teks terenkripsi:", encrypted_text) # mencetak hasil enkripsi
    elif choice == '2': # jika pilih 2
        plain_text = input("Masukkan plaintext: ") # input teks yang akan dienkripsi
        tabula_recta = generate_tabula_recta() # megenerate tabula recta
        encrypted_text = vigenere_encrypt(plain_text, key, tabula_recta) # rumus enkripsi
        print("Teks Terenkripsi:", encrypted_text) # mencetak hasil enkripsi
    elif choice == '3': # jika pilih 3
        encrypted_text = input("Masukkan teks terenkripsi: ") # input teks yang akan dideskripsi
        decrypted_text = vigenere_decrypt(encrypted_text, key, tabula_recta) # rumus deskripsi dengan tabula recta
        print("Teks Terdekripsi:", decrypted_text) # mencetak hasil deskripsi
    elif choice == '4': # jika pilih 4
        encrypted_text = input("Masukkan teks terenkripsi: ") # input teks yang akan dideskripsi
        decrypted_text = affine_decrypt(encrypted_text, key_a, key_b)# rumus deskripsi
        print("Teks Terdekripsi:", decrypted_text) # mencetak hasil deskripsi

    another = input("Lakukan operasi lainnya? (y/n): ") # melakukan perulangan
    if another.lower() != 'y': # jika tidak memilih y
        break #berhenti


# In[ ]:


SUCCESSISNOTFINALFAILUREISNOTFATALITISTHECOURAGETOCONTINUETHATCOUNTS

