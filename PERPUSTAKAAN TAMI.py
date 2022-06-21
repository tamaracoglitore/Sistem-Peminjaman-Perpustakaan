# PERPUSTAKAAN TAMARA

# Daftar Buku Awal (Silahkan Masukkan daftar buku)
DaftarBuku = [{'ID Buku': "101",
        'Judul Buku': 'Naruto Shippuden',
        'Penulis': 'Masashi Kishimoto',
        'Penerbit': 'Gramedia',
        'Genre': 'Manga',
        'Stock Buku': 5
    },
    {
        'ID Buku': "201",
        'Judul Buku': 'Becoming\t',
        'Penulis': 'Michelle Obama',
        'Penerbit': 'Crown\t',
        'Genre': 'Non-fiction',
        'Stock Buku': 25
    },
    {
        'ID Buku': "302",
        'Judul Buku': 'The Alchemist',
        'Penulis': 'Paulo Coelho\t',
        'Penerbit': 'HarperOne',
        'Genre': 'Fiction',
        'Stock Buku': 1
    }
]

# Variabel sementara
cart=[] 
DatabasePeminjam =[]
NoPinjaman = 0 

# Fungsi template tabel database peminjam buku
def Database (listData0):
    print('\t ========================== Daftar Peminjam ========================== ')
    print('\tNo Pinjaman\t| Nama Peminjam | Judul Buku\t\t| Qty\t| ID Buku')
    for i in range(len(listData0)) :
        print('\t{}\t\t| {} \t| {} \t| {}\t| {}'.format(listData0[i]['No Pinjaman'],listData0[i]['Nama Peminjam'],listData0[i]['Judul Buku'],listData0[i]['Qty'],listData0[i]['ID Buku']))

# Fungsi template tabel daftar buku
def ShowList (listData):
    print('\t ================================ Daftar Buku ================================')
    print('\tID Buku\t| Judul Buku \t\t| Penulis\t\t| Penerbit\t| Genre\t\t| Stock Buku')
    for i in range(len(listData)) :
        print('\t{}\t| {} \t| {} \t| {}\t| {}  \t| {}\t'.format(listData[i]['ID Buku'],listData[i]['Judul Buku'],listData[i]['Penulis'],listData[i]['Penerbit'],listData[i]['Genre'],listData[i]['Stock Buku']))

# Fungsi template tabel keranjang
def cartfung(listData2):
    print('\t ============ Daftar Keranjang ============ ')
    print('\tJudul Buku\t\t| Qty \t| ID Buku')
    for i in range(len(listData2)):
        print('\t{}\t| {} \t| {}'.format(listData2[i]['Judul Buku'],listData2[i]['Qty'],listData2[i]['ID Buku']))

# Fungsi template menunjukkan daftar sebelum diupdate
def ShowListUpdate (listData,x,NewData):
    print('\t ================================ Daftar Buku ================================')
    print('\tID Buku\t| Judul Buku \t\t| Penulis\t\t| Penerbit\t| Genre\t\t| Stock Buku')
    if x == 1: 
        for i in range(len(listData)) :
            print('\t{}\t| {} \t| {} \t| {}\t| {}  \t| {}\t'.format(NewData,listData[i]['Judul Buku'],listData[i]['Penulis'],listData[i]['Penerbit'],listData[i]['Genre'],listData[i]['Stock Buku']))
    elif x == 2:
        for i in range(len(listData)) :
            print('\t{}\t| {} \t| {} \t| {}\t| {}  \t| {}\t'.format(listData[i]['ID Buku'],NewData,listData[i]['Penulis'],listData[i]['Penerbit'],listData[i]['Genre'],listData[i]['Stock Buku']))
    elif x == 3:
        for i in range(len(listData)) :
            print('\t{}\t| {} \t| {} \t| {}\t| {}  \t| {}\t'.format(listData[i]['ID Buku'],listData[i]['Judul Buku'],NewData,listData[i]['Penerbit'],listData[i]['Genre'],listData[i]['Stock Buku']))
    elif x == 4:
        for i in range(len(listData)) :
            print('\t{}\t| {} \t| {} \t| {}\t| {}  \t| {}\t'.format(listData[i]['ID Buku'],listData[i]['Judul Buku'],listData[i]['Penulis'],NewData,listData[i]['Genre'],listData[i]['Stock Buku']))
    elif x == 5:
        for i in range(len(listData)) :
            print('\t{}\t| {} \t| {} \t| {}\t| {}  \t| {}\t'.format(listData[i]['ID Buku'],listData[i]['Judul Buku'],listData[i]['Penulis'],listData[i]['Penerbit'],NewData,listData[i]['Stock Buku']))
    elif x == 6:
        for i in range(len(listData)) :
            print('\t{}\t| {} \t| {} \t| {}\t| {}  \t| {}\t'.format(listData[i]['ID Buku'],listData[i]['Judul Buku'],listData[i]['Penulis'],listData[i]['Penerbit'],listData[i]['Genre'],NewData))

