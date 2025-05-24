!(bind! &add (new-space))
!(add-atom &add (val 0))

(= (sum $list)
    (let $ans (collapse (let* (
        ($atom (superpose $list))
        ($val (match &add (val $x) $x))
        ($_ (remove-atom &add (val $val)))
        ($new (+ $val $atom))
        ($_ (add-atom &add (val $new)))
        )
        $new

        )
    )
    (let* (
        ($_ (remove-atom &add (val $x)))
        ($_ (add-atom &add (val 0)))
        )
        (car-atom $ans)
    )
    )
)

!(sum (1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8))
