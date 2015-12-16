
def mrdfits(file,hdu):
	x=Table.read(file)




def idlhelp(x,rowid=0):
	 for col in x.columns:
	 	print col ,'  =  ', x[col][rowid]