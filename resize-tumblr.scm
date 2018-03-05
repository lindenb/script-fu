;; #######################################################################################################

(define
	(script-fu-resize-tumblr01 image)
	 (let* (
	 	 (SIZE 1280)
	 	 (W (car (gimp-image-width image)) )
	 	 (H (car (gimp-image-height image)) )
	 	 (W2 (if (< W H) (* (/ W H) SIZE) SIZE))
	 	 (H2 (if (< W H) SIZE (* (/ H W) SIZE )))
	 	)
	 (gimp-image-undo-group-start image)
	 (gimp-image-flatten image)
	 (gimp-image-scale image W2 H2)
	 (gimp-image-resize image SIZE SIZE (/ (- SIZE W2) 2.0) (/ (- SIZE H2) 2.0) )
	 (gimp-image-flatten image)
	 (gimp-image-undo-group-end image)
	 (gimp-displays-flush)
	 )
)

;; #######################################################################################################
(script-fu-register "script-fu-resize-tumblr01"
  _"ResizeTumblr..."
  "ResizeTumblr"
  "Pierre Lindenbaum"
  "(c) Pierre Lindenbaum"
  "2018"
  ""
 SF-IMAGE      "Image"     0
)


(script-fu-menu-register "script-fu-resize-tumblr01"
                         "<Toolbox>/Xtns/Languages/Script-Fu/Yokofakun")
