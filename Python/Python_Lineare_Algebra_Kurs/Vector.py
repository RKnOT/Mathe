import  math

from decimal import Decimal, getcontext
import Plot

getcontext().prec = 30


class Vector(object):
    CANNOT_NORALIZE_ZERO_VECTOR_MSG = 'Cannot normalize zero vector'
    NO_UNIQUE_PARALLEL_COMPONENT_MSG = 'No unique parallel component'
    def __init__(self, coordinates, v_name = ''):
        try:
            if not coordinates:
                raise ValueError
            self.V_Name = v_name
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)
            #self.Magnitude = self.magnitude()
            #self.Normalized = self.normalized() 
        except ValueError:
            raise ValueError('The coordinates must be nonempty')
        except TypeError:
            raise TypeError('The coordinates must be an iterable')
#-----
    def __str__(self):
        return 'Vector: {} x = {} | y = {}'.format(self.V_Name, self.coordinates[0], self.coordinates[1]) 

    #------
    def __eq__(self, v):
        return self.coordinates == v.coordinates
    #------    
    def plus(self, v):
    	new_coordinates = [x+y for x,y in zip(self.coordinates, v.coordinates)]
    	return Vector(new_coordinates)
    #-------
    def minus(self, v):
    	new_coordinates = [x-y for x,y in zip(self.coordinates, v.coordinates)]
    	return Vector(new_coordinates)
    #-------
    def times_scalar(self, c):
    	new_coordinates = [Decimal(c)*x for x in self.coordinates]
    	return Vector(new_coordinates)
    #----
    def magnitude(self):
      coordinates_squared = [x**2 for x in self.coordinates]
      return Decimal(math.sqrt(sum(coordinates_squared)))
    #----
    def normalized(self):
      try:
      	magnitude = self.magnitude()
      	return  self.times_scalar(Decimal('1.0')/ magnitude)
      except ZeroDivisionError:
      	raise Exception(self.CANNOT_NORALIZE_ZERO_VECTOR_MSG)
      	
    #------
    def dot(self ,v):
    	return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])
    #-----
    def angle_width(self, v, in_degrees = False):
      try:
        u1 = self.normalized()
        u2 = v.normalized()
        #print(u1, u2)
        angle_in_rad = math.acos(u1.dot(u2))
        if in_degrees:
          degrees_per_rad = 180. / math.pi
          return angle_in_rad * degrees_per_rad
        else:
          return angle_in_rad
      except Exception as e:
        if str(e) == self.CANNOT_NORALIZE_ZERO_VECTOR_MSG:
        	raise  Exception('Cannot compute an angle with the zero vector')
        else:
        	raise e
    #------
    def is_orthogonal_to(self, v, tolerance = 1e-10):
    	
    	if abs(self.dot(v) < tolerance) == 0: return False
    	else: return True
    #------
    def is_parallel_to(self, v):
    	return (self.is_zero() or self.angle_width(v) == 0 or self.angle_width(v) == math.pi)
    #--------
    def is_zero(self, tolerance=1e-10):
    	return self.magnitude() < tolerance
    #--------
    def component_parallel_to(self, basis):
    	try:
    		u = basis.normalized()
    		weight = self.dot(u)
    		return u.times_scalar(weight)
    	except Exception as e:
    		if str(e) == self.CANNOT_NORALIZE_ZERO_VECTOR_MSG:
    			raise  Exception(self.CANNOT_NORALIZE_ZERO_VECTOR_MSG)
    		else:
    			raise e
    #------------------
    def component_orthogonal_to(self, basis):
    	try:
    		projection = self.component_parallel_to(basis)
    		return self.minus(projection)
    	except Exception as e:
    		if str(e) == self.NO_UNIQUE_PARALLEL_COMPONENT_MSG:
    			raise  Exception(self.self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
    		else:
    			raise e
    		
    #---------
    def cross(self, v):
    	try:
    		x_1, y_1, z_1 = self.coordinates
    		x_2, y_2, z_2 = v.coordinates
    		new_coordinates = [ y_1*z_2 - y_2*z_1, -(x_1*z_2 - x_2*z_1), x_1*y_2 - x_2*y_1]
    		return Vector(new_coordinates)
    	except ValueError as e:
    		msg = str(e)
    		if msg == 'need more than 2 values to unpack':
    			self_embedded_in_R3 = Vector(self.coordinates +('0',))
    			v_embedded_in_R3 = Vector(self.coordinates + ('0', ))
    			return self_embedded_in_R3.cross(v_embedded_in_R3)
    		elif (msg == 'too many values to unpack' or msg == 'need more than 1 value unpack'):
    			raise Exception(self.ONLY_DEFINED_IN_TWO_THREE_DIMS_MSG)
    		else:
    			raise e
    		
    		
