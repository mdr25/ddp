p1 = {"nama": "Budi","produk": "TV", "jumlah": 3}
p2 = {"nama": "Ani","produk": "AC","jumlah": 4}
p3 = {"nama": "Siti","produk": "Kulkas","jumlah": 2}
p4 = {"nama": "Dewi","produk": "AC","jumlah": 5}
p5 = {"nama": "Andi","produk": "Kulkas","jumlah": 7}
p6 = {"nama": "Dedi","produk": "AC","jumlah": 1}
p7 = {"nama": "Sri","produk": "TV","jumlah": 4}

ar_pelanggan = [p1, p2, p3, p4, p5, p6, p7]

for p in ar_pelanggan:
    for key,data in p.items():
        # cetak data awal
        print (key,':',data)

    produk = p ["produk"]
    jum_bel = p ["jumlah"]

    if produk == "TV":
        harga_satuan = 5
        harga_kotor = jum_bel * harga_satuan
    elif produk == "AC":
        harga_satuan = 6
        harga_kotor = jum_bel * harga_satuan
    else:
        harga_satuan = 7
        harga_kotor = jum_bel * harga_satuan

    # tuple
    discount = (0.2,0.05)

    # diskon
    if produk == "Kulkas":
        if jum_bel >= 3:
            total_diskon = discount[0] *harga_kotor
            diskon = int(total_diskon)
        else:
            total_diskon = discount[1] *harga_kotor
            diskon = int(total_diskon)
    else:
        total_diskon = discount[1] * harga_kotor
        diskon = int(total_diskon)

    ppn = 0.11 * (harga_kotor - diskon)
    harga_bayar = (harga_kotor + ppn) - diskon

    print('Harga satuan :', harga_satuan, "juta"
        '\nHarga kotor  :', harga_kotor, "juta"
        '\nDiskon       :', diskon, "juta"
        '\nPPN          :', ppn, "juta"
        '\nHarga bayar  :', harga_bayar, "juta"
        '\n---------------------' 
    )