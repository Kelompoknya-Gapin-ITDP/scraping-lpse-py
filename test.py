from pyproc import Lpse
import json

lpse = Lpse('https://lpse.jabarprov.go.id')

daftar_lelang = lpse.get_paket_tender(start=0, length=50)
outputs = []

for lelang in daftar_lelang['data']:
    # info tender
    id_tender = lelang[0]

    detil = lpse.detil_paket_tender(id_paket=id_tender)
    detil.get_all_detil()
    pengumuman = detil.get_pengumuman()
    pemenang = detil.get_pemenang()
    jadwal = detil.get_jadwal()

    if pemenang is None or jadwal is None or pemenang[0] is None:
        continue

    info_tender = {
        "id" : lelang[0],
        "nama" : lelang[1],
        "lokasi_instansi": lelang[2],
        "status_tender": lelang[3],
        "nilai_tender": lelang[10],
        "tanggal_pembuatan_tender": pengumuman["tanggal_pembuatan"],
        "lokasi_pekerjaan": pengumuman["lokasi_pekerjaan"][0],
        "satuan_kerja": pengumuman["satuan_kerja"],
        "nama_pemenang": pemenang[0]["nama_pemenang"],
        "alamat_pemenang": pemenang[0]["alamat"],
        "npwp_pemenang": pemenang[0]["npwp"],
        "harga_penawaran_pemenang": pemenang[0]["harga_penawaran"],
        "harga_terkoreksi_pemenang": pemenang[0]["harga_terkoreksi"],
        "harga_negosiasi_pemenang": pemenang[0]["harga_negosiasi"],
        "tanggal_selesai": jadwal[-1]["sampai"]
    }
    outputs.append(info_tender)

with open('result.json', 'w') as f:
    json.dump(outputs, f)