hello
!(hello world)
!(+ 1 2)
(= (n) (hello world))
!(n)
( = (n A) (Input A is accepted))
!(n A)
!(n B)

( = (doublicate $a) ($a $a) )
!(doublicate 1)
!(doublicate 2)
( = (swap $a $b) ($b $a))
!(swap 1 2)
( = (cdr (cons $x $xs)) ($xs))
!(cdr (cons A (cons B null)))

( = (brother mike) tom)
( = (brother tom) mike)
!((brother $x) is brother of $x)

(= (sqr $x ) (* $x $x))
!(sqr 12)

( = (car (cons $x $xs)) ($x))
( = (driver (cons $x $xs)) (car $xs))
!(driver (cons A (cons B nail)))


( = (length ()) 0)
( = (length (:: $x $xs))
    (+ 1 (length $xs))
)
! (length (:: A (:: B (:: C ()))))
// sumation 10

( = (sum $x)
    (if (> $x 0)
        (+ $x (sum (- $x 1)))
        0
        
    )
   
)
! (sum 3)
