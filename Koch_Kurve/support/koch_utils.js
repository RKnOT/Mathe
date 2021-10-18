//--------- Koch utils -----------

var Koch_utils = {
	
	//---------------------	
	get_DrawDreieck: function(){
	dreieck = utils.get_min_value(width, height)*0.8;		
	v1 = vector.create(0, 0);
	v2 = vector.create(0, 1);
	v2.setLength(dreieck);
	vhs.push(v1, v2);
	// move Dreieck
	vc = vector.create(cpX+100, cpY/9); 
	vhs0 = Koch_utils.rotate_moveVArray(vhs, vc, -30);
	vhs1 = Koch_utils.rotate_moveVArray(vhs, vc, 30);
	//vhs2 = Koch_utils.rotate_moveVArray(vhs, vhs0[1], 90);
	vhs_d =[];
	
	//L1
	//vhs_d.push(vhs1[1], vhs1[0]);
	//L3
	//vhs_d.push(vhs1[0], vhs0[1]);
	//L2
	//vhs_d.push(vhs0[1], vhs1[1], vhs1[0], vhs0[1]);
	
	vhs_d.push(vhs0[1], vhs1[1], vhs1[0], vhs0[1]);
	return vhs_d;
	},
//-------------------------------	
	get_DrawQuadrat: function(){

  viereck = utils.get_min_value(width, height)*0.4;		
	var vhs =[];
	v2 = vector.create(-1, -1);
	v3 = vector.create(-1, 1);
	v4 = vector.create(1, 1);
	v1 = vector.create(1, -1);
	vhs.push(v4,v3,v2,v1,v4);
	v33t =	vector.getT33Matrix(cpX, cpY); 
	for(var i = 0; i < vhs.length; i +=1){
		vhs[i].setLength(viereck);
		vhs[i] = vhs[i].getM31Matrix(v33t);
		}
return vhs;
},

	
//--------------------
 cut_Lines: function(LArray){
	
				var ltemp =[];
				for(var i = 0; i < LArray.length-1; i += 1){
							var lt =[];
							lt.push(LArray[i], LArray[i+1]);
							var lines = Koch_utils.cut_Line(lt);
							//pos = print_Vlist(lines, 50);
				
							for(var j = 0; j < lines.length; j +=1){
								ltemp.push(lines[j]);
							}
							//pos = print_Vlist(ltemp, 50);
				}
				//context.fillText("items: "+ lines.length, 5, height-100);
				return ltemp;
	},
	
	
	
	cut_Line: function(VLine){
			V0 = vector.create(0,0);
			VLine_T =[];
			v23 =[];
			v23.push(V0);
			v30 =[];
			// move line with first point to center
			t33_move = VLine[0].getT33Matrix(-VLine[0].getX(), -VLine[0].getY());
			for(i =0; i< VLine.length; i +=1){
				var vt = VLine[i].getM31Matrix(t33_move);		
			  VLine_T.push(vt);
			}
			var l = VLine_T[1].getLength();
			let v1 = vector.create(VLine_T[1].getX(), VLine_T[1].getY());
			let v2 = vector.create(VLine_T[1].getX(), VLine_T[1].getY());
			let v3 = vector.create(VLine_T[1].getX(), VLine_T[1].getY());
			v1.setLength(l/3);
			v2.setLength(2*l/3);
			v3.setLength(l);
			tm33_c = v1.getT33Matrix(VLine[0].getX(), VLine[0].getY());
			tr3360p = VLine[0].getR33Matrix(60);
			tr3360m = VLine[0].getR33Matrix(-60);	
			tm33 = v1.getT33Matrix(v1.getX(), v1.getY()); 
			t33 = VLine[0].getM33Matrix(tm33, tr3360m);
			var vr = v1.getM31Matrix(t33);
			v23.push(v1);
			v23.push(vr);
			v23.push(v2);
			v23.push(v3);
			// move line with first point to center
			for(i =0; i< v23.length; i +=1){
				var vt = v23[i].getM31Matrix(tm33_c);		
			  v30.push(vt);
			}
			return v30;
},
//---------------
	rotate_moveVArray: function(LArray, vPoint, angle =0){
		ltemp=[];
	vtt = vector.create(0,0);
	t33_move = vtt.getT33Matrix(vPoint.getX(), vPoint.getY());
		tr33x = vtt.getR33Matrix(angle);
		t33 = vtt.getM33Matrix(t33_move, tr33x);	
				for(j =0; j < LArray.length; j +=1){
					var vt = LArray[j].getM31Matrix(t33);		
					ltemp.push(vt);
			}
		//print_Vlist(ltemp,370);
		return ltemp;
},		
//------------------------		
	copyPoints_in_Array: function(array, Vpoints){
			for(var i =0; i < Vpoints.length; i +=1){
				array.push(Vpoints[i]);
			}
			return array;
}
//-------------
}


