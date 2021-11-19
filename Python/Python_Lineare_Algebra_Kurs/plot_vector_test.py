import Plot
import vector_new as V
import Line_new as L 
import console
console.clear()






nP = V.Vector([0., 0.])
pg = Plot.plot_graph()







v1 = V.Vector(['4.046', '2.836'], 'v1')
v2 = V.Vector(['10.115', '7.09'], 'v2')

v1 = V.Vector(['4.', '3.'], 'v1')
v2 = V.Vector(['8.', '6.'], 'v2')

v1 = V.Vector([3., 2.], 'V1')
v2 = V.Vector([6., 4.])



v1 = V.Vector([0,3])
v2 = V.Vector([-6, 0])

G1 = L.get_chart_line_points(v1, v2, pg)
pg.plot_line(G1.gP_max, (0.7, 0.7, 0.7), G1.gP_min)




v3 = V.Vector([2, 4])
v4 =V.Vector([-1, 0])

P1 = V.Point(3.,4.1, 'P1')
#print(P1)

l1 = L.Line(normal_vector = V.Vector(['-1.', '2.']), constant_term = '6.')


#pg.plot_line(l1.normal_vector.plus(v1), (1.0, 0., 0), v1)

#print(l1.basepoint, l1.normal_vector)

pg.plot_line(v1, (1.0, 0.5, 0), v2)


l1_p2 = l1.basepoint.plus(l1.normal_vector.times_scalar(2).v_90())

#print(l1.normal_vector, l1.normal_vector.v_90())


pg.plot_line(l1_p2, (0, 0, 1), l1.basepoint)


pg.plot_line(l1.normal_vector.plus(l1_p2), (1.0, 0., 0), l1_p2)


l2 = L.Line(normal_vector = V.Vector(['-1', '2']), constant_term = '10.')
#print(l2)

l2_p1 = l2.basepoint.plus(l2.normal_vector.times_scalar(1).v_90())
l2_p2 = l2.basepoint.plus(l2.normal_vector.times_scalar(7).v_90())


G2 = L.get_chart_line_points(l2_p2, l2_p1, pg)
pg.plot_line(G2.gP_max, (0.7, 0.7, 0.7), G2.gP_min)

pg.plot_line(l2_p2, (1.0, 0.5, 0), l2_p1)


ell1 = L.Line(normal_vector = V.Vector(['4.046', '2.836']), constant_term = '1.21')
ell2 = L.Line(normal_vector = V.Vector(['10.115', '7.09']), constant_term = '3.025')
print('intersection 1:', ell1.intersection_with(ell2))




ell1 = L.Line(normal_vector = V.Vector(['4.046', '2.836']), constant_term = '1.21')

ell2 = L.Line(normal_vector = V.Vector(['10.115', '7.09']), constant_term = '3.025')
print('intersection 1:', ell1.intersection_with(ell2))



ell1 = L.Line(normal_vector = V.Vector(['7.204', '3.182']), constant_term = '8.68')
ell2 = L.Line(normal_vector = V.Vector(['8.172', '4.114']), constant_term = '9.883')
print('intersection 2:', ell1.intersection_with(ell2))







'''
#pg.plot_line(v2t, (1.0, 0.5, 0), nP)

wd = v1.angle_width(v2)
print('winkel zwischen v1 & v2: ', wd)
print('parallel to: ', v1.is_parallel_to(v2))
print('magnitude: ', v1.magnitude(), v2.magnitude())

print(v1.component_parallel_to(v2).magnitude(), v2.component_parallel_to(v1).magnitude())

l1 = L.Line(v1t, 0)
l1t = L.Line(v1, 0)

print('-----')
print(l1.normal_vector, l1t.normal_vector)
print('-----')

print(l1.is_parallel_to(l1t))




#ell1 = Line(normal_vector = Vector(['4.046', '2.836']), constant_term = '1.21')

#ell2 = Line(normal_vector = Vector(['10.115', '7.09']), constant_term = '3.025')
#print('intersection 1:', ell1.intersection_with(ell2))
#print(ell1.dot(ell2))


ell1 = Line(normal_vector = Vector(['7.204', '3.182']), constant_term = '8.68')

ell2 = Line(normal_vector = Vector(['8.172', '4.114']), constant_term = '9.883')
#print('intersection 2:', ell1.intersection_with(ell2))




nP = V.Vector([0., 0.])
u = V.Vector([2., 15.])
p2 = V.Vector([4., 1.])


v = u.minus(p2)

x = u.minus(v.times_scalar(3))
# ortsvector
#pg.plot_line(u, (1.0, 0.5, 0), nP)
#pg.plot_line(p2, (1.0, 0.5, 0), nP)

#pg.plot_line(v1, (0.5, 1., 0), p2)

#pg.plot_line(x, (0.5, 1., 0), u)




#gp = ov.plus(p1_t)

#pg.plot_line(rv, (0., 0., 1), ov)

'''
a =1

'''

#ell1 = Line(normal_vector = Vector(['4.046', '2.836']), constant_term = '1.21')

#ell2 = Line(normal_vector = Vector(['10.115', '7.09']), constant_term = '3.025')
#print('intersection 1:', ell1.intersection_with(ell2))



#ell1 = Line(normal_vector = Vector(['7.204', '3.182']), constant_term = '8.68')

#ell2 = Line(normal_vector = Vector(['8.172', '4.114']), constant_term = '9.883')
#print('intersection 2:', ell1.intersection_with(ell2))
'''
