# coding: utf-8
import time

import matplotlib.pyplot as plt 

import json
from io import BytesIO
#import os.path
from os import path

import io, math, ui

import TSP_Util_Classes as C_utils
from PIL import Image


def draw_tour(t,v): # list orte
	#print(t)
	
	xl =[]
	yl =[]    
	x_last = []
	y_last = []
	x_last.append(t[-1][1])
	y_last.append(t[-1][2])
	x_first = t[0][1]
	y_first = t[0][2]
	x_last.append(x_first)
	y_last.append(y_first)
		
	for i in range(0, len(t)):
		#print(t[i])
		
		xl.append(t[i][1])
		yl.append(t[i][2])
	
	cm = 1/2.54  # centimeters in inches
	#plt.subplots(figsize=(#5*cm, 15*cm))
	
	#plt.figure(figsize=(2, 6))
	#plt.axis('off')
	#fig, ax = plt.subplots()
	#fig.set_size_inches(1, 1, forward=True)
	#plt.rcParams["figure.figsize"] = [7.50, 3.50]
	#plt.rcParams["figure.autolayout"] = True
	#ax.format_coord = lambda x, y: ''
	#plt.imshow(plt.imread("middle-earth-flip.png"))
	#plt.plot(xl, yl, color="green", linewidth = 2)
	#plt.plot(x_last, y_last, color="red", linewidth = 3)
	#plt.scatter(x_first, y_first, color = 'black', linewidth = 5)
	#plt.set_axis_off() 
	#plt.xlim( 0.2, 600- 0.2)
	#plt.ylim( 0.2, 415 - 0.2)
	#plt.xlabel("X")
	#plt.ylabel("Y")
	#plt.title("Red shortest TSP tour " , shortes)
	#plt.show()
	
	#b = BytesIO()
	#plt.savefig(b)
	#img = ui.Image.from_data(b.getvalue())
	
	#v['image1'].image = img
	
	#a = ui.load_view('TSP_UI')
	#a.add_subview(ui.ImageView(frame=(0, 0, 500, 500)))
	#a.subviews[0].image = ui.Image.named('test:Peppers')
	#a.add_subview(ui.ImageView(frame=(0, 0, 500, 500)))
	#a.subviews[1].image = ui.Image('middle-earth.png')
	#a.present('sheet', hide_title_bar=True)

	
	
if __name__ == '__main__':
	#----------- Definitionen
	number_of_Orte = 20
	number_of_Tours = 100
	number_of_Iterations = 10000
	img = Image.open('middle-earth.png')
	flag_read_json = False
	#print(img.width, img.height)
	
	
	# load ui
	v = ui.load_view('TSP_UI')
	v.present('sheet')
	v['image1'].image = ui.Image('middle-earth.png')
	
	'''
	#----------
	I_orte = C_utils.Orte(0, img.width, 0, img.height)
	# jason file name ändern
	#I_orte.json_file_name = 'TSP_test.json'
	# liste mit orten generieren
	list_orte = I_orte.get_YX(number_of_Orte)
	l_o_j = list_orte
	#print(list_orte)	
	# neue liste orte in jason speichern
	if flag_read_json:
		I_orte.write_jason_file(list_orte)
	# ortsliste aus json file lesen
	#l_o_j = I_orte.read_jason_file()
	#print(l_o_j)
	#print('-----')
	#erste tour generieren
	I_tour = C_utils.Tour(l_o_j)
	#I_tour.debug_print_tour(I_tour.Tour_gestr_orte)
	tour_n = I_tour.Tour_gestr_orte
	#print(tour_n)	
	loop_nr = 0
	list_optimized_strecken = []
	list_optimized_strecken = tour_n
	#print(I_tour.get_gesamt_Strecke(), I_tour.get_Orte_Tour())
	
	draw_tour(l_o_j, v)
	
	for i in range(0, number_of_Iterations ):
		
		if  i%10000 == 0:
			#print('Loop: ', i, ' von insgesamt ', number_of_Iterations, ' Loops')
			pass
		I_tours = C_utils.Tours(number_of_Tours, tour_n)
		new_gest = I_tours.List_gesamt_strecken_orte_sorted_rearranged
		gesamtstrecke = I_tour.get_gesamt_Strecke(new_gest)
		if list_optimized_strecken[0][0] > gesamtstrecke:
			print(I_tour.get_gesamt_Strecke(new_gest), I_tour.get_Orte_Tour(new_gest))
			list_optimized_strecken = I_tours.List_gesamt_strecken_orte_sorted_rearranged	
			loop_nr = i
			draw_tour(list_optimized_strecken[1],v)
	print('-----')
			
	print('loop Nr.', loop_nr, '', I_tour.get_gesamt_Strecke(list_optimized_strecken), I_tour.get_Orte_Tour(list_optimized_strecken))
	draw_tour(list_optimized_strecken[1], v)
	if flag_read_json == False: 
		I_orte.write_jason_file(list_optimized_strecken[1])
'''

