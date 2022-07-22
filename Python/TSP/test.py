
import matplotlib.pyplot as plt
from io import BytesIO
#import os.path
from os import path

import io, math, ui
from PIL import Image

import ui,requests,Image
from io import BytesIO
Image_url = 'middle-earth.png'

#image_data = BytesIO(requests.get(image_url).content)

#image = Image.open(image_data)

#w,h = ui.get_screen_size()

v = ui.load_view('TSP_UI')
#v.present('sheet', hide_title_bar=True)
v.present('panel')

v['image1'].frame = (205,128,600,415)


def pil_to_ui(img):
    with io.BytesIO() as b:
        img.save(b, "png")
        return ui.Image.from_data(b.getvalue())

im = Image.open('middle-earth.png')
#print(im.info)
# manipulate im pixels
pix = im.load()
dy = 0
for i in range(0,199):
	pix[i,40+dy]= 10, 120, 70,255
	pix[i,41+dy]= 10, 120, 70,255
	pix[i,42+dy]= 10, 120, 70,255
	dy +=1
	#for k in range(0,400):
		#print( pix[30, 33])
		#pix[i, k] = 142, 121, 85, 31
#print( pix[30, 33])

img_ui = pil_to_ui(im)

v['image1'].image = img_ui
'''
#-------
#im.rotate(45).show()
#im.rotate(45)
#v['image1'].image = im

print( ui.Image('middle-earth.png'))
xxx = ui.ImageView(im)


with ui.ImageContext(100, 100) as ctx:
    ui.set_color('white')
    ui.fill_rect(0, 0, 100, 100)
    ui.set_color('red')
    circle = ui.Path.oval(10, 10, 80, 80)
    circle.fill()
    img = ctx.get_image()
    #img.show()








#v['image1'].image = img

v.add_subview(ui.ImageView(frame=(0, 0, 500, 500) ))
v.subviews[1].image = ui.Image.named('test:Peppers')
v.add_subview(ui.ImageView(frame=(0, 0, 500, 500)))
v.subviews[0].image = ui.Image('middle-earth.png')


#v.present('sheet', hide_title_bar=True)
v.present('panel')

#-------------
#Hello World
v = ui.View()

l = ui.Label()
l.text = 'Hello'
l.border_width = 2
v.add_subview(l)

l2 = ui.Label()
l2.text = 'World'
l2.border_width = 2
l2.x = 50
l2.y = 110
v.add_subview(l2)

v.present('panel')
#-------------



#---------------
label_count = 10
label_height = 100

v = ui.ScrollView()
v.content_size = (100, label_count * label_height)

for i in range(label_count):
	l = ui.Label()
	l.text = 'TestLabel:' + str(i)
	l.y = i * label_height
	l.border_width = 2
	l.flex = 'W'
	
	v.add_subview(l)

v.present('panel')
#--------------

#----------------
class MyView(ui.View):
	def __init__(self):
		l = ui.Label(name='poslabel')
		l.background_color = '#dddddd'
		l.flex = 'W'
		l.height = 50
		self.add_subview(l)
		
		l2 = ui.Label(name='loglabel')
		l2.background_color = '#ddddff'
		l2.flex = 'W'
		l2.number_of_lines = 0
		l2.y = l.height
		l2.height = 600 - l.height
		self.add_subview(l2)
		
		self.m_logs = []
		pass
		
	def log_msg(self, msg):
		self.m_logs.append(msg)
		self['loglabel'].text = "\n".join(self.m_logs[-20:])
		
	def log_touch(self, touch):
		self['poslabel'].text = str(touch.location)
		
	def did_load(self):
		self.log_msg('did_load called.')
		
	def will_close(self):
		self.log_msg('will_close called.')
		
	def draw(self):
		self.log_msg('draw called.')
		
	def layout(self):
		self.log_msg('layout called.')
		
	def touch_began(self, touch):
		self.log_msg('touch_began called.' + str(touch.location))
		self.log_touch(touch)
		
	def touch_moved(self, touch):
		self.log_msg('touch_moved called.' + str(touch.location))
		self.log_touch(touch)
	
	def touch_ended(self, touch):
		self.log_msg('touch_ended called.' + str(touch.location))
		self.log_touch(touch)
		
v = MyView()
v.present('fullscreen')

#-------------------------


v = ui.ScrollView()
v.content_size = (100, label_count * label_height)

from PIL import Image
im = Image.open('middle-earth.png')
#im.rotate(45).show()
#im.rotate(45)
#v['image1'].image = ui.Image(im)




print(im.info)
# manipulate im pixels
pix = im.load()
for i in range(0,400):
	for k in range(0,400):
		#print( pix[30, 33])
		pix[i, k] = 142, 121, 85, 31
#print( pix[30, 33])

im.show()





a = ui.load_view('TSP_UI')
a.add_subview(ui.ImageView(frame=(0, 0, 500, 500)))
a.subviews[0].image = ui.Image.named('test:Peppers')
#a.add_subview(ui.ImageView(frame=(0, 0, 500, 500)))
#a.subviews[1].image = ui.Image('middle-earth.png')
a.present('sheet', hide_title_bar=True)
 		




Img_view = ui.ImageView()

Img_view.frame() = testview.frame()

testview.add_subview(img_view)

testview.present()

v.image= ui.Image.from_data(image.tobytes())

 
# Plotting a figure of width 3 and height 6
#plt_1 = plt.figure(figsize=(8, 6))
 
# Let's plot the equation y=2*x
x = [1, 2, 3, 4, 5]
 
# y = [2,4,6,8,10]
y = [x*2 for x in x]
 
# plt.plot() specifies the arguments for
# x-axis and y-axis to be plotted
plt.plot(x, y)
plt.axis('off')
extend = 0, 600, 0, 415

plt.imshow(plt.imread("middle-earth.png"), cmap ="binary_r", interpolation ='nearest', extent= extend, alpha = 0.5)
# To show this figure object, we use the line,
# fig.show()
#plt.show()
# load ui
v = ui.load_view('TSP_UI')
v.present('sheet')
#v['image1'].image = ui.Image('middle-earth.png')

b = BytesIO()
plt.savefig(b)
img = ui.Image.from_data(b.getvalue())
	
v['image1'].image = img

v['image1'].image = ui.Image('middle-earth.png')
'''
