#!/usr/bin/env python

## gimpbook.com/scripting

from gimpfu import *
import sys
import random
import gimputils




def resizeTumblr01(image) :
	SIZE = 1280
	W = 1.0 * image.width
	H = 1.0 * image.height
	# https://stackoverflow.com/questions/394809
	W2 = ((W / H) * SIZE) if W < H else SIZE
	H2 = SIZE if W < H   else ( (H / W ) * SIZE )
	pdb.gimp_undo_push_group_start(image)
	pdb.gimp_image_flatten(image)
	pdb.gimp_image_scale(image,W2,H2)
	pdb.gimp_image_resize(image, SIZE, SIZE, (SIZE-W2)/2.0, (SIZE-H2)/2.0)
	pdb.gimp_image_flatten(image)
	pdb.gimp_undo_push_group_end(image)
	pdb.gimp_displays_flush()

register(
    "python_fu_resizeTumblr01",
    "Resize Tumblr 01",
    "Resize Tumblr",
    "Pierre Lindenbaum",
    "Pierre Lindenbaum",
    "2018",
    "Resize Tumblr...",
    "",      # Create a new image, don't work on an existing one
    [
   	(PF_IMAGE, "image", "Input image", None)
    ],
    [],
    resizeTumblr01, menu= "<Toolbox>/Xtns/Languages/Script-Fu/Yokofakun" 
    )
   
main()
