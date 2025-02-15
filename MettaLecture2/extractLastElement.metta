;find the last element of the List

( : extractLastElement (-> Expression Atom))
(= (extractLastElement (:: $x $xs))
    (if (== $xs Nil)
        $x
        (extractLastElement $xs)
    )
)
;check for (:: 12 (:: 13 (:: 14 (:: 15 empty))))
;!(extractLastElement (:: 12 (:: 13 (:: 14 (:: 15 Nil)))))