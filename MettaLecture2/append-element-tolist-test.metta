!(register-module! /home/samuel/Documents/Icog-Intern/MettaLecture2)
!(import! &self MettaLecture2:append-element-tolist)

;check for (:: 1 (:: 3 Nil)) append 4 it should be (:: 1 (:: 3 (:: 4 Nil)))
!(assertEqual (append (:: 1 (:: 3 Nil)) 4) (:: 1 (:: 3 (:: 4 Nil))))

!(test passed)