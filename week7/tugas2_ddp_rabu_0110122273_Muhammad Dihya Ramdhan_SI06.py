m1 = {}
m2 = {}
m3 = {}
m4 = {}
m5 = {}

ar_mahasiswa = [m1,m2,m3,m4,m5]
count = 0

for m in ar_mahasiswa:
    count += 1 
    print('Mahasiswa ke',count)

    # input data awal
    m["nim"] = str(input('Masukan NIM: ')) 
    m["nama"] = str(input('Masukkan Nama: '))
    m["nilai"] = int(input('Masukkan Nilai: '))

    print("NIM       : %s"
        "\nNama      : %s"
        "\nNilai     : %s"
        % (m['nim'], m['nama'], m['nilai'])
    )

    # tuple & list
    ket = ('Gagal','Lulus') [m["nilai"] >= 60]

    if m["nilai"] >= 85 and m["nilai"] <= 100:
        grade = 'A'
        predikat = 'Memuaskan'
    elif m["nilai"] >= 75 and m["nilai"] < 85:
        grade = 'B'
        predikat = 'Bagus' 
    elif m["nilai"] >= 60 and m["nilai"] < 75:
        grade = 'C'
        predikat = 'Cukup'  
    elif m["nilai"] >= 30 and m["nilai"] < 60:
        grade = 'D'
        predikat = 'Kurang'
    else:
        grade = 'E'
        predikat = 'Buruk' 

    print('Grade     : %s'
        '\nPredikat  : %s'
        '\nKeterangan: %s'
        '\n------------------------------'
        % (grade, predikat, ket)
    )