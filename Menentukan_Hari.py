print("*"*25)
print("Program menentukan hari")
print("*"*25)
day = int(input("Masukkan hari(angka)>"))
month = int(input("Masukkan bulan(angka)>"))
year = int(input("Masukkan tahun(angka)>"))
if (month == 1):
    month = 13
    year = year - 1

if (month == 2):
    month = 14
    year = year - 1

q = day
m = month
k = year % 100
j = year // 100
h = q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j
h = h % 7

def switch(h):
    return {
        0: "Sabtu",
        1: "Minggu",
        2: "Senin",
        3: "Selasa",
        4: "Rabu",
        5: "Kamis",
        6: "Jumat",
    }[h]

print(switch(h))