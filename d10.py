import numpy as np


class Asteroid:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def r(self, other):
        return ((self.x - other.x)**2 + (self.y - other.y)**2)**0.5
    
    def phi(self, other):
        return np.rad2deg(np.arctan2(other.x - self.x, other.y - self.y))
    
    def __repr__(self):
        return f'{self.x=}, {self.y=}'
    
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y


def part_one(field):
    asteroids = [Asteroid(j, i) for i in range(len(field)) for j in range(len(field[i])) if field[i][j] == '#']
    
    max_detected = 0
    pos = None
    for station in asteroids:
        tmp_asteroids = asteroids[:]
        tmp_asteroids.remove(station)
        for target in tmp_asteroids:
            phi = station.phi(target)
            others = tmp_asteroids[:]
            others.remove(target)
            same_phi = list(filter(lambda x: phi == station.phi(x), others))
            closest_in_direction = target
            for item in same_phi:
                if station.r(item) < station.r(closest_in_direction):
                    tmp_asteroids.remove(closest_in_direction)
                    closest_in_direction = item
                else:
                    tmp_asteroids.remove(item)
                    
        cur_detected = len(tmp_asteroids)
        if cur_detected > max_detected:
            max_detected = cur_detected
            pos = station
            
    return max_detected


def part_two(field):
    asteroids = [Asteroid(j, i) for i in range(len(field))
                 for j in range(len(field[i])) if field[i][j] == '#']
    
    station = Asteroid(11, 13)
    tmp_asteroids = asteroids[:]
    tmp_asteroids.remove(station)
    phi_asteroids = {}

    visited = []
    for target in tmp_asteroids:
        if target in visited:
            continue
        phi = station.phi(target)
        others = tmp_asteroids[:]
        same_phi = list(filter(lambda x: phi == station.phi(x), others))
        same_phi = sorted(same_phi, key=lambda x: station.r(x))

        visited.extend(same_phi)
        phi_asteroids[phi] = same_phi
    
    keys = sorted(phi_asteroids)
    keys = list(reversed(keys))
    
    ind = keys.index(180)
    keys = keys[ind:] + keys[:ind]
    print(keys)
    counter = 1
    while counter < 202:
        for angle in keys:
            if phi_asteroids[angle]:
                current = phi_asteroids[angle].pop(0)
            
                if counter in [1,2,3,10,20,50,100,199,200]:
                    print(f'{counter=}, {current=}')
                counter += 1
        

with open('d10_input.txt') as fin:
    data = fin.read().splitlines()


# print(part_one(data))
part_two(data)