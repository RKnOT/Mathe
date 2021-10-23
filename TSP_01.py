
import random
import time
import math

import matplotlib.pyplot as plt 


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
            
                
class Tour:
    
    def __init__(self, orte):
        self.Orte_Original = orte
        self.gesamt_strecke_Original = self.get_Gesamtstrecke(orte)
        self.Orte_New = random.sample(orte, k=len(orte))
        self.gesamt_strecke_New = self.get_Gesamtstrecke(self.Orte_New)
            
    def get_Gesamtstrecke(self, o):
        s = 0.
        for i in range(0, len(o)-1):
            delta_x = o[i+1].X - o[i].X
            delta_y = o[i+1].Y - o[i].Y
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
    anzahl_Orte = 5
    anzahl_Touren = 5
    anzahl_Iterationen = 10
    #----------
    
    o = Orte()
    o.get_YX(anzahl_Orte)
    touren_list = []
    
    touren_list = get_touren(touren_list, o.Orte, anzahl_Touren)
    #d1.Print_List_Gesamtstrecke(touren_list)
    for i in range(0, anzahl_Iterationen):

        # 20% der schlechtesten Touren sterben
    
        #d1.Print_List_Gesamtstrecke(touren_list)
        #touren_list.sort(key=lambda x: x.gesamt_strecke_New)
        #d1.Print_List_Gesamtstrecke(touren_list)
        len_original = len(touren_list)
        cut = int(len(touren_list)*0.8)
        del touren_list[cut:]
        #print(type(touren_list[0]))
        #print(touren_list[0].gesamt_strecke_New)
        #print(touren_list[0].get_Gesamtstecke(touren_list[0]))
    
        # die fehlenden werden mit neuen Mutationen auf gefüllt
    
        missing = len_original-cut
        touren_list = get_touren(touren_list, o.Orte, missing)
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
                print(temp_Wert_original)
            else:
                print((temp_Wert_new))
            print()
        
        print('temp_new')
        d1.Print_List_Gesamtstrecke(temp_new)
        print('temp_original')
        d1.Print_List_Gesamtstrecke(temp_original)
        
        
        
        
        
        
        
        #------------
        
        touren_list = t_new
    
    
    
    
    
    
    touren_list.sort(key=lambda x: x.gesamt_strecke_New)
    #d1.Print_List_Gesamtstrecke(touren_list)
    #print(b)
    
    #-------  draw ---------------
    xl =[]
    yl =[]    
    
    
    xl_short = [] 
    yl_short = []
    
    for item in touren_list:
        for i1 in item.Orte_New:
            xl.append(i1.X)
            yl.append(i1.Y)
    for i in touren_list:
         xl_short.append(i.Orte_New[0].X)   
         yl_short.append(i.Orte_New[0].Y)   
    
    #print(x)
    #plt.figure(figsize=(10, 10))
    
    plt.plot(xl, yl, color="gray", linewidth = 0.5)
    plt.plot(xl_short, yl_short, color='red', linewidth= 3)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Plot with 2 arbitrary Lines")
    plt.show()
    
    
    
    
    
    #d1.Print_List_Orte(tour_list)
    #d1.Print_Orte(o.Orte)
    #d1.Print_Tour(t1)
    #d1.Print_Tour(t2)
    #d1.Print_Orte(t1.Orte)
    
    
    
    
    