!(register-module! /home/samuel/Documents/Icog-Intern/MettaLecture3) 
!(import! &self MettaLecture3:non-deterministic)
!(import! &self MettaLecture3:path-finding)


;test find path between Adama and Harar
!(pathFind Adama Harar (Adama) 0)
!(pathFind AddisAbaba Mekelle (AddisAbaba) 0)
!(shortestPath AddisAbaba Mekelle)

