
;function: permutation
;description: Permutation of a list 
;parameter: list number
;returns: list

(: permutation (-> Expression Number Expression))
(= (permutation $list $number)
    (let $len (size-atom $list)
        (if (or (== $number 0) (> $len 5))
        ()
        (let* (
            ($atom (permutationHelper $list $number))
            ($removeUsed (findRemove $list $atom))
            ($removedSized (- $len (size-atom $removeUsed)))
            ($rec (permutation $removeUsed (- $number $removedSized)))
            ($per (cons-atom $atom $rec))  
        )
        $per
        )
        )
    )
)

;function: permutationHelper
;description: Helper function for permutation
;parameter: list number
;returns: list
(: permutationHelper (-> Expression Number Expression))
(= (permutationHelper $list $number)
    (let $atom (superpose $list)
    $atom
    )
)

