
import io, math, ui
from PIL import Image
import time

import requests
from io import BytesIO
import TSP_Util_Classes as C_utils

number_of_Orte = 15
number_of_Tours = 15
number_of_Iterations = 1000



def pil_to_ui(img):
	with io.BytesIO() as b:
		img.save(b, "png")
		return ui.Image.from_data(b.getvalue())

#--- class draw line
class draw_line():
	def __init__(self, p1 = [500,415], p2=[600,0] ):
		self.P1 = p1
		self.P2 = p2
		self.m = 0
		self.b = 0
		self.dx = p2[0]-p1[0]
		self.dy = p2[1]-p1[1]
		self.ps_xy_list =[]
		self.get_geraden_gleichung(self.P1, self.P2)
		self.get_line_points(self.P1, self.P2)
		
	def get_geraden_gleichung(self, p1,p2):
		#print(self.dx, self.dy)
		# m berechnen
		if self.dx != 0:
			self.m = self.dy / self.dx
			self.b = p1[1] - self.m*p1[0]
		else:
			self.m= 10*math.exp(100)
			self.b= p1[0]
		
	def get_line_points(self, p1, p2):
		#print(self.dx, self.dy)
		if abs(self.dx) > abs(self.dy):
			vz = 1
			x1 = p1[0]
			x2 = p2[0]
			if x1 > x2: vz =-1
			#print(x1,x2, vz)
			for dx in range(x1, x2+vz, vz):
				dy = dx*self.m + self.b
				self.ps_xy_list.append([int(dx), int(dy)])
		else:	
			vz =1
			y1 = p1[1]
			y2 = p2[1]
			if y1 > y2: vz =-1
			#print(y1,y2,vz)
			for dy in range(y1, y2+vz, vz):
				dx = (dy - self.b) / self.m
				self.ps_xy_list.append([int(dx), int(dy)])
		#print(self.ps_xy_list)
#------------				

def get_image_lines(I_image, o_list, lw =2):

	im = I_image.img.copy()
	im_xy_max = [I_image.img_xy_coodinates[1] , I_image.img_xy_coodinates[3]]
	
	
	for i in range(0,10):
		im = I_image.img.copy()
		# manipulate im pixels
		pix = im.load()

		
		for i in range(0, len(o_list)-1):
	
			p1 = [o_list[i][1], o_list[i][2]]
			p2 = [o_list[i+1][1], o_list[i+1][2]]
			line_points = draw_line(p1,p2)
	
			for item in line_points.ps_xy_list:
				#v['textview1'].text = 'p1' + str(p1)+ ' p2 '+ str(p2)
				for i in range(0, lw):
					xp = item[0]+i
					yp = item[1]+i
					#print(xp,yp, im_xy_max[0])
					if xp > im_xy_max[0]-1: 
						xp = im_xy_max[0]-1
					if yp > im_xy_max[1]-1: 
						yp = im_xy_max[1]-1
					pix[xp, yp] = 255, 30, 2,255
			
					#xp = item[0]+i
					#yp = item[1]+i		
		img_ui = pil_to_ui(im)
		#v['textview1'].text = 'wewewe'
		v['image1'].image = img_ui	
		
		v.set_needs_display()
		
		
	pass
