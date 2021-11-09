#  https://classroom.udacity.com/courses/ud953/lessons/4624329808/concepts/49147586460923

import Plot
import Vector as V

        	
nv = V.Vector([0., 0.])
a = V.Vector([3., 5.])
#print(a.coordinates)
v1 = V.Vector([7.887, 4.138])
#v2 = V.Vector([-5.955, -4.904, -1.874])
v3 = V.Vector([3.183, -7.627])
#v4 = V.Vector([7.35, 0.221, 5.188])
w1 = V.Vector([-8.802, 6.776])
#w2 = V.Vector([-4.496, -8.755, 7.103])
w3 = V.Vector([-2.668, 5.319])
#w4 = V.Vector([2.751, 8.259, 3.985])

pg = Plot.plot_graph()
#pg.plot_line(v3.coordinates, (1.0, 0.5, 0), nv.coordinates)
#pg.plot_line(w3.coordinates, (1.0, 0., 1.), nv.coordinates)


'''
print('----paralell & orthogonal')

v1 = V.Vector([-7.579, -7.88])
v2 = V.Vector([-2.029, 9.97, 4.172])
v3 = V.Vector([-2.328, -7.248, -1.214])
v4 = V.Vector([2.118, 4.827])

w1 = V.Vector([22.737, 23.64])
w2 = V.Vector([-9.231, -6.631, -7.245])
w3 = V.Vector([-1.821, 1.072, -2.94])
w4 = V.Vector([0, 0])

#pg.plot_line(v1.coordinates, (1.0, 0.5, 0), nv.coordinates)
#pg.plot_line(w1.coordinates, (1.0, 0.5, 0), nv.coordinates)

'''
#------- Projecting Vectors -------
print('---- Vector Projection --------')
v1 = V.Vector([6, -4])
v2 = V.Vector([1, 3])

v3 = v2.component_parallel_to(v1)
v4 = v2.component_orthogonal_to(v1).plus(v3)
pg.plot_line(v1.coordinates, (1.0, 0.5, 0), nv.coordinates)
pg.plot_line(v2.coordinates, (0., 0., 1.), nv.coordinates)
pg.plot_line(v3.coordinates, (0., 0., 1.), nv.coordinates)
#pg.plot_line(v3.coordinates, (0., 0., 1.), v2.coordinates)

pg.plot_line(v4.coordinates, (0.,1., 0.), v3.coordinates)


print('#1')
v = V.Vector([3.039, 1.879])
w = V.Vector([0.825, 2.036])
vpar = v.component_parallel_to(w)
print(vpar)

#pg.plot_line(v.coordinates, (1.0, 0.5, 0), nv.coordinates)
#pg.plot_line(w.coordinates, (0., 0., 1.), nv.coordinates)
#pg.plot_line(vpar.coordinates, (0., 0., 1.), w.coordinates)

print('\n#2')
v = V.Vector([-9.88, -3.264, -8.159])
w = V.Vector([-2.155, -9.353, -9.473])
print(v.component_orthogonal_to(w))
print('\n#3')
v = V.Vector([3.009, -6.172, 3.692, -2.51])
w = V.Vector([6.404, -9.144, 2.759, 8.718])
vpar = v.component_parallel_to(w)
vort = v.component_orthogonal_to(w)
print('parallel component: ', vpar)
print('orthogonal component: ', vort)

#--------- cross product --
v = V.Vector([5, 3, -2])
w = V.Vector([-1,0,3])
print(v.cross(w))




#----------------------------------
'''					        
def print_vector(v):
	print(v, v.magnitude(), v.normalized())

my_vector = Vector([1,2,3])

v1 = Vector([8.218, -9.341])
v2 = Vector([7.119, 8.215])
v3 = Vector([1.671, -1.012, -0.318])


v1_plus = v1.plus(Vector([-1.129, 2.111]))
v2_minus = v2.minus(Vector([-8.223, 0.878]))
v3_scalar = v3.times_scalar(7.41)


print('----- Beispiel plus, minus, scalar')
print(v1_plus)
print(v2_minus)
print(v3_scalar)
print('---------')

print('---Beispiel Betrag und normalized-')
#v1 = Vector([-0.221, 7.437])
#v2 = Vector([8.813, -1.331, -6.247])
v3 = Vector([5.581, -2.136])
v4 = Vector([1.996, 3.108, -4.554])


#print(v1)

print('----')

#print(v2)

print('-v3---')
#print_vector(v3)

print('--v4--')

#print_vector(v4)


print('---- dot and angle----')
v1 = Vector([7.887, 4.138])
v2 = Vector([-5.955, -4.904, -1.874])
v3 = Vector([3.183, -7.627])
v4 = Vector([7.35, 0.221, 5.188])
w1 = Vector([-8.802, 6.776])
w2 = Vector([-4.496, -8.755, 7.103])
w3 = Vector([-2.668, 5.319])
w4 = Vector([2.751, 8.259, 3.985])

print(v1.dot(w1))
print(v2.dot(w2))

print(v3.angle_width(w3))
print(v4.angle_width(w4, True))

print('----paralell & orthogonal')

v1 = Vector([7.579, -7.88])
v2 = Vector([-2.029, 9.97, 4.172])
v3 = Vector([-2.328, -7.248, -1.214])
v4 = Vector([2.118, 4.827])

w1 = Vector([22.737, 23.64])
w2 = Vector([-9.231, -6.631, -7.245])
w3 = Vector([-1.821, 1.072, -2.94])
w4 = Vector([0, 0])

v5 = Vector([2, 2])
w5 = Vector([2, -2])

print(v5.normalized())
print(w5.normalized())
#print(v5.dot(w5))

print(v3.normalized())
print(w3.normalized())
print(v3.dot(w3))


v = [(1, 3), (3, 3), (4, 6)]
plt.plot_vector(v)      # draw 3 vectors with their tails at origin
t = [numpy.array((2, 2))]
plt.plot_vector(v, t)   # draw 3 vectors with their tails at (2,2)
t = [[3, 2], [-1, -2], [3, 5]]
plt.plot_vector(v, t)   # draw 3 vectors with 3 different tails
'''
