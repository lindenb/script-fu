(define pi  (acos -1))
(define pi2  (* 2.0 pi))
(define RAND_MAX 1000000)
;;
;; returns number between 0.0 and 1.0
;; 
(define rnd  (lambda () (/ (remainder (random-next) RAND_MAX)  RAND_MAX ) ))
;;
;; returns boolean true or false
;; 
(define random-boolean  (lambda () (if (< (rnd) 0.5) #t #f)))
;;
;; returns number -1 or 1
;; 
(define random-sign  (lambda () (if (random-boolean) -1 1)))
;;
;; perimeter of a circle
;;
(define circle-perimeter  (lambda (r) (* pi2 r) ) )


(define (my-select-sketchy-circle image selmode cx cy r) 
	(let*
		(
		(angle-start (* (rnd)  pi2))
		(delta-angle (* (rnd)  pi2))
		(perimeter (* r  pi2))
		(angle 0)
		(segs (list )))
		)
	(set! segs (make-vector 0))

	(gimp-image-select-polygon image selmode num-segs segs)
	)
)
 

(let*
		(
		(cx 0)
		(cy 0)
		(radius 100.0)
		(precision 5.0)
		(nsteps (max 3 (floor (/ (circle-perimeter radius) precision ) ) ) )
		(angle-per-step (/pi2 nsteps))
		(angle 0)
		(segs  (list) ))
		(n 0)
		)
		
  (while (< n nsteps) 
  (let * 
  	(
  	(r2 (max 0 radius ))
  	) 
  	
  ) 
  
  (set! n (+ n 1))
  )
 (display "done\n")
 )