# Fungsi update barang sesuai kolom
def UpdateBarang(Data, Kolom,NewData2):
    InputUpdateBarang= (input("\t Apakah data yang diupdate sudah benar? (Ya/Tidak): ")).lower()
    if InputUpdateBarang == "ya":
        Data[0][Kolom] = NewData2
        print("\tData sudah diperbarui!")
    else:
        print("\t Data tidak terupdate!")

# Fungsi filter dictionary dalam list
def SearchList(Input):
    SearchList = (list(filter(lambda data: data['ID Buku'] == str(Input), DaftarBuku)))
    return SearchList

# Fungsi membaca daftar buku
def Read():
    inputRead = (int(input('''
        Menu Menampilkan Daftar Buku:
            1. Tampilkan semua buku
            2. Mencari buku
            3. Kembali ke menu utama
        Masukkan angka menu yang ingin dijalankan:''')))
    if inputRead == 1 and len(DaftarBuku): 
        ShowList(DaftarBuku)
    elif inputRead == 2 and len(DaftarBuku):
        BookID = (input("\tMasukkan ID Buku yang ingin dicari: "))  
        SearchList(BookID)
        if len(SearchList(BookID)): 
            ShowList(SearchList(BookID))
        else:
            print("\n\t Tidak ada data")
    elif inputRead == 3: 
        Menu()
    else: 
        print("\n\t Tidak ada data")
    Read()

# Fungsi menambah daftar buku
def Add():
    inputAdd = (int(input('''
        Menu Menambah Daftar Buku:
            1. Menambah daftar buku
            2. Kembali ke menu utama
        Masukkan angka menu yang ingin dijalankan:''')))
    if inputAdd == 1:
        AddBookID = (input("\n\tMasukkan ID Buku Baru:"))
        ListValue = [value for databuku in DaftarBuku for value in databuku.values()]
        if AddBookID in ListValue:
            print("\n\tData sudah ada!")
        else:
            JudulBaru = (input("\tSilahkan masukkan judul:"))
            PenulisBaru = input("\tSilahkan masukkan nama penulis:")
            PenerbitBaru = input("\tSilahkan masukkan penerbit:")
            GenreBaru = input("\tSilahkan masukkan genre:")
            StockBaru = int(input("\tSilahkan masukkan stock:"))
            DaftarBukuBaru=[{
                'ID Buku': AddBookID,
                'Judul Buku': JudulBaru,
                'Penulis': PenulisBaru,
                'Penerbit': PenerbitBaru,
                'Genre': GenreBaru,
                'Stock Buku': StockBaru
            }]
            ShowList(DaftarBukuBaru)
            Save = (input("\n\t Simpan Data (Ya/Tidak)?")).lower()
            if Save == "ya":
                DaftarBuku.extend(DaftarBukuBaru)
                ShowList(DaftarBuku)
                print("\n \tData buku baru tersimpan!")
            else:
                print("\n \t Data tidak tersimpan!")
    elif inputAdd == 2:
        Menu()
    Add()

