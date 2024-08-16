'''
Program ini membantu pengguna untuk membuka blokir dan memblokir situs web di windows menggunakan file host.

'''

import platform
import os
import sys
# 1. **Mengimpor Modul:**
#    - `import platform`: Modul ini menyediakan cara portabel untuk berinteraksi dengan sistem operasi yang mendasarinya.
#    - `import os`: Modul ini menyediakan cara portabel untuk menggunakan fungsionalitas yang bergantung pada sistem operasi.
#    - `import sys`: Modul ini memberikan akses ke beberapa variabel yang digunakan atau dipelihara oleh interpreter Python.

url=''

# 2. **Variabel Global:**
#    - `url = ''`: Variabel ini diinisialisasi sebagai string kosong dan dimaksudkan untuk menyimpan URL yang dimasukkan oleh pengguna.

# 3.definisi fungsi: 
 
# Berfungsi untuk memeriksa apakah program berjalan pada os windows atau tidak.
def check_w():
    if platform.system().lower() != 'windows':
       return 1
    return 0
# - `check_w()`: Fungsi ini memeriksa apakah program berjalan di sistem operasi Windows. Ini mengembalikan 0 jika berjalan di Windows, jika tidak mengembalikan 1.
#   

# Berfungsi untuk menjeda program.
def pause():
   x = input('\nTekan kunci apa pun untuk melanjutkan...')
   if check_w() == 0:
      os.system('cls')
   else:
      os.system('clear')
# - `pause()`: Menunda eksekusi program hingga pengguna menekan tombol apa pun. Membersihkan layar jika berjalan di Windows, jika tidak membersihkan layar terminal.
      
# Berfungsi untuk mendapatkan URL website sebagai input dari user.
def get_url():
    x = input('\nMAsukan Situs web Yang akan diblokir:')
    return x
 #    - `get_url()`: Meminta pengguna untuk memasukkan URL situs web dan mengembalikan input tersebut.

# Berfungsi untuk memblokir url yang diberikan sebagai input.
def engine(url):
 
    # Kode untuk mendapatkan domain dari situs web.
    if url.startswith('https://'):
               url = url[8:]
    elif url.startswith('http://'):
               url = url[7:]
               
    
      
    # Membuat file batch untuk memblokir situs web dengan mengarahkannya ke host lokal menggunakan file host.
    with open('script.bat','a') as f:
          f.write('echo 127.0.0.1 '+url+' >>C:\\Windows\\System32\\drivers\\etc\\hosts \n')

          #    - `engine(url)`: Mengambil URL sebagai input, mengekstrak domain, dan menulis skrip batch (`script.bat`) untuk memblokir situs web dengan mengarahkannya ke localhost menggunakan file hosts.


# Berfungsi untuk mengimpor url blocklisted dari file teks.
def import_text_file():
  if os.path.exists('script.bat'):
    os.remove("script.bat")
  file = input('\nMasukan File:')
  if os.path.exists(file):
    with open(file) as f:
      for line in f:
        engine(line.strip())
    print('Silakan jalankan script.bat yang dihasilkan sebagai administrator ...')
  else:
    print('File TIdak di temukan!\n')
  pause()
  menu()
  sys.exit()
 #    - `import_text_file()`: Memungkinkan impor URL yang diblokir dari file teks. Membaca setiap baris dari file, dan memanggil `engine()` untuk memblokir setiap URL.

# Block internet.
def internetblock():
    os.system('ipconfig /release')
    os.system('cls')
    print('\nInternet sekarang diblokir...')
    pause()
    menu()
    sys.exit()
    #    - `internetblock()`: Memblock akses internet dengan melepas konfigurasi IP.

 
# Unblock Internet
def internetunblock():
    os.system('ipconfig /renew')
    os.system('cls')
    print('\nInternet sekarang tidak diblokir...')
    pause()
    menu()
    sys.exit()
    #    - `internetunblock()`: Membuka blokir akses internet dengan memperbarui konfigurasi IP.
 
 
# Berfungsi untuk menghapus semua Aturan Pemblokiran untuk website.
def unblockall():

    # Membuat file batch windows untuk memotong file host.
    with open('script.bat','w') as f:
           f.write('echo #>C:\\Windows\\System32\\drivers\\etc\\hosts')
    print('Silakan jalankan script.bat yang dihasilkan sebagai administrator untuk menghapus semua situs web yang diblokir.')
    pause()
    menu()
    sys.exit()
    #    - `unblockall()`: Menghapus semua aturan pemblokiran untuk situs web dengan memotong file hosts.

 
# Berfungsi untuk memblokir situs web tertentu..
def block():
    url = get_url()
 
    # Kode untuk mendapatkan domain dari situs web.
    if url.startswith('https://'):
               url = url[8:]
    elif url.startswith('http://'):
               url = url[7:]
                 
    # Membuat file batch untuk memblokir situs web dengan mengarahkannya ke host lokal menggunakan file host.
    with open('script.bat','w') as f:
          f.write('echo 127.0.0.1 '+url+' >>C:\\Windows\\System32\\drivers\\etc\\hosts\n')
    print('Silakan jalankan script.bat yang dihasilkan sebagai administrator untuk memblokir situs web.')
    pause()
    menu()
    sys.exit()
    #    - `block()`: Meminta pengguna untuk URL situs web, mengekstrak domain, dan menulis skrip batch untuk memblokir situs web.


