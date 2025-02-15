!(register-module! /home/samuel/Documents/Icog-Intern/MettaLecture2)
!(import! &self MettaLecture2:insert-delete)

;check the append function with atom = 7 and exp = (4 5 6) the answer should be (4 5 6 7)
!(assertEqual (append 7 (4 5 6)) (4 5 6 7))

;check the appendStart function with atom = 7 and exp = (4 5 6) the answer should be (7 4 5 6)
!(assertEqual (appendStart 7 (4 5 6)) (7 4 5 6))

;check the insert function with atom = 7 index = 2 and exp = (4 5 6) the answer should be (4 5 7 6)
!(assertEqual (insert 7 2 (4 5 6)) (4 5 7 6))

;check the insert function with atom = 7 index = 0 and exp = (4 5 6) the answer should be (7 4 5 6)
!(assertEqual (insert 7 0 (4 5 6)) (7 4 5 6))

;check the insert function with atom = 7 index = 3 and exp = (4 5 6) the answer should be (4 5 6 7)
!(assertEqual (insert 7 3 (4 5 6)) (4 5 6 7))

;check the deleteStart function with exp = (4 5 6) the answer should be (5 6)
!(assertEqual (deleteStart (4 5 6)) (5 6))

;check the delete function with index = 1 and exp = (4 5 6) the answer should be (4 6)
!(assertEqual (delete 1 (4 5 6)) (4 6))

;check the delete function with index = 0 and exp = (4 5 6) the answer should be (5 6)
!(assertEqual (delete 0 (4 5 6)) (5 6))

;check the deleteEnd function with exp = (4 5 6) the answer should be (4 5)
!(assertEqual (deleteEnd (4 5 6)) (4 5))

!(test passed)
