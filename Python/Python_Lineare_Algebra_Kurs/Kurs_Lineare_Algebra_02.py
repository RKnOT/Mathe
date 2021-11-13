import Plot
import vector_new as V
import Vector_Lines
import console
console.clear()


#pg = Plot.plot_graph()


nv = V.Vector([0., 0.])

l1 = V.Vector([4.046, 2.836])
l1r = 1.21
l2 = V.Vector([10.115, 7.09])
l2r = 3.025
#print(l1.normalized())
#print(l2.normalized())
#print(l1.angle_width(l2))
#print(l1.is_parallel_to(l2))
#print(l1.is_orthogonal_to(l2))




l3 = V.Vector([7.204, 3.182])
l3r = 8.58
l4 = V.Vector([8.172, 4.114])
l4r = 9.883
#print(l3.is_parallel_to(l4))

l5 = V.Vector([1.182, 5.562])
l5r = 6.744
l6 = V.Vector([1.773, 8.343])
l6r = 9.525

#print(l5.is_parallel_to(l6))
'''
pg.plot_line(l1.coordinates, (1.0, 0.5, 0), nv.coordinates)
pg.plot_line(l2.coordinates, (1.0, 0., 1.), nv.coordinates) 

pg.plot_line(l3.coordinates, (1.0, 0., 0), nv.coordinates)
pg.plot_line(l4.coordinates, (1.0, 0., 0.), nv.coordinates) 

pg.plot_line(l5.coordinates, (0., 0., 1.), nv.coordinates)
pg.plot_line(l6.coordinates, (0., 0., 1.), nv.coordinates) 



#------- vector projection ----------
p1 = V.Vector([9,5])
p2 = V.Vector([4,7])

p1_II = p2.component_parallel_to(p1)
p1_s = p2.component_orthogonal_to(p1)
p1_s_t = p1_s.plus(p1_II)
pg.plot_line(p1.coordinates, (0., 0., 1.), nv.coordinates)
pg.plot_line(p2.coordinates, (0., 1., 0.), nv.coordinates)
pg.plot_line(p1_II.coordinates, (1., 0., 0.), nv.coordinates)
pg.plot_line(p1_s_t.coordinates, (1., 0., 0.), p1_II.coordinates)
#------------------------------------
'''

p1 = V.Vector([9.,5.], 'p1')

print(p1)
