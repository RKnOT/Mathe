
//----- draw utils ------------

function swap_N_elements(vn, start_pos){
		
		//context.fillText(vn.length, 10, pos );
		pos +=30;
		var vnSwap =[];
		if (start_pos ==0) start =0; 
		if (start_pos ==1) start = vn.length - vn.length/4;
		var nElements = start+ vn.length/4-1;
		//context.fillText(nElements , 10, pos );
		
		for(var i = start; i <= nElements; i += 1){
			vnSwap.push(vn[i]);
		}
		var index = nElements;
		for(var i = 0; i < vnSwap.length; i += 1){
			vn[index] = vnSwap[i];
			index -=1;
		}
		return vn;

}
//------------------------

function swap(input, start_index) {
    let temp0 = input[start_index];
		let temp2 = input[start_index+2];
 		input[start_index] = input[start_index+3];
    input[start_index+2] = input[start_index+1];
    input[start_index+1] = temp2;
    input[start_index+3] = temp0;
    //print_Varray(input, 40);
    return input;
}

//------------------------

function drawXY_Canvas(x,y, color = "black", xs = 0, ys = 0) {
	
     context.beginPath();
     context.strokeStyle = color;
     //context.arc(0, 0, 10, 0, Math.PI * 2, false);
     
   	 	context.moveTo(xs,ys);
   	  context.lineTo(x, y);
     
     context.stroke();		
		}		
	
//------------------------			
function drawVector_Canvas(v, color = "black") {
	
     context.beginPath();
     context.strokeStyle = color;
     //context.arc(0, 0, 10, 0, Math.PI * 2, false);
     
   	 	context.moveTo(0,0);
   	  context.lineTo(v.getX(),v.getY());
     
     context.stroke();		
		}		
//------------------------				
							
function drawVarray_Canvas(va, color = "black") {
	
     context.font = "10px Georgia";
		
     context.beginPath();
     context.strokeStyle = color;
     //context.arc(0, 0, 10, 0, Math.PI * 2, false);
     for(var i=0; i< va.length; i +=1){
   	 	if ( i ==0){
   	 		context.moveTo(va[i].getX(), va[i].getY());
   	 	}
     	else{
     		context.lineTo(va[i].getX(), va[i].getY());
     }
     }
     context.stroke();		
		context.font = "20px Georgia";
		
		}	
//------------------------

function print_Vector(v, yd=20){
		context.fillText(v.getX() +" / " + v.getY(), 10, yd);
    yd +=30;
    return yd+30;
}		
		
//------------------------

function print_Vlist(v, yd=20){
	context.font = "15px Georgia";
	for(var i=0; i < v.length; i +=1){
		context.fillText(v[i].getX() +" / " + v[i].getY(), 10, yd);
    yd +=30;
    
  }
  context.font = "20px Georgia";
	return yd+30;
}		
//------------------------				
	
