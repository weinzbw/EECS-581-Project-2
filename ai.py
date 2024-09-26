import random

class AI():
    def __init__(self):
        # ask user to select a difficulty
        # 1 = easy 2 = med 3 = hard
        # then set self.difficulty depending on what is returned
        pass
    
    def easy_shoot(self):
        pass # easy behavior goes here (returns coords)
    
    def med_shoot(self):
        if lastShot is hit: # Checks if the last shot was a hit
            # Goes through orthogonal process
            coord = self.shots[-1].split()
            new_coord = ord(coord[0])
            coord[0] = chr(new_coord + 1)
            if coord.join() in self.shots:
                coord[0] = chr(new_coord - 1)
                if coord.join() in self.shots:
                    coord[0] = chr(new_coord)
                    coord[1] += 1
                    if coord.join() in self.shots:
                        coord{1} -= 2
            self.shots.append(coord.join())
            return coord.join()
        # Else, randomly pick coord
        coord = random.randint(65, 90)
        # Must be a coord not chosen before (Fix to have Column and Row)
        while coord in self.shots:
            coord = random.randint(65, 90)
        return coord
    
    def hard_shoot(self):
        pass # hard behavior (returns coords)
    
    def turn(self):
        # depending on self.difficulty, call one of the three methods above
        pass
