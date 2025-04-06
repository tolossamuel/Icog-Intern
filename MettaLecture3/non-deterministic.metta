
;function findRemove
; parameter: list and atom
; returns: list

(: findRemove (-> Expression Atom Expression))
(= (findRemove $list $old)
    (collapse(
            let $atom (superpose $list)
            (if (== $atom $old) ;check if atom is the same as old
            (empty) ; if atom is the same as old, return empty
            $atom ;else return atom
            )
        )
    )
)

; function: findReplace
; parameter: list, atom and new atom
; returns: list

(: findReplace (-> Expression Atom Atom Expression))
(= (findReplace $list $old $new)
    (collapse (
        let $atom (superpose $list)
        (if (== $atom $old) ;check if atom is the same as old
            $new ; replace old with new
            $atom ; return atom
        )
    ))
)

;function : isMember
;parameter: List atom
;returns: boolean

(: isMember (-> Expression Atom boolean))
(= (isMember $list $atom)
    (let $checker (
        collapse (let $val (superpose $list)
        (if (== $val $atom) ; check if atom is in the list
            $val ; if atom is in the list, return it
            (empty) ; else return empty
        ))
    )
    (if (== $checker ()) ; check if checker is empty
        False ; if empty, return false
        True ; else return true
    )
    )
)
