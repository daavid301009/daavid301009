from pygame import *

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_width, player_height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (player_width, player_height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update_l(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_s] and self.rect.y < 345:
            self.rect.y += self.speed
    def update_r(self):
        keys_pressed = key.get_pressed()
        if keys_pressed[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
        if keys_pressed[K_DOWN] and self.rect.y < 345:
            self.rect.y += self.speed 

back = (80, 38, 167)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)

clock = time.Clock()
FPS = 60
racket_l = Player('ракетка.png', 30, 200, 50, 150, 4)
racket_r = Player('ракетка.png', win_width - 80, 200, 50, 150, 4)
game = True
finish = False
while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish != True:
        window.fill(back)
        racket_l.update_l()
        racket_r.update_r()
        racket_l.reset()
        racket_r.reset()
    display.update()
    clock.tick(FPS) 