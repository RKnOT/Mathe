// class UI_TSP -------------- start --------------------------                     
class UI_TSP{
		/*
		z.B. html:  tag <table id="tabelle"></table>
    */
		constructor(id, dic, table_items){
			this.id = id;
			this.dic = dic;
			//var temp = this.convert_dic_to_array(this.dic);
			this.dic_tabelle_generieren(table_items);
			}
		//----
		dic_table_modify(dic){
		 const tabelle = document.getElementById(this.id);	  
     var dic_array = this.convert_dic_to_array(dic);
 		 for (var i = 0; i < tabelle.rows.length; i++) {
		 	var r = tabelle.rows[i];
		 	var z = r.cells[1];
		 	//document.getElementById("d16").innerHTML += "zelle   "  + z.innerHTML+  ' '+ dic_array[1][i] + '. '+ "<br />";
		 	z.innerHTML = dic_array[1][i];		
			}
		}
		//----
		dic_tabelle_generieren(table_items, nr_items =5) {
     const tabelle = document.getElementById(this.id);	  
     var dic_array = this.convert_dic_to_array(this.dic);
 		 //document.getElementById("d19").innerHTML += "dic keys  "  + dic_array[0] + ' '+ 'dic values '+ dic_array[1] + "<br />";
	 	 for(var i=0, len = nr_items; i<len; i++){
		 	//document.getElementById("d19").innerHTML += len + " dic keys  "  + dic_array[0][i] + ' '+ 'dic values '+ dic_array[1][i] + "<br />";
		 	const reihe = tabelle.insertRow(i);
     	for(var k=0, len1 = dic_array.length; k<len1; k++){
     		var zelle = reihe.insertCell();
     		zelle.innerHTML = dic_array[k][i];
     		}
		 }
    }	
		//---
		
		convert_dic_to_array(dic){
			var d_key_value = [];
			var d_key = [];
			var d_value = [];
			Object.entries(dic).forEach(([key, value]) => {
  	  //document.getElementById("d1").innerHTML += "dic key "  + key + ' '+ 'dic value '+ value + "<br />";
   		d_key.push(key);
   		d_value.push(value);
  	});
		d_key_value.push(d_key);
		d_key_value.push(d_value);
		return d_key_value;
	}
	//------
		
		}
// class UI_TSP -------------- ende -------------------------- 	
       
// class get tour -------------- start --------------------------                     
class get_Tour{
		
