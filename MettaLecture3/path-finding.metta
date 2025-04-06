!(bind! &visited (new-space))
(AddisAbaba 100 Adama)
(AddisAbaba 275 Hawassa)
(AddisAbaba 565 BahirDar)
(Harar 300 Mekelle)
(Adama 350 DireDawa)
(DireDawa 75 Harar)
(Harar 480 Dessie)
(Dessie 380 Mekelle)
(Mekelle 440 Gonder)

;function pathFind
;parameter start and end city atom Number
;returns: list
(: pathFind (-> Atom Atom Expression Number Expression))
(= (pathFind $start $end $path $dis)
    (match &self ($start $val $x)
        (if (== $x $end)
            (let* (
                ($paths (union-atom $path ($x)))
                ($totalPath (+ $val $dis))
            )
                (union-atom ($paths) (($totalPath))))
            (let $checker (collapse (match &self $x $x))
                (if (== $checker ())
                    (let* (
                        ($t (add-atom &visited $x))

                        ($newPath (union-atom  $path ($x)))
                        )
                        (pathFind $x $end $newPath (+ $dis $val))
                    )
                    ()
                )
            )
        )
    )
)

;function shortestPath
;parameter: Atom Atom 
;return Expression

(: shortestPath (-> Atom Atom Expression))
(= (shortestPath $start $end)
    (let* (
        ($paths (collapse (pathFind $start $end ($start) 0)))
        ($dis (collapse (let* (
                                ($path (superpose $paths))
                                (($x $y) $path)
                            )
                            (car-atom $y)
                        )
                )
        )
        ($minDis (if (== $dis ()) 0 (min-atom $dis)))
    )
    (let* (
        ($minPath (let* (
                            ($path (superpose $paths))
                            (($x $y) $path)
                            ($num (car-atom $y))
                        )
                        (if (<= $num $minDis)
                            $path
                            (empty)
                        )
                    )
        )
    )
    $minPath
    )
    )
)
