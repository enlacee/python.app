# Execute 
# pyton file imagen.jpg
from __future__ import print_function
import os, sys
from PIL import Image

for infile in sys.argv[1:]:
	f, e = os.path.splitext(infile)
	print ("hei", infile)
	print ("f", f)
	print ("e", e)
	outfile = f + ".png"
	print ("infile", infile)
	print ("outfile", outfile)
	if infile != outfile:
		try:
			Image.open(infile).save(outfile)
		except IOError:
			print("cannot convert", infile)