		constructor(nr_Orte, c_width = 600 , c_height = 415){
		
		this.ut = new Utils();
		this.c_width = c_width;
		this.c_height = c_height;
		this.nr_Orte = nr_Orte;
		
		this.tour_length = 0.0;
		this.start_point = [];
		this.tour = [];
		
		this.generate_first_Tour(this.nr_Orte);
		   
		this.tour_first = new Array();
    this.tour_first[0] = Array.from(this.start_point);
    this.tour_first[1] = Array.from(this.tour);
    this.get_tour_length(); 
    this.tour_first[2] = this.tour_length;
		
		this.tour_n = new Array();
    this.tour_n[0] = Array.from(this.start_point);
    this.tour_n[1] = Array.from(this.tour);
    this.tour_n[2] = this.tour_length;
		
		}
  	//--------------
    get_random_points(nr_points, dez_stellen = 5){
          var points = [];
          var ort_counter = 1;
          for(var i=0, len = nr_points; i<len; i++){
           var x = this.ut.generateRandomFloat(0, this.c_width, dez_stellen);
           var y = this.ut.generateRandomFloat(0, this.c_height, dez_stellen);
           var ort_n = "Ort: " + ort_counter.toString(3);
           points.push([x,y, ort_n]);
           ort_counter +=1;
           }
          return points;
          }
    //-------------
    generate_first_Tour(nr_points = 5){
				 var r_p = this.get_random_points(nr_points);
         var r_p_0 = r_p[0];
         r_p.splice(0,1);
         this.tour = r_p;
         this.start_point = [r_p_0];
         }	
    //-------------    
     shuffel_orte(orte_list){
     			var tour = new Array();
          var ol = Array.from(orte_list); // hard copy of array
          tour[0] = ol.sort(()=> Math.random() - 0.5);
					tour[1] = this.get_tour_length(tour[0], false);
					return tour;
					}
    //-------------
    change_two_Orte(orte_list){
          var t = new Array();
          let ot = this.ut.hard_array_copy(orte_list); // hard copy of array
          //let ot = orte_list.map((x) => x); 
          var min = 0;
          var max = ot[1].length;
					var index1 =  this.ut.generateRandomIntegerInRange(min, max);   
					var index2 =  this.ut.generateRandomIntegerInRange(min, max);
					if (index1 == index2){
					   var index2 =  this.ut.generateRandomIntegerInRange(min, max);
					   }
					 //document.getElementById("d3").innerHTML ="max: "+ max + " indexes " + index1 + ' ' + index2+ ' ' +"<br />";
					  				
					
					
					var temp1 = ot[1][index1];
					var temp2 = ot[1][index2];
					//document.getElementById("d4").innerHTML ="value index1: "+ temp + ' ' +"<br />";
					ot[1].splice(index2, 1, temp1); 
					ot[1].splice(index1, 1, temp2); 
					t[0] = ot[0];
					t[1] = ot[1];
					t[2] = this.get_tour_length(ot, false);
					this.ut.print_points_list(t[1], 'd1');
					return t; 
					
					
				
    }
    
    //---------------
    print_tour(tag){
      this.ut.print_points_list(this.start_point, tag);
			this.ut.print_points_list(this.tour, tag, true);
			document.getElementById(tag).innerHTML += ' total length: '+ this.tour_length + '<br />'
      }
    //---------------------------
    get_tour_length(t = this.tour_first, flag_first_tour = true){
					// entfernung berechnen
				  var orte_temp = Array.from(t); // hard copy of array
          //document.getElementById("d2").innerHTML = "xy " + orte_temp[0][0][0]  +  ' / ' + orte_temp[0][0][1] + "<br />";
       		
				  var x_0 = orte_temp[0][0][0];
          var x_n1 = orte_temp[1][0][0];
          var y_0 = orte_temp[0][0][1];
          var y_n1 = orte_temp[1][0][1];
          var length = this.get_h(x_0, x_n1, y_0, y_n1);
          // temp list with startpoint
          //orte_temp.unshift(this.start_point);
					//document.getElementById("d12").innerHTML = "tour  first " + orte_temp[0].length  +  ' / ' + orte_temp[1].length + "<br />";
       		
       		for(var i=0, len = orte_temp[1].length -1; i < len; i++){
            x_0 = orte_temp[1][i][0];
            x_n1 = orte_temp[1][i+1][1];
            y_0 = orte_temp[1][i][0];
            y_n1 = orte_temp[1][i+1][1];
            length += this.get_h(x_0, x_n1, y_0, y_n1);
            }
            
            x_0 = orte_temp[0][0][0];
            y_0 = orte_temp[0][0][1];
            
            length += this.get_h(x_0, x_n1, y_0, y_n1);
                
           	if(flag_first_tour == true){
           		this.tour_length = length;
           		}
           	return length;
            }
       //-----------------		
       get_h(x0, x1, y0, y1){
       		  var dx = x1 - x0;// entfernung berechnen
				    var dy = y1 - y0;
				    //document.getElementById("d1").innerHTML += "pyth " + x0 +' / ' + x1 +' / '+ y0+' / ' + y1 + "<br />";
       		  
				    var lx = Math.sqrt(Math.pow(dx,2) + Math.pow(dy, 2));
				    //document.getElementById("d4").innerHTML += lx + ' dl'+'<br />';
				    return(lx);
				 }
       //--------------		
		}
// class get tour --------------- end -------------------------                     
