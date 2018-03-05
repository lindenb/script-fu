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


