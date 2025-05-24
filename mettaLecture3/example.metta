
; superpose

(= (sqr $x) (* $x $x))
(= (map $list $function)
    ($function (superpose $list))
)

!(map (1 2 3 4 5) sqr)


(= (isEven $x) (if (== (% $x 2) 0) $x (empty)))
(= (filter $list $predicate)
    (collapse ($predicate (superpose $list))))

!(filter (1 2 3 4 5) isEven)