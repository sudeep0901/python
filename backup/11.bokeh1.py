import pandas as pd
import numpy as np
import bokeh as bk

print(bk.__version__)


x = [1 ,2, 3, 4, 5]
y = [6 ,5 ,6, 4, 5]

from bokeh.plotting import figure

p =  figure(plot_width=600,
    plot_height=300)


p.line(x, y)

from bokeh.io import show
from bokeh.io import output_notebook
# output_notebook()
show(p)

# from bokeh.plotting import output_file

# output_file('line.html' )

# scatter plot
p.circle(x,y,
size=20,
color='maroon',
alpha=0.5)
show(p)

p.asterisk(x, y, size = 15, color='green')
show(p)

p.step(x, y, color='red')
show(p)