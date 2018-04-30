#!/usr/bin/env python

from gimpfu import *
import sys
import random
import gimputils
import math
from gimputils import GimpUtils

## une couleur RGBA  dans gimp c'est (num-channel (r,g,b,a) )
def is_blank_pixel(c):
  if not len(c)==2 and len(c)==c[0] :
    return
  c= c[1];
  return (len(c)> 2 and c[0]>250 and c[1]>250 and c[2]>250 ) or (len(c) > 3 and c[3]<5)

def negate01(image,layermask,drawinglayer) :
  pdb.gimp_context_push()
  pdb.gimp_undo_push_group_start(image)
  pdb.gimp_image_undo_freeze(image)
  pdb.gimp_progress_init("Start...", None)
  y = 0
  while y < pdb.gimp_image_height(image) :
    x = 0
    while x < pdb.gimp_image_width(image) :
      c2 = pdb.gimp_drawable_get_pixel(layermask,x,y)
      if not is_blank_pixel(c2):
        c1 = pdb.gimp_drawable_get_pixel(drawinglayer,x,y)
        if is_blank_pixel(c1) :
          GimpUtils.log(str(x)+"/"+str(y)+":"+str(c2)+" : "+str(is_blank_pixel(c2))+" "+str(c1)+" : "+str(is_blank_pixel(c1)))
      	  pdb.gimp_drawable_set_pixel(layermask,x,y,4,[255,255,255,255])
      x = x + 1
    pdb.gimp_progress_set_text(str(y)+" /  " + str(pdb.gimp_image_height(image)))
    y = y + 1
  pdb.gimp_drawable_update(layermask,0,0,layermask.width,layermask.height)
  pdb.gimp_progress_end()
  pdb.gimp_image_undo_thaw(image)
  pdb.gimp_undo_push_group_end(image)
  pdb.gimp_context_pop()
  
  pdb.gimp_displays_flush()




register(
    "python_fu_negate01",
    "Negate01",
    "Negate01",
    "Pierre Lindenbaum",
    "Pierre Lindenbaum",
    "2018",
    "Negate01...",
    "",
    [
    (PF_IMAGE, "image", "Input image", None),
    (PF_DRAWABLE, "layermask", "MASK:", None),
    (PF_LAYER, "drawinglayer", "DRAWING:", None)
    ],
    [],
    negate01, menu= "<Toolbox>/Xtns/Languages/Script-Fu/Yokofakun" 
    )
   
main()

