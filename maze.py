from pygame import *
win = display.set_mode((700,500))
display.set_caption('Лабиринт')
background = transform.scale(image.load('background.jpg'),(700,500))
class GameSprite(sprite.Sprite):
    def __init__(self,player_image, player_x,player_y,player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(65,65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x>5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x<620:
            self.rect.x += self.speed
        if keys[K_UP] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y<420:
            self.rect.y += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_width
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1, color_2, color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y
    def draw_wall(self):
        win.blit(self.image, (self.rect.x, self.rect.y))

class Enemy(GameSprite):
    diryctory = 'left'
    def update(self):
        if self.rect.x <= 470:
            self.diryctory = 'right'
        if self.rect.x >= 620:
            self.diryctory = 'left'
    
        if self.diryctory == 'left':
            self.rect.x -= self.speed
        if self.diryctory == 'right':
            self.rect.x += self.speed
FPS = 60
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
flag = True





st_1 = Wall(255,0,255,0,300,380,15)
st_2 = Wall(255,0,255,80,420,420,15)
st_3 = Wall(255,0,255,380,150,15,150)
st_4 = Wall(255,0,255,500,150,15,270)

finish = False


font.init()
font = font.SysFont('Arial', 70)
win_4 = font.render('YOU WIN', True, (225,215,0))
lose = font.render('YOU LOSE', True, (180,0,0))

player = Player('hero.png',5,500-80,7)
monster = Enemy('cyborg.png',500,280,3)
treasure = GameSprite('treasure.png',600,500-80,0)
clock = time.Clock()
while flag:
    for e in event.get():
        if e.type ==QUIT:
            flag=False
    if finish != True:
        win.blit(background, (0,0))
        player.update()
        monster.update()
        st_1.draw_wall()
        st_2.draw_wall()
        st_3.draw_wall()
        st_4.draw_wall()
        player.reset()
        monster.reset()
        treasure.reset()

    if sprite.collide_rect(player, monster) or sprite.collide_rect(player, st_1) or sprite.collide_rect(player, st_2) or sprite.collide_rect(player, st_3) or sprite.collide_rect(player, st_4):
        finish = True
        win.blit(lose,(200,200))
        mixer.music.load('kick.ogg')
        mixer.music.play()
    if sprite.collide_rect(player, treasure):
        finish = True
        win.blit(win_4,(200,200))
        mixer.music.load('money.ogg')
        mixer.music.play()
    
    
    display.update()
    clock.tick(FPS)
