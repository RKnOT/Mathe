import Plot
import Vector as V
import Vector_Lines
import console
console.clear()


pg = Plot.plot_graph()

nP = V.Vector([0., 0.])
u = V.Vector([2.,3.])
r = V.Vector([5., 2.])
x1 = V.Vector([14., 8.])

v_l = Vector_Lines.get_Line_End_Points()
v_l.OV_RV_get_Line(u, r, pg.min_x, pg.max_x,  2)


pg.plot_line(v_l.vl_max, (0.8,0.8,0.8), v_l.vl_min)

pg.plot_line(u, (1.0, 0.5, 0), nP)
pg.plot_line(r, (1.0, 0.5, 1.), nP)
pg.plot_line(v_l.x, (0.5, 1., 0), u)


v_l.P1_P2_get_Line(u, r, pg.min_x, pg.max_x)
pg.plot_line(v_l.vl_max, (0.8,0.8,0.8), v_l.vl_min)

'''
x = u.plus(r.times_scalar(1))


xmax =	(pg.max_x - u.coordinates[0]) / r.coordinates[0]
xmin =	(pg.min_x - u.coordinates[0]) / r.coordinates[0]

l_max = u.plus(r.times_scalar(xmax))
l_min = u.plus(r.times_scalar((xmin)))

pg.plot_line(l_max, (0.8,0.8,0.8), l_min)
pg.plot_line(l_min, (0.8,0.8,0.8), l_max)

pg.plot_line(u, (1.0, 0.5, 0), nP)
pg.plot_line(r, (1.0, 0.5, 1.), nP)
pg.plot_line(x, (0.5, 1., 0), u)


#pg.plot_line(l_min, (0.2,0.2,0.2), u)
#gp = ov.plus(p1_t)
#pg.plot_line(rv, (0., 0., 1), ov)
'''

