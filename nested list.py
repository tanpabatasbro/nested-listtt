peserta_1 = ["kaco",19,"laki-laki"]
peserta_2 = ["becce",17,"perempuan"]
peserta_3 = ["bacok",18,"laki-laki"]

list_peserta = [peserta_1,peserta_2,peserta_3]
print(f"peserta = {list_peserta}")

for peserta in list_peserta:
    print(f"nama\t:{peserta[0]}")
    print(f"umur\t:{peserta[1]}")
    print(f"gender\t:{peserta[2]}\n")
