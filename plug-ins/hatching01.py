#!/usr/bin/env python

## gimpbook.com/scripting

from gimpfu import *
import sys
import random
import gimputils
import math
from gimputils import GimpUtils

def hatching01(image) :
	layer = pdb.gimp_image_get_active_layer(image)
	center = GimpUtils.centerOf(layer)
	print(center)
	maxradius = GimpUtils.distance(center.x,center.y,0,0)
	deltaradius = 10
	minradius = deltaradius
	radius = maxradius
	precision = 4
	pdb.gimp_context_push()
	pdb.gimp_undo_push_group_start(image)
	
	pdb.gimp_context_set_paint_mode(NORMAL_MODE)
	pdb.gimp_context_set_paint_method('gimp-paintbrush')
	pdb.gimp_context_set_brush('Circle (01)')
	
	while radius >  minradius and deltaradius > 0:
		deltaangle = precision / (radius * 1.0)
		start_angle = GimpUtils.PI2 * random.random()
		angle = 0
		fg_color = (0,0,0)
		pdb.gimp_context_set_foreground(fg_color)
		while angle <  GimpUtils.PI2 :
			r0 = radius
			r1 = radius - deltaradius
			pdb.gimp_context_set_brush_size(15.1)
			x1 = center.x + math.cos( start_angle + angle ) * r0
			y1 = center.y + math.sin( start_angle + angle ) * r0
			x2 = center.x + math.cos( start_angle + angle ) * r1
			y2 = center.y + math.sin( start_angle + angle ) * r1
			ctrlPoints = [x1,y1,x2,y2]
			pdb.gimp_paintbrush_default(layer, len(ctrlPoints), ctrlPoints)			
			angle += deltaangle
		radius -= deltaradius
		deltaradius *= 0.95
	pdb.gimp_undo_push_group_end(image)
	pdb.gimp_context_pop()
	pdb.gimp_displays_flush()

register(
    "python_fu_hatching01",
    "Hatching01",
    "Speed Tunnel",
    "Pierre Lindenbaum",
    "Pierre Lindenbaum",
    "2018",
    "Hatching01...",
    "",      # Create a new image, don't work on an existing one
    [
    (PF_IMAGE, "image", "Input image", None)
    ],
    [],
    hatching01, menu= "<Toolbox>/Xtns/Languages/Script-Fu/Yokofakun" 
    )
   
main()
