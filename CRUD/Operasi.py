from time import time
from . import Database
from .Util import random_string
import time
import os

def delete(no_buku):
    try:
        with open(Database.DB_NAME,'r') as file:
            counter = 0

            while(True):
                content = file.readline()
                if len(content) == 0:
                    break
                elif counter == no_buku - 1:
                    pass
                else:
                    with open("data_temp.txt",'a',encoding="utf-8") as temp_file:
                        temp_file.write(content)
                counter += 1
    except:
        print("database error")
    
    os.replace("data_temp.txt",Database.DB_NAME)
    
def update(no_film,pk,data_add,penulis,judul,tahun):
    data = Database.TEMPLATE.copy()

    data["pk"] = pk
    data["date_add"] = data_add
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'

    panjang_data = len(data_str)

    try:
        with(open(Database.DB_NAME,'r+', encoding = "utf-8")) as file:
            file.seek(panjang_data*(no_film-1))
            file.write(data_str)
    except:
        print("Error dalam update data")    

def create(penulis,judul,tahun):
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%S%z",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    try:
        with open(Database.DB_NAME,'a',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("Data sulit ditambahkan")

def create_first_data():
    penulis = input ("Penulis   : ")
    judul = input ("Judul     : ")
    while(True):
        try:
            tahun = int(input("Tahun\t: "))
            if len(str(tahun)) == 4:
                break
            else:
                print("Tahun harus berupa angka, sialhkan masukan tahun lagi (yyyy)")
        except:
            print("Tahun harus berupa angka, sialhkan masukan tahun lagi (yyyy)")
    
    data = Database.TEMPLATE.copy()

    data["pk"] = random_string(6)
    data["date_add"] = time.strftime("%Y-%m-%d-%H-%S%z",time.gmtime())
    data["penulis"] = penulis + Database.TEMPLATE["penulis"][len(penulis):]
    data["judul"] = judul + Database.TEMPLATE["judul"][len(judul):]
    data["tahun"] = str(tahun)

    data_str = f'{data["pk"]},{data["date_add"]},{data["penulis"]},{data["judul"]},{data["tahun"]}\n'
    print(data_str)
    try:
        with open(Database.DB_NAME,'w',encoding="utf-8") as file:
            file.write(data_str)
    except:
        print("DAHLAH CAPE BROKKKKK")

def read(**kwargs):
    try:
        with open(Database.DB_NAME, 'r') as file :
            content = file.readlines()
            jumlah_film = len(content)
            if "index" in kwargs:
                index_film = kwargs["index"]-1
                if index_film < 0 or index_film > jumlah_film:
                    return False
                else:
                    return content[index_film]
            else:
                return content

    except:
        print("Membaca database eror")
        return False