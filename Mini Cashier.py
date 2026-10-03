nama_pembeli = input("Siapa namamu? ")
harga_barang = list(
    map(int, input("Harga Barang: ").split()))
subtotal = 0

for i in harga_barang:
    subtotal += i

nama_toko, kota = ("Toko Berkah Abadi", "Kota Surakarta")

biaya_layanan = subtotal * 5 / 100
total = subtotal + biaya_layanan

is_member = True
if is_member == True and subtotal >= 100000:
    eligible = True
else:
    eligible = False

riwayat_transaksi = {
    "Nama Toko": nama_toko,
    "Lokasi": kota,
    "Pembeli": nama_pembeli,
    "Daftar Harga": harga_barang,
    "Subtotal Belanja": subtotal,
    "Pajak Layanan": biaya_layanan,
    "Total Akhir": total,
    "Status Member": is_member,
    "Eligible": eligible
}

print("=== Riwayat Transaksi ===")
for k, v in riwayat_transaksi.items():
    print(f"{k} : {v}")
