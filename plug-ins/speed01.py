#!/usr/bin/env python



from gimpfu import *

def speed01(initstr, font, size, color) :
	pdb.gimp_context_push()
	img = gimp.Image(10, 10, RGB)
	gimp.Display(img)
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
        (PF_STRING, "string", "Text string", 'Hello, world!'),
        (PF_FONT, "font", "Font face", "Sans"),
        (PF_SPINNER, "size", "Font size", 50, (1, 3000, 1)),
        (PF_COLOR, "color", "Text color", (1.0, 0.0, 0.0))
    ],
    [],
    speed01, menu= "<Toolbox>/Xtns/Languages/Script-Fu/Yokofakun" 
    )
   
main()
