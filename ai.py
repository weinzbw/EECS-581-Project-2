import random

class AI():
    def __init__(self, board):
        self.shots = []
        self.lastShot = ""
        self.board = board
    
    def easy_shoot(self):
        coords = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        shot = None

        while shot is None or shot in self.shots:
            col = random.choice(coords)
            row = str(random.randint(1, 10))
            shot = col + row

        self.shots.append(shot)
        return shot
    
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
        for ship in self.opponent_ships:
            if ship not in self.shots:
                self.shots.append(ship)
                return ship
    
    def turn(self):
        # depending on self.difficulty, call one of the three methods above
        pass
