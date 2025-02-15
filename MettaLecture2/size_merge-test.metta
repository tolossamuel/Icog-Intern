!(register-module! /home/samuel/Documents/Icog-Intern/MettaLecture2)
!(import! &self MettaLecture2:size_merge)
; !(import! MettaLecture2:task1)


; test the find size function 
!(assertEqual (size (1 2 3 4)) 4)
!(assertEqual (size ()) 0)

;test the merge function of two atoms

!(assertEqual (mergeSum (1 2 3) (2 3 4)) (3 5 7))
!(assertEqual (mergeSum (1 2 3) (2 3 4 5)) (The size of the two atoms are not equal))
!(assertEqual (mergeSum () ()) ())
!("test passed")
;traling on metta
;tr