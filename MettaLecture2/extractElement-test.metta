!(register-module! /home/samuel/Documents/Icog-Intern/MettaLecture2)
!(import! &self MettaLecture2:extractElement)

!(assertEqual (extractElement (:: 2 (:: 3 (:: 4 Nil)))) (2 3 4))

!(test passed)