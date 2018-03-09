(load "utils.mod")


(define
	(script-fu-rain01 image proba minlength maxlength color)
	 (let* (
	 	(x1 0)
	 	(y1 0)
	 	(x2 (car (gimp-image-width image)) )
	 	(y2 (car (gimp-image-height image)) )
	 	(npoints (max 1 (* proba (* (- x2 x1) (- y2 y1))) ))
	 	(bg 0)
	 	(n 0.0)
	 	(rainlength 0.0)
	 	(angle 0 )
	 	(delta-angle (/ pi 20.0) )
     		(mx 0) 
     		(my 0) 
     		(nx 0) 
     		(ny 0)
     		(i 0)
     		(opac  (* (rnd ) 100.0) )
     		(pen-size  (* (rnd ) 3.0) )
	 	)
	 (gimp-image-undo-group-start image)
	 (gimp-context-push)
	 (gimp-progress-init "Start" -1)
	 (set! bg (car (gimp-image-get-active-layer image)))
	 (gimp-drawable-set-visible bg TRUE)
	 (gimp-palette-set-foreground color)
	 
	 (gimp-context-set-paint-mode NORMAL-MODE)
	 (gimp-context-set-brush "Circle (01)")
	 
	 (gimp-context-set-foreground '(0 0 0))

	 
	 (while (< n npoints) 
	   
	   (gimp-progress-update (/ n npoints) )
	   (set! rainlength (random-float-between minlength maxlength))
	   (set! angle (- (/ pi 2.0)  (random-float-between (* -1.0 delta-angle ) delta-angle ) ))
           (set! mx  (random-float-between x1 x2) )
	   (set! my  (random-float-between y1 y2) )
	   (set! nx  (+ mx (* (cos angle) rainlength)))
	   (set! ny  (+ my (* (sin angle) rainlength)))
	   (set! i 0)
	   (while (< i 10)
	   	 (set! mx (lerp 0.5 nx mx))
	   	 (set! my (lerp 0.5 ny my))
	  	 (gimp-context-set-opacity opac )
	  	 (gimp-context-set-brush-size pen-size)
	  	 (gimp-paintbrush-default  bg 4 (list->vector (list mx my nx ny)))
	  	 
	  	 (set! pen-size (* pen-size 0.8) )
	  	 (set! opac (* opac 0.8) )
	  	 (set! i (+ i 1))
	   )
	  
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
 SF-ADJUSTMENT "Min Length" (list 10  1 1000 1 10 1 SF-SLIDER)
 SF-ADJUSTMENT "Max Length" (list 100 1 1000 1 10 1 SF-SLIDER)
 SF-COLOR      "Color"   "black"
)


(script-fu-menu-register "script-fu-rain01"
                         "<Toolbox>/Xtns/Languages/Script-Fu/Yokofakun")
