data_list = [2, 10, 50, 23, 28, 31, 34, 56, 89, 200]
cari = int(input("Masukkan Angka Yang Anda Cari : "))

def bubble_sort(lis,search):
    counter = 0
    while counter != len(data_list):
        if data_list[counter] == search:
            result = counter
        counter += 1
    return result

hasil = bubble_sort(data_list,cari)+1
if cari not in data_list:
    print(data_list)
    print("Element tidak ditemukan pada list")
else:
    print("Sesudah di sorting",data_list)
    print('Element ditemukan pada posisi ke', hasil)