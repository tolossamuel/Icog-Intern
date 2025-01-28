
(= (backtracking $n) (
    if ( > $n 1)
        (+ (backtracking (- $n 1)) (backtracking (- $n 2)))
        $n
))
!(backtracking 5)


( = (checking $n $i)
(
    if ( > $n 0)
        (+ (backtracking $i) (checking (- $n 1) $i))
        0
)
)
!(checking 5 5)