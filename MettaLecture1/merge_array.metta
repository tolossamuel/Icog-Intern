;; write function to merge array
(: append (-> List List List))
(= (append Nil $ys) $ys)
( = (append (:: $x $xs) $ys) (:: $x (append $xs $ys)))

!(append (:: A (:: B (:: C Nil))) (:: D (:: E Nil)))