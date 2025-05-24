(: GroupSize Number)
(= (GroupSize) 8)

(: GroupNum Number)
(= (GroupNum) 12)
; Recursive helper to calculate the group index
(= (findGroup $imp $sum $i)
   (if (or (>= $sum $imp) (>= $i (GroupNum)))
      $i ; Return the group index
      (findGroup $imp (+ $sum (pow 2 $i)) (+ $i 1))
   )
)
;a function to find the ceil
(: ceil (-> Number Number))
(= (ceil $x)
   (let $int_part (truncate $x)
      (if(== $x $int_part)
         $int_part ; $x is already an integer
         (+ $int_part 1)
      )
   )
) ; Otherwise, round up
; Helper function to truncate a number (remove fractional part)
(: truncate (-> Number Number))
(= (truncate $x)
   (truncateHelper $x 0)
)
; Recursive helper to find the integer part of $x
(: truncateHelper (-> Number Number Number)) 
(= (truncateHelper $x $acc)
   (if (< $x (+ $acc 1))
       $acc ; The accumulated integer part
       (truncateHelper $x (+ $acc 1))
   )
)


;function to find power of a number
(: pow (-> Number Number Number))    
(= (pow $base $exp)
   (if(<= $exp 0)
      1 ; Any number to the power of 0 is 1
      (* $base (pow $base (- $exp 1)))
   )
) ; Recursive multiplication

(: ImportanceIndexSize Number)
(= (ImportanceIndexSize) 104)

(: importanceBin (-> Number Number))
; Function to calculate the bin for a given importance value
(= (importanceBin $impo)
   (let $impo_int (truncate $impo) ; Ensure $impo is treated as an integer
      (if (< $impo_int 0)
          0 ; Importance is less than 0
          (if (< $impo_int (* 2 (GroupSize)))
              $impo_int ; Importance is within the first 2 groups
              (let $imp (ceil (/ (* (- $impo_int (GroupSize)) 1.0) (GroupSize))) ; to prevent the division to be round to down multiply the number with 1.0
                 (let $i (findGroup $imp 0 0) ; Find the group index
                    (let $ad (- (GroupSize) (ceil (/ (* $impo_int 1.0) (pow 2 (- $i 1))))) ; to prevent the division to be round to down multiply the number with 1.0
                       (let $bin (- (* $i (GroupSize)) $ad)
                          (if (> $bin (ImportanceIndexSize))
                              (ImportanceIndexSize)
                              $bin
                           )
                        )
                     )
                  )
               )
         )
      )
   )
)
