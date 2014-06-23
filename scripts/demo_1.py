import cdms2
DATAPATH = './data/Obs/mo/sst/HadISST/'
f = cdms2.open(DATAPATH + 'sst_HadISST_Climatology_1961-1990.nc')
# You can query the file
print f.listvariables()
# You can “access” the data through file variable
x = f['sst']
# or read all of it into memory
y = f('sst')
# You can get some information about the variables by
x.info()
y.info()
# You can also find out what class the object x or y belong to
print x.__class__
# Close the file
f.close()
