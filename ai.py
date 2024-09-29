'''
Program Name: ai.py
Description: Adds AI ability to the game. Specifically the firing of shots for different difficulties.
Inputs: Needs a board class entity
Output: Returns coordinates being shot at
Authors: Del Endecott, Ben Weinzirl, Mick Torres
Creation Date: 9/25/24
'''
import random

class AI():
    def __init__(self, board):
        self.shots = []
        self.lastShot = ""
        self.board = board
        self.orthogonal = []
    
    def makeOrthog(self):
        coord = []
        for letter in self.shots[-1]:
            coord.append(letter)
        new_coord = ord(coord[0])

        coord[0] = str(chr(new_coord + 1))
        self.orthogonal.append(''.join(coord))
        
        coord[0] = str(chr(new_coord - 1))
        self.orthogonal.append(''.join(coord))
        
        coord[0] = str(chr(new_coord))
        coord[1] = str(int(coord[1]) + 1)
        self.orthogonal.append(''.join(coord))
        
        coord[1] = str(int(coord[1]) - 2)
        self.orthogonal.append(''.join(coord))
    
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
        # Check if ship was sunk last shot. Fire randomly if so.
        if "sunk" in self.lastShot.lower().split():
            coord = [str(chr(random.randint(65, 74))), str(random.randint(1, 10))]
            # Must be a coord not chosen before (Fix to have Column and Row)
            while ''.join(coord) in self.shots:
                coord = [str(chr(random.randint(65, 74))), str(random.randint(1, 10))]
            self.shots.append(''.join(coord))
            return ''.join(coord)
        if "hit" in self.lastShot.lower().split(): # Checks if the last shot was a hit
            # Makes a list of orthogonal shots if so
            self.makeOrthog()
        # Tries to go through list of orthogonal shots
        if len(self.orthogonal) != 0:
            for coord in self.orthogonal:
                if coord not in self.shots:
                    self.shots.append(coord)
                    return coord
        # If the list doesn't exist, then fire randomly
        else:
            coord = [str(chr(random.randint(65, 74))), str(random.randint(1, 10))]
            # Must be a coord not chosen before (Fix to have Column and Row)
            while ''.join(coord) in self.shots:
                coord = [str(chr(random.randint(65, 74))), str(random.randint(1, 10))]
            self.shots.append(''.join(coord))
            print(coord)
            return ''.join(coord)
    
    def hard_shoot(self):
        for ship in self.opponent_ships:
            if ship not in self.shots:
                self.shots.append(ship)
                return ship
