from . import Operasi

def delete_console():
    read_console()
    while(True):
        print("Silahkan pilih nomor film yang ingin di delete")
        no_film = int(input("Nomor Film : "))
        data_film = Operasi.read(index=no_film)

        if data_film:
            data_break = data_film.split(',')
            pk = data_break[0]
            data_add = data_break[1]
            penulis = data_break[2]
            judul = data_break[3]
            tahun = data_break[4][:-1]

            # data yang ingin di update
            print("\n"+"="*100)
            print("Data yang ingin anda hapus")
            print(f"1. Judul\t: {judul:.40}")
            print(f"2. Penulis\t: {penulis:.40}")
            print(f"3. Tahun\t: {tahun:4}")

            is_done = input("Anda yakin ingin di delete (y/n) ? ")
            if is_done == "y" or is_done == "Y":
                Operasi.delete(no_film)
                break
        else:
            print("Nomor tidak valid, silahkan masukan lagi")

    print("Data berhasil di hapus")

def update_console():
    read_console()
    while(True):
        print("Silahkan pilih nomor film yang ingin di update")
        no_film = int(input("Nomor Film : "))
        data_film = Operasi.read(index=no_film)
        if data_film:
            break
        else:
            print("Nomor tidak valid, silahkan masukan lagi")

    data_break = data_film.split(',')
    pk = data_break[0]
    data_add = data_break[1]
    penulis = data_break[2]
    judul = data_break[3]
    tahun = data_break[4][:-1]

    while(True):
        # data yang ingin di update
        print("\n"+"="*100)
        print("Silahkan pilih data apa yang ingin anda ubah")
        print(f"1. Judul\t: {judul:.40}")
        print(f"2. Penulis\t: {penulis:.40}")
        print(f"3. Tahun\t: {tahun:4}")

        # memilih mode untuk update    
        user_opsi = input("Pilih data [1,2,3]: ")
        print("\n"+"="*100)
        match user_opsi:
            case "1": judul = input("Judul\t: ")
            case "2": penulis = input("Penulis\t: ")
            case "3":
                while(True):
                    try:
                        tahun = int(input("Tahun\t: "))
                        if len(str(tahun)) == 4:
                            break
                        else:
                            print("Tahun harus berupa angka, sialhkan masukan tahun lagi (yyyy)")
                    except:
                        print("Tahun harus berupa angka, sialhkan masukan tahun lagi (yyyy)")
            case _: print("index tidak cocok")

        is_done = input("Apakah data sudah sesuai (y/n) ? ")
        if is_done == "y" or is_done == "Y":
            break

    Operasi.update(no_film,pk,data_add,penulis,judul,tahun)

def create_console():
    print("\n\n"+"="*100)
    print("Silahkan tambah data buku\n")
    judul = input("Judul\t: ")
    penulis = input("Penulis\t: ")
    while(True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus berupa angka, sialhkan masukan tahun lagi (yyyy)")
        except:
            print("Tahun harus berupa angka, sialhkan masukan tahun lagi (yyyy)")

    Operasi.create(judul,penulis,tahun)
    print("\nBERIKUT ADALAH DATA BARU ANDA")
    read_console()

def read_console():
    data_file = Operasi.read()
    index = "No"
    judul = "Judul"
    penulis = "Penulis"
    tahun = "Tahun"

    #Header
    print("\n"+"="*100)
    print(f'{index:4} | {judul:40} | {penulis:40} | {tahun:5}')
    print("-"*100)


    # Data
    for index, data in enumerate(data_file):
        data_break = data.split(",")
        pk = data_break[0]
        date_add = data_break[1]
        penulis = data_break[2]
        judul = data_break [3]
        tahun = data_break [4]
        print(f'{index+1:4} | {judul:.40} | {penulis:.40} | {tahun:4}',end="")


    #Footer
    print("\n"+"="*100)
