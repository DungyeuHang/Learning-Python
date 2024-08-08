from tkinter import *
from PIL import ImageTk, Image
import random 




#Tạo tkinter
giao_dien = Tk()
giao_dien.title('Kéo búa bao')
giao_dien.geometry('700x700')

ban_thang = 0
may_thang = 0


lua_chon = ['kéo', 'búa', 'bao']



#import hình ảnh scissors:
scissors_import = (Image.open(r'C:\Users\DELL\Desktop\Rock scissors paper\scissors.png'))
scissors_size = scissors_import.resize((150,150), Image.LANCZOS)
img_scissors = ImageTk.PhotoImage(scissors_size)

#chọn scissors
def chon_scissors():
    global may_thang
    global ban_thang
    ban_chon = 'kéo'
    hien_thi = Label(giao_dien, 
              text='Bạn đã chọn kéo', 
              font=('times new roman', 20))
    hien_thi.place(x=20,y=50)
    random.shuffle(lua_chon)
    may_chon = lua_chon[1]
    hien_thi_may = Label(giao_dien, 
              text='Máy đã chọn ' + may_chon, 
              font=('times new roman', 20),)
    hien_thi_may.place(x=20,y=200)
    if ban_chon == 'kéo' and may_chon == 'kéo': 
        hoa_nhau = Label(giao_dien, 
              text='Kết quả hòa nhau', 
              font=('times new roman', 20),
              bg= 'white')
        hoa_nhau.place(x=20,y=150)
    elif ban_chon == 'kéo' and may_chon == 'búa':
        ban_thua = Label(giao_dien, 
              text='Bạn thua             ', 
              font=('times new roman', 20),
              bg= 'white')
        ban_thua.place(x=20,y=150)
        may_thang+=1
    else:
        may_thua = Label(giao_dien, 
              text='Bạn thắng            ', 
              font=('times new roman', 20),
              bg= 'white')
        may_thua.place(x=20,y=150)
        ban_thang+=1
    ti_so = Label(giao_dien, 
              text='Tỷ số giữa bạn và máy là: '+ str(ban_thang) + ' - '  + str(may_thang), 
              font=('times new roman', 20),)
    ti_so.place(x=20,y=100)

#Import hình ảnh scissors vào button
hinh_scissors = Button(giao_dien, 
                 text ='', 
                 font=('times new roman', 13), 
                 image = img_scissors,
                 command= chon_scissors
                 )
hinh_scissors.place(x=75, y=250)







#import hình ảnh rock:
rock_import = (Image.open(r'C:\Users\DELL\Desktop\Rock scissors paper\rock.png'))
rock_size = rock_import.resize((150,150), Image.LANCZOS)
img_rock = ImageTk.PhotoImage(rock_size)
#chọn rock
def chon_rock():
    global may_thang
    global ban_thang
    hien_thi = Label(giao_dien, 
              text='Bạn đã chọn búa', 
              font=('times new roman', 20))
    hien_thi.place(x=20,y=50)
    random.shuffle(lua_chon)
    may_chon = lua_chon[1]
    hien_thi_may = Label(giao_dien, 
              text='Máy đã chọn ' + may_chon, 
              font=('times new roman', 20),)
    hien_thi_may.place(x=20,y=200)
    ban_chon = 'búa'
    if ban_chon == 'búa' and may_chon == 'búa': 
        hoa_nhau = Label(giao_dien, 
              text='Kết quả hòa nhau', 
              font=('times new roman', 20),
              bg= 'white')
        hoa_nhau.place(x=20,y=150)
    elif ban_chon == 'búa' and may_chon == 'bao':
        ban_thua = Label(giao_dien, 
              text='Bạn thua             ', 
              font=('times new roman', 20),
              bg= 'white')
        ban_thua.place(x=20,y=150)
        may_thang+=1 
    else:
        may_thua = Label(giao_dien, 
              text='Bạn thắng            ', 
              font=('times new roman', 20),
              bg= 'white')
        may_thua.place(x=20,y=150)
        ban_thang+=1
    ti_so = Label(giao_dien, 
              text='Tỷ số giữa bạn và máy là: '+ str(ban_thang) + ' - '  + str(may_thang), 
              font=('times new roman', 20),)
    ti_so.place(x=20,y=100)




#Import hình ảnh rock vào button
hinh_rock = Button(giao_dien, 
                 text ='', 
                 font=('times new roman', 13), 
                 image = img_rock,
                 command=chon_rock)
hinh_rock.place(x=275, y=250)



#import hình ảnh paper:
paper_import = (Image.open(r'C:\Users\DELL\Desktop\Rock scissors paper\paper.png'))
paper_size = paper_import.resize((150,250), Image.LANCZOS)
img_paper = ImageTk.PhotoImage(paper_size)
#chọn paper
def chon_paper():
    global may_thang
    global ban_thang
    ban_chon = 'bao'
    hien_thi = Label(giao_dien, 
              text='Bạn đã chọn bao', 
              font=('times new roman', 20),)
    hien_thi.place(x=20,y=50)
    random.shuffle(lua_chon)
    may_chon = lua_chon[1]
    hien_thi_may = Label(giao_dien, 
              text='Máy đã chọn ' + may_chon, 
              font=('times new roman', 20),)
    hien_thi_may.place(x=20,y=200)
    if ban_chon == 'bao' and may_chon == 'bao': 
        hoa_nhau = Label(giao_dien, 
              text='Kết quả hòa nhau', 
              font=('times new roman', 20),
              bg= 'white')
        hoa_nhau.place(x=20,y=150)
    elif ban_chon == 'bao' and may_chon == 'kéo':
        ban_thua = Label(giao_dien, 
              text='Bạn thua             ', 
              font=('times new roman', 20),
              bg= 'white')
        ban_thua.place(x=20,y=150)
        may_thang+=1 
    else:
        may_thua = Label(giao_dien, 
              text='Bạn thắng            ', 
              font=('times new roman', 20),
              bg= 'white')
        may_thua.place(x=20,y=150)
        ban_thang+=1
    ti_so = Label(giao_dien, 
              text='Tỷ số giữa bạn và máy là: '+ str(ban_thang) + ' - '  + str(may_thang), 
              font=('times new roman', 20),)
    ti_so.place(x=20,y=100)



#Import hình ảnh paper vào button
hinh_paper = Button(giao_dien, 
                 text ='', 
                 font=('times new roman', 13), 
                 image = img_paper,
                 command=chon_paper)
hinh_paper.place(x=475, y=250)











mainloop()