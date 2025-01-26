
;; binary map

( = (binary-map-add $const (:: $x Nil)) (::(+ $x $const) Nil))

( = (binary-map-add $const (:: $x $xs)) 
    (:: (+ $x $const) (binary-map-add $const $xs))
)

!(binary-map-add 14 (:: 1 (:: 3 Nil)))
!(+ 12 (superpose (5 9)))
