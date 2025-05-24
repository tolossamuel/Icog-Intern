! (bind! &space (new-space))
! (add-atom &space (startingFundsSTI 100000))
! (add-atom &space (startingFundsLTI 100000))
! (add-atom &space (fundsSTI 100000))
! (add-atom &space (fundsLTI 100000))
! (add-atom &space (stiFundsBuffer 10000))
! (add-atom &space (ltiFundsBuffer 10000))
! (add-atom &space (targetLTI  10000))
! (add-atom &space (targetSTI  10000))
! (add-atom &space (STIAtomWage  10))
! (add-atom &space (LTIAtomWage  10))
! (add-atom &space (maxAFSize  10))

 ;calculate max of two numbers

(: max (-> Number Number Number))
(= (max $x $y )
    (if (> $x $y)
        $x
        $y))
 ; set STI value for atom
( : calculateSTIWage (Number ))