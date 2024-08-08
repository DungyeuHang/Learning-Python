from pyautocad import Autocad
a = Autocad()
new_layer = a.doc.Layers.Add('Hằng yêu Dũng')
new_layer.color = 1
new_layer.Linetype = 'Continuous'
#new_layer.Lineweight = .03 #????
