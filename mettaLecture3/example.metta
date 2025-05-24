
; superpose

(= (sqr $x) (* $x $x))
(= (map $list $function)
    ($function (superpose $list))
)

!(map (1 2 3 4 5) sqr)