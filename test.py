from pyautocad import Autocad, APoint
acad = Autocad()
doc = acad.ActiveDocument
import sys

key_word = str(input('Ban muon ve song tron <tr>, thoi <th> hay song vuong <v>'))
if key_word == 'tr':
    duong_kinh_song = 34.5
elif key_word == 'th':
    duong_kinh_song = 41.5
elif key_word == 'v':
    duong_kinh_song = 31
else :
    sys.exit("Khong ro loai song")

print(duong_kinh_song)

doituong = acad.get_selection('Chọn đối tượng')

diem_tam = APoint(doc.Utility.GetPoint())

print('Nhap kich thuoc do: ')
ktdo = float(input())
sls_test = 21
for x in range (9):
    sls_test -=2
    khoang_sang = (ktdo -sls_test*duong_kinh_song)/(sls_test+1)
    tam_lo_song = khoang_sang + duong_kinh_song

    if 130 < tam_lo_song < 160:
        tam_song = tam_lo_song
        so_song = sls_test
    elif 100 < tam_lo_song <130:
        tam_song = tam_lo_song
        so_song = sls_test



sosong = so_song//2

diem_copy_1 = APoint(tam_song, 0)
diem_copy_2 = APoint(-tam_song, 0)

for i in doituong:
    for x in range(sosong):
        x +=1
        songx = i.Copy()
        songx.Move(diem_tam, APoint((tam_song*x), diem_tam.y))
for i in doituong:
    for x in range(sosong):
        x +=1
        songx = i.Copy()
        songx.Move(diem_tam, APoint((tam_song*(-x)), diem_tam.y))
print('Số song là: ' + str(so_song))
print('Khoảng cách tâm song là: ' + str(tam_song))

