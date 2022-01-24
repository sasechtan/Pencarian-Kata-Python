# 100 kata baku
kataBaku = ['abjad', 'advokat', 'aktif', 'al quran', 'apotek', 'asas',
        'atlet', 'atmosfer', 'baut', 'berpikir', 'besok', 'bus',
        'cabai', 'cendekiawan', 'cenderamata', 'daftar', 'definisi', 'Ddepot',
        'detail', 'diagnosis', 'diesel', 'dipersilakan', 'dolar', 'ekspor',
        'ekstrem', 'ekulvalen', 'embus', 'februari', 'film', 'fisik',
        'fondasi', 'formal', 'foto', 'frekuensi', 'gizi', 'gladi',
        'hafal', 'hak', 'hakikat', 'hierarki', 'hipotesis', 'ijazah',
        'ikhlas', 'imbau', 'indera', 'insaf', 'istri', 'izin', 
        'jadwal', 'jenazah', 'jenderal', 'justru', 'kaidah', 'karier',
        'kategori', 'komplet', 'konferensi', 'kongres', 'konkret', 'kreatif',
        'kreativitas', 'kualifikasi', 'kuantitatif', 'kualitas', 'kuitansi', 'kiai',
        'lubang', 'maaf', 'makhluk', 'manajemen', 'manajer', 'mencolok',
        'menerjemahkan', 'mengesampingkan', 'merek', 'meterai', 'metode', 'mesti',
        'museum', 'motif', 'motivasi', 'nasihat', 'november', 'napas',
        'objek', 'paham', 'paspor', 'pikir', 'praktik', 'provinsi',
        'risiko', 'rezeki', 'saksama', 'sekadar', 'sekretaris', 'silakan',
        'sistem', 'subjek', 'sutera', 'syukur']

# user input
z = str(input('Masukkan kata : '))
a = z in kataBaku

if a == True:
    print(f'kata {z} merupakan kata baku sesuai pada database kami')

else:
    print(f'kata {z} tidak ada dalam database kami, silahkan periksa di')
    print(f'http://kbbi.kemdikbud.go.ig/entri/{z}')

# looping
stop=False
while (not stop):
    tanya = input('Ingin mencari kata lain ? (y/t) : ')
    if (tanya == 'y')or(tanya == 'Y'):
        z = str(input('Masukkan kata : '))
        a = z in kataBaku
        if a == True:
            print(f'kata {z} merupakan kata baku sesuai pada database kami')

        else:
            print(f'kata {z} tidak ada dalam database kami, silahkan periksa di')
            print(f'http://kbbi.kemdikbud.go.ig/entri/{z}')
    else:
        stop=True
        print('Baik terimakasih')