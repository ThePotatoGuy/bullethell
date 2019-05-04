import cmath
import math

class Bullet:

    def __init__(self, pos: list, speed: int, angle: int=270):
        # angle defaults to 270 degrees, facing down
        self.pos = pos
        self.speed = speed
        self.angle = int(angle % 360)
        self._radian = math.radians(self.angle)

    def update(self):
        # angle being direction
        new_pos_as_clx = cmath.rect(self.speed, self._radian)
        xdiff = int(new_pos_as_clx.real)
        ydiff = int(new_pos_as_clx.imag)
        self.pos[0] += xdiff
        self.pos[1] += ydiff