#----------------
@ui.in_background
def tour_optimizer(loops, nO, nTs, js, ag, I_im, v):
	#print(loops, nO, nTs, js)
	I_tours = C_utils.get_tours(nO, nTs, rw_json= js)

	I_orte = I_tours.I_orte
	I_tour = I_tours.I_t
	I_tours = I_tours.I_ts

	tour_n = I_tour.Tour_gestr_orte
	#print(tour_n)	
	loop_nr = 0
	list_optimized_strecken = []
	list_optimized_strecken = tour_n
	gest, gest_str =I_tour.get_gesamt_Strecke()
	#print(gest_str, I_tour.get_Orte_Tour())
	#print('------')
	v[ag].text = 'loop Nr. ' + gest_str + '\n'+ I_tour.get_Orte_Tour()
	
	#get_image_lines(I_im, I_tour.Current_orte, 4)
	
	for i in range(0, loops ):
		if  i%loops == 0:
			#print('Loop: ', i, ' von insgesamt ', number_of_Iterations, 'Loops')
			v[ag].text = 'Loop Nr: ' + str(i) + ' von insgesamt ' +str(number_of_Iterations)+ ' Loops'
		I_tours = C_utils.Tours(number_of_Tours, tour_n)
		new_gest = I_tours.List_gesamt_strecken_orte_sorted_rearranged
		gesamtstrecke, gesamtstrecke_str  = I_tour.get_gesamt_Strecke(new_gest)
		#get_image_lines(I_im, I_tour.Current_orte, 4)
		#print(list_optimized_strecken[0], gesamtstrecke, I_tour.get_Orte_Tour(new_gest))
		if list_optimized_strecken[0] > gesamtstrecke:
			gest, gest_str = I_tour.get_gesamt_Strecke(new_gest)
			v.set_needs_display()
		
			#time.sleep(1)
			#print(gest_str, I_tour.get_Orte_Tour(new_gest))
			v[ag].text = 'Gesamtstrecke: ' + gest_str + '\n' + I_tour.get_Orte_Tour(new_gest)
			list_optimized_strecken = I_tours.List_gesamt_strecken_orte_sorted_rearranged	
			
			get_image_lines(I_im, I_tour.Current_orte, 4)
			
			loop_nr = i
	#print('-----')
	gest, gest_str = I_tour.get_gesamt_Strecke(list_optimized_strecken)
	#print('loop Nr.', loop_nr, '',  gest_str, I_tour.get_Orte_Tour(list_optimized_strecken) )
	
	v[ag].text = 'loop Nr. ' + str(loop_nr) + ' \n' + 'Gesamtstrecke: ' + gest_str+ '\n'+ I_tour.get_Orte_Tour(list_optimized_strecken)
	I_orte.write_jason_file(list_optimized_strecken[1])
	
#----------

def read_UI(UI_Name, preset):
	w = v[UI_Name].text
	#print(w)
	try:
		w_int = int(w)
	except:
		w_int = str(preset)
		v[UI_Name].text = str(preset)
	return int(w_int)
	
	
def start_tsp(sender):
	nrO = read_UI('nrO', 20)
	nrTs = read_UI('nrTs', 50)
	nrLoops = read_UI('nrLoops', 1000)
	nrJson = read_UI('nrJson', 3)
	#print(nrO, nrTs, nrJson)
	I_im = C_utils.Get_image_context()
	im = I_im.img
	ausgabe = 'textview1'
	tour_optimizer(nrLoops, nrO, nrTs,  nrJson, ausgabe, I_im, v)

#-----------
v = ui.load_view('TSP_UI')
v.present('sheet', hide_title_bar=True)
#v.present('panel')


		
v['image1'].frame = (205,128,600,415)


#get_image_lines(I_im, o_list)


'''








#-----------	
#v['image1'].image = xxx
with ui.ImageContext(100, 100) as ctx:
	with ui.GState():
		ui.concat_ctm(ui.Transform.rotation(0.1))
		ui.draw_string('    Rotated text')
	ui.draw_string('Not rotated')
	img = ctx.get_image()
#v['image1'].image = img
#-----------


v = ui.load_view('TSP_UI')
#v.present('sheet', hide_title_bar=True)
#v.present('panel')

v['image1'].frame = (205,128,600,415)





I_im = C_utils.Get_image_context()
im = I_im.img
#. rotate image
winkel = 1
for i in range(0, winkel):
	imr = im.rotate(i)
	img_ui = pil_to_ui(imr)
	#v['image1'].image = img_ui

for i in range(winkel, -1,-1):
	imr = im.rotate(i)
	img_ui = pil_to_ui(imr)
	#v['image1'].image = img_ui
	
v['image1'].frame = (205,128,600,415)


'''

