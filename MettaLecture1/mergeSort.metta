;; slice element in to two parts to merge sort
(= (slicing $left $right $index Nil) Nil)
( = (slicing $left $right $index (:: $x $xs))
(
    if (and (>= $index $left) (< $index $right))
        (:: $x (slicing $left $right (+ $index 1) $xs))
        (slicing $left $right (+ $index 1) $xs)
    
)
)

; merge two sorted list
(= (merge_sort Nil Nil) Nil)
(= (merge_sort Nil (:: $y $ys)) (:: $y $ys))
(= (merge_sort (:: $x $xs) Nil) (:: $x $xs))
( = (merge_sort (:: $x $xs) (:: $y $ys))
(
    if (> $x $y)
        (:: $y (merge_sort (:: $x $xs) $ys))
        (:: $x (merge_sort $xs (:: $y $ys)))
   
)

)

( = (divide $length Nil) Nil)
(= (divide $length (:: $x $xs))
(
    if ( > $length 1)
        (
            if (== (% $length 2) 0)
                (merge_sort (divide (/ $length 2) (slicing 0 (/ $length 2) 0 (:: $x $xs))) (divide (/ $length 2) (slicing (/ $length 2) $length 0 (:: $x $xs))))
                (merge_sort (divide (/ $length 2) (slicing 0 (/ $length 2) 0 (:: $x $xs))) (divide (+ (/ $length 2) 1) (slicing (/ $length 2) $length 0 (:: $x $xs))))
                
                
        )
        (:: $x Nil)
)
)
!( divide 3 (:: 1 (:: 0 ( :: 2 Nil))))
!( divide 6 (:: 4 (:: 6 (:: 2 (:: 10 ( :: 2 ( :: 1 Nil)))))))


