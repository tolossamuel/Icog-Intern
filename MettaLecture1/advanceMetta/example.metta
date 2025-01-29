 ; convert (a b c) to (Cons a (Cons b (Cons c Nil)))
(: makelist (-> Atom (List $t)))
(= (makelist $x)
    (if (== () $x) Nil (let $cdr (cdr-atom $x)
            (Cons (car-atom $x) (makelist $cdr)))
    )
)
! (makelist (1 3 3))
(= (var)
    (
        let
        $x 4
        (+ $x 3)
    )
)
! (var)