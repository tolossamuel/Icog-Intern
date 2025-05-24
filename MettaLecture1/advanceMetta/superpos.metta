!(bind! &atomBin (new-space))
!(bind! &attentionalFocus (new-space))
!(add-atom &atomBin (1 (A B C)))
!(add-atom &atomBin (2 (A B C)))
!(add-atom &atomBin (3 (A B C)))
!(add-atom &atomBin (4 (A B C)))
!(add-atom &attentionalFocus (3 16))
!(add-atom &attentionalFocus (4 10))
!(add-atom &attentionalFocus (1 11))
!(add-atom &attentionalFocus (2 9)) 
!(add-atom &attentionalFocus (5 8))
!(add-atom &attentionalFocus (6 7))
!(add-atom &attentionalFocus (7 6))   
(= (getSTI $atom)
    (let* (
        ($atoms (match &attentionalFocus ($atom $x) $x))
    )
        $atoms
    )
)
!(getSTI 3)
(= (getSize $binNumber)
    (let* (
        ($atoms (match &atomBin ($binNumber $x) $x))
    )
        (size-atom $atoms)
    )
)
(: getAfMaxSTI (-> Number))
(= (getAfMaxSTI)
    (let* (
        ($atoms (1 2 3 4 5 6 7))
        ($maxSti (collapse (getAfMaxSTIHelper $atoms )))
        ($ans (max-atom $maxSti))
    )
    $ans
        
    )
)
(= (getAfMaxSTIHelper $atoms)
    (let* (
        ($vals (getSTI (superpose $atoms)))
    )
    $vals
    )
)
; !(max-atom ((12 3) (19 3)))


; (: filterLinksInAF (-> List List))
(= (filterLinksInAF $incoming_set $prev)
    (let $val (collapse (helper $incoming_set $prev))
    $val)
)
(= (check $num)
    (if (not False)
        True
        False
    )
)
(= (helper $incoming_set $prev)
    (let* (
        ($val (superpose $incoming_set))
        ($ch ($prev $val))

    )
    (if $ch
    $val
    (empty)
    )
    
    )
)

!(filterLinksInAF (1 2 3 4 5) check)