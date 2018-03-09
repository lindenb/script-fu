;; #######################################################################################################

(define
	(script-fu-kirby01 image proba minradius maxradius color)
	 (let* (
	 	 (x1 0)
	 	 (y1 0)
	 	 (x2 (car (gimp-image-width image)) )
	 	 (y2 (car (gimp-image-height image)) )
	 	 (npoints (* proba (* (- x2 x1) (- y2 y1))) )
	 	 (bg 0)
	 	 (n 0.0)
	 	 (radius 0.0)
	 	 (selection 0)
	 	)
	 (gimp-image-undo-group-start image)
	 (gimp-context-push)
	 (gimp-progress-init "Start" -1)
	 (set! bg (car (gimp-image-get-active-layer image)))
	 (gimp-drawable-set-visible bg TRUE)
	 (gimp-palette-set-foreground color)
	 (set! selection (car (gimp-selection-save image)))
	 
	 
	 (while (< n npoints) 
	   
	   (gimp-progress-update (/ n npoints))
	   (set! radius (+  (min minradius maxradius) (random (- (max minradius maxradius) (min minradius maxradius)))))
	   (gimp-image-select-ellipse image CHANNEL-OP-INTERSECT (- (+ x1 (random (- x2 x1))) radius) (- (+ y1 (random (- y2 y1))) radius) (* 2.0 radius) (* 2.0 radius))
	   (gimp-edit-bucket-fill bg 0 0 (random 100) 0 0 0 0)
	   (gimp-image-select-item image  CHANNEL-OP-REPLACE selection)

	   
	   (set! n (+ n 1))
	 )
	 
	 (gimp-image-select-item image  CHANNEL-OP-REPLACE selection)
	 (gimp-context-pop)
	 (gimp-image-undo-group-end image)
	 (gimp-displays-flush)
	 (gimp-progress-end)
	 )
)

;; #######################################################################################################
(script-fu-register "script-fu-kirby01"
  _"Kirby01..."
  "Kirby01"
  "Pierre Lindenbaum"
  "(c) Pierre Lindenbaum"
  "2018"
  ""
 SF-IMAGE      "Image"     0
 SF-ADJUSTMENT "Proba"      (list 0.001  0.0 1.0 0.001 0.1 5 SF-SPINNER)
 SF-ADJUSTMENT "Min radius" (list 1  1 1000 1 10 1 SF-SLIDER)
 SF-ADJUSTMENT "Max radius" (list 10 1 1000 1 10 1 SF-SLIDER)
 SF-COLOR      "Color"   "black"
)


(script-fu-menu-register "script-fu-kirby01"
                         "<Toolbox>/Xtns/Languages/Script-Fu/Yokofakun")