# Fungsi merubah daftar buku
def Update():
    inputUpdate = (int(input('''
        Menu Mengubah Daftar Buku:
            1. Mengubah daftar buku
            2. Kembali ke menu utama
        Masukkan angka menu yang ingin dijalankan:''')))
    if inputUpdate == 1:
        ShowList(DaftarBuku)
        UpdateBook = (input("\n\tMasukkan ID yang ingin diubah:"))
        ListValue = [value for databuku in DaftarBuku for value in databuku.values()]
        if UpdateBook not in ListValue:
            print("\n\t Data yang ingin diubah tidak tersedia!")
            Update()
        else:
            SearchList(UpdateBook)
            ShowList(SearchList(UpdateBook))
            inputUpdate = (input("\tUpdate data berikut? (Ya/Tidak): ")).lower()
            if inputUpdate== "ya":
                inputKategori = int(input("""
                    \tKategori Database Buku: 
                        1. ID Buku 
                        2. Judul Buku
                        3. Penulis
                        4. Penerbit
                        5. Genre
                        6. Stock Buku
                    Masukkan kategori yang ingin diubah: """))
                if inputKategori == 1:
                    MasukkanData = input("\tMasukkan data baru: ")
                    ShowListUpdate(SearchList(UpdateBook),1,MasukkanData)
                    UpdateBarang(SearchList(UpdateBook), "ID Buku",MasukkanData)
                elif inputKategori == 2:
                    MasukkanData = input("\tMasukkan data baru: ")
                    ShowListUpdate(SearchList(UpdateBook),2,MasukkanData)
                    UpdateBarang(SearchList(UpdateBook),"Judul Buku",MasukkanData)
                elif inputKategori == 3:
                    MasukkanData = input("\tMasukkan data baru: ")
                    ShowListUpdate(SearchList(UpdateBook),3,MasukkanData)
                    UpdateBarang(SearchList(UpdateBook),"Penulis",MasukkanData)
                elif inputKategori == 4:
                    MasukkanData = input("\tMasukkan data baru: ")
                    ShowListUpdate(SearchList(UpdateBook),4,MasukkanData)
                    UpdateBarang(SearchList(UpdateBook),"Penerbit",MasukkanData)
                elif inputKategori == 5:
                    MasukkanData = input("\tMasukkan data baru: ")
                    ShowListUpdate(SearchList(UpdateBook),5,MasukkanData)
                    UpdateBarang(SearchList(UpdateBook),"Genre",MasukkanData)
                elif inputKategori == 6:
                    MasukkanData = int(input("\tMasukkan data baru: "))
                    ShowListUpdate(SearchList(UpdateBook),6,MasukkanData)
                    UpdateBarang(SearchList(UpdateBook),"Stock Buku",MasukkanData)
                else: 
                    print("\tKategori tidak ada!")
    elif inputUpdate == 2:
        Menu()
    Update()
                         
# Fungsi menghapus daftar buku
def Delete():
    inputDel = (int(input('''
        Menu Menghapus Daftar Buku:
            1. Menghapus Daftar Buku
            2. Kembali ke menu utama
        Masukkan angka menu yang ingin dijalankan:''')))
    if inputDel == 1:
        ShowList(DaftarBuku)
        DelBookID = (input("\n\tMasukkan ID Buku yang ingin dihapus:"))
        ListValue2 = [value2 for databuku in DaftarBuku for value2 in databuku.values()]
        if DelBookID not in ListValue2:
            print("\n\tData yang ingin anda hapus tidak ada!")
        else:
            SearchList(DelBookID)
            ShowList(SearchList(DelBookID))
            hapus = (input("\n\t Hapus Data (Ya/Tidak)?")).lower()
            if hapus == "ya":            
                for e in SearchList(DelBookID) :
                    DaftarBuku.remove(e)
                print("\n\t Data berhasil terhapus!")
            else: 
                print("\n\t Data tidak berhasil terhapus!")
    elif inputDel == 2:
        Menu() 
    Delete()

