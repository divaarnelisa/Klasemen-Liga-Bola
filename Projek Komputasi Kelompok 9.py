#fungsi membuat tabel klasemen
def klasemen(M,S,K,P):
    club = ['A','B','C','D']
    print("\nklasemen pertandingan")
    print("""-------------------------------
CLUB  | M | S | K | Poin |
-------------------------------""")

    for i in range(len(club)):
        kolom1 = str(club[i])
        kolom2 = str(M[i])
        kolom3 = str(S[i])
        kolom4 = str(K[i])
        kolom5 = str(P[i])
        print('| ' + kolom1 + (4-len(kolom1))*' '
         + '| ' + kolom2 + (2-len(kolom2))*' '
        + '| ' + kolom3 + (2-len(kolom3))*' '
        + '| ' + kolom4 + (2-len(kolom4))*' '
        + '| ' + kolom5 + (2-len(kolom5))*' ' + '   |')

#fungsi menambahkan hasil pertandingan
def match_result(club1,skor1,skor2,club2):
    result ={
        "club1":club1,
        "skor1":int(skor1),
        "skor2":int(skor2),
        "club2":club2
    }
    return result

#fungsi menentukan kalah atau menang
def menang_kalah(club1,skor1,skor2,club2):
    result = match_result(club1,skor1,skor2,club2)
    if result["skor1"] > result["skor2"]:
        result["club1"] = "menang"
        result ["club2"] = "kalah"
    elif result["skor1"] < result["skor2"]:
        result["club1"] = "kalah"
        result["club2"] = "menang"
    else:
        result["club1"] = "seri"
        result["club2"] = "seri"
    return result["club1"],result["club2"]

#fungsi menghitung total menang
def total_menang(club1,skor1,skor2,club2):
    A,B,C,D = 0,0,0,0
    hasil = menang_kalah(club1,skor1,skor2,club2)
    if club1 == "A":
        if hasil[0] == "menang":
            A += 1
    if club1 == "B":
        if hasil[0] == "menang":
            B += 1
    if club1 == "C":
        if hasil[0] == "menang":
            C += 1
    if club1 == "D":
        if hasil[0] == "menang":
            D += 1

    if club2 == "A":
        if hasil[1] == "menang":
            A += 1
    if club2 == "B":
        if hasil[1] == "menang":
            B += 1
    if club2 == "C":
        if hasil[1] == "menang":
            C += 1
    if club2 == "D":
        if hasil[1] == "menang":
            D += 1
    return A,B,C,D

#fungsi menghitung total seri
def total_seri(club1,skor1,skor2,club2):
    A,B,C,D = 0,0,0,0
    hasil = menang_kalah(club1,skor1,skor2,club2)
    if club1 == "A":
          if hasil[0] == "seri":
            A += 1
    if club1 == "B":
        if hasil[0] == "seri":
            B += 1
    if club1 == "C":
        if hasil[0] == "seri":
            C += 1
    if club1 == "D":
        if hasil[0] == "seri":
            D += 1

    if club2 == "A":
        if hasil[1] == "seri":
            A += 1
    if club2 == "B":
        if hasil[1] == "seri":
            B += 1
    if club2 == "C":
        if hasil[1] == "seri":
            C += 1
    if club2 == "D":
        if hasil[1] == "seri":
            D += 1
    return A,B,C,D

#fungsi menghitung total kalah
def total_kalah(club1,skor1,skor2,club2):
    A,B,C,D = 0,0,0,0
    hasil = menang_kalah(club1,skor1,skor2,club2)
    if club1 == "A":
        if hasil[0] == "kalah":
              A += 1
    if club1 == "B":
        if hasil[0] == "kalah":
            B += 1
    if club1 == "C":
        if hasil[0] == "kalah":
            C += 1
    if club1 == "D":
        if hasil[0] == "kalah":
            D += 1

    if club2 == "A":
        if hasil[1] == "kalah":
            A += 1
    if club2 == "B":
        if hasil[1] == "kalah":
            B += 1
    if club2 == "C":
        if hasil[1] == "kalah":
            C += 1
    if club2 == "D":
        if hasil[1] == "kalah":
            D += 1
    return A,B,C,D

#fungsi menambahkan point (menang +3, seri +1, kalah 0)
def add_point(club1,skor1,skor2,club2):
    hasil = menang_kalah(club1,skor1,skor2,club2)
    if hasil[0] == "menang":
        club1 = 3
    elif hasil[0] == "kalah":
        club1 = 0
    else:
        club1 = 1

    if hasil[1] == "menang":
        club2 = 3
    elif hasil[1] == "kalah":
        club2 = 0
    else:
        club2 = 1
    return club1,club2

