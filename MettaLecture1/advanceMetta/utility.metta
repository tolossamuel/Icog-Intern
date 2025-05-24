
 ;importance management
 ; get the size of atom space

(: size (-> List Number))
( = (size $list)
    (if (== $list ())
        0
        (let* (
                ($left (cdr-atom $list))
            )
        (+ 1 (size $left)))))
(: checkExistance (-> Atom Expression Bool))
( = (checkExistance $pattern $list)
    (if (== $list ())
        False
        (
            let* (
                ($atom (car-atom $list)))
            (if (== $pattern $atom)
                True
                (let* (

                        ($left (cdr-atom $list)))
                    (checkExistance $pattern $left))))))

(: remove-duplicate (-> Expression Expression))
( = (remove-duplicate $list)
    (if (== $list ())
        ()
        (let* (
                ($atom (car-atom $list))
                ($left (cdr-atom $list))
                ($checker (checkExistance $atom $left))
            )
        (if (== $checker True)
            (remove-duplicate $left)
            (
                let* (
                    ($right (remove-duplicate $left))
                )
            (collapse ($atom) $right))))))
! (remove-duplicate (1 2 1 3 4))