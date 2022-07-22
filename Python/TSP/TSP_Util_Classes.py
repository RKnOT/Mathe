
import random
import math
from os import path
import json
import sys
from time import sleep
import re

from PIL import Image 
#-- debug classes
debug_orte_flag = False
debug_tour_flag = False
debug_tours_flag = False
debug_optimize_flag = False
	


#----- preset used values
number_of_Orte = 10
number_of_Tours = 50
number_of_Iterations = 10000
img_name = 'middle-earth.png'


#----- class get_image_content
class Get_image_context:
	def __init__(self, img_file_name = img_name):
		self.img = Image.open(img_file_name)
		self.img_xy_coodinates = [0, self.img.width , 0, self.img.height]
		#print(self.img_xy_coodinates)
#------	


#-------- gen orte
class Orte:
	def __init__(self):
		I_img = Get_image_context()
		self.x_min = I_img.img_xy_coodinates[0]
		self.x_max = I_img.img_xy_coodinates[1]
		self.y_min = I_img.img_xy_coodinates[2]
		self.y_max = I_img.img_xy_coodinates[3]
		self.xy_padding = self.x_max*0.005
		self.json_file_name = 'TSP_Orte.json'
		
	def get_YX(self, nrOrte):
		count =1
		orts_liste = []
		for x in self.rand_gen(self.x_min + self.xy_padding, self.x_max - self.xy_padding, nrOrte):
			x_wert = x
			for y in self.rand_gen(self.y_min+ self.xy_padding, self.y_max- self.xy_padding, nrOrte):
				y_Wert = y
			Name = 'Ort Nr.' + str(count)
			orts_liste.append([Name, x_wert, y_Wert])
			count +=1
		return orts_liste
	
	def rand_gen(self, mi, ma, n=10):
		for i in range(n):
			yield int(random.random()*(ma -mi)+mi)
	
	def read_jason_file(self):
		if (path.exists(self.json_file_name)): # json file mit Orten exsitieren
			
			try:
				with open(self.json_file_name) as json_file:
					O_n = json.load(json_file)
					#self.write_json_file_in_orte_liste(json_orte)
					#print(O_n)
					return O_n
			except ValueError:
				print('kein json file vorhanden')
			
	def write_jason_file(self, list_orte):
		O_n = list_orte
		with open(self.json_file_name, 'w') as outfile:
			json.dump(O_n, outfile)

#------- tour
class Tour():
	def __init__(self, o):
		self.Current_orte = o
		self.Tour_gestr_orte = []
		self.ges_strecke_neu_berechnen()

	def ges_strecke_neu_berechnen(self):
		o = self.Current_orte	
		s = 0.
		for i in range(0, len(o)-1):
			#print(o[i][1], o[i][2])
			delta_x = o[i+1][1] - o[i][1]
			delta_y = o[i+1][2] - o[i][2]
			s += math.sqrt(delta_x*delta_x + delta_y*delta_y)
		delta_x = o[-1][1] - o[0][1]
		delta_y = o[-1][2] - o[0][2]
		s += math.sqrt(delta_x*delta_x + delta_y*delta_y)
		self.Tour_gestr_orte = [s, o]
		#print(self.Tour_gestr_orte)
		return s
	
	def get_gesamt_Strecke(self, tgo =''):
		if tgo=='':
			tgo = self.Tour_gestr_orte[0]
		else:
			tgo = tgo[0]
		gesamt_Strecke = tgo
		
		gesamt_Strecke_str = "{:.3f}".format(tgo)
		
		return gesamt_Strecke , gesamt_Strecke_str
	
	def get_Orte_Tour(self, tgo=''):
		if tgo=='':
			tgo = self.Tour_gestr_orte[1]
		else:
			tgo = tgo[1]
		weg ='Strecke Orte: '
		for item in tgo:
			o = item[0]
			temp = re.findall(r'\d+', o)
			res = list(map(int, temp))
			weg += str(res[0]) + '-'
		weg = weg[0:-1]
		return weg
		
	def debug_print_tour(self, t):
		print('--- tour list ---')
		print(t)
		print('--- tour gesamtstrecke ---')
		print(t[0])
		print('--- tour orte ---')
		print(t[1])
		print('--- tour ort n ---')
		print(t[1][0])
		print('-- print gesamtstecke neu berechnet------')
		self.Current_orte = t[1] # aktuelle tour setzen
		gestr = self.ges_strecke_neu_berechnen() 
		print(gestr)
		print('-------')
	
	
