
; binary map Implement a binary map function that takes a binary function f (a function with
; two arguments), a constant value, and a list, and applies f to each element of the
; list and the constant.

( = (binary-map-add $const Nil) (Nil) ) ; base case if the list is empty return empty
( = (binary-map-add $const (:: $x $xs)) 
    (:: (+ $x $const) (binary-map-add $const $xs)) ; recursive relation take every element of the list and add the constant
)

!(binary-map-add 14 (:: 1 (:: 3 Nil))) ; answer must be (:: 15 (:: 17 Nil))


; method 2
; using superpose function
; superpose work sumation from right to left and return value also from right to left
!(+ 12 (superpose (1 5))) ; answer must be (17 13)
