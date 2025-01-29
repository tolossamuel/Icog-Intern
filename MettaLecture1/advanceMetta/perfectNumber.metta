 ;  perfect number is a positive integer that is equal to the sum of its positive proper divisors,

( = (divider $n $x)
    (
        if (<= $x (/ $n 2))
        (
            if (== (% $n $x) 0)
            (+ $x (divider $n (+ $x 1)))
            (divider $n (+ $x 1))
        )
    0
)
)

( = (perfect $n)
    (
        if (and (> $n 1) (== $n (divider $n 1)))
        $n
        (empty)
    )
)
( = (perfect $n)
    (
        if (> $n 0)
        (perfect (- $n 1))
        (empty)
    )
)

! (perfect 28)
