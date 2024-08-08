#IMPORT THƯ VIỆN
from pyautocad import Autocad
a = Autocad()

layer_count = a.doc.Layers.count #ĐẾM SỐ LƯỢNG LAYER
sl_layer_str = str(layer_count)

print("Số layer là: " + sl_layer_str) #IN RA SỐ LƯỢNG LAYER
layers_names = [a.doc.Layers.Item(i).Name 
                for i in range(layer_count)] # LẤY TÊN TẤT CẢ LAYER
#layers_names là list nên dùng [] tạo mảng
#a.doc.Layers.Item(i).Name : hiển thị tên layer đó, đặt biến i
#for i in range(layer_count): lặp số lần bằng số layer

x = 1

for i in layers_names: 
    print('Tên layer thứ ' + str(x) + ' là: ' + i) #IN RA TOÀN BỘ TÊN LAYER
    x+=1
    #i ở đây khác i trên
    #với mỗi biến trong mảng layers_names, in ra...