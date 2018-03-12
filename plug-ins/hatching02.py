#!/usr/bin/env python

## gimpbook.com/scripting

from gimpfu import *
import sys
import random
import gimputils
import math
from gimputils import GimpUtils

def hatching02(image) :
	layer = pdb.gimp_image_get_active_layer(image)
	strokeLen = 60.0
	distanceBetweenStrokes = 5.0
	incertitude = 4
	y = layer.height + strokeLen
	pdb.gimp_context_push()
	pdb.gimp_undo_push_group_start(image)
	pdb.gimp_image_undo_freeze(image)
	pdb.gimp_context_set_brush("Circle (01)")
	pdb.gimp_context_set_brush_size(1)
	pdb.gimp_progress_init("Start...", None)
	while y >=  0 :
		x = random.randrange(-10,0)
		GimpUtils.log("y "+str(y)+" x="+str(x)+" w="+str(pdb.gimp_context_get_brush_size()));
		while x <  layer.width :
			x1 = x + random.randrange(-incertitude,incertitude)
			y1 = y + random.randrange(-incertitude,incertitude)
			x2 = x + random.randrange(-incertitude,incertitude)
			y2 = y - strokeLen  + random.randrange(-incertitude,incertitude)
			#x1 = 0
			#y1 = 0
			#x2 = image.width
			#y2  = image.height
			ctrlPoints = [x1,y1,x2,y2]
			pdb.gimp_paintbrush_default(layer, len(ctrlPoints), ctrlPoints)			
			x += 2.0 * pdb.gimp_context_get_brush_size()
			x += distanceBetweenStrokes + random.randrange(0,incertitude)
		pdb.gimp_progress_pulse()
		y -= strokeLen
		y -= pdb.gimp_context_get_brush_size()
	pdb.gimp_progress_end()
	pdb.gimp_image_undo_thaw(image)
	pdb.gimp_undo_push_group_end(image)
	
	pdb.gimp_context_pop()
	pdb.gimp_displays_flush()

register(
    "python_fu_hatching02",
    "Hatching02",
    "Hatching02",
    "Pierre Lindenbaum",
    "Pierre Lindenbaum",
    "2018",
    "Hatching02...",
    "",      # Create a new image, don't work on an existing one
    [
    (PF_IMAGE, "image", "Input image", None)
    ],
    [],
    hatching02, menu= "<Toolbox>/Xtns/Languages/Script-Fu/Yokofakun" 
    )
   
main()
