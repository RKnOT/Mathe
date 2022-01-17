
import random
import time
import math

import matplotlib.pyplot as plt 

import json

import os.path
from os import path





class Orte:
    
    class Ort_Data:
        
        def __init__(self):
            self.X = 0.
            self.Y = 0.
            self.Name = ''
            
    def __init__(self):
        self.Orte =[]
        
        
    def rand_gen(self, mi, ma, n=10):
            for i in range(n):
                yield random.random()*(ma -mi)+mi

    def get_YX(self, nrOrte):
            count =1
            for x in self.rand_gen(0., 1., nrOrte):
                Ort = Orte.Ort_Data()
                for y in self.rand_gen(0., 1., nrOrte):
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
        self.Orte = orte
        self.gesamt_strecke = self.get_Gesamtstrecke(orte)
            
    def get_Gesamtstrecke(self, o):
        on = o.copy()
        on.append(on[0])
        s = 0.
        for i in range(0, len(on)-1):
            delta_x = on[i+1].X - on[i].X
            delta_y = on[i+1].Y - on[i].Y
            s += math.sqrt(delta_x*delta_x + delta_y*delta_y)
        return s
    
    def tausche_zwei_orte_in_tour(self, touren_list):
        d1 =Debug()
        #d1.Print_List_Orte(touren_list)
        #d1.Print_List_Gesamtstrecke(touren_list)
        touren_list_new = []
        for tour in touren_list:
            index1 = random.randint(1, len(tour.Orte)-1)
            index2 = index1
            while index1 == index2:
                index2 = random.randint(1, len(tour.Orte)-1)
            o1 = tour.Orte[index1]
            tour.Orte[index1] = tour.Orte[index2]
            tour.Orte[index2] = o1
            
            tour_list_new = Tour(tour.Orte)
            #print(tour.gesamt_strecke, tour_list_new.gesamt_strecke)
        
            if tour.gesamt_strecke > tour_list_new.gesamt_strecke:            
                touren_list_new.append(tour_list_new)
            else:
                touren_list_new.append(tour)       
            
            
            #print(tour.gesamt_strecke, )
        
        
        #print(len(touren_list_new))
        #print(d1.Print_List_Gesamtstrecke(touren_list_new))
        #print(d1.Print_List_Orte(touren_list_new))
        return touren_list_new    
        
    
    def get_touren(self, list, orte, anzahl_touren):
        d1 = Debug()
        #d1.Print_Orte(orte)
        for i in range(0, anzahl_touren):
            t = Tour(orte)
            list.append(t)
        
        return list
        



#---------   Debug ---------
class Debug:
    
    def Print_Orte(self, orte):
        for i in orte:
            print(i.X,i.Y, i.Name)   
        print()
    
    def Print_List_Orte(self,list):
        #print(list[0].new_Orte[0].X)
        
        for item in list:
            self.Print_Orte(item.Orte)
    
    def Print_List_Gesamtstrecke(self,list):
        print('Gesamtstrecke')
        for item in list:
            print(item.gesamt_strecke)    
        print()
        
    
        
                 
         
         
#---------------------------------            




#---

if __name__ == '__main__':
    
    d1 = Debug()
    #----------- Definitionen
    anzahl_Orte = 15
    anzahl_Touren = 1
    anzahl_Iterationen = 20
    
    
    flag_read_json = True
    
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
    tr_list = Tour(o.Orte)
    touren_list = tr_list.get_touren(touren_list, o.Orte, anzahl_Touren)
    #d1.Print_List_Orte(touren_list)
    
    #d1.Print_List_Gesamtstrecke(touren_list)
    
    #d1.Print_List_Gesamtstrecke(tl_new)
    
        
    for i in range(0, anzahl_Iterationen):
        
        tl_new = []
        
        tl_new = tr_list.tausche_zwei_orte_in_tour(touren_list)
        touren_list = tl_new.copy()
        print(touren_list[0].gesamt_strecke)
        
    for i in touren_list:
        #print(i.gesamt_strecke)
        pass
    
        
    #-------  draw ---------------
    
    '''
    
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
    
    plt.plot(xl, yl, color="gray", linewidth = 0.1)
    plt.plot(xl_short, yl_short, color='red', linewidth= 1.5)
    plt.scatter(x_first, y_first, color = 'red', linewidth =5)
    plt.xlabel("X")
    plt.ylabel("Y")
    #plt.title("Red shortest TSP tour " , shortes)
    plt.show()
    
    '''
    
    
    
    
    
    
