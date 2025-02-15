; find the size of the Exprestion 
(: size (-> Expression Number))

(= (size $atoms)
    (
    ;base condition
    if (== $atoms ())
        0
        ( let $tail (cdr-atom $atoms) ; get the tail of the atom
        (+ 1 (size $tail))
        ) ; recursive call and increment the value by one   
    )
)

; check the length of the Expression of (1 2 3 4) the answer should be 4
!(size (1 2 3 4))

; write a function that merge the sumation of two Expression to one Expression
; example (1 2 3) and (2 3 4) to (3 5 7)
(: mergeSum (-> Expression Expression Expression))
;base case
(= (mergeSum () ())
    ()
)
( = (mergeSum $atoms1 $atoms2)
    (
        ;find the length of the two Expression
        let* (
            ($atomOneSize (size $atoms1))
            ($atomTwoSize (size $atoms2))
        )
        (; check if the length is equal or not 
        if (== $atomOneSize $atomTwoSize)
            (let* (
                ($head1 (car-atom $atoms1))
                ($head2 (car-atom $atoms2))
                ($tail1 (cdr-atom $atoms1))
                ($tail2 (cdr-atom $atoms2))
                ($sum (+ $head1 $head2))
                ($mergedAtoms (mergeSum $tail1 $tail2)) ; recursive call
            )
            (cons-atom $sum $mergedAtoms)
            )
            (The size of the two atoms are not equal))
    )
)

;check the merge function atoms1 = (1 2 3) and atoms2 = (2 3 4) the answer should be (3 5 7)
!(mergeSum (1 2 3) (2 3 4))