# Fungsi meminjam buku
def Borrow():
    inputBorrow = (int(input('''
        Menu Meminjam Buku:
            1. Meminjam Buku
            2. Kembali ke menu utama
        Masukkan angka menu yang ingin dijalankan:''')))
    if inputBorrow == 1:
        ShowList(DaftarBuku)
        while True:
            inputbor = (input("\n\tMasukkan ID Buku yang ingin anda pinjam:"))
            ListValue3 = [value3 for databuku in DaftarBuku for value3 in databuku.values()]
            if inputbor not in ListValue3:
                print("\n\tBuku yang ingin anda pinjam tidak tersedia!")
                Borrow()
            else:
                print("\t Data buku yang ingin di pinjam:")
                Var = SearchList(inputbor)
                ShowList(Var)
                tambahkan = (input('\n\t Tambahkan daftar buku kedalam keranjang? (Ya/Tidak):')).lower() 
                if tambahkan == 'ya':
                    Qty = int(input('\t Berapa buku yang ingin dipinjam?:'))
                    if Qty > Var[0]['Stock Buku']:
                        print("\n\t Mohon maaf stock buku tidak cukup")
                        cart.clear()
                    else:
                        cart.append({'Judul Buku': (Var[0]['Judul Buku']), 
                    'Qty': Qty,
                    'ID Buku': (Var[0]['ID Buku'])
                    })
                else:
                    print("\n\t Keranjang tidak ter-update!")
                    cart.clear()
                    Borrow()
                
            cartfung(cart)
            checker = (input('\tMau pinjam buku lain? (ya/tidak) :')).lower()
            if (checker == 'ya') :
                True
            else:
                break
            
        cartfung(cart)   
        CheckOut = (input("\t Lanjutkan check out? (Ya/Tidak): " )).lower()
        if CheckOut == "tidak":
            print("\t Tidak jadi meminjam!")
            cart.clear()
            Borrow()
        elif CheckOut == "ya":
            global NoPinjaman
            NamaPeminjam = (input("\tMasukkan Nama Peminjam:"))
            print(f"""\t\n  ======== No Pinjaman Anda adalah: {NoPinjaman} ========"""
            )
            Nopeminjam = NoPinjaman
            NoPinjaman+= 1
            penampungansementara = {"No Pinjaman":Nopeminjam, "Nama Peminjam": NamaPeminjam}
            for item in range(len(cart)):
                cart[item].update(penampungansementara)
            DatabasePeminjam.extend(cart)
            print("\n\n\t xxxxx Pengembalian buku 7 hari dari sekarang! xxxxx \n\t\t xxxxxxx Selamat Membaca xxxxxxx!")
            for item in cart:
                (SearchList(item['ID Buku']))[0]['Stock Buku']-=item['Qty']
            print("\n\t info: Stock Buku terupdate!")
        else: 
            cart.clear()
            
        cart.clear()
        ShowList(DaftarBuku)
        print("\n")
        Database(DatabasePeminjam)
    elif inputBorrow == 2:
        Menu()
    Borrow()

# Fungsi mengembalikan buku
def returnBook():
    inputReturn = (int(input('''
        Menu Mengembalikan Buku:
            1. Mengembalikan Buku
            2. Kembali ke menu utama
        Masukkan angka menu yang ingin dijalankan:''')))
    if inputReturn == 1:
        Database(DatabasePeminjam)
        while True:
            inputRet = int(input("\n\tMasukkan No Pinjaman untuk mengembalikan buku:"))
            ListValue4 = [value4 for datapeminjam in DatabasePeminjam for value4 in datapeminjam.values()]
            if inputRet not in ListValue4:
                print("\n\tNo Pinjaman tidak tersedia!")
                returnBook()
            else:
                print("\t Data buku yang ingin di kembalikan:")
                SearchList4= (list(filter(lambda data: data['No Pinjaman'] == (inputRet), DatabasePeminjam)))
                Database(SearchList4)
                Hapus1 = (input('\n\t Kembalikan semua buku? (Ya/Tidak):')).lower()
                if Hapus1 == 'ya':
                    for item in SearchList4:
                        (SearchList(item['ID Buku']))[0]['Stock Buku']+=item['Qty']
                        DatabasePeminjam.remove(item)
                    print("\n\t xxxx Buku sudah dikembalikan! xxxxx")
                    print("\n\t info: Stock Buku terupdate!")
                else:
                    print("\n\t Buku belum kembali!")
                    returnBook() 
            checker = input('\tMau kembalikan buku lain? (ya/tidak) :')
            if (checker == 'ya') :
                True
            else:
                print("\n\t *** Terima kasih! Datang kembali ***")
                break
            
    elif inputReturn == 2:
        Menu()
    returnBook()

# Fungsi menu utama
def Menu():
    while True :
        pilihanMenu = input('''
        Selamat Datang di Perpustakaan Tamara

        List Menu :
        1. Menampilkan Daftar Buku
        2. Menambah Daftar Buku
        3. Mengubah Daftar Buku
        4. Menghapus Daftar Buku
        5. Meminjam Buku
        6. Mengembalikan Buku
        7. Exit Program

        Masukkan angka Menu yang ingin dijalankan : ''')

        if(pilihanMenu == '1') :
            Read()
        elif(pilihanMenu == '2') :
            Add()
        elif(pilihanMenu == '3') :
            Update()
        elif(pilihanMenu == '4') :
            Delete()
        elif(pilihanMenu == '5'):
            Borrow()
        elif(pilihanMenu == '6') :
            returnBook()
        elif(pilihanMenu == '7') :
            exit()
        else:
            Menu()

# Memanggil Menu utama
Menu()
    
