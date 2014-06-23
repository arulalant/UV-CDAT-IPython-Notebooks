"""
Written By : Arulalan.T
Date : 31.07.2013
"""

import xmgrace
import numpy

x = xmgrace.init()

x.Graph[0].yaxis.min=-150. # ymin for graph 0
x.Graph[0].yaxis.max=300.
x.Graph[0].yaxis.tick.inc=50 # Main tick every unit
x.Graph[0].yaxis.tick.minor_ticks=0 # 4 sub in between , 1 every .25 units

x.Graph[0].xaxis.min=0.
x.Graph[0].xaxis.max=4.


# median, upperQuartile, lowerQuartile, max, min 
a = [14.9471, 125.928, -22.6248, 217.2, -52.5566]
#####
#### The order of the values to be passed in the yaxis
#### median - horizontal small line inside the box 
#### upperQuartile - box upper edge
#### lowerQuartile - box lower edge
#### max - maxmimum peak of the vertical line over the box 
#### min - lowerst value of the vertical line under the box 
#### 

yaxis = numpy.array(a)
### yaxis data should be in vertical stack.
yaxis = yaxis.reshape((5,1))

for i in range(2):
    x.Graph[0].Set[i].type = 'xyboxplot'
    # make the box color as black
    x.Graph[0].Set[i].symbol.color = 1
    if i == 0:
        # make the box fill color as white
        x.Graph[0].Set[i].symbol.fcolor = 0
        # adjust the box width size
        x.Graph[0].Set[i].symbol.size = 1
        # enable the upper and lower vertical line 
        x.Graph[0].Set[i].errorbar.status = 'on'
        # adjust the size of the horizontal lines of the edge 
        # of the upper & lower errorbar lines.
        x.Graph[0].Set[i].errorbar.size = 1
    else:
        # make the box fill color as white
        x.Graph[0].Set[i].symbol.fcolor = 10
        # adjust the box width size
        x.Graph[0].Set[i].symbol.size = 3
        # enable the upper and lower vertical line 
        x.Graph[0].Set[i].errorbar.status = 'on'
        # adjust the size of the horizontal lines of the edge 
        # of the upper & lower errorbar lines.
        x.Graph[0].Set[i].errorbar.size = 2
    # end of if i == 0:
    # add new set to the Graph '0'
    x.add_set(0)
    
x.plot([yaxis], xs=[[2]], G=0, S=0)
# pass different yaxis and x value for the another set 
x.plot([yaxis], xs=[[3]], G=0, S=1)
x.ps('box_xy_plot_multi')

print x.Graph[0].Set[0].list()