#------- generat tours
class Tours:
	def __init__(self, number_of_Tours, current_orte=''):
		self.List_gesamt_strecken_orte = []
		self.List_gesamt_strecken_orte_sorted = []
		self.List_gesamt_strecken_orte_sorted_rearranged = []
		self.orte_list = current_orte[1]
		self.get_tours(number_of_Tours)
		#print(len(self.List_gesamt_strecken_orte))
		#print(self.List_gesamt_strecken_orte_sorted[0])
		self.re_arrange_Tour_with_Orte_selected_start_name(self.List_gesamt_strecken_orte_sorted)
	
	def get_tours(self,number_of_Tours):
		#print(number_of_Tours)
		for i in range(number_of_Tours):
			#print('--------orte------')
			#print(self.orte_list)
			#print('-----')
			orte_shuffeld, Orte_ges = self.get_shuffeled_list(self.orte_list)
			#print('------orte shuffeld')
			#print(orte_shuffeld, Orte_ges)
			#print('----')
			self.List_gesamt_strecken_orte.append([orte_shuffeld, Orte_ges])
			# sort tours -> shortest tour is on index 0
		self.List_gesamt_strecken_orte_sorted  = sorted(self.List_gesamt_strecken_orte)
		
	def get_shuffeled_list(self, o):
		start_punkt = o[0]
		os = random.sample(o, k =len(o))
		I_tour = Tour(os)
		return I_tour.ges_strecke_neu_berechnen(), os
	
	def re_arrange_Tour_with_Orte_selected_start_name(self, orte, first_element = 'Ort Nr.1', show_list_flag = False):
		#print(orte[0])
		#print('---')
		#print(orte[0][1])
		#print('-----')
		#print(len(orte[0][1]))
		#print('----')
		try:
			index_shortest_strecke = next(x for x, val in enumerate(orte[0][1]) if val[0] == first_element)
		except Exception:
			self.List_gesamt_strecken_orte_sorted_rearranged = orte[0][1]
			return
		re_arranged_Orte = []
		#print(' Ort neuer start ', first_element)
		#print('index of Ort neuer start ', index_shortest_strecke)
		for i in range(index_shortest_strecke, len(orte[0][1])):
			#print(orte[0][1][i])
			re_arranged_Orte.append(orte[0][1][i])
		for i in range(0, index_shortest_strecke):
			#print(orte[0][1][i])
			re_arranged_Orte.append(orte[0][1][i])
		if show_list_flag:
			print('--- re_arrange_Tour_with_Orte_selected_start_name ---- ')
			print('--- original list -----')
			for i in orte[0][1]:
				print(i)
			print('-----')
			print('---re-arranged list -----')
			for i in re_arranged_Orte:
				print(i)
			print('-----')
		# add gesamt strecke
		I_tour_list = Tour(re_arranged_Orte)
		self.List_gesamt_strecken_orte_sorted_rearranged = I_tour_list.Tour_gestr_orte
		#print(self.List_gesamt_strecken_orte_sorted_rearranged)
	
	
	def debug_show_Tours_structure(self, TX):
		#print('--- all tours -----')
		#print(TX)
		#print('-----')
		print('---- tour on index n')
		print(TX[0])
		print('- tour on index n  gesamtstrecke ----')
		print(TX[0][0])
		print('-----')
		print('- tour on index n  orte ----')
		print(TX[0][1]) # tour on index
		print('-----')
		print('- tour on index n  orte elements ----')
		print(TX[0][1][0])
		print('-----')
		print('- tour on index n  orte element ----')
		print(TX[0][1][0][0], '|', TX[0][1][0][1] ,'|',  TX[0][1][0][2])
		print('---- list all gesamtstrecken')
		for i in TX:
			print(i[0])

class get_tours():
	def __init__(self, nrO, nrTs, rw_json = 2, with_tours_flag = True, debug_flag = False):
		if debug_flag:
			if rw_json <= 3:
				index = rw_json
			else:
				index = 4 
			json_list = ['write to json', 'read json', 'read / write to json','no read / write json']
			print('---- Einstellung---')
			print('nrO ', nrO, 'nrTs: ', nrTs, ' rw_jason:', json_list[index-1])
			print('----')
		
		self.I_orte =''
		self.I_t =''
		self.I_ts = ''
		'''
			1 -> write to json
			2 -> read json
			3 -> write and read json
			else -> no read write to json
		'''
		self.I_orte = Orte()
		list_orte = self.I_orte.get_YX(nrO)
		if rw_json == 1:
			self.I_orte.write_jason_file(list_orte)
			l_o_j = list_orte
			pass
		elif rw_json == 2:
			l_o_j = self.I_orte.read_jason_file()
			
			pass
		elif rw_json == 3:
			self.I_orte.write_jason_file(list_orte)
			l_o_j = self.I_orte.read_jason_file()
			pass
		else:
			l_o_j = list_orte
		
		#print(l_o_j)
		self.I_t = Tour(l_o_j)
		#self.I_tour.debug_print_tour(self.I_tour.Tour_gestr_orte)
		self.I_t.get_gesamt_Strecke()
		self.I_t.get_Orte_Tour()
		if with_tours_flag:
			self.I_ts = Tours(nrTs, self.I_t.Tour_gestr_orte)
			#print(len(self.I_ts.List_gesamt_strecken_orte))
			#self.I_ts.debug_show_Tours_structure(self.I_ts.List_gesamt_strecken_orte)
			#self.I_ts.debug_show_Tours_structure(self.I_ts.List_gesamt_strecken_orte_sorted)
			#print(self.I_ts.List_gesamt_strecken_orte_sorted[0])
			#print(self.I_ts.List_gesamt_strecken_orte_sorted_rearranged)
			#print(self.I_t.get_Orte_Tour(self.I_ts.List_gesamt_strecken_orte_sorted_rearranged))
		
	
