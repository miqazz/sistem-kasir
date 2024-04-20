import dataclasses
from datetime import datetime
import tempfile

menu = [
    {"jenis_menu":"minuman","nama_menu":"kopi susu","harga":15000},
    {"jenis_menu":"minuman","nama_menu":"thaitea","harga":5000},
    {"jenis_menu":"minuman","nama_menu":"jus buah","harga":5000},
    {"jenis_menu":"makanan","nama_menu":"pie pisang","harga":8000},
    {"jenis_menu":"makanan","nama_menu":"tteokbokki","harga":9000},
    {"jenis_menu":"makanan","nama_menu":"roti bakar","harga":10000}
]

member = [
    {"id":"P00001","nama_member":"Jihoon","tgl_gabung":"01-09-2020"},
    {"id":"P00002","nama_member":"hyunwook","tgl_gabung":"10-05-2020"},
    {"id":"P00003","nama_member":"Mirae","tgl_gabung":"05-08-2022"},
    {"id":"P00004","nama_member":"chaeyoung","tgl_gabung":"25-08-2022"}
]

data_transaksi = []
temp_pesanan = []

def lihat_member():
    i = 0
    no = 1
    print("DAFTAR MEMBER")
    while i < len(member):
        print(f'{no}. {member[i]["id"]}, nama : {member[i]["nama_member"]}, sejak {member[i]["tgl_gabung"]}')
        no += 1
        i += 1

def lihat_menu(jenis):
    i = 0
    no = 1
    if(jenis=="minuman"):
        print("DAFTAR MENU MINUMAN")
        while i < len(menu):
            if(menu[i]["jenis_menu"]==jenis):
                print(f'{no}. {menu[i]["nama_menu"]}, harga : {menu[i]["harga"]}')
                no += 1
            i += 1

    if(jenis=="makanan"):
        print("DAFTAR MENU MAKANAN")
        while i < len(menu):
            if(menu[i]["jenis_menu"]==jenis):
                print(f'{no}. {menu[i]["nama_menu"]}, harga : {menu[i]["harga"]}')
                no += 1
            i += 1 

def tambah_member(id,nama):
    now = datetime.now() 
    member.append({"id": id, "nama_member": nama, "tgl_gabung": now.strftime("%d-%m-%Y")})
    print("====== DATA BERHASIL DITAMBAHKAN =======")

def cek_member(id_member):
    status = False
    nama_member = "";
    for m in member:
        if m["id"] == id_member:
            status = True
            nama_member = m["nama_member"]
    return {"status":status, "nama_member":nama_member}

def lihat_pesanan():
    no = 1
    for p in temp_pesanan: 
        print(f'{no}. {p["nama_menu"]}, jumlah:{p["jumlah"]}')
        no += 1 

def get_menu_by_jenisnomor(jenis,nomor):
    temp_info = "Data tidak ada";
    temp_pilihan_menu = "";
    i = 0
    no = 1
    while i < len(menu):
        if(menu[i]["jenis_menu"]==jenis):
            if(no==nomor):
                temp_info = f'{no}. {menu[i]["nama_menu"]}, harga: {menu[i]["harga"]}'
                temp_pilihan_menu = menu[i]
            no += 1
        i += 1
    return {"info": temp_info, "pilihan_menu": temp_pilihan_menu}

        
def bayar_pesanan():
    no = 1 
    total_harga = 0
    total_harga_final = 0
    member_status = False 
    jumlah_bayar = 0
    kembalian = 0 
    for p in temp_pesanan:
        print(f'{no}. {p["nama_menu"]}, jumlah:{p["jumlah"]}, total harga: {p["total_harga"]}')
        no += 1
        total_harga+=p["total_harga"]
    print(f"Total Bayar : {total_harga}")
    pilihan=input("Apakah konsumen terdaftar sebagai member? (y/N)")
    if(pilihan=="y"):
        id_member=input("Input ID member :")
        if(cek_member(id_member)["status"]):
            member_status = cek_member(id_member)["status"]
            print(f"Member ditemukan, a/n {cek_member(id_member)['nama_member']}")
        else:
            print("member tidak ditemukan")
            member_status = False
    else:
        member_status = False

    if(member_status):
        total_harga_final = total_harga-(total_harga*0.1)
        print("Anda mendapatkan diskon 10% karena terdaftar sebagai member")
        print(f"Total harga (diskon 10%) : {total_harga_final}")
    else:
        total_harga_final = total_harga
        print(f"Pembayaran Normal : {total_harga_final}")
    jumlah_bayar = int(input("Masukan nominal uang : "))
    if(jumlah_bayar <= total_harga_final):
        print("=== Maaf, Uang Anda Kurang ====")
        bayar_pesanan()
    else:
        kembalian=jumlah_bayar-total_harga_final
        print(f"Kembalian : {kembalian}")

        cetak_struk(member_status, total_harga, total_harga_final, jumlah_bayar, kembalian)
        temp_pesanan.clear()

