

;function that append element to the list at the end
; example (:: 1 (:: 3 Nil)) append 4 (:: 1 (:: 3 (:: 4 Nil)))

(: append (-> Expression Atom Expression))

(= (append (:: $x $xs) $atom)
    (
        if (== $xs Nil)
            (:: $x (:: $atom Nil))
            (:: $x (append $xs $atom))
    )
)
;check for (:: 1 (:: 3 Nil)) append 4 (:: 1 (:: 3 (:: 4 Nil)))
!(append (:: 1 (:: 3 Nil)) 4)