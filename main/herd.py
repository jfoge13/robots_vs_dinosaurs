from dinosaurs import Dinosaur

class Herd:

    def __init__(self):
        self.herd = []
        self.add_dinosaurs()
        

    def add_dinosaurs(self):
         dinosaur1 = Dinosaur.name("Rex")
         dinosaur2 = Dinosaur.name("Morty")
         dinosaur3 = Dinosaur.name("Rick")

         self.herd.append(dinosaur1)
         self.herd.append(dinosaur2)
         self.herd.append(dinosaur3)