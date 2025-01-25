;; Write function to calculate sum of all natural numbers below a given number N that are multiple of 3 or 5

;; write sum-multiple function 
( = (sum-multiple $n) 
    (
        if (> $n 2)
            (if ( or (== (% $n 3) 0) (== (% $n 5) 0)) ;; check if the mod of number by 3 or by 5 is 0 calculate samation
                (+ $n  (sum-multiple (- $n 1)))
                (sum-multiple (- $n 1))  ;; if the mod of number by 3 or 5 is not 0 just minimize the number by 1
            )
            0 ;; if the number is less than 3 that mean no number of mod by 3 or 5 gives 0 so return 0
    )
)
!(sum-multiple 9) ;; calculate for 9 answer must be 23
