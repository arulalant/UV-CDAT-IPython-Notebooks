import cdms2, cdutil, genutil
NINO3 = cdms2.selectors.Selector(cdutil.region.domain(latitude=(-5., 5., 'ccb'), longitude=(210., 270., 'ccb')))

INDIR = '../mo/sst/HadISST/' 
infile = INDIR + 'sst_HadISST_1870-1_2011-1.nc'
f= cdms2.open(infile)

nino3_data = f('sst', NINO3)
nino3_average = cdutil.averager(nino3_data, axis='xy')
nino3_slice = nino3_average(time=('1961-1-1', '1990-12-31'))
nino3_clim = cdutil.ANNUALCYCLE.climatology(nino3_slice)
nino3_anomaly = cdutil.ANNUALCYCLE.departures(nino3_average, nino3_clim)

#
# A quick and dirty plot
#
xm = genutil.xmgrace.init()
xm.plot(nino3_anomaly, G=0, S=0)
# by default only one Set (dataset) exists. So you add another one.
xm.add_set()
xm.plot(nino3_average, G=0, S=1)



#
# Same plot done in a more presentable way
#
xm2 = genutil.xmgrace.init()
# By default only one graph exists. Add another graph so...
xm2.add_graph()

#
# Set the viewport corners
#
xm2.Graph[0].vxmin = 0.1
xm2.Graph[0].vxmax = 0.9
xm2.Graph[0].vymin = 0.1
xm2.Graph[0].vymax = 0.48
# Second graph
xm2.Graph[1].vxmin = 0.1
xm2.Graph[1].vxmax = 0.9
xm2.Graph[1].vymin = 0.52
xm2.Graph[1].vymax = 0.9

xm2.Graph[0].frame.linewidth = 2
xm2.Graph[1].frame.linewidth = 2

#
# Set the y-axis minimum and maximum
#
xm2.Graph[0].ymin = -2.0
xm2.Graph[0].ymax = 4.0
# second graph
xm2.Graph[1].ymin = 22.
xm2.Graph[1].ymax = 30.


#
# Tick marks etc.
#
xm2.Graph[0].yaxis.tick.inc = 1.
xm2.Graph[0].yaxis.tick.orientation = 'out' # By default it is 'in'
# Second graph
xm2.Graph[1].yaxis.tick.inc = 2.
xm2.Graph[1].yaxis.tick.orientation = 'out' # By default it is 'in'
xm2.Graph[1].yaxis.tick.place = 'opposite' # By default it is 'normal'
xm2.Graph[1].yaxis.tick.label.place = 'opposite' # By default it is 'normal'

xm2.Graph[1].yaxis.lbl.place.side = 'opposite'

xm2.Graph[0].yaxis.label = 'NIN\\v{0.6}\\h{-0.5}~\\h{}\\v{}O3 Anomaly (\So\NC)'
xm2.Graph[1].yaxis.label = 'NIN\\v{0.6}\\h{-0.5}~\\h{}\\v{}O3 Average (\So\NC)'


#
# Let us put a zero axis on the lower(anomaly) plot.
#
xm2.Graph[0].altxaxis.status = 'on'
xm2.Graph[0].altxaxis.zero = 'True'
xm2.Graph[0].altxaxis.tick.status = 'off'
xm2.Graph[0].altxaxis.tick.label.status = 'off'


#
# Set the y-axis minimum and maximum
#
xm2.Graph[0].xmin = 16383360.
xm2.Graph[0].xmax = 17619340.
# second graph
xm2.Graph[1].xmin = 16383360.
xm2.Graph[1].xmax = 17619340.


#
# Now let us put meaningful x-axis tick labels.
#
lbl_dict = {}
taxis = nino3_average.getTime()
tc = taxis.asComponentTime()
for i in range(len(tc)):
    if divmod(tc[i].year, 10)[1] == 0 and tc[i].month == 6:
        lbl_dict[taxis[i]] = str(tc[i].year)
        #print taxis[i], tc[i].year
    elif divmod(tc[i].year, 5)[1] == 0 and tc[i].month == 6:
        lbl_dict[taxis[i]] = ''
    else:
        pass
    # end of if
# end of for i in range(len(tc)):

xm2.Graph[0].xaxis.tick.spec.loc = lbl_dict
xm2.Graph[1].xaxis.tick.spec.loc = lbl_dict



xm2.Graph[0].xaxis.tick.orientation = 'out'
xm2.Graph[1].xaxis.tick.orientation = 'out'
xm2.Graph[1].xaxis.tick.place = 'opposite' # By default it is 'normal'
xm2.Graph[1].xaxis.tick.label.place = 'opposite' # By default it is 'normal'

#
# Set the line colors that you want to plot.
#
# default color is black.
xm2.Graph[0].Set[0].line.color = 'blue'
xm2.Graph[1].Set[0].line.color = 'red'

xm2.plot(nino3_anomaly, G=0, S=0)
xm2.plot(nino3_average, G=1, S=0)
