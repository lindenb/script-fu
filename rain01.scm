(load "utils.mod")
;; #######################################################################################################

(define
	(script-fu-rain01 image proba minradius maxradius color)
	 (let* (
	 	 (x1 0)
	 	 (y1 0)
	 	 (x2 (car (gimp-image-width image)) )
	 	 (y2 (car (gimp-image-height image)) )
	 	 (npoints (* proba (* (- x2 x1) (- y2 y1))) )
	 	 (bg 0)
	 	 (n 0.0)
	 	 (rainlength 0.0)
	 	 (angle 0 )
     (mx 0) (my 0) (nx 0) (ny 0)
	 	)
	 (gimp-image-undo-group-start image)
	 (gimp-context-push)
	 (gimp-progress-init "Start" -1)
	 (set! bg (car (gimp-image-get-active-layer image)))
	 (gimp-drawable-set-visible bg TRUE)
	 (gimp-palette-set-foreground color)
	 (gimp-context-set-opacity 100)
	 (gimp-context-set-paint-mode NORMAL-MODE)
	 (gimp-context-set-brush "Circle (01)")
	 (gimp-context-set-brush-size 10.0)
	 (gimp-context-set-foreground '(0 0 0))

	 
	 (while (< n npoints) 
	   
	   (gimp-progress-update (/ n npoints))
	   (set! rainlength (+  (min minradius maxradius) (random (- (max minradius maxradius) (min minradius maxradius)))))
	 
     (set! mx  (+ x1 (random (- x2 x1))) )
	   (set! my  (+ y1 (random (- y2 y1))) )
	   (set! nx  (+ my (* (cos angle) rainlength)))
	   (set! ny  (+ my (* (sin angle) rainlength)))

	   (gimp-paintbrush-default  bg 4 (list->vector (list mx my nx ny)))
	   
	   (set! n (+ n 1))
	 )
	 

	 (gimp-context-pop)
	 (gimp-image-undo-group-end image)
	 (gimp-displays-flush)
	 (gimp-progress-end)
	 )
)

;; #######################################################################################################
(script-fu-register "script-fu-rain01"
  _"Rain01..."
  "Rain01"
  "Pierre Lindenbaum"
  "(c) Pierre Lindenbaum"
  "2018"
  ""
 SF-IMAGE      "Image"     0
 SF-ADJUSTMENT "Proba"      (list 0.001  0.0 1.0 0.001 0.1 5 SF-SPINNER)
 SF-ADJUSTMENT "Min radius" (list 10  1 1000 1 10 1 SF-SLIDER)
 SF-ADJUSTMENT "Max radius" (list 100 1 1000 1 10 1 SF-SLIDER)
 SF-COLOR      "Color"   "black"
)


(script-fu-menu-register "script-fu-rain01"
                         "<Toolbox>/Xtns/Languages/Script-Fu/Yokofakun")
