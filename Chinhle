import bokeh.io
import bokeh.plotting
bokeh.io.output_notebook()
from bokeh.layouts import row
from bokeh.plotting import figure, show

# prepare some data
x = list(range(6))
y1 = [i**2 + 1 for i in x]
y2 = [2*i + 3 for i in x]
y3 = [3*i - 4 for i in x]
y4 = [abs(2*i - 3) for i in x]

# create three plots with one renderer each
s1 = figure(width=250, height=250)
s1.scatter(x, y1, marker="circle", size=12, color="blue", alpha=0.8)

s2 = figure(width=250, height=250)
s2.scatter(x, y2, marker="circle", size=12, color='red', alpha=0.8)

s3 = figure(width=250, height=250)
s3.scatter(x, y3, marker="triangle", size=12, color="green", alpha=0.8)

s4 = figure(width=250, height=250)
s4.scatter(x, y4, marker="square", size=12, color="yellow", alpha=0.8)

# put the results in a row and show
show(row(s1, s2, s3, s4))
