# Inisialisasi daftar data mahasiswa
data_mahasiswa = []

# Fungsi untuk menambah data mahasiswa
def tambah():
    nama = input("Masukkan nama mahasiswa: ")
    nilai = float(input("Masukkan nilai mahasiswa: "))
    data_mahasiswa.append({"nama": nama, "nilai": nilai})
    print("Data berhasil ditambahkan.\n")

# Fungsi untuk menampilkan data mahasiswa
def tampilkan():
    if data_mahasiswa:
        print("\nDaftar Nilai Mahasiswa:")
        for i, mahasiswa in enumerate(data_mahasiswa, 1):
            print(f"{i}. Nama: {mahasiswa['nama']}, Nilai: {mahasiswa['nilai']}")
    else:
        print("\nBelum ada data mahasiswa.\n")

# Fungsi untuk menghapus data mahasiswa berdasarkan nama
def hapus(nama):
    global data_mahasiswa
    data_mahasiswa = [m for m in data_mahasiswa if m['nama'] != nama]
    print(f"Data mahasiswa bernama '{nama}' telah dihapus.\n")

# Fungsi untuk mengubah data mahasiswa berdasarkan nama
def ubah(nama):
    for mahasiswa in data_mahasiswa:
        if mahasiswa['nama'] == nama:
            mahasiswa['nilai'] = float(input(f"Masukkan nilai baru untuk {nama}: "))
            print(f"Data nilai mahasiswa '{nama}' telah diperbarui.\n")
            return
    print(f"Data mahasiswa dengan nama '{nama}' tidak ditemukan.\n")

# Program utama
while True:
    print("\nMenu:")
    print("1. Tambah Data")
    print("2. Tampilkan Data")
    print("3. Hapus Data")
    print("4. Ubah Data")
    print("5. Keluar")
    pilihan = input("Pilih menu (1-5): ")

    if pilihan == "1":
        tambah()
    elif pilihan == "2":
        tampilkan()
    elif pilihan == "3":
        nama = input("Masukkan nama mahasiswa yang ingin dihapus: ")
        hapus(nama)
    elif pilihan == "4":
        nama = input("Masukkan nama mahasiswa yang ingin diubah: ")
        ubah(nama)
    elif pilihan == "5":
        print("Program selesai.")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.\n")