# from pyproc import Lpse

# lpse = Lpse('https://lpse.jabarprov.go.id')

# # # mendapatkan daftar paket lelang
# # daftar_lelang = lpse.get_paket_tender(start=0, length=2)
# # print(daftar_lelang)

# # pencarian paket non tender (penunjukkan langsung)
# # daftar_pl = lpse.get_paket_non_tender(start=0, length=30)

# # mendapatkan semua detil paket lelang
# detil = lpse.detil_paket_tender(id_paket='79768414014')
# # detil.get_all_detil()
# # print(detil)

# # mendapatkan hanya pemenang lelang
# pemenang = detil.get_pemenang()
# print(pemenang)

#################################################

from pyproc import Lpse

# Inisialisasi LPSE
lpse = Lpse('https://lpse.jabarprov.go.id')

# Mendapatkan daftar paket lelang
daftar_lelang = lpse.get_paket_tender(start=0, length=2)

# Iterasi setiap data lelang
for lelang in daftar_lelang['data']:
    # Mendapatkan ID tender dari kolom pertama
    id_tender = lelang[0]
    
    # Mengambil detail pemenang menggunakan ID tender
    detil = lpse.detil_paket_tender(id_paket=id_tender)
    detil.get_all_detil()
    pemenang = detil.get_pemenang()
    
    # Menambahkan kolom 'pemenang' ke dalam data lelang
    lelang.append(pemenang)  # atau lelang[-1].append(pemenang) untuk penempatan tertentu

# Cetak hasil yang telah ditambahkan detail pemenang
print(daftar_lelang)