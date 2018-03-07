#!/usr/bin/env python

## gimpbook.com/scripting

from gimpfu import *
import sys
import gimputils



class Speed01(gimputils.AbstractGimpPlugin):
	pass


def speed01(image, drawable, initstr, font, size, color) :
	self = Speed01()
	self.width = drawable.width
        self.height = drawable.height
	pdb.gimp_context_push()
	self.log( gimputils.add(10,17)  )
	gimp.displays_flush()
	pdb.gimp_context_pop()

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
        (PF_DRAWABLE, "drawable", "Input drawable", None),
        (PF_STRING, "string", "Text string", 'Hello, world!'),
        (PF_FONT, "font", "Font face", "Sans"),
        (PF_SPINNER, "size", "Font size", 50, (1, 3000, 1)),
        (PF_COLOR, "color", "Text color", (1.0, 0.0, 0.0))
    ],
    [],
    speed01, menu= "<Toolbox>/Xtns/Languages/Script-Fu/Yokofakun" 
    )
   
main()
