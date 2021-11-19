from decimal import Decimal, getcontext

from vector_new import Vector

getcontext().prec = 30


#  y = 1/2x + 3   y= 0 -> x = -6   x = 0 ->  y = 3

# basepoint (0 / b)   direction vector [1, m]
# bp = 3  dv [1, 1/2]

# Ax + By = k   y = 0 -> x = k/A   x = 0 ->  y = k/B  



#  y = mx + b     ->  y - mx = b
#   Ax + By = k  -> mit k = b  | B = 1 | A = -m

# k = 3 , A =-1/2 , B = 1   ->  -1/2x + y = 3 | *2      
#||||||||||  -x + 2y = 6 |||||||||||

# mit P1(x1, y1) und P2(x2, y2)
# y = ((y2-y1) / (x2 -x1)) * x + b -> m = y2 - y1 / x2 - x1


# P1(0, 3) P2(-6, 0)
# m = -3 / -6 -> 1/2 | b = y - mx -> b = 3 - 1/2*0 = 3 oder b = 0 - 1/2*-6 = 3 




class Line(object):

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2
        
        if not normal_vector:
            all_zeros = ['0']*self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector 
        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)
        self.basepoint = Decimal('0')

        self.set_basepoint()


    #---------------------
    def intersection_with(self, ell):
    	try:
    		A, B = self.normal_vector.coordinates
    		C, D = ell.normal_vector.coordinates
    		k1 = self.constant_term
    		k2 = ell.constant_term
    		#print(A, B , k1)
    		#print(C, D, k2)
    		#print(D * k1, B*k2)
    		x_numberator = D*k1 - B*k2
    		y_numberator = -C * k1 + A * k2
    		#print(x_numberator, y_numberator)
    		one_over_denom = Decimal('1')/(A * D - B * C)
    		#print(one_over_denom)
    		return Vector([x_numberator, y_numberator]).times_scalar(one_over_denom)
    	except ZeroDivisionError:
    			if self == ell:
    				return self
    			else:
    				return  None
    #---------------------
    def __eq__(self, ell):
    	if self.normal_vector.is_zero():
    		if not ell.normal_vector.is_zero():
    			return False
    		else:
    			diff = self.constant_term - ell.constant_term
    			return MyDecimal(diff).is_near_zero()
    	elif ell.normal_vector.is_zero():
    		return False
    	
    	if not self.is_parallel_to(ell):
    		return False
    	x0 = self.basepoint
    	y0 = ell.basepoint
    	basepoint_difference = x0.minus(y0)
    	n = self.normal_vector
    	return basepoint_difference.is_orthogonal_to(n)
    
    
    #---------------------
    def is_parallel_to(self, ell):
        n1 = self.normal_vector
        n2 = ell.normal_vector
        return n1.is_parallel_to(n2)
    #---------------------
    
    
    def set_basepoint(self):
        try:
            n = self.normal_vector.coordinates
            c = self.constant_term
            basepoint_coords = ['0']*self.dimension
            initial_index = Line.first_nonzero_index(n)
            
            
            initial_coefficient = n[initial_index]
            
            
            
            basepoint_coords[initial_index] = c/initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Line.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e


    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        n = self.normal_vector.coordinates

        try:
            initial_index = Line.first_nonzero_index(n)
            terms = [write_coefficient(n[i], is_initial_term=(i==initial_index)) + 'x_{}'.format(i+1)
                     for i in range(self.dimension) if round(n[i], num_decimal_places) != 0]
            output = ' '.join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output


    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Line.NO_NONZERO_ELTS_FOUND_MSG)


class MyDecimal(Decimal):
    def is_near_zero(self, eps=1e-10):
        return abs(self) < eps
        
	#-----------
class get_chart_line_points():
	def __init__(self, vh, vt, pl, plot = False, debug = False):
		#.  Vector:  x = 2 | y = 2 Vector:  x = 4 | y = 8
		if debug: print(vt, vh)
		self.gP_min = 0
		self.gP_max = 0
		
		self.geraden_gleichung(vh, vt, pl, plot, debug)
		
		
	def geraden_gleichung(self, vh, vt, pl, plot, debug ):
		x_min = float(pl.min_x)
		x_max = float(pl.max_x)
		y_min = float(pl.min_y)
		y_max = float(pl.max_y)
		x1 = float(vt.coordinates[0])
		y1 = float(vt.coordinates[1])
		x2 = float(vh.coordinates[0])
		y2 = float(vh.coordinates[1])
		yt = y2 - y1
		xt = x2 - x1
		if debug: print(yt/xt)
		m = (yt /xt)
		b = y1 - m * x1
		
		if debug: print(m,b)
		
		yl = m*x_min + b
		yh = m*x_max + b
		
		self.gP_min = Vector([x_min, yl])		
		self.gP_max = Vector([x_max, yh])
			
		if debug: print(self.gP_min, self.gP_max)	
		if plot: pl.plot_line(self.gP_min, (0.8, 0.8, 0.8), self.gP_max)	
	#-----------

'''
'''
