var vector = {
	_x: 1,
	_y: 0,

	create: function(x, y) {
		var obj = Object.create(this);
		obj.setX(x);
		obj.setY(y);
		return obj;
	},

	getT33Matrix:	function (x,y){
  	var m = [[1,0,x],[0,1,y],[0,0,1]];
		return m;
	},
					
 getS33Matrix: function(x,y){
       var s = [[x,0,0],[0,y,0],[0,0,1]];
       return s;
       },	
       
  
	getR33Matrix: function(theta, inGrad = true){
		if(inGrad) theta = theta / 180 * Math.PI;
			var r = [[Math.cos(theta), -Math.sin(theta),0], [Math.sin(theta), Math.cos(theta),0],[0,0,1]];
		  return r;
		},
	
	
	getM33Matrix: function(m1, m2){    
		var c = [[],[],[]];
		// multiplication of 2 3x3 matrices    
		for(var i=0;i<3;i +=1){    
			for(var j=0;j<3;j +=1){    
				c[i][j]=0;      
				for(var k=0;k<3;k +=1){      
					c[i][j]+=m1[i][k]*m2[k][j];      
				}//end of k loop  
			}//end of j loop  
		}// end of i loop
	return c;    
},	
	
	getM31Matrix: function(m){    
		var c = [[]];
		vm = [[this.getX()],[this.getY()],[1]];	
		//multiplying  matrix vector    
		for(var i=0;i< 3 ;i +=1){    
			c[i] = 0;
			for(var j=0; j<3; j +=1){
				c[i] += vm[j]*m[i][j];
			} //end of j loop
		} // end of i loop
		vtemp = vector.create(c[0],c[1]);
		return vtemp;
		},		
    

	setX: function(value) {
		this._x = value;
	},

	getX: function() {
		return this._x;
	},

	setY: function(value) {
		this._y = value;
	},

	getY: function() {
		return this._y;
	},

	setAngle: function(angle) {
		var length = this.getLength();
		this._x = Math.cos(angle) * length;
		this._y = Math.sin(angle) * length;
	},

	getAngle: function() {
		return Math.atan2(this._y, this._x);
	},

	setLength: function(length) {
		var angle = this.getAngle();
		this._x = Math.cos(angle) * length;
		this._y = Math.sin(angle) * length;
	},

	getLength: function() {
		return Math.sqrt(this._x * this._x + this._y * this._y);
	},

	add: function(v2) {
		return vector.create(this._x + v2.getX(), this._y + v2.getY());
	},

	subtract: function(v2) {
		return vector.create(this._x - v2.getX(), this._y - v2.getY());
	},

	multiply: function(val) {
		return vector.create(this._x * val, this._y * val);
	},

	divide: function(val) {
		return vector.create(this._x / val, this._y / val);
	},

	addTo: function(v2) {
		this._x += v2.getX();
		this._y += v2.getY();
	},

	subtractFrom: function(v2) {
		this._x -= v2.getX();
		this._y -= v2.getY();
	},

	multiplyBy: function(val) {
		this._x *= val;
		this._y *= val;
	},

	divideBy: function(val) {
		this._x /= val;
		this._y /= val;
	},
	
	
	
};
