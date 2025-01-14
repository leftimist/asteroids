from circleshape import *

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        self.pos_x = x
        self.pos_y = y
        self.radius = radius


    def draw(self, screen):
        pygame.draw.circle(screen, "red", [self.pos_x, self.pos_y] , self.radius)

    def update(self, dt):
        self.pos_x += self.velocity.x * dt
        self.pos_y += self.velocity.y * dt