#!/usr/bin/env python

## gimpbook.com/scripting

from gimpfu import *
import sys
import random
import gimputils
import math
from gimputils import GimpUtils

def hatching01(image,incertitudeExpr) :
	noiseFun = lambda r: eval(incertitudeExpr)
	MIN_BRUSH_OPACITY = 0.0
	layer = pdb.gimp_image_get_active_layer(image)
	center = GimpUtils.centerOf(layer)
	maxradius = GimpUtils.distance(center.x,center.y,0,0)
	deltaradius = 20
	minradius = deltaradius
	radius = maxradius
	precision = 20
	pdb.gimp_context_push()
	pdb.gimp_undo_push_group_start(image)
	pdb.gimp_image_undo_freeze(image)

	## pdb.gimp_context_set_paint_method('gimp-paintbrush')
	## pdb.gimp_context_set_brush(formBrush)
	brushSize = 1.0 * pdb.gimp_context_get_brush_size()
	brushOpacity = 1.0 * pdb.gimp_context_get_opacity()
	pdb.gimp_progress_init("Start...", None)
	while radius >  minradius and deltaradius >= 1.0  and brushSize >= 1.0 and brushOpacity > MIN_BRUSH_OPACITY:
		deltaangle = (precision * random.random()) / (radius * 1.0)
		start_angle = GimpUtils.PI2 * random.random()
		angle = 0
		fg_color = (0,0,0)
		pdb.gimp_context_set_foreground(fg_color)
		GimpUtils.log("brush "+str(brushSize)+" radius:"+str(radius));
		pdb.gimp_progress_set_text("brush "+str(brushSize)+" radius:"+str(radius));
		pdb.gimp_context_set_brush_size(brushSize)
		pdb.gimp_context_set_opacity(brushOpacity)
		
		
		while angle <  GimpUtils.PI2 :
			r0 = radius
			r1 = radius - deltaradius
			
			x1 = center.x + math.cos( start_angle + angle ) * r0 + noiseFun(r0)
			y1 = center.y + math.sin( start_angle + angle ) * r0 + noiseFun(r0)
			x2 = center.x + math.cos( start_angle + angle ) * r1 + noiseFun(r1)
			y2 = center.y + math.sin( start_angle + angle ) * r1 + noiseFun(r1)
			ctrlPoints = [x1,y1,x2,y2]
			pdb.gimp_paintbrush_default(layer, len(ctrlPoints), ctrlPoints)			
			angle += deltaangle
		pdb.gimp_progress_pulse()
		radius -= deltaradius
		deltaradius *= 0.95
		brushSize *= 0.95
		brushOpacity *= 0.95
	pdb.gimp_progress_end()
	pdb.gimp_image_undo_thaw(image)
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
    (PF_IMAGE, "image", "Input image", None),
    (PF_STRING, "incertitudeExpr", "Incertitude", " (random.random() * 6.0) - 3.0")
    ],
    [],
    hatching01, menu= "<Toolbox>/Xtns/Languages/Script-Fu/Yokofakun" 
    )
   
main()
