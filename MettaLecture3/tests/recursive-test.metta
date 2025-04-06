!(register-module! /home/samuel/Documents/Icog-Intern/MettaLecture3) 
!(import! &self MettaLecture3:recursive)

;test function repeat
!("============== test for function repeat ======================")
!(repeat 5 6)
!(assertEqual (repeat 5 6) (5 5 5 5 5 5)) ;check if the function returns the correct value
!(assertEqual (repeat 0 0) ()) ;check if the function returns the correct value
!(assertEqual (repeat 0 5) (0 0 0 0 0)) ;check if the function returns the correct value

;test function zip
!("==================== test for function zip ==================")
!(zip (1 2 3 4 5) (6 7 8 9 10))
!(zip (1) (2))
!(assertEqual (zip (1 2 3 4) (5 6 7 8)) ((1 5) (2 6) (3 7) (4 8)))
!(assertEqual (zip (1 2 3) (1 5)) ())

;test function zipWith
!("==================== test for function zipWith ===============")
!(zipWith (1 2 3 4) (5 6 7 8) gcd)
!(assertEqual (zipWith (1 2 3 4) (5 6 7 8) gcd) (1 2 1 4))
!(assertEqual (zipWith (1 2 3) (1 5) gcd) ())

;test function generate
!("===================== test function generate ========================")
!(generate 1 5)
!(generate 3 10)
!(assertEqual (generate 2 5) (2 3 4 5))
!(assertEqual (generate 5 2) ())
