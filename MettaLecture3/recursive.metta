
;function: repeat
;description: repeat a give atom for given number 
;parameter: Atom Number
;return Expression
(: repeat (-> Atom Number Expression) )
(= (repeat $atom $number)
    (if (<= $number 0)
        ()
        (let $rec (repeat $atom (- $number 1))
        (cons-atom $atom $rec)
        )
    )
)

;function zip 
;discription map two list
;parameter: List List
;return Expression

(: zip (-> Expression Expression Expression))
(= (zip $listOne $listTwo)
    (let* (
        ($lenOne (size-atom $listOne))
        ($lenTwo (size-atom $listTwo))
        )
        (if (== $lenOne $lenTwo)
            (if (or (== $listOne ()) (== $listTwo ()))
                ()
                (let* (
                    ($headOne (car-atom $listOne))
                    ($headTwo (car-atom $listTwo))
                    ($tailOne (cdr-atom $listOne))
                    ($tailTwo (cdr-atom $listTwo))
                    ($rec (zip $tailOne $tailTwo))
                    )
                    (cons-atom ($headOne $headTwo) $rec )
                )
            )
            ()
        )
            
    )
)

;function: zipWith
;description: map two list with a function
;parameter: List List Function
;return Expression
(: zipWith (-> Expression Expression (-> Number Number Number) Expression))
(= (zipWith $listOne $listTwo $function)
    (let* (
        ($lenOne (size-atom $listOne))
        ($lenTwo (size-atom $listTwo))
        )
        (if (== $lenOne $lenTwo)
            (if (or (== $listOne ()) (== $listTwo ()))
                ()
                (let* (
                    ($headOne (car-atom $listOne))
                    ($headTwo (car-atom $listTwo))
                    ($tailOne (cdr-atom $listOne))
                    ($tailTwo (cdr-atom $listTwo))
                    ($rec (zipWith $tailOne $tailTwo $function))
                    )
                    (cons-atom ($function $headOne $headTwo) $rec )
                )
            )
            ()
        )
            
    )
)
;function: gcd
;description: find the greatest common divisor of two numbers
;parameter: Number Number
;return Number
(: gcd (-> Number Number Number))
(= (gcd $a $b)
    (if (== $b 0)
        $a
        (gcd $b (% $a $b))
    )
)

;function: generate
;description: generate a list of numbers from start to end
;parameter: Number Number
;return list
(: generate (-> Number Number Expression))
(= (generate $start $end)
    (if (<= $start $end)
        (let* (
            ($rec (generate (+ $start 1) $end))
            )
            (cons-atom $start $rec)
        )
        ()
    )
)
