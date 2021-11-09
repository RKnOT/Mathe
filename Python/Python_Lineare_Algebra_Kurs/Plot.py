# Function Plotter

import canvas
import Vector as V
import console
from math import sin, cos, pi


class plot():
	
	def __init__(self, conf):
		'''
		{'c_size_x' : 700, 'c_size_y' : 700, 'x_min' : -10, 'x_max' : 10, 'y_min' :-10, 'y_max' :10, 'raster' : 1}
		'''
		canvas.set_size(conf['c_size_x'], conf['c_size_y'])
		self.w, self.h = canvas.get_size()
		self.min_x = conf['x_min']
		self.max_x = conf['x_max']
		self.min_y = conf['y_min']
		self.max_y = conf['y_max']
		self.raster = conf['raster']
		self.scale_x = self.w / (self.max_x - self.min_x)
		self.scale_y = self.h / (self.max_y - self.min_y)
		self.min_x, self.max_x = round(self.min_x), round(self.max_x)
		self.min_y, self.max_y = round(self.min_y), round(self.max_y)
		self.origin_x, self.origin_y = self.w / 2, self.h / 2
	#---------------	
	def draw_grid(self):
		canvas.begin_updates()
		canvas.set_line_width(1)
		canvas.set_stroke_color(0.7, 0.7, 0.7)
		#Draw vertical grid lines:
		x = self.min_x
		while x <= self.max_x:
			if x != 0:
				draw_x = round(self.w / 2 + x * self.scale_x) + 0.5
				canvas.draw_line(draw_x, 0, draw_x, self.h)
			x += self.raster
		canvas.set_line_width(3)
		canvas.draw_line(draw_x, 0, draw_x, self.h)
		canvas.set_line_width(1)
		#Draw horizontal grid lines:
		y = self.min_y
		while y <= self.max_y:
			if y != 0:
				draw_y = round(self.h/2 + y * self.scale_y) + 0.5
				canvas.draw_line(0, draw_y, self.w, draw_y)
			y += self.raster
		#Draw x and y axis:
		canvas.set_stroke_color(0, 0, 0)
		canvas.draw_line(0, self.h/2, self.w, self.h/2)
		canvas.draw_line(self.w/2, 0, self.w/2, self.h)
		canvas.end_updates()
	#--------------
	def plot_function(self, func, color):
		#Calculate scale, set line width and color:
		canvas.set_stroke_color(*color)
		canvas.set_line_width(2)
		canvas.move_to(self.origin_x + self.scale_x * self.min_x, self.origin_y + func(self.min_x) * self.scale_y)
		#Draw the graph line:
		x = self.min_x
		while x <= self.max_x:
			x += 0.05
			draw_x = self.origin_x + self.scale_x * x
			draw_y = self.origin_y + func(x) * self.scale_y
			canvas.add_line(draw_x, draw_y)
		canvas.set_fill_color(*color)
		canvas.draw_path()
	#-------------
	def plot_line(self, v_head, color, v_tail):
		x_h = float(v_head.coordinates[0])
		y_h = float(v_head.coordinates[1])
		x_t = float(v_tail.coordinates[0])
		y_t = float(v_tail.coordinates[1])
		canvas.begin_updates()
		#Calculate scale, set line width and color:
		canvas.set_stroke_color(*color)
		canvas.set_line_width(2)
		#Draw the  line:
		x_tail = x_t * self.scale_x + self.origin_x
		y_tail = y_t * self.scale_y + self.origin_y
		x_had = self.origin_x + self.scale_x * x_h
		y_had = self.origin_y+ self.scale_y * y_h
		canvas.move_to(x_tail, y_tail)
		canvas.add_line(x_had, y_had)
		canvas.set_fill_color(*color)
		canvas.draw_path()
		canvas.fill_ellipse(x_had -4, y_had -4, 8, 8)
		canvas.end_updates()
	#-----------
class plot_vector_line():
	def __init__(self, vh, vt, pl):
		#.  Vector:  x = 2 | y = 2 Vector:  x = 4 | y = 8
		print(vt, vh)
		self.geraden_gleichung(vh, vt, pl)
		
		
	def geraden_gleichung(self, vh, vt, pl):
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
		print(yt/xt)
		m = (yt /xt)
		b = y1 - m * x1
		
		print(m,b)
		
		yl = m*x_min + b
		yh = m*x_max + b
		
		gP_min = V.Vector([x_min, yl])		
		gP_max = V.Vector([x_max, yh])
		
		print(gP_min, gP_max)	
		pl.plot_line(gP_min, (1.0, 0.5, 0), gP_max)	
	#-----------
class plot_graph(plot):
	#clear any text output:
	console.clear()
	def __init__(self):
		#Draw the grid:
		grid_size_x = 15
		grid_size_y = 15
		area = {'c_size_x' : 700, 'c_size_y' : 700, 'x_min' : -grid_size_x, 'x_max' : grid_size_x, 'y_min' : -grid_size_y, 'y_max' : grid_size_y, 'raster' : 1}
		super().__init__(area)
		
		self.plt = plot(area)
		self.plt.draw_grid()

'''
pg = plot_graph()

#Draw 4 different graphs (sin(x), cos(x), x^2, x^3):
#plt.plot_function(sin, (1, 0, 0))
#plt.plot_function(cos, (0, 0, 1))
#plt.plot_function(lambda x: x ** 2, (0, 1, 1))
#pg.plot_function(lambda x: x ** 3, (1.0, 0.5, 0))
pg.plot_line(3 , 6, (1.0, 0.5, 0), -1., -6.9)
'''
