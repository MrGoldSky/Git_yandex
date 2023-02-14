import os

import pygame


class CameraGroup(pygame.sprite.Group):
    def __init__(self, procreator=None):
        super().__init__()
        self.procreator = procreator
        self.display_surface = self.procreator.screen

        self.offset = pygame.math.Vector2()
        self.half_w = self.display_surface.get_size()[0] // 2
        self.half_h = self.display_surface.get_size()[1] // 2

        self.ground_rect = (0, 0)

    def init(self):
        self.ground_rect = self.procreator.map.rect

    def center_target_camera(self, target):
        self.offset.x = target.rect.centerx - self.half_w
        self.offset.y = target.rect.centery - self.half_h

    def update(self, player):
        self.center_target_camera(player)
        ground_offset = self.ground_rect.topleft - self.offset
        self.display_surface.blit(self.procreator.map.image, ground_offset)

        try:
            for sprite in sorted(self.sprites().copy(), key=lambda sprite: sprite.rect.centery):
                sprite.update(self.display_surface, sprite.rect.topleft - self.offset)
        except AttributeError:
            pass


class Character(pygame.sprite.Sprite):
    def __init__(self, procreator=None, groups=None):
        super().__init__(*groups)
        self.procreator = procreator
        self.image = pygame.image.load("objects/character.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 1.25, self.image.get_height() * 1.25))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)

    def move(self, move):
        self.rect.left += move[0]
        self.rect.top += move[1]
        if pygame.sprite.spritecollideany(self, self.procreator.walls_group):
            self.rect.left -= move[0]
            self.rect.top -= move[1]

    def set_pos(self, pos):
        self.rect.midtop = pos

    def update(self, ds, pos):
        ds.blit(self.image, pos)


class Box(pygame.sprite.Sprite):
    def __init__(self, size, pos, groups=None):
        super().__init__(*groups)
        self.image = pygame.Surface(size)
        self.rect = self.image.get_rect()
        self.rect.topleft = pos


class Map(pygame.sprite.Group):
    def __init__(self, tile_size, map, procreator=None):
        super().__init__()
        self.tile_size = tile_size
        self.map = map
        self.image = pygame.Surface(
            (len(max(self.map, key=len)) * self.tile_size[0], len(self.map) * self.tile_size[1]))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)
        self.procreator = procreator

    def init(self):
        wall = pygame.transform.scale(pygame.image.load("objects/box.png"), self.tile_size)
        grass = pygame.transform.scale(pygame.image.load("objects/grass.png"), self.tile_size)
        for _ in range(len(self.map)):
            for _2 in range(len(self.map[0])):
                if self.map[_][_2] == '#':
                    self.image.blit(wall, Box(self.tile_size, (_2 * self.tile_size[0], _ * self.tile_size[1]),
                                              groups=(self.procreator.walls_group,)).rect)
                elif self.map[_][_2] == '.':
                    self.image.blit(grass, (_2 * self.tile_size[0], _ * self.tile_size[1]))
                elif self.map[_][_2] == '@':
                    self.image.blit(grass, (_2 * self.tile_size[0], _ * self.tile_size[1]))
                    self.procreator.player.set_pos(
                        (_2 * self.tile_size[0] + (self.tile_size[0] // 2), _ * self.tile_size[1]))

    def update(self):
        self.procreator.screen.blit(self.image, self.rect)


class Core:
    def __init__(self):
        self.tile = (50, 50)

        files = os.listdir("levels")
        print("PLEASE, SELECT LEVEL! >>\n\t> {0}".format('\n\t> '.join(files)))
        level = input("~ you: ")
        while level not in files:
            print("wrong file name")
            level = input("~ you: ")
        self.map = list(map(lambda x: x.strip(), open("levels/" + level, "r").readlines()))

    def init(self):
        pygame.init()
        pygame.display.set_caption('ъыъ')

        self.size = pygame.display.Info()
        self.size = (self.size.current_w, self.size.current_h)

        self.map = Map(self.tile, self.map, procreator=self)

        self.screen = pygame.display.set_mode(self.size)
        self.screen_rect = self.screen.get_rect()

        self.camera = CameraGroup(procreator=self)
        self.player = Character(procreator=self, groups=(self.camera,))
        self.walls_group = pygame.sprite.Group()
        self.map.init()
        self.camera.init()

    def game_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.player.move((self.tile[0], 0))
            elif event.key == pygame.K_a:
                self.player.move((-self.tile[0], 0))
            elif event.key == pygame.K_w:
                self.player.move((0, -self.tile[1]))
            elif event.key == pygame.K_s:
                self.player.move((0, self.tile[1]))

    def game_render(self):
        self.screen.fill('black')
        self.camera.update(self.player)

    def menu_events(self, event):
        if event.type == pygame.KEYDOWN:
            self.events = self.game_events
            self.render = self.game_render

    def menu_render(self):
        self.screen.blit(self.bg_img, (0, 0))

    def start_wheel(self):
        self.running = True
        self.bg_img = pygame.transform.scale(pygame.image.load("objects/fon.jpg"), self.screen_rect.size)
        self.events = self.menu_events
        self.render = self.menu_render
        while self.running:
            for event in pygame.event.get():
                self.events(event)
            self.render()
            pygame.display.update()


core = Core()
core.init()
core.start_wheel()
