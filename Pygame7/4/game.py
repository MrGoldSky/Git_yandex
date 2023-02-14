import os

import pygame


class CameraGroup(pygame.sprite.Group):
    def __init__(self, procreator=None):
        super().__init__()
        self.procreator = procreator
        self.wall = pygame.transform.scale(pygame.image.load("objects/box.png"), self.procreator.tile)
        self.grass = pygame.transform.scale(pygame.image.load("objects/grass.png"), self.procreator.tile)
        self.field = self.procreator.map.map

    def init(self):
        pass

    def walk(self, s):
        for _ in range(len(self.field)):
            try:
                index = (_, self.field[_].index('@'))
            except ValueError:
                pass

        if s[0] > 0:
            if self.field[index[0]][index[1] + 1] == '#':
                return
            self.field[index[0]][index[1]] = '.'
            self.field[index[0]][index[1] + 1] = '@'

            self.new_list = self.field.copy()
            for _ in range(len(self.field)):
                self.new_list[_] = self.field[_][1:] + self.field[_][0:1]
            self.field = self.new_list.copy()

        elif s[0] < 0:
            if self.field[index[0]][index[1] - 1] == '#':
                return
            self.field[index[0]][index[1]] = '.'
            self.field[index[0]][index[1] - 1] = '@'

            self.new_list = self.field.copy()
            for _ in range(len(self.field)):
                self.new_list[_] = self.field[_][-1:] + self.field[_][:-1]
        elif s[1] > 0:
            if self.field[index[0] + 1][index[1]] == '#':
                return
            self.field[index[0]][index[1]] = '.'
            self.field[index[0] + 1][index[1]] = '@'

            self.new_list = self.field.copy()
            self.new_list = self.field[1:] + self.field[0:1]
        elif s[1] < 0:
            if self.field[index[0] - 1][index[1]] == '#':
                return
            self.field[index[0]][index[1]] = '.'
            self.field[index[0] - 1][index[1]] = '@'

            self.new_list = self.field.copy()
            self.new_list = self.field[-1:] + self.field[:-1]
        self.field = self.new_list.copy()

    def update(self):
        for _ in range(len(self.field)):
            for _2 in range(len(self.field[_])):
                if self.field[_][_2] == '#':
                    self.procreator.screen.blit(self.wall, (_2 * self.procreator.tile[0], _ * self.procreator.tile[1]))
                elif self.field[_][_2] == '.':
                    self.procreator.screen.blit(self.grass, (_2 * self.procreator.tile[0], _ * self.procreator.tile[1]))
                elif self.field[_][_2] == '@':
                    self.procreator.screen.blit(self.grass, (_2 * self.procreator.tile[0], _ * self.procreator.tile[1]))
                    self.procreator.player.update(self.procreator.screen,
                                                  (_2 * self.procreator.tile[0], _ * self.procreator.tile[1]))


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
        self.map = list(map(lambda x: list(x), self.map))

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
        self.map.init()

        self.screen = pygame.display.set_mode(self.size)
        self.screen_rect = self.screen.get_rect()

        self.camera = CameraGroup(procreator=self)
        self.player = Character(procreator=self, groups=(self.camera,))
        self.walls_group = pygame.sprite.Group()
        self.camera.init()

    def game_events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_d:
                self.camera.walk((1, 0))
            elif event.key == pygame.K_a:
                self.camera.walk((-1, 0))
            elif event.key == pygame.K_w:
                self.camera.walk((0, -1))
            elif event.key == pygame.K_s:
                self.camera.walk((0, 1))

    def game_render(self):
        self.screen.fill('black')
        self.camera.update()

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
