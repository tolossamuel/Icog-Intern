!(register-module! /home/samuel/Documents/Icog-Intern/MettaLecture3) 
!(import! &self MettaLecture3:non-deterministic)

;test function findRemove
!("===================== test function findRemove ================")
!(findRemove (1 2 3 4 5) 5)
!(findRemove (1 2 3 4 7) 8)
!(findRemove () 2)
!(assertEqual (findRemove (1 2 3 4 5) 5) (4 3 2 1))
!(assertEqual (findRemove (1 2 3 4) 9) (4 3 2 1))
!(assertEqual (findRemove () 5) ())

;test function findReplace
!("===================== test function findReplace ================")
!(findReplace (1 2 3 4 5) 5 10)
!(findReplace (1 2 3 4 7) 8 9)
!(findReplace () 2 7)
!(assertEqual (findReplace (1 2 3 4 5) 5 10) (10 4 3 2 1))
!(assertEqual (findReplace (1 2 3 4) 9 11) (4 3 2 1))
!(assertEqual (findReplace () 5 3) ())
!(assertEqual (findReplace (1 2 3 3 3) 3 4) (4 4 4 2 1))

;test function isMember
!("===================== test function isMember ================")
!(isMember (1 2 3 4 5) 5)
!(isMember (1 2 3 4 7) 8)
!(isMember () 2)
!(assertEqual (isMember (1 2 3 4 5) 5) True)
!(assertEqual (isMember (1 2 3 4) 9) False)
!(assertEqual (isMember () 5) False)