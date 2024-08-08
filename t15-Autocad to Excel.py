#YÊU CẦU: 28 BÀI PYTHON CHO AUTOCAD
#YÊU CẦU: 5 BÀI (001 ĐẾN 005): PYTHON EXCEL

from pyautocad import Autocad, APoint
import pandas as pd #CHÈN THƯ VIỆN PANDAS

#ĐƯỜNG DẪN MỞ FILE EXCEL
duong_dan = r'C:\Users\DELL\Desktop\Python CAD\Autocad-to-Excel.xlsx' 
#ĐƯỜNG DẪN SAVE FILE EXCEL
vi_tri_luu = r'C:\Users\DELL\Desktop\Python CAD\Autocad-to-Excel-new.xlsx'

acad = Autocad()
file_excel = pd.read_excel(duong_dan,sheet_name = 0) #MỞ FILE EXCEL, SHEET1

b = acad.get_selection() #YÊU CẦU NGƯỜI DÙNG LỰA CHỌN ĐỐI TƯỢNG (LỰA CHỌN NHIỀU ĐƯỢC)

for i in b:
    danh_sach = i.Coordinates #LẤY TOẠ ĐỘ ĐIỂM
    for n in range(len(danh_sach)): #len(danh_sach) đếm số phần tử trong danh sách
        file_excel.loc[n,'Tọa Độ'] = danh_sach[n] #XUẤT SANG EXCEL
        file_excel.to_excel(vi_tri_luu)
acad.prompt('ĐÃ XUẤT XONG TOẠ ĐỘ')