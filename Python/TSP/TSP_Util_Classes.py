
import random
import math


from PIL import Image 
 

#-------- gen orte
class Orte:
    
    class Ort_Data:
    	def __init__(self):
    		self.X = 0.
    		self.Y = 0.
    		self.Name = ''
    		
    		
    def __init__(self,xmin, xmax, ymin, ymax):
    	self.Orte =[]
    	self.x_min = xmin
    	self.x_max = xmax
    	self.y_min = ymin
    	self.y_max = ymax
    	self.xy_padding = self.x_max*0.005
    	
    def rand_gen(self, mi, ma, n=10):
            for i in range(n):
                yield random.random()*(ma -mi)+mi

    def get_YX(self, nrOrte):
            count =1
            od = self.Ort_Data()
            for x in self.rand_gen(self.x_min + self.xy_padding, self.x_max - self.xy_padding, nrOrte
            ):
                Ort = Orte.Ort_Data()
                for y in self.rand_gen(self.y_min+ self.xy_padding, self.y_max- self.xy_padding, nrOrte):
                    Ort.X = x
                    Ort.Y = y
                Ort.Name = 'Ort Nr.' + str(count)
                self.Orte.append(Ort)
                count +=1
    
    def read_json_Ort(self, json_data):
            #print(data)
            for i in json_data['ort']:
                Ort = Orte.Ort_Data()
                Ort.X = i['X']
                Ort.Y = i['Y']
                Ort.Name = i['Name']
                self.Orte.append(Ort)
                
    def write_Orte_in_tuple(self, data):
        Orte_Tuple = {}
        Orte_Tuple['ort'] =[]
        for i in data:
            #print(i.X)
            Orte_Tuple['ort'].append({
            'X': i.X,
            'Y': i.Y,
            'Name': i.Name
            })
    
        return Orte_Tuple
#------- tour
class Tour:
    
    def __init__(self, orte):
        self.List_orte_gesamt_strecke = [[self.get_Gesamtstrecke(orte)], [orte]]
        
    def get_Gesamtstrecke(self, o):
        s = 0.
        for i in range(0, len(o)-1):
            delta_x = o[i+1].X - o[i].X
            delta_y = o[i+1].Y - o[i].Y
            s += math.sqrt(delta_x*delta_x + delta_y*delta_y)
        return s

#------- generat tours
class Tours:
	def __init__(self, number_of_Tours, current_orte=''):
		self.List_orte_gesamt_strecken = []
		self.List_orte_gesamt_strecken_sorted = []
		self.get_tours(number_of_Tours, current_orte)
		
	def get_tours(self,number_of_Tours, current_orte):
		for i in range(number_of_Tours):
			if i==0:
				if current_orte == '':
					a = Orte(0, img.width, 0, img.height)
					a.get_YX(number_of_Orte)
					orte = a.Orte
				else:
					orte = current_orte
			orte_shuffeld, ges = self.get_shuffeled_list(orte)
			self.List_orte_gesamt_strecken.append([ges, orte_shuffeld])
		self.List_orte_gesamt_strecken_sorted = sorted(self.List_orte_gesamt_strecken)
	
	def get_shuffeled_list(self, o):
		start_punkt = o[0]
		#print(start_punkt.Name)
		os = random.sample(o, k =len(o))
		t = Tour(os)
		t_shuffle_ges = t.get_Gesamtstrecke(os)
		return os, t_shuffle_ges

#------------
#------ get shortest tour

class get_shortest_tour:
	def __init__(self, nr_tours, orte):
		self.list_tours = Tours(nr_tours, orte)
		self.list_orte_start_with_one = []
		self.gesamt_strecke = 0.
	
	
	def find_start_punkt_re_arrange_tour(self, tours, tour_start = 'Ort Nr.1'):
		orte = tours[0][1] 
		self.gesamt_strecke = tours[0][0]
		b = [i for i , x in enumerate(orte) if x.Name == tour_start]
		first_index = b[0]
		
		for i in range(first_index, len(orte)):
			self.list_orte_start_with_one.append([orte[i].Name, orte[i].X, orte[i].Y])
		for i in range(0, first_index):
			self.list_orte_start_with_one.append([orte[i].Name, orte[i].X, orte[i].Y])
		
	def print_list(self, l):
		my_formatter = "{0:.2f}"
		#output = my_formatter.format(pi)
		for i in l:
			ges =my_formatter.format(i[0])
			tx = ''
			for k in i[1]:
				tx = tx + k.Name + ' '
			print(str(ges) + ' / ' + tx)			
		




#-------- test 

def print_list(l):
	for i in l:
		#print(i[0])

		tx = ''
		for k in i[1]:
			tx = tx + k.Name + ' '
		print(str(i[0]) + ' ' + tx)

number_of_Orte = 15
number_of_Tours = 20

img = Image.open('middle-earth.png')
#print(dir(img))

# test Tour
a = Orte(0, img.width, 0, img.height)
a.get_YX(number_of_Orte)
orte = a.Orte
t = Tour(orte)
#print(t.List_orte_gesamt_strecke)

# test tours
ts = Tours(number_of_Tours, orte)
#print_list(ts.List_orte_gesamt_strecken)

print('----')
b = ts.List_orte_gesamt_strecken_sorted
#print_list(b)


#---get shortest tour
st_first_element =[]
st = get_shortest_tour(number_of_Tours, orte)
st_first_element.append(st.list_tours.List_orte_gesamt_strecken_sorted[0])
st.print_list(st_first_element)
#-- rearrange tour start with ort 1
orte = st_first_element[0][1] 
st.find_start_punkt_re_arrange_tour(st_first_element, 'Ort Nr.1')
print(st.list_orte_start_with_one)
print(st.gesamt_strecke)