#fungsi menyimpan poin
def simpan_poin(club1,skor1,skor2,club2):
    A,B,C,D = 0,0,0,0
    poin = add_point(club1,skor1,skor2,club2)
    if club1 == "A":
        A += poin[0]
    if club1 == "B":
        B += poin[0]
    if club1 == "C":
        C += poin[0]
    if club1 == "D":
        D += poin[0]

    if club2 == "A":
        A += poin[1]
    if club2 == "B":
        B += poin[1]
    if club2 == "C":
        C += poin[1]
    if club2 == "D":
        D += poin[1]
    return A,B,C,D

def main():
    #membuat varibel poin,menang,seri,kalah
    #untuk menambahkan data dari inputan
    poin_A,poin_B,poin_C,poin_D = 0,0,0,0
    menang_A,menang_B,menang_C,menang_D = 0,0,0,0
    seri_A,seri_B,seri_C,seri_D = 0,0,0,0
    kalah_A,kalah_B,kalah_C,kalah_D = 0,0,0,0

    #perulangan sebanyak minggu
    for i in range(6):
        #perulangan sebanyak jumlah pertandingan
        for j in range(2):
            print(30*"-")
            print("perrtandingan ke-",j+1, "minggu ke-",i+1)
            print(30*"-")
            #membuat variabel inputan
            club1,skor1,skor2,club2 = input().split()

            #menambahkan poin ke variabel simpanan
            poin = simpan_poin(club1,skor1,skor2,club2)
            poin_A += poin[0]
            poin_B += poin[1]
            poin_C += poin[2]
            poin_D += poin[3]
             #menambahkan total menang ke variabel simpanan
            menang = total_menang(club1,skor1,skor2,club2)
            menang_A += menang[0]
            menang_B += menang[1]
            menang_C += menang[2]
            menang_D += menang[3]

            #menambahkan total seri ke variabel simpanan
            seri = total_seri(club1,skor1,skor2,club2)
            seri_A += seri[0]
            seri_B += seri[1]
            seri_C += seri[2]
            seri_D += seri[3]

            #menambahkan total kalah ke variabel simpanan
            kalah = total_kalah(club1,skor1,skor2,club2)
            kalah_A += kalah[0]
            kalah_B += kalah[1]
            kalah_C += kalah[2]
            kalah_D += kalah[3]
            #buat list dari variabel poin,menang,kalah
            #untuk dimasukan ke dalam tabel klasemen
            m =[menang_A,menang_B,menang_C,menang_D]
            s =[seri_A,seri_B,seri_C,seri_D]
            k = [kalah_A,kalah_B,kalah_C,kalah_D]
            p = [poin_A,poin_B,poin_C,poin_D]

            #memanggil tabel klasemen
            print(klasemen(m,s,k,p),"\n")


#fungsi membuat tabel klasemen
def klasemen(M,S,K,P):
    club = ['A','B','C','D']
    print("\nklasemen pertandingan")
    print("""-------------------------------
CLUB  | M | S | K | Poin |
-------------------------------""")

    for i in range(len(club)):
        kolom1 = str(club[i])
        kolom2 = str(M[i])
        kolom3 = str(S[i])
        kolom4 = str(K[i])
        kolom5 = str(P[i])
        print('| ' + kolom1 + (4-len(kolom1))*' '
        + '| ' + kolom2 + (2-len(kolom2))*' '
        + '| ' + kolom3 + (2-len(kolom3))*' '
        + '| ' + kolom4 + (2-len(kolom4))*' '
        + '| ' + kolom5 + (2-len(kolom5))*' ' + '   |')

#fungsi menambahkan hasil pertandingan
def match_result(club1,skor1,skor2,club2):
    result ={
        "club1":club1,
        "skor1":int(skor1),
        "skor2":int(skor2),
        "club2":club2
    }
    return result

#fungsi menentukan kalah atau menang
def menang_kalah(club1,skor1,skor2,club2):
    result = match_result(club1,skor1,skor2,club2)
    if result["skor1"] > result["skor2"]:
        result["club1"] = "menang"
        result ["club2"] = "kalah"
    elif result["skor1"] < result["skor2"]:
        result["club1"] = "kalah"
        result["club2"] = "menang"
    else:
        result["club1"] = "seri"
        result["club2"] = "seri"
    return result["club1"],result["club2"]

#fungsi menghitung total menang
def total_menang(club1,skor1,skor2,club2):
    A,B,C,D = 0,0,0,0
    hasil = menang_kalah(club1,skor1,skor2,club2)
    if club1 == "A":
        if hasil[0] == "menang":
            A += 1
    if club1 == "B":
        if hasil[0] == "menang":
            B += 1
    if club1 == "C":
        if hasil[0] == "menang":
            C += 1
    if club1 == "D":
        if hasil[0] == "menang":
            D += 1

    if club2 == "A":
        if hasil[1] == "menang":
            A += 1
    if club2 == "B":
        if hasil[1] == "menang":
            B += 1
    if club2 == "C":
        if hasil[1] == "menang":
            C += 1
    if club2 == "D":
        if hasil[1] == "menang":
            D += 1
    return A,B,C,D