def cetak_struk(status_member, total_harga, total_harga_final, jumlah_bayar, kembalian):
    print("=== STRUK MAIL'S KAFE ===")
    no = 1
    for p in temp_pesanan:
        print(f'{no}. {p["nama_menu"]}, jumlah {p["jumlah"]}, total_harga: {p["total_harga"]}')
        no += 1
    print("=======================================================================")
    if(status_member):
        print(f"== Total Harga : {total_harga}")
        print(f"== Total_Harga (Discount 10%) : {total_harga_final}")
        print(f"== Jumlah Bayar : {jumlah_bayar}")
        print(f"== Kembalian: {kembalian}")
        print("================== Terdapat Sebagai member disc 10% ===================")
    else:
        print(f"== Total Harga : {total_harga}")
        print(f"== Jumlah bayar : {jumlah_bayar}")
        print(f"== Kembalian: {kembalian}")
        print("================== Terima Kasih ===================")

def kasir():
    status = ""
    while status != "end":
        print("Pencatatan Pesanan")
        print("1. Pesan Makanan / Minuman")
        print("2. Lihat Pesanan")
        print("3. Bayar")
        print("4. Kembali Menu Awal")
        pilihan=int(input("Pilih sesuai nomor: "))
        if pilihan == 1:
            lihat_menu("makanan")
            lihat_menu("minuman")
            jawab = "y"
            while(jawab == "y"):
                print("1. Makanan")
                print("2. Minuman")
                jenis = int(input("Pilih jenis"))
                if(jenis==1):
                    pilihan_menu = int(input("Menu nomor berapa? "))  
                    print(get_menu_by_jenisnomor("makanan", pilihan_menu)["info"])
                    jumlah = int(input("Jumlah Pesanan : "))
                    total_harga = jumlah*get_menu_by_jenisnomor("makanan",pilihan_menu)["pilihan_menu"]["harga"]
                    pesanan = {
                        "nama_menu": get_menu_by_jenisnomor("makanan", pilihan_menu)["pilihan_menu"]["nama_menu"],
                        "harga" : get_menu_by_jenisnomor("makanan", pilihan_menu)["pilihan_menu"]["harga"],
                        "jumlah" : jumlah,
                        "total_harga" : total_harga
                    }       
                    temp_pesanan.append(pesanan)
                elif(jenis==2):
                    pilihan_menu = int(input("Menu nomor berapa? "))  
                    print(get_menu_by_jenisnomor("minuman", pilihan_menu)["info"])
                    jumlah = int(input("Jumlah Pesanan : "))
                    total_harga = jumlah*get_menu_by_jenisnomor("minuman", pilihan_menu)["pilihan_menu"]["harga"]
                    pesanan = {
                        "nama_menu": get_menu_by_jenisnomor("minuman", pilihan_menu)["pilihan_menu"]["nama_menu"],
                        "harga" : get_menu_by_jenisnomor("minuman", pilihan_menu)["pilihan_menu"]["harga"],
                        "jumlah" : jumlah,
                        "total_harga" : total_harga
                    }    
                    temp_pesanan.append(pesanan)
                else:
                    print("Pilihan tidak tersedia")
                jawab = input("Pesan lagi? (y/N) ")
        elif pilihan == 2:
            lihat_pesanan()
        elif pilihan == 3:
            bayar_pesanan()
        elif pilihan == 4:
            print("Kembali ke Menu Awal")
            temp_pesanan.clear()
            status= "end"
        else:
            print("Error, Pilihan tidak tersedia")

status = ""
while status != "end":
    print("Selamat datang di Sistem Kasir Mail's Kafe")
    print("LIST MENU")
    print("1. Lihat Member")
    print("2. Tambah Member Baru")
    print("3. Kasir")
    print("4. Lihat Menu")
    print("5. Keluar")
    pilihan = int(input("Pilihan Menu"))
    print(pilihan)

    if pilihan == 1:
        lihat_member()
    elif pilihan == 2:
        print("Tambah member baru")
        id_member = input("Input ID : ")
        while cek_member(id_member)["status"]:
            print("=== ID Sudah ada ===")
            id_member = input("Input ID :")
        nama_member=input("Input Nama Lengkap :")
        tambah_member(id_member,nama_member)
    elif pilihan == 3:
        temp_pesanan.clear()
        kasir()
    elif pilihan == 4:
        lihat_menu("makanan")
        lihat_menu("minuman")
    elif pilihan == 5: 
        print("Sistem Exit, Thankyou")
        status= "end"
    else:
        print("Error, Pilihan tidak tersedia")