# Berfungsi untuk membuka blokir situs web yang diblokir.
def unblock():
    flag = 0
    blocklist = []
    url = input('\nMasukkan situs web untuk membuka blokir:')
    if url.startswith('https://'):
               url = url[8:]
    elif url.startswith('http://'):
               url = url[7:]
       
    with open('C:\\Windows\\System32\\drivers\\etc\\hosts','r') as f:
       for line in f:
           if len(line.strip())>9:
                 blocklist.append(line.split()[1])
                 
    with open('script.bat','w') as f:
           f.write('echo #>C:\\Windows\\System32\\drivers\\etc\\hosts\n')
    for i in blocklist:
       if url !=i :
          flag += 1
          with open('script.bat','a') as f:
             f.write('echo 127.0.0.1 '+i+' >>C:\\Windows\\System32\\drivers\\etc\\hosts\n')
    if flag == len(blocklist):
         print('Situs web yang dimasukkan tidak diblokir!')
         if os.path.exists('script.bat'):
            os.remove('script.bat')
            pause()
            menu()
            sys.exit()
             
    print('\nSilakan jalankan skrip script.bat sebagai administrator untuk melanjutkan...')
    pause()
    menu()
    sys.exit()
    #    - `unblock()`: Meminta pengguna untuk URL situs web, membaca file hosts saat ini, menghapus entri untuk URL yang ditentukan, dan menulis skrip batch untuk memperbarui file hosts.
       
              
# Berfungsi untuk menampilkan domain yang sedang diblokir.
def display():
    mark=0
    print('\n===Situs Web yang Diblokir Saat Ini===\n')
    with open('C:\\Windows\\System32\\drivers\\etc\\hosts','r') as f:
        for line in f:
            if line.startswith('#') is False and len(line.strip()) > 9:
                print(line.split()[1])
                mark=1

    if mark==0:
       print(" tidak ada Situs Web yang Diblokir!")
    pause()
    menu()
    sys.exit()
    #    - `display()`: Menampilkan situs web yang saat ini diblokir dengan membaca file hosts.


# Berfungsi untuk mengimpor hostfile.
def import_hostfile():
  print('\nPeringatan: Pastikan Anda mempercayai hostfile yang Anda impor yang mungkin berisi malware\n\n')
  file=input('Masukkan hostfile Location yang akan diimpor:')
  if os.path.exists(file):
    with open('script.bat','w') as f:
      f.write('move \"'+os.getcwd()+'\\'+file+'\" C:\\Windows\\System32\\drivers\\etc\\hosts')
    print('\nSilakan jalankan skrip script.bat sebagai administrator untuk melanjutkan...')
  else:
    print('FIle TIdak Ditemukan!\n')
  pause()
  menu()
  sys.exit()
  #    - `import_hostfile()`: Memungkinkan mengimpor file host untuk memblokir situs web. Menulis skrip batch untuk memindahkan file host ke lokasi file host sistem.


# Berfungsi untuk mengekspor bermusuhan ke direktori kerja saat ini.
def export_hostfile():
  with open('script.bat','w') as f:
     f.write('copy C:\\Windows\\System32\\drivers\\etc\\hosts \"'+os.getcwd()+'\"')
  print('\nSilakan jalankan skrip script.bat sebagai administrator untuk melanjutkan...')
  pause()
  menu()
  sys.exit()
  #    - `export_hostfile()`: Memungkinkan mengekspor file host ke direktori kerja saat ini.

       
# Berfungsi untuk menampilkan menu.
def menu():
    if check_w() != 0:
     print('Platform tidak didukung!\nTekan sembarang tombol untuk melanjutkan...')
     sys.exit(0)
    os.system('cls')
    print('\n\t===Pemblokir Situs Web Sederhana===')
    print('\n\n1)Blokir Situs Web')
    print('2)Buka Situs Web Yang Di blokir')
    print('3)Menampilkan situs web yang diblokir')
    print('4)Hapus semua Aturan untuk memblokir Situs Web')
    print('5)Blokir Koneksi Internet')
    print('6)Buka Blokir Koneksi Internet')
    print('7)Impor Daftar Blokir Situs Web dari File teks')
    print('8)Impor File Host')
    print('9)Expor File Host')
    
    x = input('\nMasukan Pilihan:')
    if x == '1':
       block()
    elif x == '2':
       unblock()
    elif x == '3':
       display()
    elif x == '4':
       unblockall()
    elif x == '5':
       internetblock()
    elif x == '6':
       internetunblock()
    elif x == '7':
       import_text_file()
    elif x == '8':
       import_hostfile()
    elif x == '9':
       export_hostfile()
    elif x.lower() == 'c' or x.lower() == 'close':
       sys.exit()
    else:
        print('PIlihan Salah!')
        x = input('Tekan sembarang tombol untuk melanjutkan...')
        menu()
        #    - `menu()`: Menampilkan menu utama dan menangani input pengguna untuk menjalankan fungsi yang sesuai.
 
menu()
# 4. **Panggilan Fungsi Menu:**
#    - `menu()`: Memanggil fungsi `menu()` untuk memulai program.
