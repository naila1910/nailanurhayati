#Set dalam bahasa Indonesia adalah “himpunan”, merupakan struktur data yang dapat memiliki satu atau lebih anggota didalamnya.
#cara inisiasi set
#1 (kurung kurawal )
import sys

tokenword: set[str] = {"tidak", "bisa", "makan"}
print(tokenword)
print(type(tokenword))
print("ukuran memori: ",  sys.getsizeof(tokenword))

#2 (set())
katasambung: set[str] = set(["kemudian", "lalu", "setelah"])
print(katasambung)
print(type(katasambung))
print("ukuran memori: ",  sys.getsizeof(katasambung))

#pembuktian terkait tidak memiliki sistem indexing
#print(katasambung[-1])

#menghapus elemen pada set
katasambung.remove("kemudian")
print(katasambung)
tokenword.discard("tidak")
print(tokenword)

#menambahkan elemen pada set
tokenword.add("mungkin")
print(tokenword)
tokenword.update(["pasti", "mungkin",])
print(tokenword)

#mengubah elemen pada set
tokenword.remove("mungkin")
tokenword.add("mungkin")
print(tokenword)

#operasi pada set
setA: set[int] = {1, 2, 3, 4}
setB: set[int] = {3, 4, 5, 6}

#union(gabungan)
print(setA|setB)
#intersection(irisan)
print(setA&setB)
#difference(selisih)
print(setA-setB)
#symmetric difference(selisih simetris/beda setangkup)
print(setA^setB)
#cartesian product(hasil kali kartesius)
print({(a, b) for a in setA for b in setB})