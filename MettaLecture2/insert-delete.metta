;===============================================
; functions that append elements to the end of the list
(: append (-> Atom Expression Expression))
;base case 
(= (append $atom ())
    ($atom)
)
(= (append $atom $exp)
    (
        let* (
            ($head (car-atom $exp))
            ($tail (cdr-atom $exp))
            ($recursive (append $atom $tail))
        )
        (cons-atom $head $recursive)

    )
)
;check the append function with atom = 7 and exp = (4 5 6) the answer should be (4 5 6 7)
!(append 7 (4 5 6))

;===============================================
;function that append element to the start of the Expression
(: appendStart (-> Atom Expression Expression))
(= (appendStart $atom $exp)
    (
        cons-atom $atom $exp
    )
)
;check the appendStart function with atom = 7 and exp = (4 5 6) the answer should be (7 4 5 6)
!(appendStart 7 (4 5 6))

;===============================================
;function that insert element to the given index of the Expression
( : insert (-> Atom Number Expression Expression))
;base case
(= (insert $atom $index ())
    (
        if (== $index 0)
            ($atom) ; we want to append element in last
            () ; index is out of bound
    )
)

(= (insert $atom $index $exp)
    (if (== $exp ())
        (empty)
        (if (== $index 0)
                (cons-atom $atom $exp)
                (
                    let* (
                        ($head (car-atom $exp))
                        ($tail (cdr-atom $exp))
                        ($recursive (insert $atom (- $index 1) $tail)) ; recursive call
                    )
                    (cons-atom $head $recursive)
                )
        )
    )
)
;check the insert function with atom = 7 index = 2 and exp = (4 5 6) the answer should be (4 5 7 6)
!(insert 7 2 (4 5 6))
;check the insert function with atom = 7 index = 0 and exp = (4 5 6) the answer should be (7 4 5 6)
!(insert 7 0 (4 5 6))
;check the insert function with atom = 7 index = 3 and exp = (4 5 6) the answer should be (4 5 6 7)
!(insert 7 3 (4 5 6))

;===============================================
;delete element from the start
(: deleteStart (-> Expression Expression))
(= (deleteStart ())
    ()
)
(= (deleteStart $exp)
    (
       cdr-atom $exp
    )
)
;check the deleteStart function with exp = (4 5 6) the answer should be (5 6)
!(deleteStart (4 5 6))
; check the deleteStart function with exp = () the answer should be ()
!(deleteStart ())

;===============================================
;delete element from the end
(: deleteEnd (-> Expression Expression))
(= (deleteEnd ())
    ()
)
(= (deleteEnd $exp)
    (let* (
        ($head (car-atom $exp)) ;get the head of the atoms
        ($tail (cdr-atom $exp)) ; get the tail of the atoms
        )
        (if (== $tail ()) ; if the tail is empty then return empty list
            ()
            (let $recursive (deleteEnd $tail); recursive call
                (cons-atom $head $recursive)
            )
        )
            
    )
)
;check the deleteEnd function with exp = (4 5 6) the answer should be (4 5)
!(deleteEnd (4 5 6))
; check the deleteEnd function with exp = () the answer should be ()
!(deleteEnd ())

;===============================================
;function that delete element from the give index
(: delete (-> Number Expression Expression))
(= (delete $index ())
    ()
)
( = (delete $index $exp)
    (
        let* (
            ($head (car-atom $exp))
            ($tail (cdr-atom $exp))
        )
        (if (== $index 0)
            $tail ; if the index is 0 jump the head of the atom
            (let $recursive (delete (- $index 1) $tail) ; recursive call
            (cons-atom $head $recursive)
            )
        )
    )
)
;check the delete function with index = 2 and exp = (4 5 6) the answer should be (4 5)
!(delete 2 (4 5 6))
;check the delete function with index = 0 and exp = (4 5 6) the answer should be (5 6)
!(delete 0 (4 5 6))
;check the delete function with index = 3 and exp = (4 5) the answer should be (4 5 6)
!(delete 3 (4 5 6))
; check the delete function with index = 1 and exp = (4 5 6) the answer should be (4 6)
!(delete 1 (4 5 6))