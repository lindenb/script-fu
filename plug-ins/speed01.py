#!/usr/bin/env python

## gimpbook.com/scripting

from gimpfu import *
import sys
import random
import gimputils



class Speed01(gimputils.AbstractGimpPlugin):
	pass

def speed01(image, drawable) :
	self = Speed01()
	x1 = 0
	y1 = 0
	x2 = drawable.width
	y2 = drawable.height
	proba = 0.001
	npoints = proba * (( x2 - x1 ) * (y2 - y1) )
	pdb.gimp_context_push()
	pdb.gimp_progress_init("SPeed01", None)
	pdb.gimp_undo_push_group_start(image)
	selection = pdb.gimp_image_get_selection(image)
	gimp.set_foreground(0,0,0)
	bg = pdb.gimp_image_get_active_drawable(image);
	while npoints > 0:
		cx = random.randrange(x1,x2)
		cy = random.randrange(y1,y2)
		radius =  random.randrange(2,10)
		pdb.gimp_image_select_item(image,2,selection)
		pdb.gimp_ellipse_select(image, cx - radius, cy - radius, 2 * radius, 2 * radius, 0, True, False, 0)
		pdb.gimp_bucket_fill( bg, 0,0, 100,0,False,0,0)
		npoints -= 1
	pdb.gimp_undo_push_group_end(image)
	pdb.gimp_context_pop()
	pdb.gimp_displays_flush()

register(
    "python_fu_speed01",
    "Speed01",
    "Speed Tunnel",
    "Pierre Lindenbaum",
    "Pierre Lindenbaum",
    "2018",
    "Speed01...",
    "",      # Create a new image, don't work on an existing one
    [
   	(PF_IMAGE, "image", "Input image", None),
    (PF_DRAWABLE, "drawable", "Input drawable", None)
    ],
    [],
    speed01, menu= "<Toolbox>/Xtns/Languages/Script-Fu/Yokofakun" 
    )
   
main()
