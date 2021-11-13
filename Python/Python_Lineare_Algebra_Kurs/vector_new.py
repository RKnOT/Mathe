import math
from decimal import Decimal, getcontext

getcontext().prec = 30


class Vector(object):
    CANNOT_NORALIZE_ZERO_VECTOR_MSG = 'Cannot normalize zero vector'
    NO_UNIQUE_PARALLEL_COMPONENT_MSG = 'No unique parallel component'
    def __init__(self, coordinates, v_name = ''):
        self.V_Name = v_name
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)
            
        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')
    #-------------
    def v_90(self):
    	return Vector([self.coordinates[1], self.coordinates[0]*-1])
    #--------------
    def magnitude(self):
      coordinates_squared = [x**2 for x in self.coordinates]
      return (math.sqrt(sum(coordinates_squared)))
    #----
    def normalized(self):
      try:
      	magnitude = Decimal(self.magnitude())
      	return  self.times_scalar(Decimal('1.0')/ magnitude)
      except ZeroDivisionError:
      	raise Exception(self.CANNOT_NORALIZE_ZERO_VECTOR_MSG)
    
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
    	new_coordinates = [Decimal(c) * x for x in self.coordinates]
    	return Vector(new_coordinates)
    
    #------
    def dot(self ,v):
    	return sum([x*y for x,y in zip(self.coordinates, v.coordinates)])
    #-----
    #-----
    def angle_width(self, v, in_degrees = False):
      #print(self.normalized(), v.normalized())
      try:
        u1 = self.normalized()
        u2 = v.normalized()
        w = round(u1.dot(u2), 10)
        angle_in_rad = math.acos(w)
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
    	
    	return abs(self.dot(v)) < tolerance
    #------
    def is_parallel_to(self, v):
    	return (self.is_zero() or v.is_zero() or self.angle_width(v) == 0 or self.angle_width(v) == math.pi)
    #--------
    def is_zero(self, tolerance=1e-10):
    	return self.magnitude() < tolerance
    #--------
    def __str__(self):
        return '{}-Vector:  {}'.format(self.V_Name, self.coordinates)
    #---------
    def __eq__(self, v):
        return self.coordinates == v.coordinates
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
    			raise  Exception(self.NO_UNIQUE_PARALLEL_COMPONENT_MSG)
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
    	
    #---------------
    def area_of_triangle_with(self, v):
    	
    	return self.area_of_parallelogram_with(v) / 2.0
    	
    	
    #--------------
    def area_of_parallelogram_with(self, v):
    	cross_product = self.cross(v)
    	return cross_product.magnitude()
    #--------------------------
import console
console.clear()




'''


# Chapter #2
v = Vector([8.218, -9.341], 'v')
w = Vector([-1.129, 2.1118], 'w')
print(v.times_scalar(2))

v = Vector([-0.221, 7.437], 'v')
print(v.magnitude())
v = Vector(['7.887', '4.138'], 'v')
w = Vector(['-8.802', '6.776'], 'w')
print(v.dot(w))


v = Vector(['3.183', '-7.627'], 'v')
w = Vector(['-2.668', '5.319'], 'w')
print(v.angle_width(w))

print('first pair...')
v = Vector(['-7.579', '-7.88'], 'v')
w = Vector(['22.737', '23.64'], 'w')
print('is parallel: ', v.is_parallel_to(w))
print('is orthogonal: ', v.is_orthogonal_to(w))

print('second pair...')
v = Vector(['-2.029', '9.97', '4.172'], 'v')
w = Vector(['-9.231', '-6.39', '-7.245'], 'w')
print('is parallel: ', v.is_parallel_to(w))
print('is orthogonal: ', v.is_orthogonal_to(w))

print('third pair...')
v = Vector(['-2.328', '-7.284', '-1.214'], 'v')
w = Vector(['-1.821', '1.072', '-2.94'], 'w')
print('is parallel: ', v.is_parallel_to(w))
print('is orthogonal: ', v.is_orthogonal_to(w))

print('fourth pair...')
v = Vector(['2.118', '4.827'], 'v')
w = Vector(['0', '0'], 'w')

print('is parallel: ', v.is_parallel_to(w))
print('is orthogonal: ', v.is_orthogonal_to(w))



print('#1')
v = Vector(['3.039', '1.879'], 'v')
w = Vector(['0.825', '2.036'], 'w')
print(v.component_parallel_to(w))

print('#2')
v = Vector(['-9.88', '-3.264', '-8.159'], 'v')
w = Vector(['-2.155', '-9.353', '-9.473'], 'w')
print(v.component_orthogonal_to(w))

print('#3')
v = Vector(['3.009', '-6.172', '3.692', '-2.51'], 'v')
w = Vector(['6.404', '-9.144', '2.759', '8.718'], 'w')

vpart = v.component_parallel_to(w)
vort = v.component_orthogonal_to(w)
print('parallel part: ', vpart)
print('orthogonal part: ', vort)

v = Vector(['8.462', '7.893', '-8.187'], 'v')
w = Vector(['6.984', '-5.975', '4.778'], 'w')
print('#1: ', v.cross(w))


v = Vector(['-8.987', '-9.838', '5.031'], 'v')
w = Vector(['-4.268', '-1.861', '-8.866'], 'w')
print('#2: ', v.area_of_parallelogram_with(w))

v = Vector(['1.5', '9.547', '3.691'], 'v')
w = Vector(['-6.007', '0.124', '5.772'], 'w')
print('#3: ', v.area_of_triangle_with(w))
'''
