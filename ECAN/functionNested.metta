!(bind! &my-space (new-space))
!(bind! &my-sti (new-space))
!(add-atom &my-sti (A 2))
!(add-atom &my-sti (B 3))
!(add-atom &my-sti (C 4))
!(add-atom &my-sti (D 5))
!(add-atom &my-sti (E 1))
!(add-atom &my-space A)
!(add-atom &my-space B)
!(add-atom &my-space C)
!(add-atom &my-space D)
!(add-atom &my-space E)


(: getAtoms (-> symbol))
(= (getAtoms)
(collapse (get-atoms &my-space)))
(: getSTI (-> atom Number))
(= (getSTI $atom)
    (let*(
        ($val (collapse (match &my-sti ($atom $x) $x)))
        )
    (if (== $val ())
    0
    $val))
)

(= (getMaxSTI $atoms)
    (if (== $atoms ())
        0
        (let* (
            ($top (car-atom $atoms))
            ($rest (cdr-atom $atoms))
            )
            (if (== $rest ())
                $top
                (let* (
                    ($secondTop (car-atom $rest))
                    ($tail (cdr-atom $rest))
                    ($STItop (getSTI $top))
                    ($topVal (car-atom $STItop))
                    ($STIsecondTop (getSTI $secondTop))
                    ($secondTopVal (car-atom $STIsecondTop))
                    )
                    (if (> $topVal $secondTopVal)
                        (getMaxSTI (cons-atom $top $tail))
                        (getMaxSTI $rest)
                    )
                )
            )
        )
    )
)
!(getAtoms)
!(getSTI A)
!(getMaxSTI (getAtoms))