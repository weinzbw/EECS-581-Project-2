import random

class AI():
    def __init__(self):
        self.shots = []
        self.lastShot == ""
    
    def easy_shoot(self):
        pass # easy behavior goes here (returns coords)
    
    def med_shoot(self):
        if "hit" in self.lastShot: # Checks if the last shot was a hit
            # Goes through orthogonal process
            coord = self.shots[-1].split()
            new_coord = ord(coord[0])
            coord[0] = chr(new_coord + 1)
            if ''.join(coord) in self.shots:
                coord[0] = chr(new_coord - 1)
                if ''.join(coord) in self.shots:
                    coord[0] = chr(new_coord)
                    coord[1] += 1
                    if ''.join(coord) in self.shots:
                        coord[1] -= 2
            self.shots.append(''.join(coord))
            return ''.join(coord)
        # Else, randomly pick coord
        coord = [chr(random.randint(65, 74)), str(random.randint(1, 10))]
        # Must be a coord not chosen before (Fix to have Column and Row)
        while ''.join(coord) in self.shots:
            coord = [chr(random.randint(65, 74)), str(random.randint(1, 10))]
        self.shots.append(''.join(coord))
        return ''.join(coord)
    
    def hard_shoot(self):
        pass # hard behavior (returns coords)
    
    def turn(self):
        # depending on self.difficulty, call one of the three methods above
        pass
