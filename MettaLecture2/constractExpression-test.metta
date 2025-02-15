!(register-module! /home/samuel/Documents/Icog-Intern/MettaLecture2)
!(import! &self MettaLecture2:constractExpression)

; (1 2 3 4)
;output is 
; 1
; 2
; 3
; 4
; (4)
; (3 4)
; (2 3 4)
; (1 2 3 4)
!(constractExpression (1 2 3 4))