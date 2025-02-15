; constract Expression also Print every stage of the recursion functions
;example
; (1 2 3 4)
;output is 
; 1
; 2
; 3
; 4
; (4)
; (3 4)
; (2 3 4)
; (1 2 3 4)
(: constractExpression (-> Expression empty))
;base case
(= (constractExpression ()) ())
(= (constractExpression $atoms)
    (
        let* (
            ($head (car-atom $atoms))
            ($tail (cdr-atom $atoms))
            )
        (!(println! $head) ; print the head of the atom
        (constractExpression $tail) ; recursive call
        !(println! $atoms) ; print the tail of the atom
        )
    )
)
