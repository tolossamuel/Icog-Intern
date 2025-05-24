
(= (sum $list)
    (if (== $list ())
        0
        (let* (
            ($head (car-atom $list))
            ($tail (cdr-atom $list))
            )
            (+ $head (sum $tail))
        ))
)
!(sum (1 2 3 4 5 6 7 8 1 2 3 4 5 6 7 8))