import Plot
import vector_new as V
import Vector_Lines
import console
console.clear()


pg = Plot.plot_graph()

nP = V.Vector([0., 0.])


v = V.Vector(['1.887', '5.138'], 'v')
w = V.Vector(['-8.802', '6.776'], 'w')

v = V.Vector(['6.2', '5.138'], 'v')
w = V.Vector(['8.802', '1.776'], 'w')


vll = v.component_parallel_to(w)
vs = v.v_90()


pg.plot_line(v, (1.0, 0.5, 0), nP)
pg.plot_line(w, (1.0, 0.5, 1.), nP)




pg.plot_line(vs, (1.0, 0.5, 1.), nP)
print(v.angle_width(vs, True))