#fungsi menghitung total seri
def total_seri(club1,skor1,skor2,club2):
    A,B,C,D = 0,0,0,0
    hasil = menang_kalah(club1,skor1,skor2,club2)
    if club1 == "A":
        if hasil[0] == "seri":
            A += 1
    if club1 == "B":
        if hasil[0] == "seri":
            B += 1
    if club1 == "C":
        if hasil[0] == "seri":
            C += 1
    if club1 == "D":
        if hasil[0] == "seri":
            D += 1

    if club2 == "A":
        if hasil[1] == "seri":
            A += 1
    if club2 == "B":
        if hasil[1] == "seri":
            B += 1
    if club2 == "C":
        if hasil[1] == "seri":
            C += 1
    if club2 == "D":
        if hasil[1] == "seri":
            D += 1
    return A,B,C,D

#fungsi menghitung total kalah
def total_kalah(club1,skor1,skor2,club2):
    A,B,C,D = 0,0,0,0
    hasil = menang_kalah(club1,skor1,skor2,club2)
    if club1 == "A":
        if hasil[0] == "kalah":
            A += 1
    if club1 == "B":
        if hasil[0] == "kalah":
            B += 1
    if club1 == "C":
        if hasil[0] == "kalah":
            C += 1
    if club1 == "D":
        if hasil[0] == "kalah":
            D += 1

    if club2 == "A":
        if hasil[1] == "kalah":
            A += 1
    if club2 == "B":
        if hasil[1] == "kalah":
            B += 1
    if club2 == "C":
        if hasil[1] == "kalah":
            C += 1
    if club2 == "D":
        if hasil[1] == "kalah":
            D += 1
    return A,B,C,D

#fungsi menambahkan point (menang +3, seri +1, kalah 0)
def add_point(club1,skor1,skor2,club2):
    hasil = menang_kalah(club1,skor1,skor2,club2)
    if hasil[0] == "menang":
        club1 = 3
    elif hasil[0] == "kalah":
        club1 = 0
    else:
        club1 = 1

    if hasil[1] == "menang":
        club2 = 3
    elif hasil[1] == "kalah":
        club2 = 0
    else:
        club2 = 1
    return club1,club2

#fungsi menyimpan poin
def simpan_poin(club1,skor1,skor2,club2):
    A,B,C,D = 0,0,0,0
    poin = add_point(club1,skor1,skor2,club2)
    if club1 == "A":
        A += poin[0]
    if club1 == "B":
        B += poin[0]
    if club1 == "C":
        C += poin[0]
    if club1 == "D":
        D += poin[0]

    if club2 == "A":
        A += poin[1]
    if club2 == "B":
        B += poin[1]
    if club2 == "C":
        C += poin[1]
    if club2 == "D":
        D += poin[1]
    return A,B,C,D

def main():
    #membuat varibel poin,menang,seri,kalah
    #untuk menambahkan data dari inputan
    poin_A,poin_B,poin_C,poin_D = 0,0,0,0
    menang_A,menang_B,menang_C,menang_D = 0,0,0,0
    seri_A,seri_B,seri_C,seri_D = 0,0,0,0
    kalah_A,kalah_B,kalah_C,kalah_D = 0,0,0,0

    #perulangan sebanyak minggu
    for i in range(6):
        #perulangan sebanyak jumlah pertandingan
        for j in range(2):
            print(30*"-")
            print("perrtandingan ke-",j+1, "minggu ke-",i+1)
            print(30*"-")
            #membuat variabel inputan
            club1,skor1,skor2,club2 = input().split()

            #menambahkan poin ke variabel simpanan
            poin = simpan_poin(club1,skor1,skor2,club2)
            poin_A += poin[0]
            poin_B += poin[1]
            poin_C += poin[2]
            poin_D += poin[3]

            #menambahkan total menang ke variabel simpanan
            menang = total_menang(club1,skor1,skor2,club2)
            menang_A += menang[0]
            menang_B += menang[1]
            menang_C += menang[2]
            menang_D += menang[3]

            #menambahkan total seri ke variabel simpanan
            seri = total_seri(club1,skor1,skor2,club2)
            seri_A += seri[0]
            seri_B += seri[1]
            seri_C += seri[2]
            seri_D += seri[3]

            #menambahkan total kalah ke variabel simpanan
            kalah = total_kalah(club1,skor1,skor2,club2)
            kalah_A += kalah[0]
            kalah_B += kalah[1]
            kalah_C += kalah[2]
            kalah_D += kalah[3]
            #buat list dari variabel poin,menang,kalah
            #untuk dimasukan ke dalam tabel klasemen
            m =[menang_A,menang_B,menang_C,menang_D]
            s =[seri_A,seri_B,seri_C,seri_D]
            k = [kalah_A,kalah_B,kalah_C,kalah_D]
            p = [poin_A,poin_B,poin_C,poin_D]

            #memanggil tabel klasemen
            print(klasemen(m,s,k,p),"\n")

main()
