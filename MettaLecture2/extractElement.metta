;exctract element from list
;example (:: 1 (:: 3 (:: 4 Nil))) to (1 3 4)

(: extractElement (-> Expression Expression))

(= (extractElement (:: $x $xs))
    (if (== $xs Nil)
        ($x)
        (let $recursive (extractElement $xs)
            (cons-atom $x $recursive)
        )
    )
)

;check for (:: 1 (:: 3 (:: 4 Nil))) to (1 3 4)

!(extractElement (:: 1 (:: 3 (:: 4 Nil))))