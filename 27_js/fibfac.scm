#lang racket
; Renggeng Zheng
; SoftDev
; K27 -- Scheme, Javascript, and functional programming
; 2022-02-04
; time spent: 30 min
(define fib
  (lambda (n)
    (if (= n 0) 0 (+ n (fib(- n 1)))
    )
  )
)
(fib 0)
(fib 1)
(fib 2)

(define factorial
  (lambda (n)
    (if (<= n 1) 1 (* n (factorial (- n 1))))
  )
)
(factorial 0)
(factorial 1)
(factorial 2)
