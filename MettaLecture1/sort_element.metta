;; write function that sort the array
(: sort_element (-> List List))
(= (sort_element Nil) Nil)
(= (sort_element (:: $x Nil)) (:: $x Nil))
(= (sort_element (:: $x (:: $y $xs)))
   (if (< $x $y)
       (:: $x  (sort_element (:: $y $xs)))
       (:: $y (sort_element (:: $x $xs)))))
;; recursive call
( = (sort_all $x $n)
    (if (> $n 0)
        (sort_all (sort_element $x) (- $n 1))
        $x
    )
)
!(sort_all (:: 5 (:: 6 (:: 2 Nil))) 3)