#-----------------------------------

	
		
if __name__ == '__main__':
	
		
	#---- debug Orte
	if debug_orte_flag:
		I_orte = Orte()
	
		# jason file name ändern
		#I_orte.json_file_name = 'TSP_test.json'
	
		# liste mit orten generieren
		list_orte = I_orte.get_YX(number_of_Orte)
		#print(list_orte)
		print('----')
	
		# neue liste orte in jason speichern
		I_orte.write_jason_file(list_orte)
		# ortsliste aus json file lesen
		l_o_j = I_orte.read_jason_file()
		print(l_o_j)
	
		
		
	#---- debug tour
	

	if debug_tour_flag:
	
		I_orte = Orte()
	
		# jason file name ändern
		#I_orte.json_file_name = 'TSP_test.json'
	
		# liste mit orten generieren
		list_orte = I_orte.get_YX(number_of_Orte)
		#print(list_orte)
		#print('----')
	
		# neue liste orte in jason speichern
		I_orte.write_jason_file(list_orte)
		# ortsliste aus json file lesen
		l_o_j = I_orte.read_jason_file()
		#print(l_o_j)
	
		I_tour = Tour(l_o_j)
		I_tour.debug_print_tour(I_tour.Tour_gestr_orte)
		I_tour.get_gesamt_Strecke()
		I_tour.get_Orte_Tour()
	
	#---- debug tours
	
	if debug_tours_flag:
		
		I_orte = Orte()
		# jason file name ändern
		#I_orte.json_file_name = 'TSP_test.json'
		# liste mit orten generieren
		list_orte = I_orte.get_YX(number_of_Orte)
		l_o_j = list_orte.copy()
		#print(list_orte)	
		# neue liste orte in jason speichern
		#I_orte.write_jason_file(list_orte)
		# ortsliste aus json file lesen
		#l_o_j = I_orte.read_jason_file()
		#print(l_o_j)
	
		#erste tour generieren
		I_tour = Tour(l_o_j)
		#I_tour.debug_print_tour(I_tour.Tour_gestr_orte)
		print(number_of_Tours)
		print(I_tour.Tour_gestr_orte)
		
		
		I_tours = Tours(number_of_Tours, I_tour.Tour_gestr_orte)
		#print(len(I_tours.List_gesamt_strecken_orte))
		#I_tours.debug_show_Tours_structure(I_tours.List_gesamt_strecken_orte)
		#I_tours.debug_show_Tours_structure(I_tours.List_gesamt_strecken_orte_sorted)
		print(I_tours.List_gesamt_strecken_orte_sorted[0])
		print(I_tours.List_gesamt_strecken_orte_sorted_rearranged)
		print(I_tour.get_Orte_Tour(I_tours.List_gesamt_strecken_orte_sorted_rearranged))
	

	#---- tour optimize

	if debug_optimize_flag:
		I_orte = Orte()
		# jason file name ändern
		#I_orte.json_file_name = 'TSP_test.json'
		# liste mit orten generieren
		list_orte = I_orte.get_YX(number_of_Orte)
		l_o_j = list_orte
		#print(list_orte)	
		# neue liste orte in jason speichern
		I_orte.write_jason_file(list_orte)
		# ortsliste aus json file lesen
		l_o_j = I_orte.read_jason_file()
		#print(l_o_j)
		#print('-----')
		#erste tour generieren
		I_tour = Tour(l_o_j)
		#I_tour.debug_print_tour(I_tour.Tour_gestr_orte)
		tour_n = I_tour.Tour_gestr_orte
		#print(tour_n)	
		loop_nr = 0
		list_optimized_strecken = []
		list_optimized_strecken = tour_n
		print(I_tour.get_gesamt_Strecke(), I_tour.get_Orte_Tour())
	
		#print(list_optimized_strecken)
		'''
		values = range(0, 100)
		for i in values:
		print ("Complete: ", i,'\r')
		print ("\rCompleteHJHJ: 100%")
		'''
			

		for i in range(0, number_of_Iterations ):
		
			if  i%10000 == 0:
				print('Loop: ', i, ' von insgesamt ', number_of_Iterations, ' Loops')
			I_tours = Tours(number_of_Tours, tour_n)
			new_gest = I_tours.List_gesamt_strecken_orte_sorted_rearranged
			gesamtstrecke = I_tour.get_gesamt_Strecke(new_gest)
			if list_optimized_strecken[0] > gesamtstrecke:
				print(I_tour.get_gesamt_Strecke(new_gest), I_tour.get_Orte_Tour(new_gest))
				list_optimized_strecken = I_tours.List_gesamt_strecken_orte_sorted_rearranged	
				loop_nr = i
		print('-----')
			
		print('loop Nr.', loop_nr, '', I_tour.get_gesamt_Strecke(list_optimized_strecken), I_tour.get_Orte_Tour(list_optimized_strecken))
		I_orte.write_jason_file(list_optimized_strecken[1])
	
				
			
			
