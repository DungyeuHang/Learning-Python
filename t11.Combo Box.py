#IMPORT THƯ VIỆN
from tkinter.ttk import * #thư viện tạo ra combo box
from tkinter import * #thư viện chạy ra hộp thoại

#CODE TẠO CỬA SỔ TKINTER
window = Tk()
window.title('Lựa chọn rau củ quả')
window.geometry('400x400') 

#CODE TẠO LABEL
lbl = Label(window, 
            text = 'Loại rau củ', 
            font = ('Times New Roman',14))
lbl.place(x = 20, y = 20)

#CODE TẠO COMBO BOX
combo = Combobox(window, 
                 font = ('Times New Roman',14), 
                 width=20) #THIẾT LẬP HIỂN THỊ COMBO BOX
combo['value'] = ('Cà Rốt', 'Cải Thìa', 'Rau Quế', 'Cà Chua', 'Khoai tây')
#LIST DANH SÁCH TRONG COMBO BOX
combo.current(3) #Hiển thị mặc định đếm 0, 1, 2...
combo.place(x = 150, y = 20)

#CODE TẠO BUTTON
def clicked():
    name = Label(window, width = 0, 
                 text = 'Bạn đã chọn: ' + combo.get(), 
                 font = ('Times New Roman',10), fg = 'red')
    name.place(x = 50, y = 200)
btn = Button(window, text= 'Lựa chọn', command=clicked)
btn.place(x = 150, y = 100)


#VÒNG LẶP TKINTER
window.mainloop()