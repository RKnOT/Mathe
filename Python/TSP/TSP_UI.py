
import random
import time
import math

import matplotlib.pyplot as plt 

import json
from io import BytesIO
#import os.path
from os import path


# coding: utf-8
#import matplotlib.pyplot as plt
import io, math, ui




   


class Orte:
    
    class Ort_Data:
    	def __init__(self):
    		self.X = 0.
    		self.Y = 0.
    		self.Name = ''
    		
    def __init__(self):
    	self.Orte =[]
    	self.x_min = 0.
    	self.x_max = 600.
    	self.y_min = 0.
    	self.y_max = 415.
    	self.xy_padding = self.x_max*0.005
    	#print(self.xy_padding)
    	
    def rand_gen(self, mi, ma, n=10):
            for i in range(n):
                yield random.random()*(ma -mi)+mi

    def get_YX(self, nrOrte):
            count =1
            od = self.Ort_Data()
            for x in self.rand_gen(self.x_min + self.xy_padding, self.x_max - self.xy_padding, nrOrte+1
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
        
                
        
            
                
class Tour:
    
    def __init__(self, orte):
        self.Orte_Original = orte
        self.gesamt_strecke_Original = self.get_Gesamtstrecke(orte)
        self.Orte_New = random.sample(orte, k=len(orte))
        self.gesamt_strecke_New = self.get_Gesamtstrecke(self.Orte_New)
            
    def get_Gesamtstrecke(self, o):
        on = o.copy()
        on.append(on[0])
        s = 0.
        for i in range(0, len(on)-1):
            delta_x = on[i+1].X - on[i].X
            delta_y = on[i+1].Y - on[i].Y
            s += math.sqrt(delta_x*delta_x + delta_y*delta_y)
        return s
                
        


#---------   Debug ---------
class Debug:
    
    def Print_Orte(self, orte):
        for i in orte:
            print(i.X,i.Y, i.Name)   
        print()
    
    def Print_List_Orte(self,list):
        #print(list[0].new_Orte[0].X)
        
        for item in list:
            self.Print_Orte(item.Orte_New)
    
    def Print_List_Gesamtstrecke(self,list):
        for item in list:
            self.Print_Tour(item)    
        print()
    
    
    def Print_Tour(self, tour):
         print(tour.gesamt_strecke_Original, tour.gesamt_strecke_New)
        
                 
         
         
#---------------------------------            



def get_touren(list, orte, anzahl_touren):
    d1= Debug()
    for i in range(0, anzahl_touren):
        t = Tour(orte)
        list.append(t)
    #print(len(t.Orte))
    return list

#---

if __name__ == '__main__':
    
    d1 = Debug()
    #----------- Definitionen
    anzahl_Orte = 10
    anzahl_Touren = 50
    anzahl_Iterationen = 100
    
    
    flag_read_json = False
    
    #----------
    
    
    #----------
    
    json_Orte = 'TSP_Orte.json'

    o = Orte()
    if (path.exists(json_Orte) and flag_read_json): # json file mit Orten exsitieren
        
        with open(json_Orte) as json_file:
            data = json.load(json_file)
            o.read_json_Ort(data)
        i = data['meta']
        if i[0]['Anzahl Orte'] != anzahl_Orte or \
           i[0]['Anzahl Touren'] != anzahl_Touren or \
           i[0]['Anzahl Iterationen'] != anzahl_Iterationen:
                 flag_read_json = False
                 o = Orte() # reset Orte
                    
            
    if flag_read_json == False: # Orte neu generieren und in json file schreiben
        o.get_YX(anzahl_Orte)
        O_n = o.write_Orte_in_tuple(o.Orte)
        
        O_n['meta'] = []
        O_n['meta'].append({
            'Anzahl Orte': anzahl_Orte,
            'Anzahl Touren': anzahl_Touren,
            'Anzahl Iterationen': anzahl_Iterationen
            })
        with open(json_Orte, 'w') as outfile:
            json.dump(O_n, outfile)
        
        
    
    #-----------
    
    touren_list = []
    
    touren_list = get_touren(touren_list, o.Orte, anzahl_Touren)
    #d1.Print_List_Gesamtstrecke(touren_list)
    #d1.Print_List_Orte(touren_list)
    
    for i in range(0, anzahl_Iterationen):

        # 20% der schlechtesten Touren sterben
    
        len_original = len(touren_list)
        cut = int(len(touren_list)*0.8)
        del touren_list[cut:]
        
        # die fehlenden werden mit neuen Mutationen auf gefüllt
    
        missing = len_original-cut
        touren_list = get_touren(touren_list, o.Orte, missing)
        '''
        t_new =[]
        for tour in touren_list:
            t_new.append(Tour(tour.Orte_New))
        #d1.Print_List_Gesamtstrecke(t_new)
        t_new.sort(key=lambda x:x.gesamt_strecke_New)       
        
        # Entscheidung ob die neue Strecke einen günstigeren weg hat
        temp_original = t_new.copy()
        temp_new = t_new.copy()
        
        temp_new.sort(key=lambda x:x.gesamt_strecke_Original)
        temp_new.sort(key=lambda x:x.gesamt_strecke_New)
        
        temp_original.sort(key=lambda x:x.gesamt_strecke_Original)
        temp_original.sort(key=lambda x:x.gesamt_strecke_New)
        
        for i in range(0, len(temp_original)):
            temp_Wert_original = temp_original[i].gesamt_strecke_Original
            temp_Wert_new = temp_new[i].gesamt_strecke_New
            #print(temp_Wert_original, temp_Wert_new)
            
            if(temp_Wert_original <= temp_Wert_new):
                #print(temp_Wert_original)
                pass
            else:
                #print((temp_Wert_new))
                pass
            #print()
        
        #print('temp_new')
        #d1.Print_List_Gesamtstrecke(temp_new)
        #print('temp_original')
        #d1.Print_List_Gesamtstrecke(temp_original)
        '''
        
        
        
        
        
    
        #------------
        
        #touren_list = t_new
    
    
    
    
    
    format_two_dez = "{0:.3f}"

    
    touren_list.sort(key=lambda x: x.gesamt_strecke_New)
    #d1.Print_List_Gesamtstrecke(touren_list)
    shortes = str(format_two_dez.format(touren_list[0].gesamt_strecke_New))
    longest = str(format_two_dez.format(touren_list[-1].gesamt_strecke_New))
    #print(shortes)
    #print(longest)
    
    #-------  draw ---------------
    xl =[]
    yl =[]    
    
    
    xl_short = [] 
    yl_short = []
    x_first = 0.
    y_first = 0.
    
    #print(touren_list[0])
    
    
    #all tours
    for item in touren_list:
        for i1 in item.Orte_New:
            xl.append(i1.X)
            yl.append(i1.Y)
    
    #first tour
    tl = touren_list[1]
    flag_first_wert = True 
    
    
    for i in tl.Orte_New:
        xn = i.X
        yn = i.Y
        if flag_first_wert:
            x_first = xn
            y_first = yn
            flag_first_wert =False 
        xl_short.append(xn)   
        yl_short.append(yn)
        #print(xn, yn)
    xl_short.append(x_first)
    yl_short.append(y_first)   
    
    
    
    #plt.figure(figsize=(10, 10))
    #plt.figure(figsize=(3, 3))
    ort_d = Orte()
    
    
    
    fig, ax = plt.subplots()
    #plt.rcParams["figure.figsize"] = [7.50, 3.50]
    #plt.rcParams["figure.autolayout"] = True
    #ax.format_coord = lambda x, y: ''
    ax.imshow(plt.imread("middle-earth-flip.png"))
    
    ax.plot(xl, yl, color="green", linewidth = 2)
    ax.plot(xl_short, yl_short, color='red', linewidth= 3)
    ax.scatter(x_first, y_first, color = 'black', linewidth = 10)
    ax.set_axis_off() 
    plt.xlim(ort_d.x_min - 0.2, ort_d.x_max+ 0.2)
    plt.ylim(ort_d.y_min - 0.2, ort_d.y_max+ 0.2)
    #plt.xlim(60)
    #plt.ylim(41)
    
    #plt.xlabel("X")
    #plt.ylabel("Y")
    #plt.title("Red shortest TSP tour " , shortes)
    #plt.show()
    #plt.savefig('demo.png', transparent=True)
    
    
    #demo_BlurView()
    '''
    a = ui.load_view('TSP_UI')
    
    a.add_subview(ui.ImageView(frame=(0, 0, 500, 500)))
    a.subviews[0].image = ui.Image.named('test:Peppers')
    a.add_subview(ui.ImageView(frame=(0, 0, 500, 500)))
    a.subviews[1].image = ui.Image('middle-earth.png')
    a.present('sheet', hide_title_bar=True)
 		'''
    
    
    v = ui.load_view('TSP_UI')
    v.present('sheet')
    
    
    b = BytesIO()
    plt.savefig(b)
    img = ui.Image.from_data(b.getvalue())
    
    
    
    
    
    
    
    v['image1'].image = img
    
    #v.add_subview(plot_to_scrollable_image_view(plt))
      
    #v.subviews[0].frame = v.bounds
    #v.subviews[0].x, v.subviews[0].y=(5,5)
    #v.content_size=tuple(v.subviews[0].bounds.size+(11,11))
    #v.content_offset=(1,1)
    #v.delegate=delegate()
    
    
    ''' Code snipped original
    plt.plot([math.sin(x/10.0) for x in range(95)])
    plt.xlim(0, 94.2)
    view = plot_to_scrollable_image_view(plt)
    view.present()
    view.subviews[0].frame = view.bounds
    view.subviews[0].x,view.subviews[0].y=(5,5)
    view.content_size=tuple(view.subviews[0].bounds.size+(11,11))
    view.content_offset=(5,5)
    view.delegate=delegate()
    view.hidden = False
    ------------------------
    with ui.ImageContext(100, 100) as ctx:
    	ui.set_color('white')
    	ui.fill_rect(0, 0, 100, 100)
    	ui.set_color('red')
    	circle = ui.Path.oval(10, 10, 80, 80)
    	circle.fill()
    	img = ctx.get_image()
    7
    
    '''
    
