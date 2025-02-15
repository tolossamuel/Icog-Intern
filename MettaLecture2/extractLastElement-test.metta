!(register-module! /home/samuel/Documents/Icog-Intern/MettaLecture2)
!(import! &self MettaLecture2:extractLastElement)

;check for (:: 12 (:: 13 (:: 14 (:: 15 empty))))

!(assertEqual (extractLastElement (:: 12 (:: 13 (:: 14 (:: 15 Nil))))) 15)

!(test passed)