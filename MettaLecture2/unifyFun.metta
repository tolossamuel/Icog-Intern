
!(bind! my-space (new-space)) ; create a new space

;add patter to the space
!(add! my-space (A 12 34))
!(add! my-space (B 1 30))
!(add! my-space (C 10 33))

;match patter using unify

!(unify &my-space (A $x $y) (* $x $y) (Not Fuound))

; check unexpected result
!(unify &my-space (D $x $y) (* $x $y) (Not Found))



