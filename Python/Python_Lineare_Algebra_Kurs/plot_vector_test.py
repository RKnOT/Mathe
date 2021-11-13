import Plot
import vector_new as V
import Vector_Lines
import console
console.clear()


pg = Plot.plot_graph()

nP = V.Vector([0., 0.])
u = V.Vector([2., 15.])
p2 = V.Vector([4., 1.])


v = u.minus(p2)

x = u.minus(v.times_scalar(3))
# ortsvector
pg.plot_line(u, (1.0, 0.5, 0), nP)
pg.plot_line(p2, (1.0, 0.5, 0), nP)

#pg.plot_line(v1, (0.5, 1., 0), p2)

pg.plot_line(x, (0.5, 1., 0), u)




#gp = ov.plus(p1_t)

#pg.plot_line(rv, (0., 0., 1), ov)


